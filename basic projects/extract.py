import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_European_Cup_and_UEFA_Champions_League_finals"

res=requests.get(url)

print(res.content)