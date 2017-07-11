#!/bin/env python

import re

def parser (ip, username, password, response_string):

        network_device = {}

        network_device['ip'] = ip
        network_device['username'] = username
        network_device['password'] = password

        class Uptime(object):
                def __init__(self, uptime_string):
                        self.uptime = uptime_string
                        years = re.search(r" (\d+?) year", self.uptime)
                        if years:
                                self.years = years.group(1)
                        weeks = re.search(r" (\d+?) week", self.uptime)
                        if weeks:
                                self.weeks = weeks.group(1)
                        days = re.search(r" (\d+?) day", self.uptime)
                        if days:
                                self.days = days.group(1)
                        hours = re.search(r" (\d+?) hour", self.uptime)
                        if hours:
                                self.hours = hours.group(1)
                        minutes = re.search(r" (\d+?) minute", self.uptime)
                        self.minutes = minutes.group(1)

                def uptime_in_seconds(self):
                        sec = 0
                        if hasattr(self, 'years'):
                                sec += int(self.years)*31536000
                        if hasattr(self, 'weeks'):
                                sec += int(self.weeks)*604800
                        if hasattr(self, 'days'):
                                sec += int(self.days)*86400
                        if hasattr(self, 'hours'):
                                sec += int(self.hours)*3600
                        sec += int(self.minutes)*60
                        return sec

        vendor_and_model = re.search(r"(.+?) (.+?) (.+?) processor (.+?) bytes of memory", response_string)
        if vendor_and_model:
                network_device['vendor'] = vendor_and_model.group(1)
                network_device['model'] = vendor_and_model.group(2)

        os_ver = re.search(r"Version (.+),", response_string)
        if os_ver:
                network_device['os_version'] = os_ver.group(1)

        sn = re.search(r"Processor board ID (.+)", response_string)
        if sn:
                network_device['serial_number'] = sn.group(1)

        host_and_uptime = re.search(r"(.+) uptime is (.+)\n", response_string)
        if host_and_uptime:
                network_device['hostname'] = host_and_uptime.group(1)
                uptime_string = host_and_uptime.group(2)
                uptime = Uptime(uptime_string)
                network_device['uptime'] = uptime.uptime_in_seconds()

        return network_device

def main():

        ip = '192.168.0.1'
        username = 'cisco'
        password = 'password'

	with open('show_version.txt', 'r') as f:
        	response_string = f.read()

        print parser(ip, username, password, response_string)


if __name__ == "__main__":
        main()

