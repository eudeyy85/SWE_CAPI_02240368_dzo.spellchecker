import re

url = 'https://csf101-server-cap1.onrender.com/get/input/368'
txt_file = re.get(url)

with open('368.txt', 'wb') as f:
    data = f.write(txt_file.content)

print("Downloaded 368.txt")