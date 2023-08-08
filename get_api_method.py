import requests
import json


response = requests.get("http://216.10.245.166/Library/GetBook.php",
                        params={"AuthorName": "Michael Block"},)

# dict_response = json.loads(response.text)
# correct_response = dict_response[0]["isbn"]

json_response = response.json()
print(json_response)

# correct_response = json_response[0]["isbn"]

# assert response.status_code == 200
# assert correct_response == "PSRS"
#
# headers = response.headers["content-Type"]
# print(headers)
#
# assert headers == "application/json;charset=UTF-8"
#
# try:
#     assert response.status_code == 200
#     assert correct_response == "PSRS"
# except ValueError as e:
#     print(e)

