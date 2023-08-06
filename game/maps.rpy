
screen main_map():
    zorder 1
    # modal True

    viewport:
        # draggable True
        window:
            xysize (3000,3000)
            background 'gui/map/base.png'
            for location in range(1,10):
                $ inf = map.show_spot(location)
                if inf:
                    textbutton inf[0]:
                        pos inf[2]
                        action Function(map.action, inf)
                        tooltip inf[1]


            $ tooltip = GetTooltip()
            frame:
                xpos 200 ypos 200
                if tooltip:
                    text tooltip
                else:
                    text '_______'






screen libr_map_base():
    zorder 1
    ## 如果这东西不是一个viewport的话，就不用操心拖拽的问题了。或许可以从美术层面上解决，反正玩家需要打开大地图的时候不多，暂且不管它了。
    viewport:
        # draggable True
        scrollbars 'both'
        window:
            xysize (3000,3000)
            background 'gui/map/base.png'
            transclude


