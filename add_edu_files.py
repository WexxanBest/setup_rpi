from pathlib import Path
import shutil

print(f"Copying files to '{Path.home()}'...")

base_dir = Path(__file__).parent / 'base'
shutil.copytree(base_dir, Path.home() / 'base')
