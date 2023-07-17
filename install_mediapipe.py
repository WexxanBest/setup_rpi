import os


commands = [
    "pip install opencv-contrib-python",
    "pip install mediapipe",
    "pip uninstall protobuf",
    "pip install protobuf==3.20.0"
]

for cmd in commands:
    print(f"Running '{cmd}'...")
    os.system(cmd)
