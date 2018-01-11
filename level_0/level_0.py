import requests
url = "http://158.69.76.135/level0.php"
payload = {'id':"27",'holdthedoor':'submit'}

for i in range(1024):
    response = requests.post(url, data=payload)
    print(response)
