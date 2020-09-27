from bs4 import BeautifulSoup
import requests
import os
import pandas as pd

path_1 = os.path.abspath('C:/Users/gebruiker/Project/')
with open(path_1+"/links_list.txt", "r") as f:
    links = [line.strip() for line in f]
count = 0
skipped = 0
duplicate = 0
ids = []
type_properties = []
type_subproperties = []
prices = []
localities = []
netHabitableSurfaces = []
nr_bedrooms = []
kitchen_installeds = []
nr_facades = []
hasGardens = []
garden_m2s = []
hasTerraces = []
terrace_m2s = []
furnished_YNs = []
swimpool_YNs = []
type_of_sales = []
lands = []
basements = []
buildings = []
fireplaceExists = []
# fields to add to a list
id = 0
type_of_property = ""
subtype_of_property = ""
price = 0
location = 0
netHabitableSurface = 0
bedroomCount = 0
kitchen = False
facadeCount = 0
hasGarden = False
gardenSurface = 0
hasTerrace = False
terraceSurface = 0
isFurnished = False
hasSwimmingPool = False
type_of_sale = ""
land = 0
basement = 0
building = ""
fireplaceExist = False
for link in links:
    count += 1
    # if "8887719" in link:
    if count <= 25000 and count >= 1:
        try:
            no_data = False
            response = requests.get(link)
            s = BeautifulSoup(response.content, 'lxml')
            k = 0
            print(count, "======", link)
            for script in s.find_all('script'):
                k += 1
                if k == 6:

                    question_mark = link.index('?')
                    id = link[question_mark-7:question_mark]
                    if id in ids:
                        duplicate += 1
                        break  # id is in the list then skip
                    type_of_property = ""
                    subtype_of_property = ""
                    price = 0
                    location = 0
                    netHabitableSurface = 0
                    bedroomCount = 0
                    kitchen = False
                    facadeCount = 0
                    hasGarden = False
                    gardenSurface = 0
                    hasTerrace = False
                    terraceSurface = 0
                    isFurnished = False
                    hasSwimmingPool = False
                    type_of_sale = ""
                    land = 0
                    basement = 0
                    building = ""
                    fireplaceExist = False
                    index = script.string.index('=')
                    indexNV = []
                    for i in range(0, len(script.string)):
                        if script.string[i] == ";":
                            indexNV.append(i)
                    index2 = indexNV[len(indexNV)-1]
                    null = ""
                    true = True
                    false = False
                    try:
                        i_window = script.string.index('window.classified')
                        i_media = script.string.index('"media"')
                        i_property = script.string.index('"property"')
                        data = eval(script.string[index+1:i_media] +
                                    script.string[i_property:index2])
                        id = data['id']
                        pass
                    except ValueError:
                        no_data = True
                        pass
                    if data['flags']['isLifeAnnuitySale'] == False and not no_data and not 'HOUSE_GROUP' in data['property']['type'] and not 'APARTMENT_GROUP' in data['property']['type']:
                        for x in data['flags']:
                            if data['flags'][x]:
                                type_of_sale = x
                        for x in data['transaction']['sale']:
                            if x == 'price':
                                if data['transaction']['sale']['price'] == "":
                                    c = 'cluster'
                                    u = 'units'
                                    i = 'items'
                                    p = 'price'
                                    if data['flags']['isSoldOrRented'] == True:
                                        price = 0
                                    else:
                                        if data[c] == "":
                                            price = 0
                                        else:
                                            for a in data[c][u][0][i]:
                                                if a['saleStatus'] == 'AVAILABLE':
                                                    price = int(a[p])
                                else:
                                    price = int(data['transaction']['sale'][x])
                            elif x == 'isFurnished':
                                if data['transaction']['sale'][x] == True:
                                    isFurnished = True
                                else:
                                    isFurnished = False
                        for x in data['property']:
                            if x == 'location':
                                location = data['property'][x]['postalCode']
                            elif x == 'type':
                                type_of_property = data['property'][x]
                            elif x == 'subtype':
                                subtype_of_property = data['property'][x]
                            elif x == 'bedroomCount':
                                if data['property'][x] == "":
                                    if data['cluster'] == "":
                                        bedroomCount = 0
                                    else:
                                        bedroomCount = int(
                                            data['cluster']['units'][0]['items'][0]['bedroomCount'])
                                else:
                                    bedroomCount = int(data['property'][x])
                            elif x == 'netHabitableSurface':
                                if data['property'][x] == "":
                                    c = 'cluster'
                                    u = 'units'
                                    i = 'items'
                                    s = 'surface'
                                    if data[c] == "":
                                        netHabitableSurface = 0
                                    else:
                                        for a in data[c][u][0][i]:
                                            if a['saleStatus'] == 'AVAILABLE':
                                                netHabitableSurface = int(a[s])
                                else:
                                    netHabitableSurface = int(
                                        data['property'][x])
                            elif x == 'kitchen':
                                if len(data['property'][x]) > 0:
                                    kitchen = True
                                else:
                                    kitchen = False
                            elif x == 'fireplaceExists':
                                if data['property'][x] == "False" or data['property'][x] == False:
                                    fireplaceExist = False
                                else:
                                    fireplaceExist = True
                            elif x == 'hasTerrace':
                                if data['property'][x] == "" or data['property'][x] == "False" or data['property'][x] == "false":
                                    hasTerrace = False
                                else:
                                    if data['property'][x] == "False" or data['property'][x] == False:
                                        hasTerrace = False
                                    else:
                                        hasTerrace = True
                                    if data['property']['terraceSurface']:
                                        terraceSurface = int(
                                            data['property']['terraceSurface'])
                                    else:
                                        terraceSurface = 0
                            elif x == 'hasGarden':
                                if data['property']['gardenSurface'] == "":
                                    hasGarden = False
                                else:
                                    if data['property'][x] == "False" or data['property'][x] == False:
                                        hasGarden = False
                                    else:
                                        hasGarden = True
                                    if data['property']['gardenSurface']:
                                        gardenSurface = int(
                                            data['property']['gardenSurface'])
                                    else:
                                        gardenSurface = 0
                            elif x == 'land':
                                if len(data['property'][x]) > 0:
                                    if data['property']['land']['surface'] == "" or data['property']['land']['surface'] == null or data['property']['land']['surface'] == None:
                                        land = 0
                                    else:
                                        land = int(
                                            data['property'][x]['surface'])
                                else:
                                    land = 0
                            elif x == 'facadeCount':
                                facadeCount = int(data['property'][x])
                            elif x == 'hasSwimmingPool':
                                if data['property'][x] == True:
                                    hasSwimmingPool = True
                                else:
                                    hasSwimmingPool = False
                            elif x == 'building':
                                if data['property'][x] == "":
                                    building = "Not specified"
                                else:
                                    building = data['property'][x]['condition']
                            elif x == 'basement':  # Surface area of the plot of land
                                if data['property']['basement'] == "":
                                    if data['property']['land'] == "":
                                        basement = 0
                                    else:
                                        if data['property']['land']['surface'] == "" or data['property']['land']['surface'] == null or data['property']['land']['surface'] == None:
                                            basement = 0
                                        else:
                                            basement = int(
                                                data['property']['land']['surface'])
                                elif data['property']['basement']['surface']:
                                    basement = int(
                                        data['property']['basement']['surface'])
                                else:
                                    basement = 0
                    else:
                        skipped += 1
                    ids.append(id)
                    type_properties.append(type_of_property)
                    type_subproperties.append(subtype_of_property)
                    prices.append(price)
                    localities.append(location)
                    netHabitableSurfaces.append(netHabitableSurface)
                    nr_bedrooms.append(bedroomCount)
                    kitchen_installeds.append(kitchen)
                    nr_facades.append(facadeCount)
                    hasGardens.append(hasGarden)
                    garden_m2s.append(gardenSurface)
                    hasTerraces.append(hasTerrace)
                    terrace_m2s.append(terraceSurface)
                    furnished_YNs.append(isFurnished)
                    swimpool_YNs.append(hasSwimmingPool)
                    type_of_sales.append(type_of_sale)
                    lands.append(land)
                    if basement == 0:
                        if land == 0:
                            basements.append(netHabitableSurface)
                        else:
                            basements.append(land)
                    else:
                        basements.append(basement)
                    buildings.append(building)
                    fireplaceExists.append(fireplaceExist)
            pass
        except:
            skipped += 1
            pass
