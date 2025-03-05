import subprocess
import optparse
import re

def Parsing_Options():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")
    return parse_object.parse_args()

def Mac_changer(interface,mac_address):
    try:
        ifconfig = subprocess.check_output(["ifconfig",interface]).decode()
        old_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)
        subprocess.call(["ifconfig",interface,"down"])
        ret_val = subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
        if ret_val != 0:
            print("Mac adress has not changed")
        else:
            subprocess.call(["ifconfig",interface,"up"])
            print("Mac address changed succesfully")

        return old_mac.group(0)

    except Exception as error:
        print(f"There is a {error} error exist")



def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface]).decode()
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
    return new_mac.group(0)


print("My Mac Changer Started")
(options,arguments) = Parsing_Options()
old_mac = Mac_changer(options.interface,options.mac_address)
new_mac = control_new_mac(options.interface)
print(f"Old Mac Address is {old_mac}")
print(f"New Mac Address is {new_mac}")
