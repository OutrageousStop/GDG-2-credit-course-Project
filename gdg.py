import requests
import json
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

def astronauts_data():
    astronauts = requests.get('http://api.open-notify.org/astros.json')
    astronauts = json.loads(astronauts.text)
    return astronauts


def location_data():
    location = requests.get('http://api.open-notify.org/iss-now.json')
    location = json.loads(location.text)
    return location

def plot(lats, longs):
    lats = float(lats)
    longs = float(longs)
    print('latitude: ', lats, 'longitude: ', longs)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1,projection=ccrs.PlateCarree())
    ax.scatter(longs, lats, c = '#FF0000')
    ax.stock_img()
    ax.coastlines()
    ax.gridlines()
    plt.show()

def printAstronauts(astronauts):
    print("People Currently in ISS: ")
    for i in astronauts['people']:
        print(i['name'])


if __name__ == "__main__":
    astronauts = astronauts_data()
    location = location_data()
    longs = location['iss_position']['longitude']
    lats = location['iss_position']['latitude']
    printAstronauts(astronauts)
    plot(lats, longs)
