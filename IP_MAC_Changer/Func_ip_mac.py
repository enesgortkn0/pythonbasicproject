import optparse
import subprocess
import re

def ip_mac_changer():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-i","--interface",dest="interface",help="Enter interface!")
    parse_object.add_option("-m","--mac",dest="mac_address",help="Enter mac address!")


    (user_inputs,_) = parse_object.parse_args()

    interface = user_inputs.interface
    mac_adress = user_inputs.mac_address
    return interface,mac_adress

def sub(interface,mac_addr):



    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_addr])
    subprocess.call(["ifconfig",interface,"up"])


def control_new_mac(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])

    mac_control = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if mac_control:
        return mac_control.group(0)
    else:
        return None


iface,mac = ip_mac_changer()
sub(iface,mac)
mac_adr = control_new_mac(iface)
if mac_adr == mac:
    print(mac_adr)

else:
    print("Mac address not changed!!!")