print("skipped=", skipped, "duplicate = ", duplicate)
data = {'type_property': type_properties, 'type_subproperty': type_subproperties, 'price': prices,
        'locality': localities, 'netHabitableSurface': netHabitableSurfaces,
        'nr_bedrooms': nr_bedrooms, 'kitchen_installed': kitchen_installeds, 'nr_facades': nr_facades,
        'hasGarden': hasGardens, 'garden_m2': garden_m2s, 'hasTerrace': hasTerraces, 'terrace_m2': terrace_m2s,
        'furnished_YN': furnished_YNs, 'swimpool_YN': swimpool_YNs, 'type_of_sale': type_of_sales,
        'land': lands, 'basement': basements, 'building': buildings, 'fireplaceExist': fireplaceExists
        }
df = pd.DataFrame(
    data, columns=['type_property', 'type_subproperty', 'price', 'locality', 'netHabitableSurface',
                   'nr_bedrooms', 'kitchen_installed', 'nr_facades', 'hasGarden', 'garden_m2', 'hasTerrace', 'terrace_m2',
                   'furnished_YN', 'swimpool_YN', 'type_of_sale',
                   'land', 'basement', 'building', 'fireplaceExist'], index=ids)
try:
    df.to_csv(path_1+"/dataSet.csv", encoding='utf-8', index=ids)
    pass
except PermissionError:
    df.to_csv(path_1+"/dataSet1.csv", encoding='utf-8', index=ids)
    pass
print("Finished records = ", len(ids), len(type_properties), len(type_subproperties), len(prices), len(localities), len(netHabitableSurfaces), len(nr_bedrooms), len(kitchen_installeds), len(nr_facades),
      len(hasGardens), len(garden_m2s), len(hasTerraces), len(terrace_m2s), len(furnished_YNs), len(swimpool_YNs), len(type_of_sales), len(lands), len(basements), len(buildings), len(fireplaceExists))
