def width_and_height(dumpster, img_width):              
   for line in dumpster:
      for width in line.split(':1'):
        if not "; width: auto" in width:
            print("Логотипу заданы жесткие размеры ширины, ", end='', file=open('result.txt', 'a', encoding='UTF-8'))

            for line in dumpster:
               for height in line.split(':1'):
                     if not "; height: auto" in height:
                        print("жесткие размеры высоты", file=open('result.txt', 'a', encoding='UTF-8'))
        else:       
            for line in dumpster:
                  if not "; width: 100%" in width:
                     print("Логотипу заданы жесткие размеры ширины,  ", end='', file=open('result.txt', 'a', encoding='UTF-8')) 
                     for line in dumpster:
                           if not "; height: 100%" in height:
                              print("жесткие размеры высоты", file=open('result.txt', 'a', encoding='UTF-8'))
                              