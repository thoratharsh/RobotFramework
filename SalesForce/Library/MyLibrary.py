from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def switch_to_other_window(window):
    sellib=BuiltIn().get_library_instance('Selenium2Library')
    driver=sellib._current_browser()
    sellib=BuiltIn().get_library_instance('Selenium2Library')
    driver=sellib._current_browser()
    driver.switch_to_window(window)
