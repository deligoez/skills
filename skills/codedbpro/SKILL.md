---
name: codedbpro
version: 1.3.0
description: >-
  Use the codedbpro MCP toolset (CodeDB Pro daemon) as the primary way to read, search, and edit
  code — batched round-trips, outline-first reading, symbol-safe edits, dry-run-first refactors.
  Use whenever codedbpro MCP tools are available in the session, especially in repos where native
  Read/Write/Edit/cat/grep are hook-blocked, and whenever you catch yourself firing single reads or
  greps one at a time, or doing text surgery through python/sed/perl heredocs. Triggers: "use
  codedb", "codedbpro", "be token-efficient with the codebase", "batch your reads", repeated
  one-file-at-a-time tool calls in your own transcript.
license: MIT
compatibility: any-agent
---

# codedbpro — daemon-backed read/search/edit for agents

A persistent daemon over MCP: a dozen code tools with no fork/exec per call (~1–13 ms/op measured),
a symbol index, and shell-free writes. Content travels as JSON, so curly quotes, non-ASCII,
backticks and `$` are all safe — this replaces python/perl heredoc surgery and its classic traps.

Where hooks block native `Read`/`Write`/`Edit`/`grep`, codedbpro is the primary toolchain, not a
fallback. The CLI twins (`zigread`/`zigrep`/`zigpatch`/`zigcreate`) are for bash loops or a dead
daemon. Use `node`/`python3` to compute or verify a claim — never as a grep/sed substitute.

Four habits produce almost all of the win: **never let an edit expand**, **batch everything**,
**outline before you read**, **verify every write**.

## ⚠ Rule 0 — an unscoped `pattern` edit replaces the WHOLE function

This is the one call that silently destroys code, and it is the single most valuable thing in this
skill.

`edit` matches your text, then **expands the replaced region to the enclosing function/block**. If
`content` is only the small piece you matched, the rest of that function — signature included — is
deleted, and the call still returns `ok:true`.

Reproduced on 0.2.10, re-verified unchanged on 0.2.22, against a Go file:

```
edit {file, pattern:'suffix := "!"', content:'\tsuffix := "!!"'}
  → lines_removed: 5   # the entire Greet function, signature and all
edit {file, pattern:'suffix := "!"', content:'\tsuffix := "!!"', scope:"line"}
  → lines_removed: 1   # only the matched line
```

- **Pass `scope:"line"` whenever the replacement is not the entire function** — that is the test, not
  whether the change feels small. (Verified working, even though it is absent from some published
  schemas. `scope:"line"` keeps exactly the matched lines, however many they are.)
- **A multi-line pattern is not safer.** Scope expands from the *match*, not from how much you
  matched. A pattern covering a whole `if` block still replaced the enclosing function
  (`lines_removed: 8` for a 4-line pattern); the same call with `scope:"line"` removed 4.
  `scope:"block"` does **not** narrow to the enclosing block — on that test it expanded to the
  function exactly like a bare pattern.
- **Reserve a bare `pattern` for when you mean to swap a whole function** — and then prefer
  `symbol:"name"`, which says so explicitly and survives line drift.
- **Read `lines_removed` on every write.** Larger than the line count of your pattern = the scope
  expanded and you clobbered neighbours. Revert and retry with `scope:"line"`.
- **`dry_run:true` previews the diff without writing** — the response carries `dry_run:true` (the
  older `op:"verify"` shape is gone). One call, and it saves reconstructing a function by hand.
- **The built-in scope-shrink guard will not save you here.** `confirm_scope_shrink` only fires above
  a 10:1 shrink; the everyday Rule 0 accident — 8 lines replaced by 4 — writes silently.

## Tool signatures

Guessing parameter names is the second-biggest time sink. These are exact:

```
read    {file, mode: outline|full|lines|symbol|section|smart_range|ls|compact|json|query,
         range?:"10-20"|"10-$", name?, heading?, line?, path?, query?, numbers?,
         if_revision?, fresh?, live?}         # every read returns hash + revision
edit    {file, symbol|pattern|range|after, content, scope?: line|block|symbol,
         op?: replace|delete|insert|str_replace|byte_delta,
         old_string?, new_string?, expected?, match_index?, replace_all?,
         if_revision?, whole_file?, confirm_scope_shrink?, dry_run?, backup?}
patch   {file, range:"10-20" | after:N, content, op?: replace|delete|insert,
         if_revision?, dry_run?, backup?}
create  {file, content, parents?, force?, append?, executable?, content_b64?}
faster_search {pattern, path, mode?: literal|word|regex, i?, w?, l?, c?, scope?, type?,
               find?, fuzzy?, A?, B?, limit?, max_per_file?, fresh?, no_ignore?}
search        {…identical interface}          # canonical baseline output
meta_search   {query, path?, detail?: auto|merged|plan|full, run?, max_variants?, prefer_fast?}
replace {pattern, replacement, path|paths, regex?, apply?, dry_run?=true,
         max_files?=50, allow_large?, allow_cwd_root?, backup?, atomic_write?, i?, type?}
diff    {file?, staged?, stat?, no_cache?}
lint    {file, fresh?}
memo    {action: store|get|tag|ls|dump|drop|clear|status|error|errors|plan|context,
         value?, tag?, hash?, check?, next?, status?}
batch   {ops:[{tool, args}, …]}
```

