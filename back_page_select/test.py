import requests
from bs4 import BeautifulSoup


file_path = 'http://krov.slavik-test.21.oml.ru/'


response = requests.get(file_path)
soup = BeautifulSoup(response.text, features="html.parser")
find_MapClass = soup.select_one('.mosaic-map')['class'][1]
print(find_MapClass)