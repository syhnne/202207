
define e = Character("艾琳")
define a = Character("an", dynamic=True)
define b = Character("bn", dynamic=True)
define c = Character("cn", dynamic=True)
define y = Character("yn", dynamic=True)

default an = ''
default bn = 'b'
default cn = 'c'
default yn = 'y'


label start:


    scene bg c classroom
    show eileen happy
    e "原来是这样解决的吗？太离谱了！"
    e "不会吧不会吧。不会有人从没完整地做完过一个游戏，还要一上来就改gui吧，这个蠢人没想过自己画立绘的时候会有多么头疼吗"
    e '字体测试，隔壁有个字体连脑子的“脑”字都显示不出来，肯定影响我做游戏'
    e '嗷遨氨欸庵锕嗄隘乂鵪岇盦鼇'
    e '可以啊，只有三个字没显示出来'
    e '太↗好了（那种徐特语气）'
    e '接下来我要测试一下，用这种字体说怪话会不会很怪。。'
    $ an = renpy.input('请输入姓名：', length=8)
    a '大家好，我是本作的主角。'
    a '实际上我和玩家除了几个无足轻重的选项以外，没有任何其他关系，但为什么还要玩家给我起名？'
    a '原因很简单，因为作者不会起名，起3个名字对她来说已经是极限了。'

    ## 现在就是一个非常头大。。
    ## 算了，我们的主角就不要做屑人了，这样人设重合比较严重，我不想让所有的角色说出来的话都像是我本人在自言自语。
    ## 我是不是选择了一种看似最好写，实则最难写的形式？

    return


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