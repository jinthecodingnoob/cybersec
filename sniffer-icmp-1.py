#!/usr/bin/env python3

from scapy.all import *


def print_pkt(pkt):
  print_pkt.counter += 1
  print("-------------packet: ", print_pkt.counter, "-------------")
  pkt.show()
  
print_pkt.counter=0 

#https://www.gigamon.com/content/dam/resource-library/english/guide---cookbook/gu-bpf-reference-guide-gigamon-insight.pdf

#Sniff ICMP packets 
pkt = sniff(iface=['br-f8afce37f7aa'], filter='icmp', prn=print_pkt)