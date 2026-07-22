---
name: codedbpro
version: 1.1.0
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

codedbpro is a persistent daemon exposed over MCP: a dozen code tools with no fork/exec per call
(~1–13 ms/op measured), a symbol index, and shell-free writes. Three habits produce almost all of
the win: **batch everything**, **outline before you read**, **edit by symbol, not by line number**.

## Division of labor — decide before you reach for a tool

| Job | Tool |
|---|---|
| Read / search / edit files | **codedbpro** (this skill) |
| Compute, simulate, verify a numeric claim | `node` / `python3` — *never* as a grep/sed substitute |
| Run tests, commit | the project's own flow (test runner, `hc`, …) |

If the repo blocks native `Read`/`Write`/`Edit`/`grep` via hooks, codedbpro is the primary
toolchain, not a fallback. CLI fallbacks (`zigread`/`zigrep`/`zigpatch`/`zigcreate`) exist for
bash loops or a dead daemon; prefer the MCP tools otherwise.

## Rule 1 — two or more operations = ONE `batch`

`batch {ops: [{tool, args}, …]}` is the default shape for everything beyond a single call.

- Reads and searches run **in parallel**.
- Edits to the **same file** are safe in one batch: the daemon serializes them and applies them
  bottom-up, so earlier line numbers never drift. A run of sequential single `edit` calls to one
  file is the anti-pattern this rule kills.
- `ops` must be a real JSON array — not a JSON-encoded string.

```json
{"ops": [
  {"tool": "read",          "args": {"file": "src/widgets/interactions.js", "mode": "outline"}},
  {"tool": "faster_search", "args": {"pattern": "onReady", "path": "src", "c": true}},
  {"tool": "read",          "args": {"file": "src/core/i18n.js", "mode": "symbol", "name": "yonelme"}},
  {"tool": "diff",          "args": {"stat": true}}
]}
```

Self-check while working: if your last three tool calls were single codedbpro calls that did not
depend on each other's output, you should have sent one batch.

## Rule 2 — outline first, then the symbol

Never pull a big file whole. Measured example: a 7,878-line widget file → `mode:"outline"` returns
a 72-symbol map (name + line span each); then fetch only what you need.

- `read {file, mode:"outline"}` → symbol map. Start here for any file you don't know.
- `read {file, mode:"symbol", name:"cpuRun"}` → one function's full body.
- `read {file, mode:"lines", range:"120-180"}` / `mode:"smart_range", line:150` → exact or
  context-expanded ranges. `range:"10-$"` reads to end of file.
- `read {file, mode:"section", heading:"Install"}` → a markdown section. `mode:"ls"` lists a dir.
- Re-reading a file you already saw? Pass `if_hash` with the hash from the previous read —
  unchanged files come back as `{unchanged:true}` for free.
- Small files (a screen of prose, a config) — just read them full; outline-first is for big files.

**Known limit:** a one-line arrow const (`export const f = x => …`) resolves as symbol to just its
signature line. Use `lines`/`smart_range` for those.

## Rule 3 — search with the right tool for how much you know

- You know the pattern → `faster_search {pattern, path}`. Flags: `l:true` (paths only), `c:true`
  (counts), `scope:true` (return the enclosing function instead of bare lines), `w:true`
  (whole word), `mode:"regex"`, `type:"ts"` (file-type filter), `find:true` (filename glob,
  `fuzzy:true` for typo-tolerant), `A`/`B` context lines. Unicode patterns work.
- The question is fuzzy ("where is auth handled?") → `meta_search {query, path}` — the daemon
  fans out several strategies and merges results. Once you know the exact pattern, go back to
  `faster_search`.
- You need the canonical baseline output → plain `search` (same interface).
- After a rebase / checkout / pull / any out-of-band edit → add `fresh:true` once to force a
  reindex; stale-index results are the usual cause of "it's there but search can't see it".

## Rule 4 — edit by intent, verify by diff

Pick the write tool by what you know, not by habit:

| You know… | Use |
|---|---|
| the function/type name | `edit {file, symbol:"name", content}` — survives line drift; best default for code |
| a pattern inside the target scope | `edit {file, pattern:"…", content, scope:"line"}` — **`scope:"line"` replaces only the matched lines; without it the whole enclosing function is replaced** |
| exact line numbers | `patch {file, range:"10-20", content}` (or `after:N`, `op:"insert"/"delete"`) |
| an exact sentence/string to swap (prose, comments, cross-file renames) | `replace {pattern, replacement, path, apply:true}` |
| you're creating a file | `create {file, content, parents:true}` (`force:true` overwrites, `append:true` appends) |

