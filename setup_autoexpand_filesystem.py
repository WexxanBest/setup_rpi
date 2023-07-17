from utils import check_for_root


check_for_root()

with open('/boot/cmdline.txt') as file:
    old_data = file.read().strip()

line_to_add = 'init=/usr/lib/raspi-config/init_resize.sh'
new_data = f'{old_data} {line_to_add}'

with open('/boot/cmdline.txt', 'w') as file:
    file.write(new_data)
