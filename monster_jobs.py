import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt

def next(result):

    pass

def scrape(job_title=None, country=None, pages=None):


    # data
    title = []
    company = []
    location = []

    for page in range(1,pages):

        # Url
        print('Accessing the Url')
        url = f'https://www.monster.com/jobs/search/?q={job_title}&where={country}&page={page}'
        print('Url Accessed Successfully')
        page = requests.get(url).text
        print('Accesssed page data successfully')
        soup = BeautifulSoup(page, 'html.parser')
        print('Souped Successfully')
        # Stroring the result
        results = soup.find(id='ResultsContainer')
        # Stroing the Job Element
        job_elems = results.find_all('section', class_='card-content')


        for job_elem in job_elems:
            title_elem = job_elem.find('h2', class_='title')
            company_elem = job_elem.find('div', class_='company')
            location_elem = job_elem.find('div', class_='location')
            if None in (title_elem, company_elem, location_elem):
                continue
            title.append(title_elem.text.strip())
            company.append(company_elem.text.strip())
            location.append(location_elem.text.strip())
            # print(title_elem.text)
            # print(company_elem.text)
            # print(location_elem.text)

    # Check the next page

    #Storing the data into csv file
    data = pd.DataFrame()
    data['Job Title'] = title
    data['Company name'] = company
    data['Location'] = location
    data.to_csv(f'data/monster jobs/{country}_{job_title}.csv', index=False)
    

    print('Data Scraped Successfully')


if __name__ == '__main__':
    # ask input from user
    job_position = str(input('Enter the Job title of your chioce: '))
    job_location = str(input('Enter the Country of your chioce: '))
    pages = int(input('Enter the number of pages you want to scrape: '))
       
    # Scrape the data
    scrape(job_position, job_location, pages)