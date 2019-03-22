import requests
import json
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import wikipedia

def fetch_data(key):
    data = wikipedia.summary(key)
    return data

def astronauts_data():
    astronauts = requests.get('http://api.open-notify.org/astros.json')
    astronauts = json.loads(astronauts.text)
    return astronauts


def location_data():
    location = requests.get('http://api.open-notify.org/iss-now.json')
    location = json.loads(location.text)
    return location

def printAstronauts(astronauts):
    print("People Currently in ISS: ")
    for i in astronauts['people']:
        print(i['name'])
def get_names(astronauts_data):
    names = []
    for i in astronauts_data['people']:
        names.append(i['name'])
    return names

def liveTrack():
    for i in range(20):
        location = location_data()
        longs = location['iss_position']['longitude']
        lats = location['iss_position']['latitude']
        lats = float(lats)
        longs = float(longs)
        print('latitude: ', lats, 'longitude: ', longs)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1,projection=ccrs.PlateCarree())
        ax.scatter(longs, lats, c = '#FF0000')
        ax.stock_img()
        ax.coastlines()
        ax.gridlines()
        plt.show(block= False)
        plt.pause(1)
        plt.close()
if __name__ == "__main__":
    astronauts = astronauts_data()
    names = get_names(astronauts)
    printAstronauts(astronauts)
    print("\n\nFetching Details ...")
    details = {k:v for k,v in zip(names, [fetch_data(i) for i in names])}
    for i in details:
        print(i, details[i])
    liveTrack()