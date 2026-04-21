# Creates a zip file to upload as a BioT plugin.
# Run from the plugin root: `python scripts/pack.py`.
#
# Downloads Linux wheels for the Lambda's Python runtime directly (NOT a local
# venv), so C-extension packages like cffi/cryptography land as Linux .so files
# compatible with the Lambda runtime — even when packing from macOS or a host
# Python version that differs from the Lambda's.

import os
import shutil
import subprocess
import sys
import traceback

TARGET_PY = "3.13"  # Lambda runtime Python version; pip resolves wheels for this target
LAMBDA_PLATFORM = "manylinux2014_x86_64"  # change to manylinux2014_aarch64 for arm64 Lambdas
PACKAGE_DIR = "package"
REQUIREMENTS_FILE = "requirements.txt"


def install_linux_deps():
    if os.path.isdir(PACKAGE_DIR):
        shutil.rmtree(PACKAGE_DIR)
    os.makedirs(PACKAGE_DIR)
    print(f"Installing {LAMBDA_PLATFORM} wheels for python{TARGET_PY} into {PACKAGE_DIR}/")
    subprocess.run(
        [
            sys.executable, "-m", "pip", "install",
            "--platform", LAMBDA_PLATFORM,
            "--target", PACKAGE_DIR,
            "--implementation", "cp",
            "--python-version", TARGET_PY,
            "--only-binary=:all:",
            "--upgrade",
            "-q",
            "-r", REQUIREMENTS_FILE,
        ],
        check=True,
    )


try:
    install_linux_deps()

    print("Copy src directory")
    shutil.copytree("./src", os.path.join(PACKAGE_DIR, "src"))

    print("Copy index.py")
    shutil.copyfile("./index.py", os.path.join(PACKAGE_DIR, "index.py"))

    print("Zip")
    shutil.make_archive("plugin", "zip", PACKAGE_DIR)

    shutil.rmtree(PACKAGE_DIR)

except Exception:
    if os.path.isdir(PACKAGE_DIR):
        shutil.rmtree(PACKAGE_DIR)
    print("packing plugin failed with error: ", traceback.format_exc())
