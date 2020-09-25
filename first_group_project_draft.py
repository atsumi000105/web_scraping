from lxml import etree
from bs4 import BeautifulSoup
from parsel import Selector
from selenium.webdriver.common.keys import Keys
import requests
import getpass
from selenium import webdriver
import time
import random
import pandas

print("1-start")

url = 'https://www.immoweb.be'
driver = webdriver.Firefox()
driver.implicitly_wait(30)

print("2-open browser")

driver.get(url)
time.sleep(random.uniform(1.0, 2.0))

print("3-get url")

driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]').click()

print("4-coockie is clicked")
i = 1
url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance'
k=0
links = []

while (i<334):
    if (i ==1):
        print("5 - Search launched")
    driver.get(url)
    demo2 = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/main/div/div[2]/div/div[3]/div/div/div[1]/div/ul')
    prices = []
    for x in demo2:
        soup = BeautifulSoup(x.get_attribute('outerHTML'), 'lxml')
        for elem in soup.find_all('a'):
            url1 = elem.get('href')
            if "www.immoweb.be" in url1:
                links.append(url1.rstrip("\n"))
        
    previous = i
    i += 1
    url = url.replace(str(previous),str(i))

print(len(links))

with open('links_list.txt', 'w') as f:
    for link in links:
        f.write("%s\n" % link)

print("6-did you get the link?")
print("the browser will be closed in a few seconds")
driver.implicitly_wait(30)

driver.close()
print("Finish - browser is closed")