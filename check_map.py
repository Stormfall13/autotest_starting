try:
    def check_map_none(map_class):
        with open("style.css", "r") as openfile:
            map_none = list()
            check_map_class = list()
            for line in openfile:
                for mosaicMap in line.split(':1'):
                    if " ".join(map_class) in mosaicMap:
                        map_none.append(mosaicMap)
            for line in map_none:
                for mapClass in line.split(':1'):
                    if map_class[0] or f"@media (max-width: 991px)" in mapClass:
                        check_map_class.append(mapClass)
        for line in check_map_class:
            for checkDisplay in line.split(':1'):
                if "display: none" in checkDisplay:
                    print("\nКарта скрыта на адаптации, отобразите её", file=open('result.txt', 'a', encoding='UTF-8'))
except Exception as ex:
    pass