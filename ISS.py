import urllib.request
import json
import geocoder
import webbrowser
import time
import turtle

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open(
    "iss.txt",
    "w")  #this will include the data of lon and lat for the code and the map.
file.write("There are currently " + str(result["number"]) +
           " astronauts on the iss: \n")
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")
g = geocoder.ip('me')
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()

webbrowser.open("iss.txt")

screen = turtle.Screen()
screen.setup(1280, 720)  #this will be the dimensions for the map.
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("map.gif")
screen.register_shape(
    "iss.gif"
)  #this will be the satalite, which will act as a pointer on the map
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result["iss_position"]
    lon = location['longitude']
    lat = location['latitude']
    lat = float(lat)
    lon = float(lon)
    print("\nLongitude: " + str(lon))
    print("\nLatitude: " + str(lat))
    iss.goto(lon, lat)

    time.sleep(7)  #Refresh every 7 seconds