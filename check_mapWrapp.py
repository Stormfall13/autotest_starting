try:
    def check_map_wrapp(MapClassWrapp):
        with open("style.css", "r") as openfile:
            map_noneWrapp = list()
            checkWrappMapClass = list()
            for line in openfile:
                for mosaicMap in line.split(':1'):
                    if " ".join(MapClassWrapp) in mosaicMap:
                        map_noneWrapp.append(mosaicMap)
            for line in map_noneWrapp:
                for MapClassWrapp in line.split(':1'):
                    if MapClassWrapp or f"@media (max-width: 991px)" in MapClassWrapp:
                        checkWrappMapClass.append(MapClassWrapp)
        for line in checkWrappMapClass:
            for checkDisplay in line.split(':1'):
                if "display: none" in checkDisplay:
                    print("\nКарта скрыта на адаптации, отобразите её", file=open('result.txt', 'a', encoding='UTF-8'))
except Exception as ex:
    pass