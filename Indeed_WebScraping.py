# Inport library
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# Set target URL
URL = "https://hk.indeed.com/jobs?q=Data&l="
URL1 = "https://hk.indeed.com"
# Use Chrome webdriver to scrap data
driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
driver.get(URL)
# Set wait for website completely load the pagn
wait = WebDriverWait(driver,100)
subhtml = requests.get(URL)
soup = BeautifulSoup(subhtml.text, "html.parser")
# Create a dataframe
df = pd.DataFrame()


while True:
    for i in soup.find_all(class_="jobsearch-SerpJobCard unifiedRow row result"):
        # Get job title
        title = i.h2.a.get('title')
        # Get job location
        location = i.find('div', 'recJobLoc').get('data-rc-loc')
        # Get job Summary 
        summary = i.find('div', 'summary').text.strip()
        # Get job URL
        job_url = "https://hk.indeed.com" + i.h2.a.get('href')
        try:
            # Get job company
            company = i.find('span','company').text.strip()
        except:
            company = np.nan
        try:
            # Get job salary
            salary = i.find('span', 'salaryText').text.strip()
        except:
            salary = np.nan
        one_level = job_url
        # Click into each job post
        if one_level:
            driver.get(one_level)
            subhtml = driver.page_source
            soup = BeautifulSoup(subhtml,"html.parser")
        try:
            # Get job description
            description = soup.find_all('div', class_="jobsearch-jobDescriptionText")[0].text
        except:
            description = np.nan
        # Append all data into dataframe
        df = df.append({'JobTitle': title, 'Company': company, "Location": location, 'Summary': summary, "Description": description, 'Salary': salary, 'JobUrl': job_url},ignore_index=True)        
    subhtml = requests.get(URL)
    soup = BeautifulSoup(subhtml.text,"html.parser")
    nextlink = soup.find_all(class_="pagination")[0].a["href"]
    print(nextlink)
    # If 'next' pagn button available, click it then go to next pagn and repeat above step
    if nextlink:
        nextlink = URL1 + soup.find('a', {'aria-label':'Next'}).get('href')
        URL = nextlink
        print(URL)
        subhtml = requests.get(URL)
        soup = BeautifulSoup(subhtml.text,"html.parser")
    # If 'next' pagn button unavailable, shop process
    else:
        break
    # Export to csv
    df.to_csv('indeed.csv')