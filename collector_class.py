import PySimpleGUI as sg
import bs4
from bs4 import BeautifulSoup
import requests

def class_parser(file_path):

    # file_path = 'http://slavik-test.21.oml.ru'
    response = requests.get(file_path)
    soup = BeautifulSoup(response.text, features="html.parser")
    ############################
    link_logo = soup.select_one(".link-universal")['class'][1]
    logo_link_class.append('.' + link_logo)
    # print(logo_link_class)
    ###########################
    div_logo = soup.select_one(".imageFit")['class'][1]
    logo_div_class.append('.' + div_logo)
    # print(logo_div_class)
    ###########################
    h1_class = soup.select_one(".page-title")['class'][1]
    h1_main_class.append('.' + h1_class)
    # print(h1_main_class)

