import unittest
from selenium import webdriver

def setUp(Target_OS, Target_Browser, Target_Browser_version, username, accessKey):
        # Set the default (placeholder value) to Chrome
        desired_capabilities = webdriver.DesiredCapabilities.CHROME
        
        # Set the target browser to the specified browser.
        if (Target_Browser == "CHROME"):
            desired_capabilities = webdriver.DesiredCapabilities.CHROME
        if (Target_Browser == "INTERNETEXPLORER"):
		    desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        if (Target_Browser == "FIREFOX"):
		    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        if (Target_Browser == "OPERA"):
		    desired_capabilities = webdriver.DesiredCapabilities.OPERA
        if (Target_Browser == "SAFARI"):
		    desired_capabilities = webdriver.DesiredCapabilities.SAFARI
        if (Target_Browser == "IPHONE"):
            desired_capabilities = webdriver.DesiredCapabilities.IPHONE
        if (Target_Browser == "IPAD"):
            desired_capabilities = webdriver.DesiredCapabilities.IPAD
        if (Target_Browser == "ANDROID"):
            desired_capabilities = webdriver.DesiredCapabilities.ANDROID
        
		# Set the target browser version to the specified version.
        desired_capabilities['version'] = Target_Browser_version
        
		# Set the target OS to the specified OS.
        desired_capabilities['platform'] = Target_OS
        desired_capabilities['name'] = 'Testing Selenium 2 in Python at Sauce'
        global driver
        driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://" + str(username) + ":" + str(accessKey) + "@ondemand.saucelabs.com:80/wd/hub"
        )
        driver.implicitly_wait(30)

def test_sauce():
	driver.get('https://piacc.navimedix.com')

def tearDown():
	print("Link to your job: https://saucelabs.com/jobs/%s" % driver.session_id)
	driver.quit()
	
def main(Target_OS, Target_Browser, Target_Browser_version, username, accessKey):
	setUp(Target_OS, Target_Browser, Target_Browser_version, username, accessKey)
	test_sauce()
	tearDown()
	
#main()