> **⚠ `pattern` without `scope` is a whole-function replace.** `edit` matches your text, then expands
> the replaced region to the enclosing function/block. If `content` is only the small piece you
> matched, everything else in that function — signature included — is deleted, and the call still
> reports `ok:true`. Default to **`scope:"line"`** for surgical changes; reserve bare `pattern` for
> when you *mean* to swap a whole function (and then prefer `symbol:`, which says so explicitly).

- `edit`/`patch` return the written lines — you rarely need a follow-up read.
- `replace` is **dry-run by default**: preview first, then re-send with `apply:true`. It refuses
  `path:"."` (set `allow_cwd_root` deliberately) and refuses writes touching more than 50 files
  (`max_files`/`allow_large` to override) — these guards are features; don't reflex-override them.
  `regex:true` enables backreferences in the replacement (`\1`, backslash form).
- **No shell in the loop.** Content travels as JSON: curly quotes, non-ASCII, backticks, `$` are
  all safe. This replaces python/perl heredoc surgery — and kills the classic heredoc traps
  (backticks executing, quoting mangling UTF-8).
- After edits: `diff {file}` (or `diff {stat:true}` for a summary; `staged:true` for the index).
  `lint {file}` auto-detects the project linter and returns normalized diagnostics — it returns
  `{linter:null}` when the repo has no linter config; then your verification is the test suite.

## Rule 5 — memo for anything that must survive context loss

`memo {action:"store", value:"…", tag:"findings"}` persists notes across compaction;
`action:"plan"` keeps a checklist (`check:N` marks steps done), `action:"context"` reloads after
compression. Use it for multi-hour tasks instead of re-deriving state.

## Field-tested pitfalls

- **Paths are relative to the daemon's working directory** (usually the repo root). If unsure, one
  `diff {stat:true}` echoes the cwd. Absolute paths also work.
- `replace` without `apply:true` **wrote nothing** — don't move on after a preview.
- Batch `ops` as a string instead of an array is the most common malformed call.
- Two independent facts you need → still one batch; only serialize when call B needs call A's output.
- Don't re-read a file after `edit`/`patch` "to check" — the response already contains the written
  lines; use `diff` if you want the change in context.
- **A zero-match search is a claim, not a fact — verify it with a second pattern.** `faster_search
  {pattern:"first-letter"}` returned 0 matches while `::first-letter` sat in the file (hyphenated
  patterns have misfired in the field); a search for a nearby word found it immediately. Before
  acting on "not found" (deleting a rule, skipping a rename), re-check with a different substring
  or `mode:"regex"`.
- `create` takes **`file`**, not `path` — `{file:"...", content:"...", force:true}`. Passing `path`
  fails with "missing 'file'" (read/edit/patch use `file` too; only search/replace take `path`).
- **`edit` + `pattern` replaces the WHOLE enclosing function — the #1 cause of lost code.**
  Reproduced on 0.2.10: pattern `suffix := "!"` (one line) returned `lines_removed: 5` and the diff
  deleted the entire `Greet` function, signature included. The same edit with **`scope:"line"`**
  returned `lines_removed: 1`. So: **check `lines_removed` on every edit response** — bigger than the
  line count of your pattern means the scope expanded and you clobbered neighbours. Revert and retry
  with `scope:"line"`. `dry_run:true` previews the diff without writing (costs one call, saves a
  reconstruction).
- **Don't span a doc-comment → `func` boundary in a `pattern`.** `// Greet says…\nfunc Greet(…)`
  fails with `no enclosing scope found for pattern match`: the comment sits outside the symbol's
  scope. Match from the `func` line, or use `symbol:` / `scope:"line"`.
- **You cannot force a literal search — escape instead.** `mode:"literal"` *and* `regex:false` were
  both overridden: `alpha|beta` still matched lines containing only `alpha` or only `beta`
  (`interpreted:"regex"`). Escaping worked: `alpha\|beta` matched just the literal line. Escape
  `| ( ) . * + ? [` when you want a literal substring, or add `w:true` for whole-word.
- **Absolute paths outside the repo work.** `read`/`faster_search`/`edit`/`create` all succeed on
  `/tmp`, `~/.claude`, another checkout — codedbpro is not repo-locked. A failure out there is
  usually a missing parent dir (`parents:true`) or the scope error above, not a workspace boundary.

## Minimal decision card

```
know nothing about the file      → read outline
know the function                → read symbol / edit symbol
know the exact line              → read lines / patch range
surgical change inside a func    → edit scope:"line"  (bare pattern = whole-function replace)
know the exact string            → faster_search / replace (dry-run → apply)
question is vague                → meta_search
≥2 of anything                   → batch
just rebased/pulled              → fresh:true
long task, fragile context       → memo
```
