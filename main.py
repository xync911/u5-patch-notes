"""Copy entry.txt to the output directory for the make.fun entry.

The entry is one line, at most 160 characters: a software patch
note for a bug in real life, in the terse register of a real
release note.
v2.4.2 fixes Monday arriving before the weekend finished loading,
with a known issue: the weekend is still buffering. The bug is
universal, the fix is honest, and the known issue is the joke.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
