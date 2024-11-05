import requests
url = 'https://csf101-server-cap1.onrender.com/get/input/368'
response = requests.get(url)

with open('368.txt', 'wb') as f:
    f.write(response.content)
print("Downloaded 368.txt")
