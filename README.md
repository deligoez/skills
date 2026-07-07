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
| [`turkish-humanizer`](skills/turkish-humanizer) | Makes Turkish text read naturally — cleans AI-generated and English-translationese patterns (signpost connectors, bureaucratic `-maktadır`, `sahip olmak`, `-lı bir şekilde`, calques, em dashes) and rewrites toward fluent, TDK-correct Turkish while preserving meaning. |

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
    └── references/     # deeper docs loaded on demand
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

## License

[MIT](LICENSE) © Yunus Emre Deligöz. The license covers the skill packaging and prose in this repo,
not the third-party source material it distills or the commercial fonts it names.
