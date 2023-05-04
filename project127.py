from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Edge('msedgedriver.exe')
browser.get(start_url)
time.sleep(10)

def scrape():
    coloumn = ['proper_name','distance','mass','radius']
    planet_data = []
    for i in range(2):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for ul in soup.find_all('tr'):
            li = ul.find_all("th", attrs={'class','headerSort'})
            temp_list = []
            for index, li_tag in enumerate(li):
                if index == 0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append('')
            planet_data.append(temp_list)
    with open('project127output.csv','w', encoding='utf8') as f:
        data = csv.writer(f)
        data.writerow(coloumn)
        data.writerows(planet_data)

scrape()