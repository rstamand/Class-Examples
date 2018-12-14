import requests

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\":\t{\n\t\t\"attributes\":\t{\n\t\t\t\"name\" : \"admin\",\n\t\t\t\"pwd\" : \"ciscoapic\"\n\t\t}\n\t}\n}"
response = requests.request("POST", url, data=payload)

print(response.text)