
## 天台那扇门的密码。一般来说玩家不会知道他是多少，除非他们已经通关一次还闲的没事把这个数字记了下来。
default persistent.HEYWHATAREYOUDOING = renpy.random.randint(100000,999999)
default persistent.playthrough = 1

define character.a = Character("an", dynamic=True)
define character.b = Character("bn", dynamic=True)
define character.c = Character("cn", dynamic=True)
define character.y = Character("yn", dynamic=True)

default an = 'A'
default bn = 'B'
default cn = 'C'
default yn = 'Y'
## 啊这，半次元？





## 决定结局的是一个随机数，但玩家可以修改这个随机数的权重。这个数字是权重占比，意为初始权重1:1
default random_he = 1
default random_be = 1



## 程序内部使用，不要再动了
default in_map = False




label roof:
    a '天台的门锁着。'
    label roof_enter_code:
        menu:
            '要打开门锁吗？'
            '输入密码。':
                call screen roof_code
                if _return == True:
                    jump wewillwritethislater
                elif _return == False:
                    a '密码好像不对。'
                    jump roof_enter_code
                else:
                    jump main_loop
            '（离开）':
                jump main_loop




screen school_map():
    zorder 1
    modal True

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


label main_loop:
    'open the map'
    
    $ map.opt_init()
    $ in_map = True
    call screen school_map()
    $ in_map = False
    '（回到主循环）'
    jump main_loop
    
    return


screen map_say():
    pass










label y_1:
    'y_1'
    return

label y_2:
    'y_2'
    return

label y1:
    'y1'
    return

label y2:
    'y2'
    return

label y3:
    'y3'
    return

label c_1:
    'c_1'
    return

label c_2:
    'c_2'
    return

label c1:
    'c1'
    return

label c2:
    'c2'
    return

label c3:
    'c3'
    return

label b_1:
    'b_1'
    return

label b_2:
    'b_2'
    return

label b1:
    'b1'
    return

label b2:
    'b2'
    return

label b3:
    'b3'
    return


label playground:
    'playground'
    return

label building:
    'building'
    return

label cafeteria:
    'cafeteria'
    return

label p4:
    'p4'
    return

label p5:
    'p5'
    return

label p6:
    'p6'
    return

label p7:
    'p7'
    return

label p8:
    'p8'
    return

label p9:
    'p9'
    return














