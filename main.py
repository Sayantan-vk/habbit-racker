import requests
from datetime import datetime

date = datetime.now()
YEAR = date.strftime("%Y")
MONTH = date.strftime("%m")
DAY = date.strftime("%d")
USERNAME = "aritra453"
TOKEN = "hhsdksiwrurytisomksnihf"

pixela_url = "https://pixe.la/v1/users"
user_praams = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# request = requests.post(url=pixela_url, json=user_praams)
# print(request.text)

pixela_graph = f"{pixela_url}/{USERNAME}/graphs"

GRAPH_ID = "mygraph1"

pixela_graph_prms = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "ajisai"
}

headers = {"X-USER-TOKEN": TOKEN}

pixel_pixel_url = f"{pixela_graph}/{GRAPH_ID}"

HOURS = "9"

pixela_pixel_data = {
    "date": f"{YEAR}{MONTH}{DAY}",
    "quantity": HOURS,

}



# grap_request = requests.post(url=pixela_graph, json=pixela_graph_prms, headers=headers )
# print(grap_request.text)




# pixel_request = requests.post(url=pixel_pixel_url, json=pixela_pixel_data, headers=headers)
# print(pixel_request.text)
#


DATE = "20210602"
update_data_url = f"{pixel_pixel_url}/{DATE}"

update_data ={"quantity": "5"}

# update_request = requests.put(url=update_data_url, json=update_data, headers=headers)
# print(update_request.text)

delete_data = requests.delete(url=update_data_url,headers=headers)
print(delete_data.text)