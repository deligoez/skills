#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6,<7"]
# ///
"""turkish-humanizer regression set: validate the cases, emit prompts, score outputs.

    uv run evals/check.py validate
    uv run evals/check.py prompts > prompts.jsonl
    uv run evals/check.py score outputs.jsonl

See evals/README.md for the case schema and a runner example.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

EVALS = Path(__file__).resolve().parent
SKILL = EVALS.parent
CASES = EVALS / "cases"

KINDS = {"fix", "control"}
MODES = {"rewrite", "review"}
CHECKS = (
    "expected",
    "expected_contains",
    "expected_not_contains",
    "expected_sentences",
    "expected_max_sentences",
    "expected_property",
)
FIELDS = {"id", "source", "ref", "kind", "mode", "input", "context", *CHECKS}
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Reference files that teach by worked example rather than by rule need no case of their own.
UNCOVERED_OK = {"references/examples.md"}
MIN_CONTROL_SHARE = 0.2


def tr_lower(text: str) -> str:
    """Lowercase with Turkish dotted/dotless I, so 'Işık' matches 'ışık' and 'İl' matches 'il'."""
    return text.replace("I", "ı").replace("İ", "i").lower()


def count_sentences(text: str) -> int:
    # A terminal mark followed by whitespace ends a sentence; 14.30 and 4,8 have no space after
    # the mark, so they do not split.
    return len([p for p in re.split(r"(?<=[.!?…])\s+", text.strip()) if p.strip()])


def _norm(text: str) -> str:
    return " ".join(tr_lower(re.sub(r"[*_`]", "", text)).split())


def skill_text() -> str:
    files = [SKILL / "SKILL.md", *sorted((SKILL / "references").glob("*.md"))]
    return _norm("\n".join(f.read_text(encoding="utf-8") for f in files))


def is_seen(case: dict, corpus: str) -> bool:
    """True when a line of the input is quoted in SKILL.md or a reference.

    Such a case can pass by recalling the worked example, so it measures memory of the example
    more than grasp of the rule. Lines under 12 characters (Hizmetler, Kaydetmek) are too common
    to tell.
    """
    for line in case["input"].splitlines():
        key = _norm(line).strip(" .!?:;")
        if len(key) >= 12 and key in corpus:
            return True
    return False


def unwrap(text: str) -> str:
    match = re.search(r"<metin>\s*(.*?)\s*</metin>", text, re.S)
    return (match.group(1) if match else text).strip()


def load() -> list[tuple[Path, dict]]:
    cases = []
    for path in sorted(CASES.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as error:
            sys.exit(f"ERROR: {path.name}: {error}")
        for case in data.get("cases") or []:
            cases.append((path, case))
    return cases


def refs_of(case: dict) -> list[str]:
    ref = case.get("ref")
    return ref if isinstance(ref, list) else [ref]


def validate(cases: list[tuple[Path, dict]]) -> list[str]:
    errors = []
    seen: set[str] = set()
    covered: set[str] = set()

    for path, case in cases:
        where = f"{path.name}:{case.get('id', '?')}"
        if not isinstance(case, dict):
            errors.append(f"{path.name}: case is not a mapping")
            continue

        for key in sorted(set(case) - FIELDS):
            errors.append(f"{where}: unknown field '{key}'")

        cid = case.get("id")
        if not isinstance(cid, str) or not ID_RE.match(cid):
            errors.append(f"{where}: id must be kebab-case")
        elif cid in seen:
            errors.append(f"{where}: duplicate id")
        else:
            seen.add(cid)

        if not case.get("source"):
            errors.append(f"{where}: source is required")

        for ref in refs_of(case):
            if not isinstance(ref, str) or not (SKILL / ref).is_file():
                errors.append(f"{where}: ref '{ref}' does not exist")
            else:
                covered.add(ref)

        kind = case.get("kind")
        if kind not in KINDS:
            errors.append(f"{where}: kind must be one of {sorted(KINDS)}")
        if case.get("mode", "rewrite") not in MODES:
            errors.append(f"{where}: mode must be one of {sorted(MODES)}")

        text = case.get("input")
        if not isinstance(text, str) or not text.strip():
            errors.append(f"{where}: input is required")
            continue

        if not any(key in case for key in CHECKS):
            errors.append(f"{where}: needs at least one expected_* check")

        for key in ("expected_contains", "expected_not_contains"):
            value = case.get(key)
            if value is not None and not (isinstance(value, list) and all(isinstance(v, str) for v in value)):
                errors.append(f"{where}: {key} must be a list of strings")
        for key in ("expected_sentences", "expected_max_sentences"):
            value = case.get(key)
            if value is not None and not (isinstance(value, int) and value > 0):
                errors.append(f"{where}: {key} must be a positive integer")

        if kind == "control" and case.get("expected") != text:
            errors.append(f"{where}: a control must have expected equal to input")
        if kind == "fix":
            if case.get("expected") == text:
                errors.append(f"{where}: a fix whose expected equals input tests nothing; make it a control")
            # At least one forbidden string must be in the input, or the case removes nothing. The
            # rest may be traps the fix itself tends to introduce (dünyaya verdin → toprağa verdin).
            banned = case.get("expected_not_contains") or []
            if banned and not any(tr_lower(n) in tr_lower(text) for n in banned):
                errors.append(f"{where}: no expected_not_contains string occurs in the input")

    for ref in sorted(p.relative_to(SKILL).as_posix() for p in (SKILL / "references").glob("*.md")):
        if ref not in covered and ref not in UNCOVERED_OK:
            errors.append(f"coverage: no case references {ref}")
    if "SKILL.md" not in covered:
        errors.append("coverage: no case references SKILL.md")

    controls = sum(1 for _, c in cases if isinstance(c, dict) and c.get("kind") == "control")
    if cases and controls / len(cases) < MIN_CONTROL_SHARE:
        errors.append(f"controls are {controls}/{len(cases)}; keep at least {MIN_CONTROL_SHARE:.0%}")

    return errors


def prompt_for(case: dict) -> str:
    context = f"Bağlam: {case['context'].strip()}\n" if case.get("context") else ""
    if case.get("mode") == "review":
        task = (
            "turkish-humanizer skill'ini inceleme kipinde kullan. Metni yeniden yazma; "
            "yalnızca konumlu bulgu tablosunu döndür."
        )
    else:
        task = (
            "turkish-humanizer skill'ini yeniden yazma kipinde kullan. "
            "Yalnızca düzeltilmiş metni <metin>...</metin> içinde döndür."
        )
    return f"{task}\n{context}\n<metin>\n{case['input']}\n</metin>"


def score_case(case: dict, raw: str) -> tuple[str, list[str]]:
    out = unwrap(raw)
    low = tr_lower(out)
    failures = []

    if "expected" in case and " ".join(out.split()) != " ".join(case["expected"].split()):
        failures.append(f"expected {case['expected']!r}, got {out!r}")
    for needle in case.get("expected_contains") or []:
        if tr_lower(needle) not in low:
            failures.append(f"missing {needle!r}")
    for needle in case.get("expected_not_contains") or []:
        if tr_lower(needle) in low:
            failures.append(f"still contains {needle!r}")
    if "expected_sentences" in case and count_sentences(out) != case["expected_sentences"]:
        failures.append(f"{count_sentences(out)} sentences, expected {case['expected_sentences']}")
    if "expected_max_sentences" in case and count_sentences(out) > case["expected_max_sentences"]:
        failures.append(f"{count_sentences(out)} sentences, max {case['expected_max_sentences']}")

    if failures:
        return "fail", failures
    if "expected_property" in case:
        return "judge", [case["expected_property"]]
    return "pass", []


def cmd_validate(_: argparse.Namespace) -> int:
    cases = load()
    errors = validate(cases)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    controls = sum(1 for _, c in cases if c["kind"] == "control")
    files = len({p for p, _ in cases})
    corpus = skill_text()
    fixes = [c for _, c in cases if c["kind"] == "fix"]
    unseen = sum(1 for c in fixes if not is_seen(c, corpus))
    print(f"OK: {len(cases)} cases in {files} files, {controls} controls, every reference covered")
    print(f"    {unseen}/{len(fixes)} fixes use an input the skill text does not quote")
    return 0


def cmd_prompts(_: argparse.Namespace) -> int:
    for _, case in load():
        print(json.dumps({"id": case["id"], "prompt": prompt_for(case)}, ensure_ascii=False))
    return 0


def cmd_score(args: argparse.Namespace) -> int:
    outputs = {}
    for line in Path(args.outputs).read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            outputs[row["id"]] = row["output"]

    corpus = skill_text()
    results = []
    for _, case in load():
        if case["id"] not in outputs:
            results.append((case, "missing", []))
            continue
        status, notes = score_case(case, outputs[case["id"]])
        results.append((case, status, notes))

    if args.json:
        for case, status, notes in results:
            row = {"id": case["id"], "kind": case["kind"], "seen": is_seen(case, corpus), "status": status, "notes": notes}
            print(json.dumps(row, ensure_ascii=False))
    else:
        for case, status, notes in results:
            if status != "pass":
                print(f"{status.upper():7} {case['id']}: {'; '.join(notes)}")

    def tally(keep) -> str:
        rows = [s for c, s, _ in results if keep(c)]
        parts = [f"{rows.count(s)} {s}" for s in ("pass", "judge", "fail", "missing") if rows.count(s)]
        return f"{', '.join(parts)} of {len(rows)}"

    counts = {s: sum(1 for _, st, _ in results if st == s) for s in ("fail", "missing")}
    print(
        f"\nfixes, input quoted in the skill: {tally(lambda c: c['kind'] == 'fix' and is_seen(c, corpus))}"
        f"\nfixes, input not quoted:         {tally(lambda c: c['kind'] == 'fix' and not is_seen(c, corpus))}"
        f"\ncontrols:                        {tally(lambda c: c['kind'] == 'control')}",
        file=sys.stderr,
    )
    return 1 if counts["fail"] or counts["missing"] else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="check case schema, ids, refs, coverage and control share")
    sub.add_parser("prompts", help="emit one JSON line per case: {id, prompt}")
    score = sub.add_parser("score", help="score a JSONL file of {id, output} rows")
    score.add_argument("outputs")
    score.add_argument("--json", action="store_true", help="one JSON line per case")
    args = parser.parse_args()
    return {"validate": cmd_validate, "prompts": cmd_prompts, "score": cmd_score}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
