from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep   

search = input('Enter the job: ')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe', options=options)
wait = WebDriverWait(driver, 20)
driver.get(url=f'https://www.naukri.com/{search}-jobs?k={search}')

headings = driver.find_elements_by_xpath('//*[@class="title fw500 ellipsis"]')
job_links = []
for i in headings:
    link = i.get_attribute('href')
    job_links.append(link)
print(job_links)
print(len(job_links))

