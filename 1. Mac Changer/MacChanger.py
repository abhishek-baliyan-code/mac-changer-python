#!/usr/bin/env python

import subprocess
import optparse

def check_mac(user_mac, system_mac):
    if (user_mac == system_mac):
        return True
    return false

def read_mac(interface):
    # read
    shell_output = subprocess.run(["ifconfig", interface], capture_output=True)    
    # Select stdout, decode byte to str
    stdout_str = shell_output.stdout.decode("UTF-8")
    #  find index of "ether"
    index = stdout_str.find("ether")
    #  get the mac using string slice
    mac = stdout_str[index + 6:index + 6 + 17]
    return mac


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an Interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC, use --help for more info.")
    return options

# def change_mac(interface, new_mac):
#     print("Mac is changing of " + interface + " to " + new_mac)
#     subprocess.run(["ifconfig", interface, "down"])
#     subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
#     subprocess.run(["ifconfig", interface, "up"], check=True)

# change_mac(options.interface, options.new_mac)

options = get_arguments()
# change_mac(options.interface, options.new_mac)

mac_address = read_mac(options.interface)

# str_decode = command_output.decode("UTF-8")

print(type(mac_address))
# print(command_output.decode("UTF-8"))

print(type(mac_address), type(options.new_mac))
