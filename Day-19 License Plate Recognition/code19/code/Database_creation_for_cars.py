import json
import base64
import requests
from authKey import SECRET_KEY
import pandas as pd

IMAGE_PATH = 'first.jpg'


with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)

num_plate=(json.dumps(r.json(), indent=2))
info=(list(num_plate.split("candidates")))
print(info)
plate=info[1]
plate=plate.split(',')[0:3]
p=plate[1]
p1= p.split(":")
number=p1[1]
number=number.replace('"','')
number=number.lstrip()
print (number)

file = pd.read_excel('carDetails.xlsx')
num_list = file['Vehicle Number']

for i in range(len(file)):
    if number == file.iloc[i][1]:
        print("----------------------------")
        print(f"Owner Name: {file.iloc[i][0]}")
        print(f"Vehicle Number: {file.iloc[i][1]}")
        print(f"Address: {file.iloc[i][2]}")
    else:
        name = str(input("Enter Owner Name: "))
        Vehicle_Number = str(input("Enter Vehicle Number: "))
        address = str(input("Enter Address: "))
        file.loc[len(file.index)] = [name, Vehicle_Number, address]

file.to_excel("carDetails.xlsx")
