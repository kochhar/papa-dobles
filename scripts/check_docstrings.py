#!/usr/bin/env python3
"""Score a branch: every function in toolkit/ must have a docstring.

Exits non-zero listing what is still missing, so a finished agent branch can
be checked out and graded without trusting that the session reached `idle`.
"""

import ast
import pathlib
import sys

PACKAGE = pathlib.Path(__file__).resolve().parent.parent / "toolkit"


def undocumented(path):
    tree = ast.parse(path.read_text(), str(path))
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if ast.get_docstring(node) is None:
            yield node.lineno, node.name


def main():
    missing = []
    total = 0
    for path in sorted(PACKAGE.glob("*.py")):
        found = list(undocumented(path))
        total += sum(
            1
            for node in ast.walk(ast.parse(path.read_text(), str(path)))
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        )
        for lineno, name in found:
            missing.append("{}:{} {}".format(path.name, lineno, name))

    documented = total - len(missing)
    print("{}/{} functions documented".format(documented, total))

    for item in missing:
        print("  missing: " + item)

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
