from shutil import copy
from pathlib import Path

from utils import check_for_root


check_for_root()

motd_file = Path(__file__).parent / 'motd'
copy(motd_file, '/etc/motd')
