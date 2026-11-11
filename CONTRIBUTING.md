# Contributing

Open a GitHub issue to report a bug or suggest an improvement. For a geometry
bug, include a small synthetic example with the voxel index, spacing, origin,
expected result and actual result. Include your Python version and operating
system so someone else can reproduce it.

For a code change, open a pull request into `main`. Explain the reason for the
change and update the tests when the expected behaviour changes. State the
coordinate order and units for any new geometry function. Use synthetic data
for examples and tests.

Before opening the pull request, run these commands from the repository root.

```shell
python -m unittest -v
python example.py
```

GitHub Actions also runs these checks on Windows and Ubuntu.
