import bs4
import requests
import sys
import time
import os
from bs4 import BeautifulSoup
from select_logo_div import *
from select_logo_link import *
from div_div_logo import *
from select_string_h1 import *
from cursor_pointer import *
from check_map import *
from check_mapWrapp import *
from back_page_select.parser_back_page import *




# file_path = 'http://krov.slavik-test.21.oml.ru/'
# file_path = 'https://lestorg78.ru/'
file_path = 'https://mos-936406.oml.ru/'

response = requests.get(file_path, verify=False)
soup = BeautifulSoup(response.text, features="html.parser")
############################
css_file = soup.select_one('link')['href']
css_file = file_path + str(css_file)
#############################
response_css = requests.get(css_file)
soup_css = BeautifulSoup(response_css.text, features="html.parser")
soup_css.select('pre')

sys.stdout=open("style.css","w")
print (soup_css)
sys.stdout.close()

logo_link_class = list()
logo_div_class = list()
h1_main_class = list()
logo_container_class = list()
flex_class = list()
map_class = list()
MapClassWrapp = list()


response = requests.get(file_path)
soup = BeautifulSoup(response.text, features="html.parser")
############################
link_logo = soup.select_one(".link-universal")['class'][1]
logo_link_class.append('.' + link_logo)
###########################
div_logo = soup.select_one(".imageFit")['class'][1]
logo_div_class.append('.' + div_logo)
###########################
h1_class = soup.select_one(".page-title")['class'][1]
h1_main_class.append('.' + h1_class)
###########################
# logo_div_div = soup.select_one(".imageFit")
# logo_container_class.append('.' + logo_div_div.findParent()['class'][1])
###########################
try:
   if soup.select_one('.mosaic-map'):
      find_MapClass = soup.select_one('.mosaic-map')['class'][1]
      map_class.append('.' + find_MapClass)
   if soup.select_one('.mosaic-map').find_parent():
      find_MapClassWrapp = soup.select_one('.mosaic-map').find_parent()['class'][1]
      MapClassWrapp.append(find_MapClassWrapp)
except Exception as ex:
   pass
###########################
try:
   if soup.select_one('.hor-menu'):
      find_flexMenu = soup.select_one('.hor-menu > ul:nth-child(2)')['class'][0]
      flex_class.append('.' + find_flexMenu)
except Exception as ex:
   print(ex)
###########################
try: 
   if soup.select_one('.link-universal:has(> .div ~ .div)'):
      select = soup.select_one('.link-universal div:nth-child(1)')['class'][1]
      logo_container_class.append(select)
except:
   pass

soup.find("div", "list").decompose()

      
def select_structure(file_path):
   
   response = requests.get(file_path, verify=False)

   soup = BeautifulSoup(response.text, features="html.parser")
   
   try:
      if soup.select_one('.link-universal:has(> .div > .imageFit ~ .div)'):
         # print('Совпадение 1')
         # Поиск по div div
         div_div_select(logo_container_class) 
      else:
         if soup.select_one('.link-universal:has(> .div ~ .div)'):
            # print('Совпадение 2')
            # Поиск по div div
            div_div_select(logo_container_class) 
            
         else:
            if soup.select_one('.link-universal:has(> .imageFit ~ .div)'):
               # print('Совпадение 4')
               # Поиск по div
               logo_div_check(logo_div_class)
            else:
               return False
   except:
      pass

try:
   if select_structure(file_path) == False:
         # print('Совпадение 3')
         logo_link_check(logo_link_class) 
except:
   pass

   
check_string_h1(h1_main_class)

parser_back(file_path)

cursor_pointer_check(flex_class)

check_map_none(map_class)

check_map_wrapp(MapClassWrapp)

time.sleep(2)



time.sleep(2)
os.startfile('result.txt')


time.sleep(2)
os.remove('style.css')
os.remove('back.css')

