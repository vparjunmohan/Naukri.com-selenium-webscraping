from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import csv
from time import sleep

search = input('Search Job: ')
location = input('Job Location: ')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe', options=options)
wait = WebDriverWait(driver, 20)
driver.delete_all_cookies()
driver.get(url=f'https://www.naukri.com/{search}-jobs?k={search}&l={location}')

csv_filename = input('Enter CSV file name: ')     # Creating CSV File
csv_file = open(csv_filename+'.csv', 'a', encoding="utf-8", newline='')  # Opening CSV File

csv_writer = csv.writer(csv_file)

