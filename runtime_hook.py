import os
import sys

os.environ["QT_MAC_WANTS_LAYER"] = "1"
if getattr(sys, "frozen", False):
    base = sys._MEIPASS
    os.environ["JHORA_DATA_PATH"] = os.path.join(base, "jhora", "data")
EOF
