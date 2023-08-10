

## 这个特殊事件的红点提示只能持续一层，如果有两层及以上套娃，就寄了。解决方法很简单：别写多层套娃就行。
screen map_common(l, bg, sizep, ev):

    viewport:
        draggable True
        window:
            xysize sizep
            background bg
            for loc in l:
                if ev and loc in list(ev.keys()):
                    $ print('has event:',str(loc))
                    imagebutton:
                        idle At('gui/map/loc.png', pixelzoom4)
                        hover At('gui/map/loc.png', hv, pixelzoom4)
                        foreground At('gui/map/loc_evfg.png',pixelzoom4)
                        pos loc.p()
                        action loc_action(loc)
                        tooltip ev[loc][0]
                elif ev and isinstance(loc, Map) and list_common(loc.list, ev.keys()):
                    imagebutton:
                        idle At('gui/map/loc.png', pixelzoom4)
                        hover At('gui/map/loc.png', hv, pixelzoom4)
                        foreground At('gui/map/loc_evfg.png',pixelzoom4)
                        pos loc.p()
                        action loc.l()
                        tooltip loc.n()
                else:
                    imagebutton:
                        idle At('gui/map/loc.png', pixelzoom4)
                        hover At('gui/map/loc.png', hv, pixelzoom4)
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







screen school_map(ev):
    zorder 1 tag map
    $ l = [playgr, t_building, cafe, s_building, libr]
    use map_common(l, 'gui/map/base.png', (3000,3000), ev)





screen t_b_f1(ev):
    zorder 2 tag map
    $ l = [cls2_1, cls2_2, ]
    use map_common(l, 'gui/map/base.png', (3000,3000), ev):
        textbutton '返回' action ShowTransient('school_map', dissolve, ev)
        textbutton '2层' action ShowTransient('t_b_f2', dissolve, ev)
            

screen t_b_f2(ev):
    zorder 2 tag map
    $ l = [cls2_3, ]
    use map_common(l, 'gui/map/base.png', (3000,3000), ev):
        textbutton '返回' action Show('school_map', dissolve, ev)
        textbutton '1层' action Show('t_b_f1', dissolve, ev)




screen s_b_f1(ev):
    zorder 2 tag map
    $ l = [sh01]
    use map_common(l, 'gui/map/base.png', (3000,3000), ev):
        textbutton '返回' action Show('school_map', dissolve, ev)
        textbutton '2层' action Show('s_b_f2', dissolve, ev)    

screen s_b_f2(ev):
    zorder 2 tag map
    $ l = [sh04]
    use map_common(l, 'gui/map/base.png', (3000,3000), ev):
        textbutton '返回' action Show('school_map', dissolve, ev)
        textbutton '1层' action Show('s_b_f1', dissolve, ev)   





screen libr_map(ev):
    zorder 2 tag map
    $ l = [sroom]
    use map_common(l, 'gui/map/base.png', (3000,3000), ev):
        textbutton '返回' action Show('school_map', dissolve, ev)






screen phone_button():
    frame:
        pos (20,20)
        has vbox
        spacing gui.navigation_spacing
        if not _in_phone:
            textbutton '手机…' action Call('contact')
        else:
            textbutton '收起手机' action [ToggleVariable('_in_phone'), Return() ]