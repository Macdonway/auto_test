import requests

url = "http://121.43.98.145:8081/admin/login"

r = requests.get(url=url)

print(r.text)

print(r.status_code)
