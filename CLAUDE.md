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

## Skills — English by default, the target language when the skill *is* that language

Write skills in **English** by default: instructions, headings, rules, and structure. English is the
model's strongest instruction-following language and keeps the repo consistent and shareable via
`npx skills`. This covers every general-purpose skill (`codedbpro`, `typography-for-lawyers`, …).

**Exception — a skill about a natural language is authored in that language.** When the subject *and*
the output are one language, its instructions belong in that language: the prose then models the
register it is asking for, and every example is in that language anyway.
`skills/turkish-humanizer` is deliberately Turkish — that is correct, not debt.

Conversation with the user follows the user's language; that is separate from the artifact.
