#!/usr/bin/python3.9

import socket

from ip2geotools.databases.noncommercial import DbIpCity
def ip_inf():

        ip = input(str('enter ip address:'))
        response = DbIpCity.get(ip, api_key='free')
        print(f'IP: {ip}')
        print(f'COUNTRY: {response.country}')
        print(f'CITY: {response.city}')
        print(f'LATITUDE: {response.latitude}')
        print(f'LONGTITUDE: {response.longitude}')
ip_inf()
