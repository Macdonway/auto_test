import requests

url_login = 'http://121.43.98.145:8081/api/admin/login'

data = {
    "userName": "admin",
    "password": "da652bdba09dc49e3d272efd55f533e4",
    "https": False,
    "key": 1688396202189
}

method = "post"

r_res = requests.request(
    url=url_login,
    method=method,
    json=data,
    verify=False
)

print(r_res.text)

print(r_res.json())
