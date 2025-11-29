import requests
import json

def get_dog_picture(breed:str): 
    all_breeds_url = "https://dog.ceo/api/breeds/list/all"

    all_breeds_response = requests.get(all_breeds_url)

    if all_breeds_response.status_code == 200:
        all_breeds_json = json.load((all_breeds_response.text))

get_dog_picture('retriever')
