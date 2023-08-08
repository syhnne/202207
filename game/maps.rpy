
screen base_map(map):
    zorder 1
    # modal True

    viewport:
        # draggable True
        window:
            xysize (3000,3000)
            background 'gui/map/base.png'
            for loc in map.locations:
                if loc.cond():
                    textbutton loc.name() pos loc.pos() action Function(loc.action, )
            if map != base_:
                textbutton '返回' action Return()


            # $ tooltip = GetTooltip()
            # frame:
            #     xpos 200 ypos 200
            #     if tooltip:
            #         text tooltip
            #     else:
            #         text '_______'





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


