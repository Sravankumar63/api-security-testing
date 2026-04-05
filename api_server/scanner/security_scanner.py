import requests
import time

BASE_URL = "http://127.0.0.1:5000"

def wait_for_api():
    while True:
        try:
            requests.get(BASE_URL)
            print("[✔] API is up!")
            break
        except:
            time.sleep(2)

def test_login():
    res = requests.post(f"{BASE_URL}/login", json={"username": "admin", "password": "admin"})
    if res.status_code == 200:
        print("[✔] Token received")
        return res.json()['token']
    return None

def test_access(token):
    headers = {"Authorization": token}
    res = requests.get(f"{BASE_URL}/data", headers=headers)
    if res.status_code == 200:
        print("[✔] Access successful")
    else:
        print("[!] Access failed")

wait_for_api()
token = test_login()
if token:
    test_access(token)
