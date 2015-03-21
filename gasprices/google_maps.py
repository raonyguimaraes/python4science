#pip install -U googlemaps
import googlemaps

gmaps = googlemaps.Client(key='Add Your Key here')

# Geocoding and address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')