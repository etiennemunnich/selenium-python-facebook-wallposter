#!python3

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from secrets import pw # where one places the password to login, not recommended but fine to test
import random

"""
Having fun with Selenium whilst posting jokes from a text
file to one's Facebook wall.

NOTE: Please be careful playing with this when posting to Facebook
      This was an excercise to understand how to use Selenium only!

REQUIREMENTS: place jokes/puns in joes.txt, 1 per line
              place password in secrets.py, eg:
              pw = 'mypasswordthatshouldbesecretandnotinafile'

"""

__author__ = "Etienne Munnich"
__version__ = "0.1.1"
__license__ = "MIT"

def main():

    # seed cause random
    random.seed()

    # get from file a pun to share
    try:
        with open("jokes.txt", 'r') as file:
            for i in range(random.randrange(0, 76)):
                read_data = file.readline()
    except:
        print('Could not open file.')
        exit(1)

    file.close()

    # Facebook 
    service = Service('/python-selenium/chromedriver') #path to the chromedriver
    service.start()
    
    driver = webdriver.Remote(service.service_url)
    driver.get('https://www.facebook.com');

    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    submit   = driver.find_element_by_id("loginbutton")

    # facebook login
    username.send_keys("YOUR-EMAIL")
    password.send_keys(pw)
    time.sleep(3.2) # wait for a bit
    submit.click()

    time.sleep(4.8) # wait for a bit

    # setup the post to share a joke
    status= driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
    status.send_keys(str(read_data));
    postbutton = driver.find_element_by_xpath("//button[contains(.,'Post')]")
    # post!
    postbutton.click()
    time.sleep(7.8) # wait for a bit
    driver.quit()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
