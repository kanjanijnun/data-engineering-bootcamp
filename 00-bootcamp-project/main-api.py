import configparser
import csv

import requests

<<<<<<< HEAD
#อ่านจาก Config ที่ชื่อ Pipeline.conf โดยดู Section ที่ชื่อ api_config
=======

>>>>>>> refs/remotes/origin/main
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
host = parser.get("api_config", "host")
port = parser.get("api_config", "port")

API_URL = f"http://{host}:{port}"
DATA_FOLDER = "data"

### Events
data = "events"
date = "2021-02-10"
<<<<<<< HEAD
#ดึงจาก aip เราใช้ library ชื่อว่า requests แล้วก็ Get จาก URL Data ชื่อว่า Events (ใส่ Filter '?created_at={date}' ไว้ ทำให้ดึง Events เป็นวันที่ได้)
=======
>>>>>>> refs/remotes/origin/main
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/events.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())

### Users
data = "users"
date = "2020-10-23"
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/users.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())

### Orders
data = "orders"
date = "2021-02-10"
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/orders.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())