**`file` vs `path`:** read/edit/patch/create/lint/diff take **`file`**; search/replace take
**`path`**. Passing `path` to `create` fails with `missing 'file'`; passing `query` to
`faster_search` fails with `missing 'pattern'` (only `meta_search` takes `query`).

## Rule 1 — two or more operations = ONE `batch`

- Reads and searches run **in parallel**.
- Same-file writes are serialized, but **applied in call order, top-down — they are not reordered**.
  Tested on 0.2.14 and again on 0.2.22: `{after:2, op:"insert"}` followed by `{range:"6-6"}` in one
  batch hit the original line 5, and two plain `patch` ranges behave the same. The 0.1.04 release
  note about bottom-up auto-coalescing no longer describes the MCP batch path. Batch them anyway
  for the round-trip, but every line range after the first write must already account for the shift
  — or use `symbol`/`pattern` ops, or `if_revision` (Rule 4), which don't care. A run of sequential
  single `edit` calls to one file is still the anti-pattern this rule kills.
- Batches run in bounded eight-op waves; a wide batch of large payloads trips the 64 MiB retention
  cap (`batch_output_limit`) or the 256 KiB per-response ceiling. Batch freely, but keep payloads
  narrow — outlines and ranges, not `mode:"full"`.
- `ops` must be a real JSON array, and each element needs **both** `tool` and `args` — args nested,
  not spread. `{ops:[{op:"edit", …}]}` and `{ops:[{tool:"edit", file:…}]}` both fail.

```json
{"ops": [
  {"tool": "read",          "args": {"file": "src/widgets/interactions.js", "mode": "outline"}},
  {"tool": "faster_search", "args": {"pattern": "onReady", "path": "src", "c": true}},
  {"tool": "read",          "args": {"file": "src/core/i18n.js", "mode": "symbol", "name": "yonelme"}},
  {"tool": "diff",          "args": {"stat": true}}
]}
```

Returns `{ok, op:"batch", total, failed, results:[…]}` in call order. Self-check: if your last three
calls were single codedbpro calls that did not depend on each other's output, that was one batch.

## Rule 2 — outline first, then the symbol

Never pull a big file whole. A 7,878-line widget file → `mode:"outline"` returns a 72-symbol map
(name + line span each); then fetch only what you need.

- `read {file, mode:"outline"}` → symbol map. Start here for any file you don't know.
- `read {file, mode:"symbol", name:"cpuRun"}` → one function's body.
- `read {file, mode:"lines", range:"120-180"}` / `mode:"smart_range", line:150` → exact or
  context-expanded ranges. `range:"10-$"` reads to end of file.
- `read {file, mode:"section", heading:"Install"}` → a markdown section. `mode:"ls"` lists a dir.
- Re-reading a file you already saw? Pass `if_hash` from the previous read — unchanged files come
  back as `{unchanged:true}` for free.
- Small files (a screen of prose, a config) — just read them full. Outline-first is for big files.

**Known limit:** a one-line arrow const (`export const f = x => …`) resolves as a symbol to just its
signature line. Use `lines`/`smart_range` for those.

## Rule 3 — search with the right tool for how much you know

- You know the pattern → `faster_search {pattern, path}`. Both are required.
- The question is fuzzy ("where is auth handled?") → `meta_search {query}` — the daemon fans out
  several strategies and merges. Once you know the exact pattern, go back to `faster_search`.
- After a rebase / checkout / pull / any out-of-band edit → add `fresh:true` once. A stale index is
  the usual cause of "it's there but search can't see it".

**You cannot force a literal search — escape instead.** `mode:"literal"` *and* `regex:false` were
both overridden in testing: `alpha|beta` still matched lines containing only `alpha` or only `beta`
(the response says `interpreted:"regex"`). Escaping worked — `alpha\|beta` matched only the literal
line. Escape `| ( ) . * + ? [` for a literal substring, or add `w:true` for whole-word.

