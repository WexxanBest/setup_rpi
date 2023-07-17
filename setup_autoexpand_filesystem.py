import os

from utils import check_for_root


check_for_root()

def change_cmdline_file():
    with open('/boot/cmdline.txt') as file:
        old_data = file.read().strip()

    line_to_add = 'init=/usr/lib/raspi-config/init_resize.sh'
    new_data = f'{old_data} {line_to_add}'

    with open('/boot/cmdline.txt', 'w') as file:
        file.write(new_data)

print("Changing '/boot/cmdline.txt' file...")
change_cmdline_file()

print("Downloading 'resize2fs_once' file...")
os.system('sudo wget -O /etc/init.d/resize2fs_once https://raw.githubusercontent.com/RPi-Distro/pi-gen/master/stage2/01-sys-tweaks/files/resize2fs_once')

print("Make it runnable and enable service...")
os.system('sudo chmod +x /etc/init.d/resize2fs_once')
os.system('sudo systemctl enable resize2fs_once')
