import sqlite3
import urllib.request, json
from datetime import datetime


conn = sqlite3.connect('weather.sqlite')
cur = conn.cursor()

#Crear la tabla Tracks
#cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE IF NOT EXISTS weather (lat REAL, long REAL, temp REAL, ts INTEGER)')


url="http://api.openweathermap.org/data/2.5/weather?lat=19.48&lon=-99.56&appid=f3cb31dcc25cfb362340ebb20ab2c11b&units=metric"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
lon = data['coord']['lon']
lat = data['coord']['lat']
temp = data['main']['temp']
#ts = data['dt']
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
ts = current_time


cur.execute('INSERT INTO weather (lat, long, temp, ts) VALUES (?, ?, ?, ?)',#Los signos de interrogación son place holders
    (lat,lon,temp,ts))
conn.commit()

#Mostrar los datos de la tabla Tracks
print('Temps:')
cur.execute('SELECT * FROM weather')
for row in cur:
     print(row)

#cur.execute('DELETE FROM Tracks WHERE plays < 100')
#conn.commit()

conn.close()