"""Copy the entry image to the output directory (stdlib only, no network)."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
with open(OUT, "rb") as f:
    assert f.read(8) == b"\x89PNG\r\n\x1a\n", "output is not a PNG"
print("wrote", OUT)
