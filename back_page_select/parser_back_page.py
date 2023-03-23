import requests
import sys
from bs4 import BeautifulSoup
from back_page_select.back_page_h1 import *
from back_page_select.select_crumbs import *


def parser_back(file_path):
   response = requests.get(file_path)
   soup = BeautifulSoup(response.text, features="html.parser")
   select = soup.select_one('ul:nth-of-type(1) li:nth-of-type(2) a')['href']
   back_page = file_path + str(select)
   ######################################
   back_response = requests.get(back_page)
   back_soup = BeautifulSoup(back_response.text, features="html.parser")
   back_select = back_soup.select_one('link')['href']
   back_css = file_path + str(back_select)
   ######################################
   response_css = requests.get(back_css)
   css_back = BeautifulSoup(response_css.text, features="html.parser")
   css_back_tag = css_back.select_one('pre')
   #######################################
   sys.stdout=open("back.css", "w", encoding='utf-8')
   print(css_back)
   sys.stdout.close()
   

   h1_back_class = list()

   response = requests.get(back_page)
   soup = BeautifulSoup(response.text, features="html.parser")
   ############################
   h1_class = soup.select_one(".page-title")['class'][1]
   h1_back_class.append('.' + h1_class)
   
   
   check_back_h1(h1_back_class) 
   
   crumbs_search(back_page)
   
   
   