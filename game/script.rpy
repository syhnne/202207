
## 天台那扇门的密码。一般来说玩家不会知道他是多少
default persistent.HEYWHATAREYOUDOING = renpy.random.randint(100000,999999)
default persistent.playthrough = 1
default persistent.firstrun = False

define a = Character("an", dynamic=True)
define b = Character("bn", dynamic=True)
define c = Character("cn", dynamic=True)
define y = Character("yn", dynamic=True)
define e = Character("艾琳")
## 妈的，这种前面带character.的用法竟然和cds冲突。。

default an = 'a'
default bn = 'b'
default cn = 'c'
default yn = 'y'
## 啊这，半次元？





## 决定结局的是一个随机数，但玩家可以修改这个随机数的权重。这个数字是权重占比，意为初始权重1:1
default random_he = 1
default random_be = 1

## 字面意思，就是san值，小于等于4的时候会看到乱码，目前正在尝试攻克显示乱码的核心技术
default san = 10

default time = 0



## 程序内部使用，不要再动了
default _in_map = False
default _in_phone = False
default loop_count = 0
default _out_of_events = False
default opt = None
default temp1 = None ## 调查界面退出flag
default temp2 = None
default _glitch_text = False

##
## 很重要，没有下面的4行，NVL会没有办法清理掉。
init python:
    # config.empty_window = None
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

define n_nvl = Character("naruto", kind=nvl,)
define e_nvl = Character("iruka", kind=nvl,)
define nvl_ = Character(None, kind=nvl)




label splashscreen:
    if not persistent.firstrun:
        $ preferences.text_cps = 40
        $ persistent.firstrun = True
    return

label after_load:
    $ print('---------------Game loaded!----------------')
    return

















label start:
    $ print('-------------------Game started!------------------------')
    




    $ IRUKA.texting_send.append('script_1')
    $ NAVI.texting_recieved.append('script_2')
    # jump contact



    scene black with dissolve
    jump main_loop
    















    ## 坏，我正文就这么几个字，现在估计要改不少。不过鉴于我对这次想出来的东西非常满意，整体来看不算损失惨重
    window hide

    # '（显然，你是一位名字叫做[an]的高中学生，正坐在教室里上课。）'
    # '（此时此刻，你正在专心思考自己的名字为什么如此敷衍，并没有注意到你的好朋友正在和你说话。）'
    b '……醒醒，你记不记得化学作业？'
    a '啊，什么？咋了？'
    b '化学作业……'
    a '哟，你要开卷啦？'
    b '我是说，你记没记化学作业……'
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
    b '{alpha=*0.5}*小声*{/alpha}咱还去图书馆？'
    a '{alpha=*0.5}*小声*{/alpha}去楼下空教室吧。那儿放学没人查，不像图书馆6点半就关门了。'
    '老师' '……这还有几天就期末考试了，我现在花了几节课给你串一遍这两本书知识点，为的就是你们期末考试能冲一把，别到下学期影响你分班。有的同学他不认真听讲，我也没办法……'
    a '{alpha=*0.5}*小声*{/alpha}就是现在，润！'
    show shadow onlayer effects
    scene bg c classroom with dissolve
    b '这地方挺好，比图书馆人少，还能玩班里电脑。'
    a '最主要是大部分人还没意识到空教室可以来，还在往图书馆挤。'
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
    ## 呃不过有人出事应该是一年多以前，y刚上高二那会儿，还不是现在，我还得另找理由
    scene black with dissolve
    scene bg c classroom with dissolve
    '（没过多久，）'
    '（这里原先是高三上课的教室，他们走的很匆忙，大部分人都落下了点什么东西在课桌里。）'
    '（你面前的这张桌子也不例外，半张字迹非常潦草的稿纸正躺在桌洞中间。）'
    ## 这里做个dismiss组件
    '（出于好奇，你把它拿了出来。）'
    show rule01 at top with dissolve 
    hide rule01 with dissolve
    a '（写的什么？“不要在早上5:30-9:30去图书馆”……）'
    '（没错，这纸上的内容像极了你闲来无事逛b站会刷到的那种规则类怪谈。）'
    '（）'
    a '（难道图书馆里有灵异事件？）'
    menu:
        '好可怕，我再也不想上学了！':
            a '（……哇，好可怕，我再也不要来学校了！）'
        '还有这种好事？':
            a '（他什么意思，图书馆有脏东西吗？）'
            a '（真是太棒了！他说的最好是真的，运气好的话以后再也不用上学了！）'
    a '哎，别睡了，看看这个。'
    b '……干嘛？……你真摸着高三落下的门卡了？'
    a '你看，这不是那种规则类怪谈吗？时间写的这么详细，必然是此地无银三百两。'
    a '明天早上你陪我来趟图书馆吧！肯定会有令人惊喜的发现。'
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
    ## 绷不住了，每次打开vscode都要被自己写的东西创一遍，然后疯狂地改

    scene black
    '（第二天）'

    
    '（）'
    a '好家伙，图书馆值班老师都没来呢。'
    b '{alpha=*0.5}*吃东西*{/alpha}确实，除了咱俩以外谁闲的没事来这么早。'
    ## 这是冬天，应该会很冷。。
    a '那是为了拯救整个高二年级而做出的必要牺牲！'
    a '你看！这书架上都落了这么厚一层灰，还有这个杂志……2013年的，都多久没有更新了！肯定不对劲！'
    b '{alpha=*0.5}*吃东西*{/alpha}呃，但是我觉得这儿啥也没有。'
    a '那是因为你一直在吃东西，感知不到一些微小的变化。'
    b '{alpha=*0.5}*收起早餐*{/alpha}你是怎么确定这里一定有鬼的……'
    a '那还用说！这既然是个游戏，肯定得有真家伙才能推进后面的剧情啊！'
    b '啊？'
    a '咱们先分头找找，我觉得肯定有！'
    b '好吧，别找太久，不然要被班主任制裁了。'
    b '而且我说……以学校那尿性，有没有一种可能，闹鬼了也得照常期末考试。'
    ## 这里可以加一些让玩家自己调查的内容，可以是给选项，也可以做得更复杂一点，以后再说吧
    b '……不过这2013的杂志确实离谱。图书馆是根本没人来么？'
    a '你有没有听说过那个图书馆素养的选修课？'
    a '据说那个课特别水，除了自习以外就是拿学生当工具人，让他们整理书。'
    a '估计是上回选修课被占了，所以没人整理。'
    b '这么好？可以睡两节课啊。'
    a '啊这，你别光想着睡觉，周五选修课报什么不好？有的课你还能白嫖教具，报这个不亏死了。'
    a '之前我报的那个油画选修，自己画的东西都能带走！虽然我画的不怎么好看……'








    if persistent.playthrough == 2:
        jump main_1


    return






















label main_1:

    b '你看看表。几点了？'
    '（手表上显示7:28。）'
    a '坏了，要早读了，快跑。'
    b '哎，我特么饭没吃完呢……'


    




    




    # menu:
        # '你这个年纪，你怎么睡得着的？':

    ## 
    
    call main_loop

    if loop_count > 30:
        jump normal_ending
    

    return


















label weekend:
    '（一周结束了。）'
    return





label normal_ending:
    'normal'
    return