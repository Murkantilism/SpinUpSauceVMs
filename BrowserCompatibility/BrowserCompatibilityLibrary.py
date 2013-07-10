#@author: Deniz Ozkaynak - Created: 06/20/2013 - Last Updated: 06/20/2013
# This library provides automated cross-browser & cross-OS compatibility 
# testing for NaivNet QA Engineers working with Robot.

import subprocess, SendToSauce

# When QA imports this script, they will invoke this main method
# This method takes a variable amount of tests
def BrowserCompatibility(*arg):
	configOptionsList = ReadConfig()

# Read & parse the configuration file to find out which browsers 
# and OS's the user has designated for testing.
def ReadConfig():
	# Ask for the user's Sauce credentials
	SauceUsername = raw_input("\nEnter your Sauce Username: ")
	SauceAPIKey = raw_input("Enter your Sauce API Key: ")
	
	print "Parsing config file..."
	print "Proving P = NP..."
	
	# Open the configuration file
	readFile = open('BrowserCompatibility.config.py', 'r')
	
	# Initialize a string to keep track of uncommented options
	configOptionsList = ''

	# Read every line in the file individually, ignore if the q	
	# line starts with #, otherwise append to configOptionsList.
	for line in readFile:
		myLine = line.strip()
		if not myLine.startswith("#"):
			configOptionsList += "\n" + line.rstrip()
			
			# Set the default variable values
			Target_OS = "DEFAULT"
			Target_Browser = "DEFAULT"
			Target_Browser_version = "DEFAULT"
			
			# Parse config file to find target OS
			if ("WIN_EIGHT" in line):    # Windows 8
				Target_OS = "Windows 8"
			if ("WIN_SEVEN" in line):    # Windows 7
				Target_OS = "Windows 7"
			if ("WIN_XP" in line):       # Windows XP
				Target_OS = "Windows XP"
			if ("OSX_SL" in line):       # Mac OS Snow Leopard 
				Target_OS = "OS X 10.6"
			if ("OSX_MT" in line):       # Mac OS Mountain Lion
				Target_OS = "OS X 10.8"
			if ("LINUX" in line):        # Linux
				Target_OS = "LINUX"
			if ("iOS" in line):          # iOS 10.8 (newest for iPhone & iPad)
				Target_OS = "OS X 10.8"
			if ("iOS_old" in line):      # iOS 10.6 (old)
				Target_OS = "OS X 10.6"
				
			# Parse config file to find target BROWSER
			if ("IE" in line):
				Target_Browser = "INTERNETEXPLORER"
			if ("FF" in line):
				Target_Browser = "FIREFOX"
			if ("CHROME" in line):
				Target_Browser = "GOOGLECHROME"
			if ("OP" in line):
				Target_Browser = "OPERA"
			if ("SAFARI" in line):
				Target_Browser = "SAFARI"
			if ("iPHONE" in line):
				Target_Browser = "IPHONE"
			if ("iPAD" in line):
				Target_Browser = "IPAD"
			if ("DROID" in line):
				Target_Browser = "ANDROID"
			
			
			# Parse config file to find target BROWSER VERSION
			for x in range(2, 28):
				if (str(x) in line):
					Target_Browser_version = x
			# NOTE: The above for loop checks for browser versions ranging from
			# 2 to 25 (2 being the oldest version of any given browser that 
			# Sauce supports, 27 being the currently the latest version of any
			# given browser that Sauce supports)			

			print "\nSpinning up Sauce Labs VM for " + Target_OS + ", " + Target_Browser + ", version " + str(Target_Browser_version)
			
			# Send the target OS+Browser+BrowserVersion to Sauce
			# script to kick off a new Sauce test
			SendToSauce.main(Target_OS, Target_Browser, Target_Browser_version, SauceUsername, SauceAPIKey)
	if configOptionsList != "":
		print "\nThe requested OS and browser combinations have been created."
		print "See your Sauce Labs account page for results."
	else:
		print "ERROR: You have not configured any OS & browser combinations for testing!"
		print "No Sauce VM's were created, edit the config file to begin."
	return configOptionsList

# An example test to demonstrate how QA will pass 
# Robot tests to this library.
def exampleRobotTest():
	testString = 'fooBar'
	
BrowserCompatibility(1, 2, 3, exampleRobotTest)