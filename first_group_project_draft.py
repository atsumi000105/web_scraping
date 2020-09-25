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
import time

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
with open('links_list.txt', 'w') as f:
    while (i<334):
        if (i==1):
            print("5 - Search Lauched")
        if (i%10 == 0):
            time.sleep(10)
        driver.get(url)
        demo2 = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/main/div/div[2]/div/div[3]/div/div/div[1]/div/ul')
        for x in demo2:
            soup = BeautifulSoup(x.get_attribute('outerHTML'), 'lxml')
            for elem in soup.find_all('a'):
                url1 = elem.get('href')
                if "www.immoweb.be" in url1:
                    f.write("%s\n" % url1)
        print("page: ", i)
        previous = i
        i += 1
        url = url.replace(str(previous),str(i))
    

print("6-did you get the link?")
print("the browser will be closed in a few seconds")
driver.implicitly_wait(30)

driver.close()
print("Finish - browser is closed")