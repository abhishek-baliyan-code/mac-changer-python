#!/usr/bin/env python

import subprocess
import optparse
import re

def check_mac(user_mac, system_mac):
    if (user_mac == system_mac):
        return True
    return False

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

def change_mac(interface, new_mac):
    print("Mac is changing of " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"], check=True)

def get_current_mac(interface):
    ifconfig_result = subprocess.run(["ifconfig", interface], capture_output=True)    
    ifconfig_result = ifconfig_result.stdout.decode("UTF-8")
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if current_mac:
        return current_mac.group(0)
    else:
        print("[-] Could not find MAC address")

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address has been sucessfully changed to " + current_mac)
else:
    print("[-] MAC address didn't change")

