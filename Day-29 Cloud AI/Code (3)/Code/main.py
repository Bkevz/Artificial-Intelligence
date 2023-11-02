import requests
import json

url = "https://api.imagga.com/v2/tags"

querystring = {"image_url":"https://cdn.pixabay.com/photo/2021/03/03/14/55/rhino-6065480_1280.jpg"}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjXzJhNDg3YWFiZWM4ZWUwZjoyYzIyYTc1OTc4ZTc2MDZhNTllOTlmODllODhhNDFkOA=="
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))

for i in range(6):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)
