from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://www.immoweb.be/nl/zoekertje/huis/te-koop/hamoir/4180/8901692?searchId=5f6dde5f0a186')
s = BeautifulSoup(response.content, 'lxml')
k = 0

for script in s.find_all('script'):
    k += 1
    if k == 6:
        index = script.string.index('=')
        indexNV = []
        for i in range(0, len(script.string)):
            if script.string[i] == ";":
                indexNV.append(i)
        index2 = indexNV[len(indexNV)-1]
        null = ""
        true = True
        false = False
        data = eval(script.string[index+1:index2])
        if data['flags']['isLifeAnnuitySale'] == False:
            for x in data['flags']:
                if data['flags'][x]:
                    print("Type of sale : ", x)
            for x in data['transaction']['sale']:
                if x == 'price':
                    print(x, ":", int(data['transaction']['sale'][x]))
                elif x == 'isFurnished':
                    if data['transaction']['sale'][x] == True:
                        print(x, ": True")
                    else:
                        print(x, ": False")
            for x in data['property']:
                if x == 'location':
                    print(x, ":", data['property'][x]['postalCode'])
                elif x == 'type':
                    print("Type of property : ", data['property'][x])
                elif x == 'subtype':
                    print("subtype of property:", data['property'][x])
                elif x == 'bedroomCount':
                    print(x, ":", int(data['property'][x]))
                elif x == 'netHabitableSurface':
                    print(x, ":", int(data['property'][x]))
                elif x == 'kitchen':
                    if len(data['property'][x]) > 0:
                        print(x, " : True")
                    else:
                        print(x, " : False")
                elif x == 'fireplaceExists':
                    print(x, ":", data['property'][x])
                elif x == 'hasTerrace':
                    print(x, ":", data['property'][x])
                    if data['property']['terraceSurface'] > 0:
                        print("terraceSurface:", int(
                            data['property']['terraceSurface']))
                elif x == 'hasGarden':
                    print(x, ":", data['property'][x])
                    if data['property']['gardenSurface'] > 0:
                        print("gardenSurface : ",
                              int(data['property']['gardenSurface']))
                elif x == 'land':
                    if len(data['property'][x]) > 0:
                        print("land Surface:", int(
                            data['property'][x]['surface']))
                    else:
                        print("land Surface : 0")
                elif x == 'facadeCount':
                    print(x, ":", int(data['property'][x]))
                elif x == 'hasSwimmingPool':
                    if data['property'][x] == True:
                        print(x, ": True")
                    else:
                        print(x, ": False")
                elif x == 'building':
                    print("State of the building :",
                          data['property'][x]['condition'])
                elif x == 'basement':  # Surface area of the plot of land
                    if len(data['property'][x]['surface']) > 0:
                        print(x, ":", int(data['property'][x]['surface']))
                    else:
                        print(x, ": 0")
