import os
import subprocess
from uranium import task_requires


ROOT = os.path.dirname(os.path.realpath("__file__"))
WHISPER_FOR_PY3 = "https://github.com/graphite-project/whisper/tarball/feature/py3"


def main(build):
    build.packages.install(".", develop=True)


def distribute(build):
    """ distribute the uranium package """
    build.packages.install("wheel")
    build.executables.run([
        "python", "setup.py",
        "sdist", "bdist_wheel", "--universal", "upload"
    ])


@task_requires("main")
def build_docs(build):
    build.packages.install("sphinx")
    build.packages.install("sphinx_rtd_theme")
    return subprocess.call(
        ["make", "html"], cwd=os.path.join(build.root, "docs")
    )
