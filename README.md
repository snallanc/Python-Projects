# Python-Projects
This repo has data structures, algorithms and coding examples implemented in Python

## Revision Coverage Guardrail

This repo includes an automated check to ensure every .py file under algorithms/ is represented in the single source of truth summary file:
- revision_summary.txt

Interview problems are organized into pattern/data-structure folders under algorithms/interview_problems (for example: dp, two_pointers, sliding_window). The summary also tracks counts per interview pattern folder.

### Run manually

python scripts/check_revision_coverage.py

### Enable local git hooks

git config core.hooksPath .githooks

After this is set once, the check runs automatically on commit and push.

### CI enforcement

GitHub Actions also runs the same check on every push and pull request.
