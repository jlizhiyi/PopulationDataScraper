from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import csv

driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Metropolitan_statistical_area')

## Get US MSA names from website
names = driver.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"][1]/tbody/tr/td[2]')
## Get salaries from website
salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]')

# Create CSV
csv_filename = 'basketballdata.csv'

# Add to CSV
entry = []
for p in range(len(players)):
    print(players[p].text + "," + salaries[p].text)
    entry.append((players[p].text,salaries[p].text))
with open(csv_filename, 'a', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(entry)