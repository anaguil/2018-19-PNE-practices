import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes"
METHOD = "GET"

def connection():
    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    # -- If we do not specify the port, the standar one
    # -- will be used
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()
    jokes = json.loads(text_json)
    return jokes

value = connection()['value']
print("Total jokes of Chuck Norris: ", len(value))

list_categories = []
for id in value:
    category = id['categories']
    if category not in list_categories:
        list_categories.append(category)
print()
print("Categories available: ")
for cat in list_categories:
    print(cat)

print()
print("Number of categories: ", len(list_categories))

ENDPOINT = "/jokes/random"
joke = connection()['value']['joke']
print()
print("A random joke: ", joke )