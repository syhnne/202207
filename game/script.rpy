
define persistent.HEYWHATAREYOUDOING = renpy.random.randint(100000,999999)

define character.Q = Character(None, what_prefix='(', what_suffix=')')
define character.a = Character("an", dynamic=True)
define character.b = Character("bn", dynamic=True)
define character.c = Character("cn", dynamic=True)
define character.y = Character("yn", dynamic=True)

default an = 'A'
default bn = 'B'
default cn = 'C'
default yn = 'Y'

## 啊这，半次元？

default persistent.playthrough = 1


image shadow:
    'gui/shadow.png'
    alpha 0.4

transform l2:
    xalign 0.2
transform r2:
    xalign 0.8

image rule01 = Text('不要在早上5:30-9:30去图书馆！！')


label test:
    a '天台的门锁着。'
    label enter_code:
        menu:
            '要打开门锁吗？'
            '输入密码。':
                call screen roof_code
                # '[_return]'
                if _return == True:
                    jump roof
                elif _return == False:
                    a '密码好像不对。'
                    jump enter_code
                else:
                    jump test2
            '（离开）':
                jump test2
        
label test2:
    '（返回主页面）'
    jump test

label roof:
    '到达世界最高城，理塘！太美丽了理塘'
    '好吧这只是一个程序测试内容，现在我们回到游戏开头'
    jump start
    return



screen roof_code():
    modal True
    frame:
        align (0.5, 0.5)
        has vbox
        text roofcode.refresh()
        grid 3 5:
            textbutton '1' action Function(roofcode.enter, 1)
            textbutton '2' action Function(roofcode.enter, 2)
            textbutton '3' action Function(roofcode.enter, 3)

            textbutton '4' action Function(roofcode.enter, 4)
            textbutton '5' action Function(roofcode.enter, 5)
            textbutton '6' action Function(roofcode.enter, 6)

            textbutton '7' action Function(roofcode.enter, 7)
            textbutton '8' action Function(roofcode.enter, 8)
            textbutton '9' action Function(roofcode.enter, 9)

            textbutton 'Clear' action Function(roofcode.clear)
            textbutton '0' action Function(roofcode.enter, 0)
            textbutton 'Confirm' action Function(roofcode.confirm)

            null 
            textbutton 'Return' action Return('')
            null




















