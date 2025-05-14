import requests

url="https://api.football-data.org/v4/matches"

params = {
    "dateFrom": "2025-04-20",
    "dateTo": "2025-04-29"
    }

headers={"X-Auth_Token":"a45627de0d7042ca968bcfbe96e0e5f5"}

response=requests.get(url,headers=headers,params=params)


data =response.json()


print(data)