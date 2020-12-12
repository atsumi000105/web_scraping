from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
import pandas as pd
import re

def scrap(link):
    print(link)
    try:
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req)
        soup = BeautifulSoup(response, 'lxml')
    except Exception as e:
        print(f'Error while downloading the page {link}.\n')
        print(f'Message: {e}')
        return 0

    # #immoweb_code
    # code = soup.find('div', {'class': 'classified__information--immoweb-code'})
    # code_immo = code.text.strip().split(' ')[-1]
    # print(code_immo)

    # #type_property
    # type_p = soup.find("div",{"class":"classified__header-content"})
    # type_immo = type_p.find("h1",{"class":"classified__title"}).text.strip().split(' ')[0]
    # print(type_immo.strip())

    # #price
    # price = soup.find("span",{"aria-hidden":"true"}).text.strip()
    # price = re.findall(r"\d+\,\d+", price)[0].replace(",", "")
    # print(price)

    # #zip-code
    # zip_code = link.split('/')[8]
    # print(zip_code)

    # #rooms number
    # rooms = soup.find_all("span", {'class': 'overview__text'})[0].text.strip()
    # print(rooms.split(" ")[0])

    # #area
    # area = soup.find_all("span", {'class': 'overview__text'})[2].text.strip()
    # print(area.split(" ")[0].strip())

    # #garden
    # garden = soup.select('td.classified-table__data')[22]
    # print(int(garden.contents[0].strip()))

    # #kitchen
    # garden = soup.select('td.classified-table__data')[10]
    # print(garden.contents[0].strip())

    # #pool
    # garden = soup.select('td.classified-table__data')[25]
    # print(garden.contents[0].strip())
    garden = soup.select('td.classified-table__data')
    print(len(garden))



if __name__ == "__main__":
    with open("Dataset/links.txt", "r") as f:
        links = [line.strip() for line in f]
    
    for link in links:
        scrap(link)