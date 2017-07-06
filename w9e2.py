#!/usr/bin/env python

import re

class Uptime(object):
	def __init__(self, uptime_string):
		uptime = re.search(r"uptime is(.+)", uptime_string)
		self.uptime = uptime.group(1)
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

	def uptime_seconds(self):
		sec = 0
		try:
			if self.years:
				sec += int(self.years)*31536000
                except AttributeError:
                        pass
		try:
                	if self.weeks:
                        	sec += int(self.weeks)*604800
                except AttributeError:
                        pass
		try:
                	if self.days:
                        	sec += int(self.days)*86400
                except AttributeError:
                        pass
		try:
                	if self.hours:
                        	sec += int(self.hours)*3600
                except AttributeError:
                        pass
                sec += int(self.minutes)*60
		return sec 

def main():

	list = ['twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes', '3750RJ uptime is 1 hour, 29 minutes', 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes', 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes']

	for i in list:
		print i
		uptime = Uptime(i)
		try:
			if uptime.years:
				print "uptime.years =", uptime.years
		except AttributeError:
			pass
		try:
			if uptime.weeks:
                		print "uptime.weeks =", uptime.weeks
                except AttributeError:
                        pass
		try:
			if uptime.days:
                		print "uptime.days =", uptime.days
                except AttributeError:
                        pass
		try:
			if uptime.hours:
                		print "uptime.hours =", uptime.hours
                except AttributeError:
                        pass
        	print "uptime.minutes =", uptime.minutes
		
		print "uptime in seconds = ", uptime.uptime_seconds()


if __name__ == '__main__':
        main()



