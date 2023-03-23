# Поиск стилей для H1
def check_back_h1(h1_back_class):
    with open("back.css", "r") as openfile:
        for line in openfile:
            for h1 in line.split(':1'):
                if h1_back_class[0] in h1:
                    for line in h1_back_class:
                            if "text-transform: uppercase" in h1:
                                print ('На внутренних страницах к Н1 присвоен заглавный стиль букв, отключите пожалуйста text-transform: uppercase', file=open('result.txt', 'a', encoding='UTF-8'))
                            elif "text-transform: lowercase" in h1:
                                print ('На внутренних страницах к Н1 присвоен нижний регист букв, отключите пожалуйста text-transform: lowercase', file=open('result.txt', 'a', encoding='UTF-8'))
                            elif "text-transform: capitalize" in h1:
                                print ('На внутренних страницах к Н1 присвоены заглвные буквы в каждом слове, отключите пожалуйста text-transform: capitalize', file=open('result.txt', 'a', encoding='UTF-8'))
