# Repository guidelines

## Commits — always use `hc` (hunk commits)

Create every commit in this repo with the **`hc`** tool (the hunk-commits skill), never raw
`git add` / `git commit`. `hc` splits changes into atomic, one-idea-per-commit history.

Workflow:

- Read the diff once: `hc diff --json` (includes hunk content and section — don't run `git diff`).
- Start from the mechanical draft: `hc plan > draft.json`, then replace each `TODO` with a real
  conventional-commit message.
- Execute: `hc run draft.json` (or `hc run - <<'PLAN' … PLAN`).
- **Default granularity is one file per commit.** Only a mechanical sweep (same transformation
  across files) or an inseparable change may bundle files. New tests each get their own commit.
- Re-split existing (too-coarse) commits: `hc log <base>..HEAD --json` + `hc rewrite` — conflict-free,
  keeps a backup ref. Use `--force` for commits already pushed, then `git push --force-with-lease`.

Do **not** run `git add` / `git commit` directly alongside `hc`.

## Skills — author in English

Write every skill (`SKILL.md` and its `references/`) in **English**: instructions, headings, rules,
and structure. English is the model's strongest instruction-following language, and it keeps the
repo consistent and shareable via `npx skills`.

The one exception is **target-language material**, which stays in its own language: examples, term
tables, quoted patterns, and before/after pairs. A skill *about* Turkish therefore reads as English
prose wrapped around Turkish examples — not as Turkish prose.

Conversation with the user is a separate matter and follows their language; the artifact is English.

**Known debt:** `skills/turkish-humanizer` (v2.1) is currently written mostly in Turkish and does
not follow this rule yet — normalize it to English framing on the next substantial edit.
