from lxml import etree
from bs4 import BeautifulSoup
from parsel import Selector
from selenium.webdriver.common.keys import Keys
import requests
import getpass
from selenium import webdriver
import time
import random

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

driver.find_element_by_xpath('//*[@id="searchBoxSubmitButton"]').click()

print("5-search button is clicked")

demo = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/main/div/div[2]/div/div[3]/div/div/div[1]/div/ul/li[1]/article/div[1]/h2/a')
demo2 = driver.find_elements_by_xpath(
    '/html/body/div[1]/div[2]/div/main/div/div[2]/div/div[3]/div/div/div[1]/div/ul/li')
links = []
count = 0
k = 0
prices = []
for x in demo2:
    soup = BeautifulSoup(x.get_attribute('outerHTML'), 'lxml')
    for elem in soup.find_all('a'):
        url = elem.get('href')
        r = requests.get(url)
        soup1 = BeautifulSoup(r.content, 'lxml')
        counter = 0
        for elem in soup1.find_all('span', attrs={"class": "sr-only"}):
            counter += 1
            if counter == 1 and ("From" not in elem.text):
                print("price = ", elem.text)
                prices.append(elem.text)
                print(k)
                k += 1

print("links", links)
print("6-did you get the link?")
print("the browser will be closed in a few seconds")
driver.implicitly_wait(30)
print("Finish - browser is closed")
# driver.close()
