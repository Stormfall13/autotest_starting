def cursor_pointer_check(flex_class):
    with open("style.css", "r") as openfile:
        cursor_pointer = list()
        check_cursor_class = list()
        for line in openfile:
            for flexMenu in line.split(':1'):
                if "".join(flex_class) in flexMenu:
                    cursor_pointer.append(flexMenu)
                    
    for line in cursor_pointer:
        for cursorClass in line.split(':1'):
            if "cursor: pointer" in cursorClass:
                check_cursor_class.append(cursorClass)
    if not check_cursor_class:
        print("\nУ Флекс-меню отсутствует cursor: pointer", end='', file=open('result.txt', 'a', encoding='UTF-8'))
    else:
        # print('Всё ОК')
        pass