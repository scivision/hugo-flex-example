#!/usr/bin/env python
"""
Advanced users should instead use Netlify or other CD system.

This method below keeps all the generated HTML in your Git history,
which doesn't necessarily scale well for large websites.
However, this method below is simple for small / beginning users.
"""
import subprocess
import shutil
import sys
from datetime import datetime
from pathlib import Path

R = Path(__file__).parent.resolve()

if sys.version_info < (3, 5):
    raise SystemExit("Python >= 3.5 required")

hugo = shutil.which("hugo")
if not hugo:
    raise SystemExit("Could not find Hugo")
assert isinstance(hugo, str)

git = shutil.which("git")
if not git:
    raise SystemExit("Could not find Git")
assert isinstance(git, str)

print("Deploying updates to GitHub Pages")

# Build the project.
subprocess.check_call([hugo, "--source", str(R)])

# Add changes to git.
subprocess.check_call([git, "-C", str(R), "add", "docs"])

# Commit changes.
msg = "rebuilding site {}".format(datetime.now().isoformat()[:-10])

subprocess.check_call([git, "-C", str(R), "commit", "-m", msg, "--no-verify"])

# Push source and build repos.
subprocess.check_call([git, "-C", str(R), "push"])
