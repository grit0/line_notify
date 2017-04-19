import requests,json
from urlparse import urlparse

LINE_ACCESS_TOKEN=""
url = "https://notify-api.line.me/api/notify"

message ="Hello python"
msg = urllib.urlencode(({"message":message}))
LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
session = requests.Session()
sendLine=session.post(url, headers=LINE_HEADERS, data=msg)
print(sendLine.text)
