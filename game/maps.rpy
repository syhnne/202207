

transform hv:
    alpha 0.8


## 这个特殊事件的红点提示只能持续一层，如果有两层及以上套娃，就寄了。解决方法很简单：别写多层套娃就行。
screen map_common(l, bg, sizep):
    viewport:
        draggable True
        window:
            xysize sizep
            background bg
            for loc in l:
                if loc in _current_events.keys():
                    imagebutton:
                        idle 'gui/map/loc.png' 
                        hover At('gui/map/loc.png', hv)
                        foreground 'gui/map/loc_evfg.png'
                        pos loc.p()
                        action Call(_current_events[loc][0])
                        tooltip _current_events[loc][0]
                elif isinstance(loc, Map) and list_common(loc.list, _current_events.keys()):
                    imagebutton:
                        idle 'gui/map/loc.png' 
                        hover At('gui/map/loc.png', hv)
                        foreground 'gui/map/loc_evfg.png'
                        pos loc.p()
                        action loc.l()
                        tooltip loc.n()
                else:
                    imagebutton:
                        idle 'gui/map/loc.png' 
                        hover At('gui/map/loc.png', hv)
                        pos loc.p()
                        action loc.l()
                        tooltip loc.n()
            vbox:
                ypos 300
                transclude
            
            $ tooltip = GetTooltip()
            frame:
                xpos 200 ypos 200
                if tooltip:
                    text tooltip
                else:
                    text '_______'







screen school_map():
    zorder 1 tag map
    $ l = [playgr, t_building, cafe, s_building, libr]
    use map_common(l, 'gui/map/base.png', (3000,3000))





screen t_b_f1():
    zorder 2 tag map
    $ l = [cls2_1, cls2_2, ]
    use map_common(l, 'gui/map/base.png', (3000,3000)):
        textbutton '返回' action ShowTransient('school_map', dissolve)
        textbutton '2层' action ShowTransient('t_b_f2', dissolve)
            

screen t_b_f2():
    zorder 2 tag map
    $ l = [cls2_3, ]
    use map_common(l, 'gui/map/base.png', (3000,3000)):
        textbutton '返回' action Show('school_map', dissolve)
        textbutton '1层' action Show('t_b_f1', dissolve)




screen s_b_f1():
    zorder 2 tag map
    $ l = [sh01]
    use map_common(l, 'gui/map/base.png', (3000,3000)):
        textbutton '返回' action Show('school_map', dissolve)
        textbutton '2层' action Show('s_b_f2', dissolve)    

screen s_b_f2():
    zorder 2 tag map
    $ l = [sh04]
    use map_common(l, 'gui/map/base.png', (3000,3000)):
        textbutton '返回' action Show('school_map', dissolve)
        textbutton '1层' action Show('s_b_f1', dissolve)   





screen libr_map():
    zorder 2 tag map
    $ l = [sroom]
    use map_common(l, 'gui/map/base.png', (3000,3000)):
        textbutton '返回' action Show('school_map', dissolve)