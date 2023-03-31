# from hard_wh_logo import *

# Поиск стилей в ссылке логотипа по требованияем на десктопе 170х170
def logo_link_check(link_logo):
    dumpster = list()
    img_width = list()
    with open("style.css", "r") as openfile:
        for line in openfile:
            for logo in line.split(':1'):
                if link_logo[0] in logo:
                    dumpster.append(logo)

    for line in dumpster:
        for width in line.split(':1'):
                if "max-width: 170px" in width:
                    img_width.append(width)
                # width_and_height(dumpster, img_width)
                    
    if not img_width:
        print("(Поиск по ссылке)Максимальный размер логотипа на десктопе должен быть 170х170", end='', file=open('result.txt', 'a', encoding='UTF-8'))
    # else:    
    #     for line in img_width:
    #         for height in line.split(':1'):
    #             if "max-height: 170px" in height:
    #                 print(height)
    #             else:
    #                 print("(Поиск по ссылке)Максимальный размер логотипа на десктопе должен быть 170х170", end='', file=open('result.txt', 'a', encoding='UTF-8'))
# Поиск стилей в ссылке логотипа по требованияем на адаптации 140x140

    with open("style.css", "r") as openfile:
        for line in openfile:
            for logo in line.split(':1'):
                if link_logo[0] or "@media (max-width: 991px)" in logo:
                 dumpster.append(logo)
             
 
    for line in dumpster:
        for width in line.split(':1'):
                if "max-width: 140px" in width:
                    img_width.append(width)

      
    if not  img_width:
        print(" на адаптации 140x140", file=open('result.txt', 'a', encoding='UTF-8'))
    else:    
        for line in img_width:
            for height in line.split(':1'):
                if "max-height: 140px" in height:
                    print(height)
                else:
                    print(" на адаптации 140х140", file=open('result.txt', 'a', encoding='UTF-8'))
