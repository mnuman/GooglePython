import urllib.request
import math
import webbrowser
from xml.etree.ElementTree import parse
 
def retrieveBusRoute():
  u  = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
  data = u.read()
  f = open('route22.xml','wb')
  f.write(data)
  f.close()
  print("Data retrieved and written to file")

'''http://www.johndcook.com/blog/python_longitude_latitude/'''
'''To get the distance in miles, multiply by 3960. To get the distance in kilometers, multiply by 6373.'''
def distance_on_unit_sphere(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
         
    # Compute spherical distance from spherical coordinates.
         
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
     
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc

retrieveBusRoute()
doc = parse('route22.xml')
'''Base URL for Google Maps, marking office as A:'''
mapsURL = 'https://maps.googleapis.com/maps/api/staticmap?zoom=13&size=1200x1200&maptype=roadmap&markers=color:green%7Clabel:A%7C41.980262,-87.668452'
base_label=65
for bus in doc.findall('bus'):
  if bus.findtext('d') == 'North Bound' and float(bus.findtext('lat'))>41.980262:
    base_label += 1
    bus_lat = float(bus.findtext('lat'))
    bus_lon = float(bus.findtext('lon'))
    print("Matching bus")
    print("  Id : " + bus.findtext('id'))
    print("  Lat: " + str(bus_lon))
    print("  Lon: " + str(bus_lat))
    print(" Dist: " + str(round(6373*distance_on_unit_sphere(41.980262,-87.668452,bus_lat, bus_lon),2)))
    mapsURL = mapsURL + '&markers=color:red%7Clabel:' + chr(base_label) + '%7C' + str(bus_lat) + "," + str(bus_lon)
# Open a browser with the map data !
webbrowser.open(mapsURL)
