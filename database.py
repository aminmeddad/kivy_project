###
# Script by Ezechiel
# Date : 2019/xx/xx
# Description :  PiDimTouch database 
###

import sqlite3
from  const import *
class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]
		
		
class Database(object, metaclass=Singleton):
	connexion = None
	cursor = None
	
	def __init__(self):
		self.connexion = sqlite3.connect(DATABASE)
		self.cursor = self.connexion.cursor()
		
	@property
	def close(self):
		self.connexion.close()
		
	@property
	def getcursor(self):
		return self.cursor
		
	@property
	def getconnexion(self):
		return self.connexion
		
		
	

