#!/usr/bin/env python3

from scapy.all import *

print("----------- sending spoofing packets -------")
a = IP()


a.src = '8.8.8.8'
a.dst = '10.9.0.5'
b = ICMP()

pkt = a/b
pkt.show()
send(pkt)
ls(a)
