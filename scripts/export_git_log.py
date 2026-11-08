"""Export a reproducible text snapshot; does not modify Git history."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def export():
    def git(*args):
        return subprocess.check_output(["git", "-C", str(ROOT), *args]).decode("utf-8")
    head = git("rev-parse", "HEAD").strip()
    history = git("log", "--date=iso-strict", "--pretty=format:%H | %aI | %an | %s")
    text = ("HW03 Git commit log\nSnapshot HEAD: " + head + "\n"
            "This snapshot includes commits through HEAD above. A later commit that stores\n"
            "this file is not included in its own snapshot.\n\n" + history + "\n")
    (ROOT / "git_commit_log.txt").write_text(text, encoding="utf-8", newline="\n")
    print("Exported Git log at " + head[:12])


if __name__ == "__main__":
    export()
