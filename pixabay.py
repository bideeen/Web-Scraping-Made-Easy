import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt

# Url
print('Accessing the Url')
url = f'https://pixabay.com/images/search/cat'
print('Url Accessed Successfully')
page = requests.get(url).text
print('Accesssed page data successfully')
soup = BeautifulSoup(page, 'html.parser')
print('Souped Successfully')
# Stroring the result
results = soup.find(id='content')
print(results)
# Stroing the Job Element
# cats_items = results.find_all('div', class_='item')


# for cats in cats_items:
#     cat_item = cats.find('a')
#     if None in (cat_item):
#         continue

#     print(cat_item.text)
#     print('\n')
