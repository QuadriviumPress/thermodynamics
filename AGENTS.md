# AGENTS.md

## Standard

This book follows the [QuadriviumPress MyST baseline](https://github.com/QuadriviumPress/bindery/blob/main/doc/myst-baseline.md) and the [presentation skill](https://github.com/QuadriviumPress/bindery/blob/main/skills/quadrivium-myst-presentation/SKILL.md).

## Commands

```bash
npm run start
npm run build
npm run verify
npm run check
npm run convert
```

`npm run check` is the production-equivalent verification and HTML build.

## Intentional differences

- `verify` runs `python3 scripts/verify_book.py`.
- `convert` (`sh scripts/build.sh`) rebuilds the book from the source edition. It is not part of `check`.
- Front and back matter are split out of `chapters/`.

## Presentation gap

Worked examples are `{prf:example}`. Problems are `{exercise}` with a manual enumerator, and answers are an `{admonition}` Answer dropdown rather than `{solution}`. Source numbering is kept until a later presentation pass.
