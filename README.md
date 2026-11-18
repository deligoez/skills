# skills

A collection of [Agent Skills](https://code.claude.com/docs/en/skills) by
[@deligoez](https://github.com/deligoez), distributed via
[`npx skills`](https://github.com/vercel-labs/skills). Each skill is a self-contained package of
domain knowledge and workflows that extends an AI coding agent (Claude Code, Codex, Cursor,
OpenCode, and others). Different skills, different topics — one repo.

## Skills in this repo

| Skill | What it does |
|-------|--------------|
| [`typography-for-lawyers`](skills/typography-for-lawyers) | Professional typography for legal and professional documents — fonts, point size, margins, line spacing, court-rule compliance, and fixing "typewriter habits" — distilled from Matthew Butterick's *Typography for Lawyers*. |
| [`turkish-humanizer`](skills/turkish-humanizer) ([README](skills/turkish-humanizer/README.md)) | Makes Turkish text read naturally — cleans AI-generated and English-translationese patterns (signpost connectors, bureaucratic `-maktadır`, `sahip olmak`, `-lı bir şekilde`, calques, em dashes) and rewrites toward fluent, TDK-correct Turkish while preserving meaning. A review mode returns positioned findings for long texts, and a regression set with held-out variants measures each rule. |
| [`codedbpro`](skills/codedbpro) | Teaches an agent to drive the codedbpro MCP toolset efficiently — batch-everything discipline, outline-first reading, symbol-safe edits, dry-run-first refactors, and the field-tested pitfalls (stale index, dry-run defaults, blast-radius guards). |
| [`digital-lexicography`](skills/digital-lexicography) | Turns an existing dictionary into structured data, audits it non-circularly, then grows it — the source-fidelity contract, entry-parsing traps, damaged-character forensics, safe merging and cross-verification, meaning-based search, and DMLex / TEI Lex-0 export. |

## Install

Install every skill in this repo to all detected agents:

```bash
npx skills add deligoez/skills --all
```

List the available skills first:

```bash
npx skills add deligoez/skills --list
```

Install a specific skill (globally, for Claude Code):

```bash
npx skills add -g deligoez/skills --skill typography-for-lawyers
```

The CLI auto-detects which agents you have installed; if none are found it will ask which to
install to. Update after new commits:

```bash
npx skills update deligoez/skills
```

## Repo layout

```
skills/
└── <skill-name>/
    ├── SKILL.md        # entry point: name, description (the trigger), and instructions
    ├── references/     # deeper docs loaded on demand
    └── evals/          # optional: regression cases and their checker, never loaded at runtime
```

Each `SKILL.md` uses progressive disclosure: the `name` + `description` are always in context, the
body loads when the skill triggers, and the `references/` files load only when the specific task
needs them.

## Contributing / building your own

These follow the standard Agent Skill format. To create or improve one, the
[skill-creator](https://code.claude.com/docs/en/skills) workflow is a good starting point. A skill
is valid as soon as it has a `SKILL.md` with `name` and `description` frontmatter.

## Credits

- `typography-for-lawyers` distills the freely available web edition of Matthew Butterick's
  [*Typography for Lawyers*](https://typographyforlawyers.com). All credit for the underlying rules
  belongs to Butterick — [buy the book](https://typographyforlawyers.com) to support the work.
- `turkish-humanizer` adapts several patterns and regression cases from Oğuzhan Kayan's
  [turkish-native](https://github.com/oguzhankayan/turkish-native) (MIT); the borrowed cases are
  marked `source: turkish-native/…` and the license notice is kept in
  [`skills/turkish-humanizer/evals/README.md`](skills/turkish-humanizer/evals/README.md).
- `turkish-humanizer` also adapts discourse-skeleton tells, genre and domain do-not-touch rules,
  narrative flow rules, an idiom list and product-copy templates from Tahir Yıldız's
  [insanca](https://github.com/tahiryildiz/insanca) (MIT), which in turn draws on
  [insanlik-oldu-mu](https://github.com/MesutARIDORU/insanlik-oldu-mu) and
  [turkish-anti-ai-skill](https://github.com/yucezerey/turkish-anti-ai-skill) (both MIT). Each
  adapted section names its source.

## License

[MIT](LICENSE) © Yunus Emre Deligöz. The license covers the skill packaging and prose in this repo,
not the third-party source material it distills or the commercial fonts it names.
