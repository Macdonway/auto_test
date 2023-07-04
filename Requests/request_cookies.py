import requests

url = 'http://121.43.98.145:8081/api/admin/article/create'

data = {
    "id": None,
    "editorType": "markdown",
    "title": "您好",
    "alias": "您好",
    "thumbnail": None,
    "typeId": "1",
    "keywords": None,
    "digest": None,
    "canComment": False,
    "recommended": False,
    "privacy": False,
    "content": "<p>您好</p>\n",
    "markdown": "您好",
    "rubbish": False
}

cookies = {"admin-token": "1#654C6E754D6D68306B6E7652707551784C2B704A7162424E2F4B5764323966344B4C3178526A584E624A743246553367735169714C522B4E33694A644864744C6C4C544B4E4B36554F497A315632744F4B56353745305043703241713042374637696C6B554A78437375303D"}

r = requests.post(url=url, json=data, cookies=cookies)

print(r.text)

print(r.json())