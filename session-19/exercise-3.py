import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input("Enter a username from GitHub: ")
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Generate the object from the json file
user = json.loads(text_json)

# -- Get some data
login = user['login']
name = user['name']
if name is None:
    name = login
nrepos = user['public_repos']

print()
print("Name: {}".format(name))
print("Repos: {}".format(nrepos))

# Second connection to enter inside the user page
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + GITHUB_ID + "/repos", None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
repositories = json.loads(text_json)

list_repos = []
for dict in repositories:
    name_repo = dict['name']
    list_repos.append(name_repo)
print("The name of repos:", list_repos)

# Third connection to enter inside the repo to see the commits
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, "/repos/" + GITHUB_ID + "/2018-19-PNE-practices/commits", None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
commits = json.loads(text_json)

i = 0
for com in commits:
    i += 1
print("Number of commits to the '2018-19-PNE-practices' repo: {}".format(i))