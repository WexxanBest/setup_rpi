import os

from utils import check_for_root


check_for_root()

commands = [
    "sudo apt update",
    "sudo apt install build-essential cmake libgtk-3-dev libboost-all-dev libatlas-base-dev",
    "pip3 install dlib"
]

for cmd in commands:
    print(f"Running '{cmd}'...")
    os.system(cmd)
