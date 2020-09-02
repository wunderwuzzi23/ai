import os
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO, StringIO
import uuid

#config
download_folder = "data/huskies"
search_term = "siberian husky"
subscription_key =  open("/home/hacker/.bingimagessearchkey","rt").readline().rstrip("\n")
count = 100
max_page = 10   


#setup
os.makedirs(download_folder,exist_ok=True)
search_url = "https://huskyai-imagesearch.cognitiveservices.azure.com/bing/v7.0/images/search"
headers = {"Ocp-Apim-Subscription-Key" : subscription_key}


#query and save images
offset = 0
for current_page in range(max_page):

    print("Page:" + str(current_page+1))
    params  = {"q": search_term, "license": "public", "imageType": "photo", "count": count, "offset": offset}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    offset = search_results["nextOffset"]


    for i in range(count):
        url  = search_results["value"][0:count][i]["thumbnailUrl"]  #contentUrl
        id  = search_results["value"][0:count][i]["imageId"]

        print(f"Processing ({i}) - {id}")
        image_data = requests.get(url)
        image_data.raise_for_status()
        filename  = os.path.join(download_folder, id + ".jpg")
    
        image = Image.open(BytesIO(image_data.content))
        image = image.save(filename, "JPEG")    

print("Done")
