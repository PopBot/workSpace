from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import html, etree
import requests
import pandas as pd
import lxml
import urllib3
import requests_cache
requests_cache.install_cache('demo_cache')


df = pd.DataFrame(columns=['Company', 'Web'])

base_url = "https://expresscarriers.org/member/"

new_df = df

for x in range(987, 999):
    scrape_url = base_url + str(x)
    page = requests.get(scrape_url)
    root = lxml.html.fromstring(page.content)
    company_name = root.xpath('/html/body/div[2]/div[1]/div[1]/div/h1')
    c = company_name[0].text.strip()
    web = root.xpath('/html/body/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div/div[2]/ul[1]/li[3]/a')
    # w = web[0].text
    data = [{'Company': c, 'Web': web}]
    print(c)
    new_df = new_df.append(data, ignore_index=True)

new_df.to_csv('carriers.csv')