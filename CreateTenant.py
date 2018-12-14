import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
cookie = {"APIC-Cookie": "XsoJGO9tiWOePm2LJugQIS0oOb7C0ML4e56WBgeAlf1z7VEjbHw1HzUZCBcLtS0UqBuWd4j2QOldOghf+AuRDTTCh6r9j4Hr2Xx6O7Hh1ZfnYibCorH2vhzXrkrPKJJuaMcDHzDPaKZmXD1hhZTBl3EVue9Utevgf3OLIUaIuDQ="}

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)