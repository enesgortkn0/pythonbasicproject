import scapy.all as scapy
import optparse
import re

def parse_input():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-r","--range",dest="range",help="Enter range! Ex:192.168.15.0/24")

    (user_inputs, arguments) = parse_object.parse_args()

    if not user_inputs.range:
        return "Enter range IP address!"

    return user_inputs.range

def ARP_packets(rangee):

    if rangee is None:
        return "IP address not defined!"

    arp_request_packet = scapy.ARP(pdst=rangee)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combinad_packet = broadcast_packet/arp_request_packet

    (answerd,unanswerd) = scapy.srp(combinad_packet,timeout=1)

    return answerd.summary()




ARP_packets(parse_input())

