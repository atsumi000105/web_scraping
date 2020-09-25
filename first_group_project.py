from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://www.immoweb.be/nl/zoekertje/huis/te-koop/heverlee/3001/8777400?searchId=5f6dde5f0a186')
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
                    print(x, ":", data['transaction']['sale'][x])
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
                    print(x, ":", data['property'][x])
                elif x == 'netHabitableSurface':
                    print(x, ":", data['property'][x])
                elif x == 'kitchen':
                    print(x, ":", data['property'][x]['type'])
                elif x == 'fireplaceExists':
                    print(x, ":", data['property'][x])
                elif x == 'hasTerrace':
                    print(x, ":", data['property'][x])
                elif x == 'terraceSurface':
                    print(x, ":", data['property'][x])
                elif x == 'hasGarden':
                    print(x, ":", data['property'][x])
                elif x == 'gardenSurface':
                    print(x, ":", data['property'][x])
                elif x == 'land':
                    print("land Surface:", data['property'][x]['surface'])
                elif x == 'facadeCount':
                    print(x, ":", data['property'][x])
                elif x == 'hasSwimmingPool':
                    if data['property'][x] == True:
                        print(x, ": True")
                    else:
                        print(x, ": False")
                elif x == 'building':
                    print(x, ":", data['property'][x]['condition'])
                elif x == 'basement':  # Surface area of the plot of land
                    print(x, ":", data['property'][x]['surface'])
