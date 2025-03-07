import scapy.all as scapy
from optparse import OptionParser

# 1)arp_request
# 2)broad_cast
# 3)response

def Opt_parse():
    parser = OptionParser()
    parser.add_option("-I","--ipdest",dest="ipdest")
    return parser.parse_args()

def Arp_pack_prep(ipdest):

    arp_request_packet = scapy.ARP(pdst=ipdest)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    return combined_packet

(options,args) = Opt_parse()
Arp_packet = Arp_pack_prep(options.ipdest)

(answered_list,unanswered_list) = scapy.srp(Arp_packet,timeout=1)
answered_list.summary()

