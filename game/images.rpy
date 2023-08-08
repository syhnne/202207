

## overlay effects ##############
image shadow:
    'gui/shadow.png'
    alpha 0.4




## transforms for character images #################

transform l2:
    xalign 0.2
transform r2:
    xalign 0.8







## click to continue #####################


screen ctc():
    zorder 100
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

image ctc_pixel = At('gui/ctc.png', ctcmove)




## story contexts ###################

image rule01 = Text('不要在早上5:30-9:30去图书馆！！')






## 紧急测试立绘 ####
image a test = 'images/a_test.png'
image a t2 = 'images/a_t2.png'