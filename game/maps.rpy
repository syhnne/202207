
screen base_map(map):
    zorder 1
    tag map
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





screen libr_map_base(map):
    zorder 1
    tag map
    ## 如果这东西不是一个viewport的话，就不用操心拖拽的问题了。或许可以从美术层面上解决
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



