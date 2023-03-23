# Поиск стилей для H1
def check_string_h1(string_h1):
    main_tag = list()
    with open("style.css", "r") as openfile:
        for line in openfile:
            for h1 in line.split(':1'):
                if string_h1[0] in h1:
                    main_tag.append(h1)
    for line in main_tag:
        for h1 in line.split(':1'):
            if "text-transform: uppercase" in h1:
                print ('К Н1 присвоен заглавный стиль букв, отключите пожалуйста text-transform: uppercase', file=open('result.txt', 'a', encoding='UTF-8'))  
            elif "text-transform: lowercase" in h1:
                print ('К Н1 присвоен нижний регист букв, отключите пожалуйста text-transform: lowercase', file=open('result.txt', 'a', encoding='UTF-8'))  
            elif "text-transform: capitalize" in h1:
                print ('К Н1 присвоены заглвные буквы в каждом слове, отключите пожалуйста text-transform: capitalize', file=open('result.txt', 'a', encoding='UTF-8'))
