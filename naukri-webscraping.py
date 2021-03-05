from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import csv
import pandas as pd
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

# Header of CSV File
csv_writer.writerow(['Job Title', 'Company Name', 'Experience', 'Salary', 'Location', 'Date Posted', 'Job Description', 'Role', 'Industry Type', 'Functional Area', 'Employment Type', 'Role', 'Education', 'Key Skills', 'About Company'])

while True:
    total_pages = driver.find_elements_by_xpath('//*[@class="fleft grey-text mr-5 fs12"]')
    for i in total_pages:
        page = i.text
    print()
    print('Scraping: ', page)

    
    job_titles = driver.find_elements_by_xpath('//*[@class="title fw500 ellipsis"]')
    job_links = []                  # List of job links on a particular page
    
    for title in job_titles:
        link = title.get_attribute('href')
        job_links.append(link)

    page_url = driver.current_url  # URL of the current page
    
    for link in job_links:         # Scraping individual job link on the particular page

        driver.get(link)

        titles = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[1]/header/h1')
        for title in titles:
            a = title.text             # Job title

        names = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[1]/div/a[1]')
        for name in names:
            b = name.text              # Company Name

        experiences = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[1]/span')
        for experience in experiences:
            c = experience.text        # Year of Experience

        salaries = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[2]/span')
        for salary in salaries:
            d = salary.text            # Salary

        locations = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[3]/span')
        for location in locations:
            e = location.text          # Job location

        dates = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[1]/div[2]/div[1]/span[1]/span')
        for date in dates:
            f = date.text              # Posted Date

        descriptions = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[2]/div[1]')
        for description in descriptions:
            g = description.text       # Job Description

        roles = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[2]/div[2]/div[1]/span')
        for role in roles:
            h = role.text              # Job Role  

        industry_types = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[2]/div[3]/div[2]/span')
        for industry_type in industry_types:
            i = industry_type.text     # Industry Type

        functional_areas = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[2]/div[2]/div[3]')
        for functional_area in functional_areas:
            j = functional_area.text   # Functional Area

        employment_types = driver.find_elements(By.XPATH, 'html/body/div[1]/main/div[2]/div[2]/section[2]/div[2]/div[4]/span')
        for employment_type in employment_types:
            k = employment_type.text   # Employement Type

        role_categories = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[2]/div[2]/div[5]/span')
        for role_category in role_categories:
            l = role_category.text     # Role Category


        educations = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[2]/div[3]')
        for education in educations:
            m = education.text         # Education

        skills = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[2]/div[4]')
        for skill in skills:
            n = skill.text             # Skills

        company_details = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/section[4]')
        for company_detail in company_details:
            o = company_detail.text    # About Company

            
            csv_writer.writerow([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o])  # Writing all the scrapped data into CSV file.
    
    driver.get(page_url)           # Redirecting back to particular search result URL
    del job_links                  # Deleting the job_links list of previous page
    sleep(10)
    try:
        next_page = driver.find_element_by_xpath('//*[@class="fright fs14 btn-secondary br2"]')
        next_page.click()          # Button click for the next page
        sleep(10)
    except Exception as e:
        print(e)

    page_url = driver.current_url  # URl of the currently opened page
    
    print('New Page URL: ', page_url)
    print()


# Converting CSV file to a dataframe
df = pd.read_csv("yourFileName.csv")     # Scrapped CSV file name
print(df)

# Total number of rows (may include duplicate rows)
print(len(list(df))) 


# Removing duplicate rows  
df.drop_duplicates(subset=None, inplace=True)
# print(df)
# print(len(list(df)))

# Creating new CSV file
output_filename = input('Enter output filename: ') 

# Writing the results to a new CSV file
df.to_csv(output_filename+'.csv', index=False)