label start:

    ## 这里最好加点旁白，来简单介绍一下玩家的身份，比如说“你是一个高二学生”之类。但我写不出来，下次一定。
    jump main_loop
    
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
    a '好家伙。'
    b '不然我干嘛找你问，你猜课代表为啥没把作业写黑板上。'
    a '你这课代表当的可真尽责啊。'
    a '要不这样，你别把作业写上去了，这样你就是1班的大英雄。'
    b '……一会下课找人问吧。还有多久下课？'
    '老师' '还有10分钟。'
    '老师' '你跟[an]聊什么呢？聊得这么开心。我看你趴那儿睡好久了，要不你俩都站后面去，精神一会儿再回来上课。'
    a '……'
    a '老师对不起，我们错了。'
    b '老师对不起。'
    '老师' '唉……算了，今天最后一节课了，你们上了一天课可能也是累了，先坐下吧。'
    a '谢谢老师。'
    '老师' '……大家都高二了，现在学习压力也大，休息时间不充分……但是最基础的上课听讲，起码还是得做到吧？现在学的东西可比以前难多了，高二这个阶段是分水岭，这两极分化的时候，你缺了一节课没听，后面的内容也容易跟不上……'
    a '{alpha=*0.5}*小声*{/alpha}把你东西拿上。'
    b '{alpha=*0.5}*小声*{/alpha}什么东西？'
    a '{alpha=*0.5}*小声*{/alpha}自习课用的东西。'
    a '{alpha=*0.5}*小声*{/alpha}看到那个后门没有？一会趁他不注意，直接开溜。'
    b '{alpha=*0.5}*小声*{/alpha}成。还去图书馆？'
    a '{alpha=*0.5}*小声*{/alpha}去楼下空教室。那儿放学没人查，不像图书馆6点半就关门了。'
    '老师' '……这还有几天就期末考试了，我现在花了几节课给你串一遍这两本书知识点，为的就是你们期末考试能冲一把，别到下学期影响你分班。有的同学他不认真听讲，我也没办法……'
    a '{alpha=*0.5}*小声*{/alpha}就是现在，快溜！'
    show shadow onlayer effects
    scene bg c classroom with dissolve
    b '这地方挺好，比图书馆人少，还有电脑玩。'
    a '而且，大部分人还没意识到这一点，还在往图书馆挤。'
    a '唯一可惜的是，咱没有高三的门卡，教室门一旦关上就没人能打得开了，这都是不可再生资源。'
    b '那好办，地上随便捡一张高三落下的门卡就行。'
    b '他们搬哪儿去了？走的这么急，还几天就期末了。'
    a '好像是操场对面那块。'
    b '啊？就原来小学部那地方？'
    a '是，之前上操的时候那边一直在装修。'
    b '这么惨？这要去食堂还得横跨一整个操场，食堂不全被高一高二占了？'
    a '不是有高三通道吗？'
    b '那玩意基本没用，老有别的年级的在那儿排，也没人管。'
    '（……）'
    ## 高三搬走是因为有几间教室闹鬼，影响学生学习。这是我码字的时候现想的东西，我压根就不知道要怎么把它圆回来，可能这几天y阳了请假在家所以没人修门？？？
    scene black with dissolve
    scene bg c classroom with dissolve
    '（这里原先是高三上课的教室，他们走的很匆忙，大部分人都落下了点什么东西在课桌里。）'
    '（你面前的这张桌子也不例外，半张字迹非常潦草的稿纸正躺在桌洞中间。）'
    menu:## 这里做个dismiss组件
        '把它拿出来。':
            show rule01 at top with dissolve 
            hide rule01 with dissolve
    a '（写的什么？“不要在早上5:30-9:30去图书馆”……）'
    a '（这不那什么规则怪谈吗？竟有此等好事……保不齐这期末也不用考了！）'
    a '哎，别睡了，看看这个。'
    b '……干嘛？……你真摸着高三落下的门卡了？'
    a '不是。你看，他让咱们别在早上去图书馆……'
    b '废话，图书馆10点才开门。'
    a '虽然但是，就是说，他这时间为什么写得这么详细？'
    b '谁知道，为了装x随手瞎写的吧。我要睡了。'
    a '明天早上你陪我来趟图书馆吧！'
    b '……不去，别耽误我睡觉。'
    a '有没有一种可能，图书馆10点才开门，就是因为他说的是真的？'
    a '去看看嘛，给你枯燥无味的校园生活增添一点乐趣。'
    a '而且万一是真的，小则不用操心作业，大则取消期末考试……多么美好的未来啊！快跟我去看看！'
    with hpunch
    '（楼道里传来一声巨响，和一个女生的尖叫声。）'
    b '……啥玩意这么大动静？给我都吵醒了。'
    a '好像有个人。现在几点了？'
    b '快7点了。'
    a '啊~保不齐是怪谈成真！赶紧的，明天跟我看看去。'
    b '不去。'
    a '你放心，不用早起，从食堂过来的时候顺路看一眼就行。迟到的话就说是我们吃食堂拉肚子了。'
    b '……行吧。'


    scene black
    '（第二天）'

    
    a '好家伙，图书馆值班老师都没来呢。'
    b '{alpha=*0.5}*吃东西*{/alpha}确实，除了咱俩以外谁闲的没事来这么早。'
    a '那是为了拯救整个高二年级而做出的必要牺牲！'
    a '你看！这书架上都落了这么厚一层灰，还有这个杂志……2013年的，都多久没有更新了！肯定不对劲！'
    b '{alpha=*0.5}*吃东西*{/alpha}就我觉得这儿啥也没有？'
    a '那是因为你一直在吃东西，感知不到一些微小的变化。'
    b '{alpha=*0.5}*收起早餐*{/alpha}找不着鬼就赶紧走吧，别一会被班主任制裁了。'
    b '再说了，你动脑子想想，以学校那尿性，闹鬼了不也得期末考试。'
    b '不过这2013的杂志确实离谱，这都没人管吗？'
    a '你有没有听说过那个图书馆素养的选修课？'
    a '据说那个课特别水，除了自习以外就是拿学生当工具人，让他们整理书。'
    b '这么好？可以睡两节课。'
    a '别光想着睡觉啊，周五选修课报什么不好？有的课你还能白嫖教具，报这个不亏死了。'
    a '之前我报的那个油画选修，自己画的东西都能带走！虽然我画的不怎么好看……'
    b '你看看表。几点了？'
    '（手表上显示7:28。）'
    a '坏了，要早读了，快跑。'
    b '哎，我特么饭没吃完呢……'
    a '{alpha=*0.5}*边跑边说*{/alpha}不好意思啊，今天运气不太好，要是真碰见鬼，咱们都不用操心这个。'




    

    ## 第二天：b：没什么东西就赶紧走吧，别一会被班主任制裁了。你不动脑子想想，学校还能闹鬼？哪里有这种好事？



    ## 怎么样，学会导数了吗？
    ## 导数是什么？

    # menu:
        # '你这个年纪，怎么睡得着的？':

    return


















label weekend:
    '（一周结束了。）'
    return





label wewillwritethislater:
    '到达世界最高城，理塘！太美丽了理塘'
    '好吧这只是一个程序测试内容，现在我们回到游戏开头'
    return




    # menu:
    #     '咳咳，测试一下字数上限'
    #     '（适当的沉默）':
    #         pass
    #     '……艺考一般12月就结束了。':
    #         pass
    ## 好好好，很有感觉！！！（