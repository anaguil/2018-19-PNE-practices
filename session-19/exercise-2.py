import http.client
import json

# -- API information
HOSTNAME = "www.metaweather.com"
capital = input("Please enter the capital from where you want to retrieve information: ")
ENDPOINT = "/api/location/search/?query="

METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + capital.lower() , None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

weather = json.loads(text_json)
woeid = weather[0]['woeid']


ENDPOINT = "/api/location/"
LOCATION_WOEID = str(woeid)

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + LOCATION_WOEID + '/', None, headers)

r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
weather = json.loads(text_json)

time = weather['time']
temp0 = weather['consolidated_weather'][0]
sun_set = weather['sun_set']
temp = temp0['the_temp']
place = weather['title']

print()
print("Place: {}".format(place))
print("Time: {}".format(time))
print("Sun set: {}".format(sun_set))
print("Current temp: {} degrees".format(temp))

# Falta hacer que si introduce mal la ciudad que salga