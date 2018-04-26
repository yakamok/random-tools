from scapy.all import *
import socket
import time

interface_name = "eth0"

file_dump = "dns-dump"
if os.path.exists(file_dump) != True:
	open(file_dump,'w').close()

def find_dns_requests(pkt): #checking to see if any dns requests found then record them to file
	if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
		with open("dns-dump","a") as handle:
			handle.write(str(pkt.getlayer(DNS).qd.qname) + " -- " + str(pkt.addr2)  + " -- " + str(pkt.getlayer(IP).src) + "\n")
		print str(pkt.getlayer(DNS).qd.qname) + " -- " + str(pkt.addr2)  + " -- " + str(pkt.getlayer(IP).src) + " -- " + str(datetime.datetime.now()) + "\n"

sniff(iface=interface_name, prn = find_dns_requests, filter = 'dst port 53 ',store=0)
