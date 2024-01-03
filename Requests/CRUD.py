import requests
import json
from faker import Faker
from pprint import pprint
import random
import pytest

base_url = "https://gorest.co.in/"
access_token = "16bfeb441a22700fea9bccc3409a1b6affadf845376de18a57de87e00555e5ea"
header = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
faker = Faker()


def get_request():
    url = base_url + "/public/v2/users/"
    print("Get Url is ", url)
    response = requests.get(url=url, headers=header)
    json_response = response.json()
    json_str = json.dumps(json_response, indent=3)
    print(json_str)


def post_request():
    url = base_url + "/public/v2/users/"
    print("post url is", url)
    data = {
        "name": "Kapil Kumar",
        "email": faker.email(),
        "gender": "male",
        "status": "active"
    }

    response = requests.post(json=data, headers=header, url=url)
    json_response = response.json()
    json_str = json.dumps(json_response, indent=4)
    print(json_str)
    assert response.status_code == 201
    assert json_response["name"] == "Kapil Kumar"
    assert "name" in json_response
    user_id = json_response["id"]
    return user_id


def put_request(userid):
    url = base_url + f"/public/v2/users/{userid}"
    print("put url is", url)
    data = {"name": "Kapil Kumar kukkar G",
            "email": faker.email(),
            "gender": "male",
            "status": "inactive"}

    response = requests.put(url=url, headers=header, json=data)
    json_response = response.json()
    json_str = json.dumps(json_response, indent=4)
    print(json_str)
    assert json_response["name"] == "Kapil Kumar kukkar G"
    assert json_response["status"] == "inactive"


def delete_request(userid):
    url = base_url + f"/public/v2/users/{userid}"
    print("Delete url is", url)
    response = requests.delete(url=url, headers=header)
    assert response.status_code == 204
    print("User has been deleted")


get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)
