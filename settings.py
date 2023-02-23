
import time
import os
import platform
from const import *
from database import *

class Singleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]


class Setting(object, metaclass=Singleton):
	
	current_indexsys = 0
	current_ip = 0
	view_ping_success = False
	view_ping_fail = False

	ip0, ip1, ip2 = 0, 0, 0
	ip3, ip4, ip5 = 0, 0, 0
	ip6, ip7, ip8 = 0, 0, 0
	ip9, ip10, ip11 = 0, 0, 0

	time_interface = None  # timestamps
	time_setting = None  # timestamps
	# False for View, True if user set a new IP Address in attent to save database or return
	change_value = False

	def __init__(self):
		self.time_setting = time.time()

	@property
	def setTimestamp(self):
		self.time_interface = time.time()

	@property
	def setTimestampSettingInterface(self):
		self.time_setting = time.time()
		#
	#
	def setSubNavigation(self, value):
		self.sub_navigation = value

	@property
	def getSubNavigation(self):
		return self.sub_navigation

	#Increment number max 9, restart 0

	def rotateIncrNumber(self, number):
		number += 1

		if number > 9:
			number = 0

		return number

	#Decremente number min 0, restart 9
	def rotateDecrNumber(self, number):
		number -= 1

		if number < 0:
			number = 9

		return number

	#Get Ip in Database for System (Naomi, ..)

	def getIpSystem(self, system):
		database = Database()
		return database.getcursor.execute("SELECT %s FROM setting" % system).fetchone()[0]

	#Set a new IP address
	
	def ipsorting(self):
		if self.current_indexsys <3 :
			self.current_ip = self.getIpSystem("ip_naomi")
		elif self.current_indexsys ==3 :
			self.current_ip = self.getIpSystem("ip_triforce")
		else:
			self.current_ip = self.getIpSystem("ip_chihiro")
		
	def setNewIpAddress(self, ip ,system):
		new_ip = "%s.%s.%s.%s" % (ip[0],ip[1],ip[2],ip[3] )

		database = Database()
		database.getcursor.execute(
				"UPDATE setting SET %s = '%s' WHERE id =1" % (system, new_ip))
		database.getconnexion.commit()

		self.change_value = False

	@property
	def formatViewIpAddress(self):
		cpt = 0
		string = ""

		for x in str(self.current_ip):
			if cpt == 0:
				if x == '0':
					x = '-'

			if cpt == 1:
				if x == '0' and string[cpt-1:cpt] == '-':
					x = '-'

			if cpt == 4:
				if x == '0':
					x = '-'

			if cpt == 5:
				if x == '0' and string[cpt-1:cpt] == '-':
					x = '-'

			if cpt == 8:
				if x == '0':
					x = '-'

			if cpt == 9:
				if x == '0' and string[cpt-1:cpt] == '-':
					x = '-'

			if cpt == 12:
				if x == '0':
					x = '-'

			if cpt == 13:
				if x == '0' and string[cpt-1:cpt] == '-':
					x = '-'

			string += x
			cpt += 1

		return string.replace("-", "")

	#Ping Ip Address

	@property
	def pingIdAddress(self):
		self.ipsorting
		parameter = '-n' if platform.system().lower()=='windows' else '-c'
		if os.system(f"ping {parameter} 1 " + str(self.current_ip)) == 0:
			self.view_ping_success = True
			self.view_ping_fail = False
		else:
			self.view_ping_fail = True
			self.view_ping_success = False

	#Protect interface for setting new Ip and not reload database value

	def setChangeValue(self, value):
		self.change_value = value

	#Re-init value to False
	@property
	def setFalsePingTestResult(self):
		self.view_ping_success = False
		self.view_ping_fail = False

	@property
	def getZeroKey(self):
		database = Database()
		return database.getcursor.execute("SELECT zero_key FROM setting").fetchone()[0]

	#Define value Zero Key to database
	def setZeroKey(self, value):
		database = Database()
		database.getcursor.execute(
			'''UPDATE setting SET zero_key = ? WHERE id =1''', [value])
		database.getconnexion.commit()
