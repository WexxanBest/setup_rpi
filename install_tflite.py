import os

commands = [
    "pip3 install tflite-runtime"
]

for cmd in commands:
    print(f"Running '{cmd}'...")
    os.system(cmd)