label start:

    ## 这里最好加点旁白，来简单介绍一下玩家的身份，比如说“你是一个高二学生”之类。但我写不出来，下次一定。
    call test

    Q '周三下午'
    b '哎，今天化学作业是啥？'
    pause
    a '啊，什么？咋了？'
    b '你记没记化学作业？'
    a '哟，你要开卷啦？'
    b '不是，你就说你到底记没记？'
    menu:
        '（化学作业是什么来着？）'
        '好像是期中模拟卷子？':
            a '是不是那个期末模拟2？就今天发的那个。'
            b '你确定？别骗我啊。'
            a '当然不确定，我猜的。你还是去问课代表吧。'
        '好像是绿色通道？':
            a '是不是留的绿色通道？今天不是讲新课来着吗。'
            b '你确定？别骗我啊。'
            a '当然不确定，我猜的。你还是去问课代表吧。'
        '不记得。':
            a '啊这，你觉得我是那种能记得住作业的人吗。'
            a '要不你去问问课代表？'
    b '……我特么就是课代表。'
    a '……'
    b '不然我干嘛找你问，你猜课代表为啥没把作业写黑板上。'
    a '你这课代表当的可真尽责啊。'
    a '要不这样，今天你就别把作业写上去了，这样全班都会感谢你的。'
    b '……一会下课找人问吧。还有多久下课？'
    '老师' '还有10分钟。'
    '老师' '你跟[an]聊什么呢？聊得这么开心。我看你趴那儿睡好久了，要不你俩站后面去，精神一会儿再回来上课。'
    a '……'
    a '老师，对不起，我们错了。'
    b '老师对不起。'
    '老师' '唉……算了，今天最后一节课了，你们上了一天课可能也是累了，先坐下吧。'
    a '谢谢老师。'
    '老师' '……大家都高二了，现在学习压力也大，休息时间不充分……但是最基础的上课听讲，起码还是得做到吧？现在学的东西可比以前难多了，高二这个阶段是分水岭，这两极分化的时候，你缺了一节课没听，后面的内容也容易跟不上……'
    a '{alpha=*0.5}*小声*{/alpha}把你东西拿上。'
    b '{alpha=*0.5}*小声*{/alpha}什么东西？'
    a '{alpha=*0.5}*小声*{/alpha}自习课用的东西。'
    a '{alpha=*0.5}*小声*{/alpha}看见那个后门没有？一会趁他不注意，我数到三，咱们直接开溜。'
    b '{alpha=*0.5}*小声*{/alpha}成。还去图书馆？'
    a '{alpha=*0.5}*小声*{/alpha}去楼下空教室。那儿放学没人查，不像图书馆6点半就关门了。'
    '老师' '……这还有几天就期末考试了，我现在花了几节课给你串一遍这两本书知识点，为的就是你们期末考试能冲一把，别到下学期影响你分班。有的同学他不认真听讲，我也没办法……'
    a '{alpha=*0.5}*小声*{/alpha}就是现在，快溜！'
    show shadow onlayer effects
    scene bg c classroom with dissolve
    b '这地方挺好，比图书馆人少，还有电脑玩。'
    a '那肯定，大部分人还没意识到可以来空教室，还在往图书馆挤。'
    a '唯一可惜的是，咱没有高三的门卡，教室门一旦关上就没人能打得开了，这都是不可再生资源。'
    b '没关系，瞅瞅地上有没有原高三落在这的门卡就行了。'
    b '话说高三那帮人搬到哪儿去了？'
    a '好像是操场对面那块。'
    b '啊？就原来小学部那地方？那么远？'
    a '谁知道呢，可能怕我们干扰他们期末复习。'
    b '这不纯扯淡吗，我们对他们的影响能有搬家对他们的影响大？'
    b '再说了，那破地方离食堂那么远，纯纯的负优化。我要是高三，我直接骂娘了就。'
    a '不是有高三通道吗？'
    b '那东西基本没啥用，老有别的年级的的在那儿排，也没人管。'
    b '我看最耽误高三时间的就是中午吃饭排队，楼道里吵点把门一关不就听不见了吗。'
    a '确实。'
    Q '……'
    ## 高三搬走是因为有几间教室闹鬼，影响学生学习。这是我码字的时候现想的东西，我压根就不知道要怎么把它圆回来，可能这几天y阳了请假在家所以没人修门？？？
    scene black with dissolve
    scene bg c classroom with dissolve
    Q "两小时后"
    a '哎，别睡了，醒醒。'
    a '你来看看这个。'
    b '……干嘛？……你真摸着高三落下的门卡了？'
    a '不是。你看看这纸条。'
    b '啥玩意？'
    show rule01 at top with dissolve 
    ## 这里做个dismiss组件
    hide rule01 with dissolve
    a '你看，他说别去图书馆。'
    b '废话，图书馆特么10点才开门。'
    b '这不就那个校园怪谈吗？网上很火的那种。'
    a '不是，我是说，他这时间为什么写得这么详细？'
    b '谁知道，为了看起来很酷随手瞎写的吧。我要睡了。'
    a '明天早上你陪我来看看。'
    b '……不去，别耽误我睡觉。'
    a '有没有一种可能，图书馆10点才开门，就是因为他说的是真的？'
    a '去看看嘛，给你枯燥无味的校园生活增添一点乐趣。'
    a '而且万一是真的，你也就不用操心那化学作业了。'
    b '我不想早起。'
    with hpunch
    Q '楼道里传来一声巨响，和一个女生的尖叫声。'
    b '什么动静？'
    a '刚才那是有个人？这个点除了我们还有人会呆在教学楼吗。'
    b '估计跟你一样，是来内卷的。'
    b '啥玩意儿那么吓人啊，给我都吵醒了。'
    a '保不齐是怪谈成真！赶紧的，明天跟我过去看看。'
    b '不用我早起吧？不然打死我也不去。'
    a '不用，从食堂过来顺路看一眼就行。到教室就说是我们吃食堂拉肚子了，没赶上早读。'
    b '行吧。'


    ## 第二天：b：没什么东西就赶紧走吧，别一会被班主任制裁了。你不动脑子想想，学校还能闹鬼？哪里有这种好事？


    # menu:
    #     '咳咳，测试一下字数上限'
    #     '（适当的沉默）':
    #         pass
    #     '……艺考一般12月就结束了。':
    #         pass
    ## 好好好，很有感觉！！！（

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