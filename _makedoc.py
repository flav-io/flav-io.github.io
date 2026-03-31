#!/usr/bin/env python3
"""Generate API documentation using pdoc3.

Creates a temporary virtualenv with a clean (non-editable) install of flavio
and pdoc3, then runs pdoc to generate HTML docs. This avoids issues with
untracked files in the editable flavio source tree.
"""

import subprocess
import sys
import os
import tempfile
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FLAVIO_REPO = os.path.expanduser("~/Repositories/flavio")


def main():
    with tempfile.TemporaryDirectory(prefix="makedoc_") as tmpdir:
        venv_dir = os.path.join(tmpdir, "venv")
        python = os.path.join(venv_dir, "bin", "python")

        print("Creating temporary virtualenv...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])

        print("Installing flavio and pdoc3...")
        # Install from git to get only tracked files (avoids untracked .py files)
        subprocess.check_call([python, "-m", "pip", "install", "--quiet",
                               f"git+file://{FLAVIO_REPO}", "pdoc3",
                               "matplotlib"])

        print("Running _flaviomake.py...")
        subprocess.check_call([python, os.path.join(SCRIPT_DIR, "_flaviomake.py")],
                              cwd=SCRIPT_DIR)

        print("Running pdoc...")
        # Use a helper script inside the venv to apply the citations workaround
        helper = os.path.join(tmpdir, "_pdoc_helper.py")
        with open(helper, "w") as f:
            f.write(HELPER_SCRIPT)

        subprocess.check_call([python, helper], cwd=SCRIPT_DIR)

    print("Done.")


HELPER_SCRIPT = r"""
import sys
import inspect
from types import ModuleType

import pdoc
import pdoc.cli

# Monkey-patch pdoc.import_module to handle flavio.citations replacing itself
# in sys.modules with a Citations instance instead of a module.
_orig_import_module = pdoc.import_module

def _import_module(module, reload=False, skip_errors=False):
    if isinstance(module, str):
        existing = sys.modules.get(module)
        if existing is not None and not inspect.ismodule(existing):
            dummy = ModuleType(module)
            dummy.__doc__ = f"(skipped: replaced by {type(existing).__name__})"
            dummy.__path__ = []
            dummy.__package__ = module
            sys.modules[module] = dummy
    return _orig_import_module(module, reload=reload, skip_errors=skip_errors)

pdoc.import_module = _import_module

sys.argv = [
    "pdoc",
    "flavio",
    "--html",
    "--output-dir", "apidoc",
    "--force",
]
pdoc.cli.main()
"""


if __name__ == "__main__":
    main()
