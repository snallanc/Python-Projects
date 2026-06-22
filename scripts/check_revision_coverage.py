from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ALGO_GROUPS = {
    "interview_problems": Path("algorithms/interview_problems"),
    "searching": Path("algorithms/searching"),
    "sorting": Path("algorithms/sorting"),
    "traversals": Path("algorithms/traversals"),
}
INTERVIEW_ROOT = ALGO_GROUPS["interview_problems"]

SUMMARY_FILE = Path("revision_summary.txt")

FILE_ROW_RE = re.compile(r"^\s*([A-Za-z0-9_./-]+\.py)\s*\|")
CHECKLIST_ROW_RE = re.compile(
    r"^\s*algorithms/(interview_problems|searching|sorting|traversals)\s*:\s*(\d+)\s*/\s*(\d+)\s+covered\s*$"
)
PATTERN_COVERAGE_ROW_RE = re.compile(
    r"^\s*interview_problems/([A-Za-z0-9_\-]+)\s*:\s*(\d+)\s+problems?\s*$"
)


def python_files_in_dir(base: Path, folder: Path) -> set[str]:
    target = base / folder
    if not target.exists():
        return set()
    return {p.name for p in target.glob("*.py") if p.is_file()}


def interview_problem_paths(base: Path) -> set[str]:
    root = base / INTERVIEW_ROOT
    if not root.exists():
        return set()
    paths = set()
    for p in root.rglob("*.py"):
        if p.is_file():
            paths.add(p.relative_to(root).as_posix())
    return paths


def interview_pattern_counts(base: Path) -> dict[str, int]:
    root = base / INTERVIEW_ROOT
    counts: dict[str, int] = {}
    if not root.exists():
        return counts

    for child in root.iterdir():
        if child.is_dir():
            count = sum(1 for p in child.rglob("*.py") if p.is_file())
            if count > 0:
                counts[child.name] = count
    return counts


def summary_filenames(summary_text: str) -> set[str]:
    names: set[str] = set()
    for line in summary_text.splitlines():
        match = FILE_ROW_RE.match(line)
        if match:
            names.add(match.group(1))
    return names


def checklist_counts(summary_text: str) -> dict[str, tuple[int, int]]:
    counts: dict[str, tuple[int, int]] = {}
    for line in summary_text.splitlines():
        match = CHECKLIST_ROW_RE.match(line)
        if match:
            group = match.group(1)
            left = int(match.group(2))
            right = int(match.group(3))
            counts[group] = (left, right)
    return counts


def pattern_coverage_counts(summary_text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for line in summary_text.splitlines():
        match = PATTERN_COVERAGE_ROW_RE.match(line)
        if match:
            folder = match.group(1)
            count = int(match.group(2))
            counts[folder] = count
    return counts


def validate_summary(base: Path, summary_path: Path) -> int:
    full_path = base / summary_path
    if not full_path.exists():
        print(f"ERROR: Summary file not found: {summary_path}")
        return 1

    text = full_path.read_text(encoding="utf-8")
    listed_entries = summary_filenames(text)

    missing_by_group: dict[str, list[str]] = {}
    total_missing = 0

    for group, folder in ALGO_GROUPS.items():
        if group == "interview_problems":
            actual_files = interview_problem_paths(base)
        else:
            actual_files = python_files_in_dir(base, folder)

        missing = sorted(name for name in actual_files if name not in listed_entries)
        if missing:
            missing_by_group[group] = missing
            total_missing += len(missing)

    if total_missing:
        print(f"\nCoverage check failed for {summary_path}:")
        for group, missing_names in missing_by_group.items():
            print(f"  - algorithms/{group} missing entries: {', '.join(missing_names)}")
        return 1

    checklist = checklist_counts(text)
    expected_groups = set(ALGO_GROUPS.keys())
    missing_checklist_groups = sorted(expected_groups.difference(checklist.keys()))
    if missing_checklist_groups:
        print(f"\nCoverage check failed for {summary_path}:")
        print(
            "  - Missing checklist rows for groups: "
            + ", ".join(f"algorithms/{g}" for g in missing_checklist_groups)
        )
        return 1

    checklist_errors: list[str] = []
    for group, folder in ALGO_GROUPS.items():
        if group == "interview_problems":
            actual_count = len(interview_problem_paths(base))
        else:
            actual_count = len(python_files_in_dir(base, folder))
        left, right = checklist[group]
        if left != actual_count or right != actual_count:
            checklist_errors.append(
                f"algorithms/{group} expected {actual_count}/{actual_count}, found {left}/{right}"
            )

    if checklist_errors:
        print(f"\nCoverage check failed for {summary_path}:")
        for err in checklist_errors:
            print(f"  - {err}")
        return 1

    expected_pattern_counts = interview_pattern_counts(base)
    actual_pattern_counts = pattern_coverage_counts(text)

    missing_pattern_rows = sorted(
        set(expected_pattern_counts.keys()).difference(actual_pattern_counts.keys())
    )
    if missing_pattern_rows:
        print(f"\nCoverage check failed for {summary_path}:")
        print(
            "  - Missing interview pattern coverage rows: "
            + ", ".join(f"interview_problems/{p}" for p in missing_pattern_rows)
        )
        return 1

    pattern_errors: list[str] = []
    for pattern, expected_count in expected_pattern_counts.items():
        found_count = actual_pattern_counts.get(pattern)
        if found_count != expected_count:
            pattern_errors.append(
                f"interview_problems/{pattern} expected {expected_count} problems, found {found_count}"
            )

    if pattern_errors:
        print(f"\nCoverage check failed for {summary_path}:")
        for err in pattern_errors:
            print(f"  - {err}")
        return 1

    print(f"Coverage check passed for {summary_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate that revision summaries include all algorithms files and checklist counts."
    )
    parser.add_argument(
        "--base",
        default=".",
        help="Repository root path (default: current directory).",
    )
    args = parser.parse_args()

    base = Path(args.base).resolve()

    result = validate_summary(base, SUMMARY_FILE)

    if result:
        print("\nTip: Update revision_summary.txt")
    return result


if __name__ == "__main__":
    sys.exit(main())
