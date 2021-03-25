#!/usr/bin/python

import whois
import socket

domain = input(str('enter domain name:'))

ip = socket.gethostbyname(domain)

print(whois.whois(ip))
