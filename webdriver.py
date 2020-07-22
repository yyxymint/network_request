
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")

import pyautogui
import requests
import selenium
import time

from bs4 import BeautifulSoup

from datetime import datetime


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException

def close_tab():
	driver.switch_to.window(driver.window_handles[-1])
	driver.close()
	driver.switch_to.window(driver.window_handles[-1])

def back():
	driver.switch_to.window(driver.window_handles[-1])

def by_xp(s):
	driver.find_element_by_xpath(s).click()
  
# driver.find_element_by_xpath('//*[@id="id"]').send_keys(m_id)

driver = webdriver.Chrome('C:/Users/HWNAG YE CHAN/Downloads/zoo/chromedriver.exe')
driver.get('https://www.melon.com/index.htm')
