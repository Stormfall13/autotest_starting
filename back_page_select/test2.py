import requests
import sys
import json
from bs4 import BeautifulSoup






# file_path = 'http://krov.slavik-test.21.oml.ru/' # Проверить карту на адаптации

# map_class = list()

# response = requests.get(file_path, verify=False)
# soup = BeautifulSoup(response.text, features="html.parser")
# find_MapClass = soup.select_one('.mosaic-map')['class'][1]
# map_class.append('.' + find_MapClass)
# print(map_class)

# id_logo_json = '"' + 'ic5lq39rv' + '"'
# id_logo_json = 'ic5lq39rv'


# with open("json_mosaic.json") as openfile:
#     map_none = list()
#     check_map_class = list()
#     for line in openfile:
#         if 'ic5lq39rv' in line:
            


# with open("test_json.json", "r") as openfile:
#     for line in openfile:
#         if "ic5lq39rv" in line:
#             print(line.find(id))
        
            
        # print({'id':'ic5lq39rv'} in line)
    # pass
#     cursor_pointer = list()
#     check_cursor_class = list()
#     for line in openfile:
#         for flexMenu in line.split(':1'):
#             if "".join(id_logo_json) in flexMenu:
#                 cursor_pointer.append(flexMenu)
                
# for line in cursor_pointer:
#     for cursorClass in line.split(':1'):
#         if "ic5lq39rv" in cursorClass:
#             check_cursor_class.append(cursorClass)
#             print(check_cursor_class)
# if not check_cursor_class:
#     print("+")
# else:
#     # print('Всё ОК')
#     pass


# response = requests.get(file_path, verify=False)
# soup = BeautifulSoup(response.text, features="html.parser")
# ############################
# css_file = soup.select_one('link')['href']
# css_file = file_path + str(css_file)
# #############################
# response_css = requests.get(css_file)
# soup_css = BeautifulSoup(response_css.text, features="html.parser")
# soup_css.select('pre')


# sys.stdout=open("style.css","w")
# print (soup_css)
# sys.stdout.close()

# import PySimpleGUI as sg

# layout = [[sg.Text('Вставьте ссылку сайта')],      
#                 [sg.Input(key=1)],      
#                 [sg.Button("Старт", enable_events=True)]]      

# window = sg.Window('Autotest version 1.3', layout)    

# event, values = window.read()
# file_path = values[1]
# window.close()


from write_test import *



# with open('test_json.txt') as openfile:
#     bolean_items = openfile.read()

# bolean_true = bolean_items.replace("true", "True")
# bolean_false = bolean_true.replace("false", "False")

# with open('write_test.py', 'w') as file_out:
#     file_out.write(bolean_false)
    

id = 'ic5lq39rv'

data_id = data[0]
data_id_key = data_id[id]
visibility_settings = data_id_key['visibilitySettings']
visibility_controlled = visibility_settings['visibilityControlled']
if visibility_controlled:
    print('True')
else:
    print('False')


# from test_json import *

# all_boleans = data['true']
# try:
#    for all_bolean in all_boleans:
#     all_bolean['true'] = 'True'
# except Exception as ex:
#     pass 






