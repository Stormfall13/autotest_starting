import requests
import os
import time
from bs4 import BeautifulSoup
from back_page_select.parser_back_page import *


def crumbs_search(back_page):
    crumbs = list()

    response = requests.get(back_page)
    soup = BeautifulSoup(response.text, features="html.parser")
    select_crumbs = soup.select_one(".mosaic-crumbs")
    crumbs.append(select_crumbs.findParent().findParent()['class'][1])


    with open("back.css", "r") as openfile:
        for line in openfile:
            for check_crumbs in line.split(':1'):
                if "".join(crumbs) in check_crumbs:
                    if "display: none" in check_crumbs:
                        print('Хлебные крошки скрыты(display: none), отобразите их', file=open('result.txt', 'a', encoding='UTF-8'))

                     


