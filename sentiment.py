import urllib.parse
import urllib.request  
import json
text = input()
data = urllib.parse.urlencode({"text": text}).encode("utf-8")
u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)
response = u.read()
result_dict = json.loads(response.decode('utf-8'))
positivity=float(result_dict['probability']['pos'])*100
negativity=float(result_dict['probability']['neg'])*100
print ([positivity,negativity])
