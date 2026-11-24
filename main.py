"""conf-1125: whisper one line into the output dir; gate 1..200."""

import json
import os

ROOF = 200


def whisper_in(folder):
    throat = os.path.join(folder, "entry.txt")
    lungs = open(throat, encoding="utf-8")
    air = lungs.read().strip()
    lungs.close()
    if not air:
        raise LookupError("nothing to confess")
    return air


def whisper_out(folder, secret):
    ear = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    if not os.path.isdir(ear):
        os.makedirs(ear, exist_ok=True)
    mouth = os.path.join(ear, "entry.txt")
    handle = open(mouth, "w", encoding="utf-8", newline="\n")
    handle.write(secret + "\n")
    handle.close()
    return mouth


secret = whisper_in(os.path.dirname(os.path.abspath(__file__)))
if len(secret) > ROOF:
    raise SystemExit("the secret does not fit: %d chars" % len(secret))
mouth = whisper_out(os.path.dirname(os.path.abspath(__file__)), secret)
print(json.dumps({"whisper": secret[:44], "decibels": len(secret), "latency": "theatrical", "mouth": mouth}))
