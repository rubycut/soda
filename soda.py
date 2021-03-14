# fetch number of tickets from gitlab
import urllib.request
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
token = config['gitlab'].get("token")
url = config['gitlab'].get("url")
print("Token is: ", token)

gitlab_url = f'{url}/api/v4/issues?state=opened&private_token={token}'

with urllib.request.urlopen(gitlab_url) as response:
   raw_json = response.read()
   json = json.loads(raw_json)
   print("Number of Gitlab open issues: ", len(json))
# fetch number of errors on loki

# fetch number of unassigned email on front