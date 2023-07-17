import os

from utils import ask_question, prompt_user, check_for_root


DHCPCD_CONF_FILE = '/etc/dhcpcd.conf'


check_for_root()

print('Enable SSH on Raspberry! It can be done using raspi-config!')
print('You should go to "Interface Options" > "SSH" > "enable"!')

raspi_config = ask_question('\nOpen raspi-config?', default_answer='y')
if raspi_config:
    os.system('sudo raspi-config')

install_hostapd = ask_question('\nInstall hostapd?', default_answer='y')
if install_hostapd:
    os.system('sudo apt install -y hostapd dnsmasq')
    os.system('sudo systemctl unmask hostapd')
    os.system('sudo systemctl enable hostapd')

set_static_ip = ask_question('\nSet static IP?', default_answer='y')
if set_static_ip:
    static_ip = prompt_user('Static IP:', '192.168.4.1/24')
    with open(DHCPCD_CONF_FILE) as file:
        file_data = file.read()

    lines_to_add = f'\ninterface wlan0\nstatic ip_address={static_ip}\nnohook wpa_supplicant'

    file_data += lines_to_add
    with open(DHCPCD_CONF_FILE, 'w') as file:
        file.write(file_data)

edit_dnsmasq_file = ask_question("\nEdit '/etc/dnsmasq.conf' file?", default_answer='y')
if edit_dnsmasq_file:
    os.system('sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig') # save original file
    print("Saved original file as '/etc/dnsmasq.conf.orig' as backup!")

    lines_to_write = "interface=wlan0\ndhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h\n"\
                    "domain=wlan\naddress=/gw.wlan/192.168.4.1"
    with open('/etc/dnsmasq.conf', 'w') as file:
        file.write(lines_to_write)

    print("Wrote following lines to '/etc/dnsmasq.conf' file:\n" + lines_to_write)

edit_hostapd_conf = ask_question("\nEdit 'hostapd.conf' file?", default_answer='y')
if edit_hostapd_conf:
    wifi_ssid = prompt_user("WiFi AP SSID:", default_answer='RPI_AVT')
    wifi_psk = prompt_user("WiFi password:", 'raspberry')
    wifi_mode = prompt_user("WiFi mode (a - 5 GHz, g - 2.4 GHz)", 'g')

    lines_to_write = 'country_code=GB\n'\
                    'interface=wlan0\n'\
                    f'ssid={wifi_ssid}\n'\
                    f'hw_mode={wifi_mode}\n'\
                    'channel=7\n'\
                    'macaddr_acl=0\n'\
                    'auth_algs=1\n'\
                    'ignore_broadcast_ssid=0\n'\
                    'wpa=2\n'\
                    f'wpa_passphrase={wifi_psk}\n'\
                    'wpa_key_mgmt=WPA-PSK\n'\
                    'wpa_pairwise=TKIP\n'\
                    'rsn_pairwise=CCMP'
    
    with open('/etc/hostapd/hostapd.conf', 'w') as file:
        file.write(lines_to_write)
    
    print("Wrote following lines to '/etc/hostapd/hostapd.conf' file:\n" + lines_to_write)


reboot_system = ask_question('\nReboot system? (Recommended!)', default_answer='yes')
if reboot_system:
    os.system('sudo systemctl reboot')
