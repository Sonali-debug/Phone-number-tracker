import opencage
import phonenumbers
import folium
from test import number

from phonenumbers import geocoder
key="2f396d701c9c41368535adddbd5bd98a"
ch_nmber = phonenumbers.parse(number, "CH")
location = geocoder.description_for_number(ch_nmber, "en")
print(location)

from phonenumbers import carrier

service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print (results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start = 9)

folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
