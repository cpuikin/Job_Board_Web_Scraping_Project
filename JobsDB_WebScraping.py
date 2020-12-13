# Inport library
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# Set target URL
URL = "https://hk.jobsdb.com/hk/search-jobs/data/"
URL1 = "https://hk.jobsdb.com"
# Use Chrome webdriver to scrap data
driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
subhtml = requests.get(URL)
# Set wait for website completely load the pagn
wait = WebDriverWait(driver,10)
subhtml = driver.page_source
soup = BeautifulSoup(subhtml.text, "html.parser")
x = soup.find_all(class_="FYwKg _3j_fQ _2PHih _3sxhA _1Epz5_6 _1A6vC_6 _20Cd9 _3RqUb_6 _3MPd_ Of_Sx_6 _2qcxd _3_RCw_6 C6ZIU_6 _6ufcS_6 _27Shq_6 _29m7__6 MxhoO_6")
maxpage = URL + (x[0].find_all("option")[-1].text)
print(maxpage)
# Create a dataframe
df = pd.DataFrame()

while True:
    for i in soup.find_all(class_="FYwKg _3j_fQ _2mOt7_6 _1A6vC_6 _3VCZm _29sNS _2cWXo _1Swh0 _3gPuF_6 _2Nlzp_6"):
        try:
            # Get job title
            title = i.find(class_="FYwKg _2j8fZ_6 sIMFL_6 _1JtWu_6").text
        except:
            title = np.nan
        try:
            # Get job company
            company = i.find(class_="ELZOd_6 qbDva _2CELK_6 FYwKg _2k9O2 _29sNS _58veS_6").text
        except:
            company = np.nan
        posts = i.a["href"]
        # Click into each job post
        if posts:
            posts = posts
            subhtml = requests.get(posts)
            soup = BeautifulSoup(subhtml.text,"html.parser")
        try:
            # Get job post date
            new_a = soup.find_all(class_="FYwKg d7v3r _3122U_6")
            location_salary_postdate = ((new_a[0].text))
        except:
            location_salary_postdate = np.nan
        try: 
            # Get job highlights
            new_a = soup.find_all(class_="FYwKg _1GAuD C6ZIU_6 _6ufcS_6 _27Shq_6 _29m7__6 _2WTa0_6") 
            job_highlights = (new_a[1].text+','+new_a[3].text+','+new_a[5].text)
        except:
            job_highlights = np.nan
        try:
            # Get job description
            new_a = soup.find(class_="vDEj0_6")
            job_description = new_a.div.text
        except:
            job_description = np.nan
        try:
            # Get job level
            new_a = soup.find_all(class_="FYwKg _32Ekc _2fqoM_6 _1hqiH_6") 
            career_level = new_a[0].text[12:]
        except:
            career_level = np.nan
        try:
            # Get job qualification
            qualification = new_a[1].text[13:]
        except:
            qualification = np.nan
        try:
            # Get job EXP request
            years_of_exp = new_a[2].text[19:]
        except:
            years_of_exp = np.nan
        try:
            # Get job type
            job_type = new_a[3].text[8:]
        except:
            job_type = np.nan
        try:
            # Get job benefits
            new_a = soup.find_all(class_="FYwKg d7v3r _3BZ6E_6") 
            industry_benefits_others = new_a[1].text
        except:
            industry_benefits_others = np.nan
        # Append all data into dataframe
        df = df.append({"title": title, "company": company, "location_salary_postdate": location_salary_postdate, "highlights": job_highlights, "description": job_description, "career_level": career_level, "qualification": qualification, "years_of_exp": years_of_exp, "job_type": job_type, "industry_benefits_others": industry_benefits_others,},ignore_index=True)
    subhtml = requests.get(URL)
    print(URL)
    soup = BeautifulSoup(subhtml.text,"html.parser")
    nextlink = soup.find_all(class_="FYwKg _2cWXo _1QYmq")
    # If 'next' pagn button unavailable, shop process
    if URL == maxpage:
        break
    # If 'next' pagn button available, click it then go to next pagn and repeat above step
    else:
        nextlink = URL1 + nextlink[0].find_all('a')[-1]["href"]
        URL = nextlink
        print(URL)
        subhtml = requests.get(URL)
        soup = BeautifulSoup(subhtml.text,"html.parser")
 # Export to csv      
df.to_csv('JobsDB.csv')

