# fetch number of tickets from gitlab
import urllib.request
import json
import configparser
import os 
import sys
import types

config = configparser.ConfigParser()
if (not os.path.exists("config.ini")):   
   sys.exit("config.ini not found")
config.read('config.ini')
token = config['gitlab'].get("token")
if ( type(token)() is None ):
   sys.exit("Gitlab token not found in config.ini, see config-sample.ini for more info.")

url = config['gitlab'].get("url")
if (type(url)() is None):
   sys.exit(
       "Gitlab url not found in config.ini, see config-sample.ini for more info.")

gitlab_url = f'{url}/api/v4/issues?state=opened&private_token={token}'

try:
   with urllib.request.urlopen(gitlab_url) as response:
      raw_json = response.read()
      json = json.loads(raw_json)
      print("Number of Gitlab open issues: ", len(json))
except:
   sys.exit(
       f'Can\'t connect to: {gitlab_url}')

# fetch number of errors on loki

# fetch number of unassigned email on front
