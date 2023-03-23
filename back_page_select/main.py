import PySimpleGUI as sg
import time
from interface import *
from dynamic_selen import *




sg.theme('Dark')

layout = [[sg.Text('Вставьте ссылку сайта')],      
                [sg.Input(key=1)],      
                [sg.Button("Старт", enable_events=True)]]      

window = sg.Window('Autotest version 1.3', layout)    

event, values = window.read()
file_path = values[1]
window.close()

captcha_get = '?captcha_testing_mode=3'

dyn_selen(file_path + captcha_get)
time.sleep(2)
interface(file_path)

# http://shop3.slavik-test.21.oml.ru/
# http://temporary1.slavik-test.21.oml.ru/