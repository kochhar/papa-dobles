# papa-dobles

A small stdlib-only utility package, used as a workload for chaos-testing a
cloud-agent control plane. Nothing here is meant to be useful software: it is
a deterministic pile of small, independent functions that an agent can work
through one file at a time.

## The task

Most functions in `toolkit/` have no docstring. A few do, and they set the
house style: one summary line, then any detail worth knowing, in the
imperative mood.

Add a docstring to every function that does not have one. Do not change
behaviour — the suite is green before the task and must be green after it.

## Running the tests

```bash
./run_tests.sh
```

or directly:

```bash
python3 -m unittest discover -s tests -t . -q
```

Standard library only, no pytest, and it has to run on Python 3.9, so no
`match` statements and no `X | Y` annotations.

## Scoring

```bash
python3 scripts/check_docstrings.py
```

Lists every function in `toolkit/` still missing a docstring and exits
non-zero if there are any. This is how a finished branch gets scored, rather
than by trusting that the session reached `idle`.
