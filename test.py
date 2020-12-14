from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
import pandas as pd
import re
import sqlite3
def scrap(link):
    try:
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req)
        soup = BeautifulSoup(response, 'lxml')
    except:
        # print(f'Error while downloading the page {link}.\n')
        # print(f'Message: {e}')
        return 0
    
    immo_code = 404
    price = 0
    area = 0
    property_type = "Missing"
    rooms = 0
    zip_code = 404
    land_area = 0
    garden_area = 0
    kitchen = "No"
    pool = "No"
    furnished = "No"
    terrace = "No"


    # immoweb_code
    try:
        code = soup.find('div', {'class': 'classified__information--immoweb-code'})
        code_immo = int(code.text.strip().split(' ')[-1])
        immo_code = code_immo
    except:
        pass

    #type_property
    try:
        type_p = soup.find("div",{"class":"classified__header-content"})
        type_immo = type_p.find("h1",{"class":"classified__title"}).text.strip().split(' ')[0]
        property_type =  type_immo.strip()
    except:
        pass

    # #price
    try:
        price_t = soup.find("span",{"aria-hidden":"true"}).text.strip().replace(",", "")
        price_tu = re.findall(r"\d+", price_t.replace("€", ""))[0]
        price = price_tu
    except:
        pass

    # #zip-code
    try:
        zip_co = link.split('/')[8]
        zip_code = zip_co
    except:
        pass

    #rooms number
    try:
        rooms_t = soup.find_all("span", {'class': 'overview__text'})[0].text.strip()
        rooms = rooms_t.split(" ")[0]
    except:
        pass

    #List of the remaining elements
    try:
        tags = soup.select('tr.classified-table__row')
        for tag in tags:
            temp = tag.select('th.classified-table__header')[0].contents
            if len(temp) > 0:
                #area
                if str(temp[0]).strip() == "Living area":
                    area = tag.select('td.classified-table__data')[0].contents
                    if (len(area) > 0):
                        area = str(area[0]).strip()
                elif str(temp[0]).strip() == "Garden surface":
                    garden = tag.select('td.classified-table__data')[0].contents
                    if (len(garden) > 0):
                        garden_area = str(garden[0]).strip()
                elif str(temp[0]).strip() == "Terrace":
                    terra = tag.select('td.classified-table__data')[0].contents
                    if (len(terra) > 0):
                        terrace = str(garden[0]).strip()
                elif str(temp[0]).strip() == "Kitchen type":
                    kitchen_t = tag.select('td.classified-table__data')[0].contents
                    if (len(kitchen_t) > 0):
                        kitchen = str(kitchen_t[0]).strip()
                elif str(temp[0]).strip() == "Furnished":
                    furni = tag.select('td.classified-table__data')[0].contents
                    if (len(furni) > 0):
                        furnished = str(furni[0]).strip()
                elif str(temp[0]).strip() == "Surface of the plot":
                    land_plot = tag.select('td.classified-table__data')[0].contents
                    if (len(land_plot) > 0):
                        land_area = str(land_plot[0]).strip()
    except:
        print("")
    
    try:
        tags_b = soup.select('tbody.classified-table__body')
        for tag_b in tags_b:
            temp_b = tag_b.select('th.classified-table__header')[0].contents
            if len(temp_b) > 0:
                if str(temp_b[0]).strip() == "Swimming pool":
                    pool_t = tag_b.select('td.classified-table__data')[0].contents
                    if (len(pool_t) > 0):
                        pool = str(pool[0]).strip()
    except:
        pass

    result = [immo_code, zip_code, property_type, price, area, land_area, rooms, garden_area, 
    terrace, kitchen, furnished, pool]

    return result


if __name__ == "__main__":
    data = []
    df = pd.DataFrame(columns=["immo_code","zip_code","property_type","price","area",
    "land_area","rooms","garden_area","terrace","kitchen","furnished","pool"])
    df.to_csv("Dataset/test.csv")

    # create database
    connection = sqlite3.connect("Database/davy.db")
    cursor = connection.cursor()

    #create table immo_davy
    cursor.execute('CREATE TABLE IF NOT EXISTS immo(immo_code INTEGER, zip_code INTEGER, property_type TEXT,'
    'price INTEGER, area INTEGER, land_area TEXT, rooms INTEGER, garden_area INTEGER, terrace TEXT'
    'kitchen TEXT, furnished TEXT, pool TEXT)')

    # # create table for immo_davy
    # cursor.execute('CREATE TABLE IF NOT EXISTS immo_davy(area INTEGER,property_type TEXT,rooms_number INTEGER,'
    #            'zip_code INTEGER, land_area INTEGER,garden_area INTEGER,equipped_kitchen INTEGER, swimmingpool INTEGER,'
    #            'funrnished INTEGER,open_fire INTEGER, terrace INTEGER, terrace_area INTEGER)')
    
    # print("table created")

    # # insert values into immo_davy table
    # items = [300, "OTHERS", 1, 3000, 126, 200, 1, 0, 0, 1, 0, 40]
    # item_tu = tuple(items)
    # print(item_tu)
    # cursor.execute("INSERT INTO immo_davy VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", item_tu)
    # print("values inserted")

    # fetch data from immo_davy table
    # cursor.execute('SELECT * from immo_davy')
    # data = cursor.fetchall()
    # print(data)


    with open("Dataset/links_list.txt", "r") as f:
        links = [line.strip() for line in f]
    count = 1
    for link in links:
        test = scrap(link)
        try:
            if len(test) > 1:
                print(count, " =======")
                print(test)
                count += 1
        except:
            pass