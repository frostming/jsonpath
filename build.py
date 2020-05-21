"""
This script is run by poetry when building from source.

The function signature is fixed to ``def build(params)``, where ``params`` is the
kwargs dictionary passed to ``setuptools.setup()``.
"""


def build(setup_kwargs):
    import sys
    import subprocess

    output = subprocess.check_output(
        args=[
            sys.executable,
            "-m",
            "lark.tools.standalone",
            "jsonpath/grammar.lark",
        ]
    )
    with open("jsonpath/lark_parser", "wb") as f:
        f.write(output)
