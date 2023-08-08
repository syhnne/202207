
screen school_map():
    zorder 1
    tag map
    # modal True

    viewport:
        draggable True
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




screen building_map():
    zorder 1
    tag map

    viewport:
        draggable True
        window:
            xysize (3000,3000)
            background 'gui/map/base.png'
            has vbox
            textbutton '返回' action Return(1)
            textbutton 'building_1' action Return('building_1')





screen libr_map_base():
    zorder 1

    viewport:
        draggable True
        window:
            xysize (3000,3000)
            background 'gui/map/base.png'
            transclude


