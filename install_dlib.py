import os

from utils import check_for_root, prompt_user, ask_question


check_for_root()

# --- SWAP --- #
swapfile = '/etc/dphys-swapfile'
swap_changed = False
line_num = -1
old_swapsize = 0

with open(swapfile) as file:
    swapfile_lines = file.read().splitlines()

for i, line in enumerate(swapfile_lines):
    if line.startswith('CONF_SWAPSIZE'):
        old_swapsize = int(line.split('=')[1].strip())
        line_num = i
        break

if old_swapsize < 1024:
    print(f'Recommended size of swap for compiling dlib is at least 1024MB, but you have {old_swapsize}MB!')
    
    if ask_question('Change swap size?', default_answer='yes'):
        new_swapsize = int(prompt_user('Enter new size of swap in MB', default_answer='1024'))
        swapfile_lines[line_num] = f'CONF_SWAPSIZE={new_swapsize}'
        with open(swapfile, 'w') as file:
            file.write('\n'.join(swapfile_lines))
        os.system('sudo dphys-swapfile swapoff; sudo dphys-swapfile setup; sudo dphys-swapfile swapon')
        print('Swap was changed!\n')
        swap_changed = True
# --- SWAP --- #


# --- INSTALLING --- #
commands = [
    "sudo apt update",
    "sudo apt install -y build-essential cmake libgtk-3-dev libboost-all-dev libatlas-base-dev",
    "sudo apt install -y libavdevice-dev libavfilter-dev libavformat-dev libavcodec-dev libswresample-dev libswscale-dev libavutil-dev",
    "pip3 install dlib"
]

for cmd in commands:
    print(f"Running '{cmd}'...")
    os.system(cmd)
    print()
# --- INSTALLING --- #


# --- SWAP --- #
if swap_changed:
    if ask_question(f'Change swap size back ({new_swapsize}MB -> {old_swapsize}MB)?', default_answer='yes'):
        swapfile_lines[line_num] = f'CONF_SWAPSIZE={old_swapsize}'
        with open(swapfile, 'w') as file:
            file.write('\n'.join(swapfile_lines))
        os.system('sudo dphys-swapfile swapoff; sudo dphys-swapfile setup; sudo dphys-swapfile swapon')
        print('Swap was changed!\n')
# --- SWAP --- #