

## overlay effects ##############
image shadow:
    'gui/shadow.png'
    alpha 0.4

image shadow2:
    'gui/shadow2.png'
    alpha 0.8


## transforms for character images #################

transform l2:
    xalign 0.2
transform r2:
    xalign 0.8

transform center:
    xalign 0.5 yalign 1
transform leftcenter:
    xpos 30 yalign 0.5
transform leftcenter5:
    yalign 0.5

transform pixelzoom4:
    ## loc, loc_evfg
    nearest True subpixel True zoom 4

transform pixelzoom6:

    nearest True subpixel True zoom 6

transform pixelzoom8:
    ## filesave, fileload, filedelete
    nearest True subpixel True zoom 8

transform pixelzoom10:
    ## slotbutton
    nearest True subpixel True zoom 10

transform pixelzoom11:
    ## window, ctc
    nearest True subpixel True zoom 11






















## click to continue #####################


screen ctc():
    zorder 1000
    if renpy.get_mode() in ['nvl', 'nvl_menu']:
        pass
    else:
        hbox:
            at ctc_appear
            xalign 0.82 yalign 0.95
            image 'ctc_pixel'

transform ctc_appear:
    on show:
        alpha 0.0 yoffset -5
        easeout 0.25 alpha 1.0 yoffset 0
    on hide:
        alpha 1.0 yoffset 0
        easein 0.25 alpha 0.0 yoffset 5

transform ctcmove:
    easeout 0.5 yoffset 5
    easein 0.5 yoffset 0
    repeat

image ctc_pixel = At('gui/ctc.png', pixelzoom11, ctcmove)




## story contexts ###################

image rule01 = Text('不要在早上5:30-9:30去图书馆！！')
