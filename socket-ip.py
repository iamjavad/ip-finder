#!/usr/bin/python3.9
print('''
======================================================================
###   ######          #######   ###   #     # ######  ####### ######
 #    #     #         #          #    ##    # #     # #       #     #
 #    #     #         #          #    # #   # #     # #       #     #
 #    ######          #####      #    #  #  # #     # #####   ######
 #    #               #          #    #   # # #     # #       #   #
 #    #               #          #    #    ## #     # #       #    #
###   #               #         ###   #     # ######  ####### #     #

======================================================================
''')
import socket
#import whois
host = input(str('enter domain name:'))
#domain = whois.query(host)
def get_ip(host):
    print(f'IP: {socket.gethostbyname(host)}')
    #print(socket.gethostbyname_ex(host))
    #print(f'expiration day: {domain.expiration_date}')
    #print(f'registrar: {domain.registrar}')
    #print(f'name servers: {domain.name_servers}')
get_ip(host)