**A zero-match search is a claim, not a fact.** `faster_search {pattern:"first-letter"}` returned 0
while `::first-letter` sat in the file. Before acting on "not found" — deleting a rule, skipping a
rename — re-check with a different substring or an escaped pattern.

## Rule 4 — pick the write tool by what you know

| You know… | Use |
|---|---|
| the function/type name | `edit {file, symbol:"name", content}` — survives line drift; best default for code |
| less than a whole function | `edit {file, pattern:"…", content, scope:"line"}` — **never omit `scope`**, however many lines you matched (Rule 0) |
| exact line numbers | `patch {file, range:"10-20", content}` (or `after:N`, `op:"insert"/"delete"`) |
| an exact string to swap across files | `replace {pattern, replacement, path, apply:true}` |
| you're rewriting the whole file | `create {file, content, force:true}` |
| you're creating a file | `create {file, content, parents:true}` |

- **After any write to a file, line numbers from an earlier read are stale.** `patch` and
  `edit {range}` are deterministic: they apply to whatever now sits there and return `ok:true`.
  Re-read (the read cache is refreshed by the write — no `fresh:true` needed), or send the write
  with `dry_run:true` — the diff comes back without touching the file, one call instead of a broken
  one. On a range-based write into a file you have already edited, treat `dry_run:true` as the
  default, not the last resort. Verified failure: a range two lines stale doubled a docblock's
  `@return` and ate the blank `*` line.
- **Prose and Markdown have no parseable scopes.** `edit {pattern}` on a `.md` file fails with
  `no enclosing scope found for pattern match`. Use `range`/`after`, or `replace` for a string swap.
- **Don't span a doc-comment → `func` boundary in a pattern.** `// Greet says…\nfunc Greet(…)` fails
  the same way: the comment sits outside the symbol's scope. Match from the `func` line instead.
- `replace` is **dry-run by default**: preview, then re-send with `apply:true`. It refuses
  `path:"."` (`allow_cwd_root`) and refuses touching more than 50 files (`max_files`/`allow_large`).
  Those guards are features — don't reflex-override them. `regex:true` enables backreferences
  (`\1`, backslash form).
- `create` needs **`parents:true`** for a new directory tree, and **`force:true`** to overwrite.
  Without them you get `failed to create file` / `file already exists`.

## Rule 5 — verify every write

1. `lines_removed` in the response — the Rule 0 check. Do this every time. The count alone is not
   enough: a stale range removes the right *number* of lines and the wrong ones. Read the `-` lines
   of the returned diff, not just the tally.
2. `edit`/`patch` return the written lines, so a follow-up read is usually waste. Want the change in
   context? `diff {file}` (or `diff {stat:true}`, `staged:true`).
3. `lint {file}` auto-detects the project linter and returns normalized diagnostics. It returns
   `{linter:null}` when the repo has no linter config — then your verification is the test suite.

## Rule 6 — memo for anything that must survive context loss

`memo {action:"store", value:"…", tag:"findings"}` persists notes across compaction;
`action:"plan"` keeps a checklist (`check:N` marks steps done), `action:"context"` reloads after
compression. Use it on multi-hour tasks instead of re-deriving state.

## Pitfalls

- **Paths are relative to the daemon's working directory** (usually the repo root); absolute paths
  also work. One `diff {stat:true}` echoes the cwd if unsure.
- **codedbpro is not repo-locked.** read/search/edit/create all succeed on `/tmp`, `~/.claude`, or
  another checkout. A failure out there is a missing parent (`parents:true`) or a scope error — not
  a workspace boundary.
- `replace` without `apply:true` **wrote nothing** — don't move on after a preview.
- Batch `ops` passed as a string instead of an array is the most common malformed call.
- Two independent facts you need → still one batch. Only serialize when call B needs call A's output.

## Decision card

```
know nothing about the file      → read outline
know the function                → read symbol / edit symbol
replacing less than a function   → edit scope:"line"   (any pattern, 1 line or 40 = whole func)
know the exact line              → read lines / patch range
line numbers after a prior write → stale; re-read, or send it with dry_run:true
markdown or prose                → patch range / replace   (pattern edits have no scope there)
know the exact string            → faster_search / replace (dry-run → apply)
question is vague                → meta_search
≥2 of anything                   → batch
just rebased/pulled              → fresh:true
long task, fragile context       → memo
after any write                  → check lines_removed, then diff / lint
```
