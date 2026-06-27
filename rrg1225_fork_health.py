from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "requirements.txt",
    "conf.py",
    "index.rst",
    "CONTRIBUTING.md",
    "docs/RRG1225_FORK_OPERATIONS.md",
]


def main() -> None:
    problems: list[str] = []
    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            problems.append(f"missing {rel_path}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "PyTorch Tutorials" not in readme:
        problems.append("README does not identify the upstream PyTorch Tutorials project")

    if problems:
        for problem in problems:
            print(f"[fork-health] {problem}")
        raise SystemExit(1)

    print("[fork-health] PyTorch tutorials fork health checks passed")


if __name__ == "__main__":
    main()
