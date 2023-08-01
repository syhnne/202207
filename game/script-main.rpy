


####################################################
## library #########################################
####################################################

label libr_loop_main(phase):
    '调查图书馆'
    $ in_map = True
    show screen expression 'libr_map_'+str(phase) with dissolve onlayer map
    label libr_loop:
        scene black
        pause
        $ allow_skipping = False
        if not temp1:
            jump libr_loop
    ## 这里还可以接着说话
    hide screen expression 'libr_map_'+str(phase) with dissolve onlayer map
    $ in_map = False
    $ temp1 = None
    return





## libr_1 #########################################

## 为什么会有map写在这？因为这个map属于只是往里面填东西的纯体力劳动，而且每个地点得跟一个label对应，
## 为了避免写的时候来回翻文件，消耗我的注意力，干脆放在一起
## 请务必遵循命名规范，至少最后一个字得是数字
screen libr_map_1():
    use libr_map_base:
        has vbox
        textbutton 'libr_1_1' action Call('libr_1_1')
        textbutton '结束调查' action Call('libr_1_end')


default libr_1_1_ = False
label libr_1_1:
    '调查内容'
    if not libr_1_1_:
        '你第一次读这个label'
    else:
        '你第2次或更多次读了这个label'
    '真不好意思，要在这里写屎山代码了，但我想不到别的办法来判断玩家是否看过这个label'
    'renpy唯一给的函数就是那个read，但是它判断的不是这个存档，而是tmd全局'
    '判断玩家在该存档是否读过一个label的函数，renpy难道没有吗？还是说让我给每个label都手动写一个变量才是设计者的本意？？'
    $ libr_1_1_ = True
    return




label libr_1_end:
    '现有的东西都调查完了。'
    $ temp1 = True
    return



## libr_2 #########################################

screen libr_map_2():
    use libr_map_base:
        has vbox
        textbutton 'libr_2_1' action Call('libr_2_1')
        textbutton '结束调查' action Call('libr_2_end')


default libr_2_1_ = 1
label libr_2_1:
    '第二次来图书馆'
    '你第[libr_2_1_]次点开这个东西'
    $ libr_2_1_ += 1
    return

label libr_2_end:
    '现有的东西都调查完了。'
    $ temp1 = True
    return





## main #########################################

label main_loop:
    $ loop_count += 1
    '打开地图'
    
    $ map.opt_init()
    $ in_map = True
    call screen school_map()
    $ in_map = False
    '（回到主循环）'
    if not out_of_events or loop_count <= 30:
        jump main_loop
    return





























label test_memory:
    '测试回放模式'
    '一般来说这个模式下不可以存档'
    return






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



















label temporary1:
    ## 有关主角一不小心发现第二张卡这件事。目前由于想不起别的特殊要求，他是在空教室里发现的。好吧，可能要改，要是有这么容易，岂不是早就被发现了（

    ## 另外，我现在面临一些困扰：写这东西的时候我采用了那种很奇葩的旁白，就是读起来好像a在和旁白对话一样。
    ## 目前我管这个叫星穹铁道式旁白，但是它会带来一些问题，真要搞吓人的东西或者正经的东西，就不能这么写了。

    ## 好了，修改了一下设定圆回来了。这种生动而欠揍的旁白只会在主角身边没有其他人的时候出现，因为主角其实也是阴暗b，详见文档

    a '那是什么东西？'
    a '好家伙，还真有高三落下的门卡。'
    '（没错，这是一张高三的门卡——一张外观很别致的门卡。）'
    '（卡面上贴了不少贴纸与小纸条，但透过它们的缝隙，你能看出原本的卡面甚至不是绿色的。）'
    '（也许它是旧版的学生一卡通，但总之，和你拿到的那版有很大差异。）'
    a '这卡长得还挺别致，感觉跟我那款不太一样啊。'
    '（你拿起卡，在教室的门禁上刷了一下。一声很长的“滴——”声告诉你，它能打开这间教室的门。）'
    ## 那当然，这是那个万能卡，打不开就见鬼啦
    a '看来就是这个班的。'
    a '真是太棒了，拿上这张卡，出去的时候把门一关，以后这间教室就归我了！'
    a '再也不用跟去食堂抢饭一样抢空教室了……好日子来临力！'
    a '……唉，话虽如此，这毕竟是有人用的卡。'
    a '要不，还是还回去？'
    menu:
        '要把卡还给这个班的同学吗？'
        '虽然很想留着……还是还吧。':
            a '算了，还是给人家还回去比较好。'
            a '我看看……高三3班，他们放学好像比较晚，过去看一眼。'
            ## y在高三3班，至于这张卡为什么刚好出现在这，这大概是命运的选择吧！
        '丢了就是用不到，归我了！':
            a '不过，这个人要是真用得着这张卡，不至于丢了这么久也不回来找。'
            a '也就是说，这卡对他来说没用。'
            a '那就由我替他保管吧！'
            '（高兴地写了一会作业之后，你决定带上这张卡，离开教室并顺手关门。）'
            '（这个时间大部分人都离开了学校，楼道里很安静。）'
            '（其他教室的门几乎也都关着，而且并没有亮灯。）'
            a '怪不得最近找地方这么费劲。别的教室是门真的关了，不是里面有人。'
            '（你下意识地拿着手里的门卡在门禁上晃悠了两下……反正楼道里也没人，听个门禁响玩玩。）'
            '（滴、滴——！）'
            '（滴、滴——！）'
            '（滴、滴——！）'
            '（你拿着卡在门禁上刷了又刷。没办法，虽然打不开门，但这个响声实在太好玩了，你感觉自己根本停不下来。）'
            '（等等，有什么不太对……）'
            '（刚才的声音里，除了滴滴声以外，好像还有一些机械结构发出的响动。）'
            a '嗯？？这门是开了吗？？这不是3班教室啊。'
            '（没错，这是4班教室。门真的开了，而且不出意外的话，就是被你手里那张卡刷开的。）'
            a '真是我刷开的？难不成这卡是老师的……'
            a '但这卡出现在教室后座，上面还贴了这么多东西，也没写老师名字。'
            a '不管了，要真是老师的卡，教务处会给他们补办的。'
            a '不过它能开门是真的，要不我趁机把所有门都刷开，造福全年级，这样也没人会介意我关一间3班教室的门吧。'
            '（于是你拿着门卡，挨个去刷整条楼道的教室门。）'
            '（滴、滴——！）'
            '（门禁的响声真是美妙，尤其是在你知道门已经开了的时候。）'
            '（刷开某一间教室时，你打开了门，猛然看到一片人影——）'
            a '（怎么有人……'
            with hpunch
            extend 'woc，小情侣！打扰了……）'
            '（你赶紧关上了门离开现场，装作无事发生。）'
            a '这都几点了还不走，过一会开门的可就不是我，而是保安师傅了……'
            ## a被小情侣吓了一跳，一不小心发动了卡的时停技能，现在y正在赶来的路上（
            a '接着刷剩下的门吧，一天碰见两对小情侣的概率应该没那么高……'
            '（外面的夕阳似乎变得更灿烂耀眼了。你望向窗外，原本万里无云的天空忽然出现了大片云彩。…'
            '…图书馆楼上方的一层云，都被阳光镀上一层金色，云彩的反光透过窗户，映在走廊里，熄了灯的教学楼都变得明亮了一些。）'
            a '好漂亮的云彩，拍张照吧。'
            '（手机提示：无法连接到互联网，请检查您的网络设置。）'
            a '照相机不用联网啊！'
            '（咔嚓！）'
            '（外面的云很漂亮，但拍到手机上，色彩就暗淡了很多。）'

            ## 奶奶的，想不出来，这一旮瘩先不写了，快进到y出场
            ## 仔细一想，y在他们那个教学楼搜了个遍，然后一溜烟穿过操场跑过来，还要一口气爬三层楼，好惨
            ## 我giao，刚写一旮瘩突然想起来他们这会儿应该已经认识了
            ## 奶奶的，这才意识到写上面那堆东西的时候我一眼草稿也没看……又有bug可以修了……

            # '（楼梯上忽然传来了很重的脚步声，听声音大概是非常着急，一步上两层台阶地走。）'
            
            # y '……'
            # a '好家伙，你放学不回家的吗？'
            # y '我倒是挺想问你这个问题的。你刚才干啥了？'
            # '（刚才你捡到了一张门卡。但相比之下，你觉得把看到小情侣这件事说出来更重要。万一他们其实不是小情侣……）'
            # a '这个，我刚刚看到了一些我不该看到的东西……'
            # y '什么东西？别扯废话，说重点。'
            # a '我打开一间教室的门，看到一男一女……'
            # y '……你是不是捡到了一张学生卡？'
            # menu:
            #     '没有！（理直气壮）':


            ## 好消息，人设圆回来了。坏消息，以上这一整段要删掉或者重写。
            ## 这就是写东西不看草稿的下场

    return







    
label temporary2:

    ## ab在图书馆被y救的那段。写的时候感觉简直太扯了，还好圆回来了（
    ## 前面的内容暂时略过

    a '你是图书馆管理员吗？'
    y '呃…对，我是。'
    menu:
        '对不起，我们这就回班。':
            $ opt = 1
            pass
        '我一眼就看出你不是人！':
            $ opt = 2
            a '（虽然很想这么说……还是算了吧。）'
            a '（可是这人真的很不对劲！高三不是都在卷吗，怎么会有学校喊高三的来给图书馆干活？学校不要高考成绩了？）'
            a '（而且这个犹豫的语气，一看就不是真负责管理图书的。）'

    a '这样……不好意思，我们马上回班。'
    b '抱歉，给你添麻烦了。'
    a '{alpha=*0.5}*小声*{/alpha}快走吧…'
    ## 一会之后
    if opt == 2:
        b '话说，学校真有图书管理员吗？'
        a '……你也这么觉得？'
        b '什么意思？'
        a '我觉得他不对劲！'
        a '你看他那个随意的态度，不像是真的。'
        # a '再说了，'
        ## 不写了，下次写
        ## a：学校没有夹击妹抖啊！！
        # b '我刚才就随口一说……不过你说的也对，我除了在食堂和操场对面那块以外就没见过高三的。'





## 写这种既无聊又毫无用途的片段真的有意义吗……
## 算了，就当是测试程序用的材料吧
label temporary3:
    a '所以，你为什么要穿一个黑t恤？'
    # a '（只是以防万一……很多怪谈里面穿黑衣服的还细分为正邪两派，不知道这人什么成分。）'
    a '（其实一次就算了，他每回出场都穿着这个黑t恤，他们老师不管的吗？）'
    y '因为第一次来酒店的时候忘带校服t恤了。'
    a '这都能忘的吗……'
    y '没办法，当时走得比较着急。'
    a '这……好家伙，那校服外套也只带了一件？你不回家取的吗？'
    y '对，懒得去。'
    a '所以从你搬到酒店以来，就从来没洗过衣服……？'
    y '我确实只有这一件衣服，但是我会洗。'
    y '很简单，衣服没干的话就别来学校，这样就不用穿校服了。'
    a '？？？'
    a '呃，看来高三生活并没有想象中那么辛苦啊。'
    y '你最好别这么觉得……高三每天上课到5点，并且留的作业基本都不是一个晚上能写完的。'
    y '而且每周六还要额外补课，周六也是晚上5点放，一般的高三生没时间到处乱跑。'
    y '但我不是一般的高三生，因为我根本不写作业。'
    a '这样考试不会寄吗……'
    y '不会，我写不写作业都考一样的分。'
    y '其实上课听讲也差不多，反正到了高三都是复习，不听课一样会做……'
    menu:
        '可惜我没有允许我不上学的家长。':
            a '真羡慕你们这种家长不管的……我只要病得不是特别厉害，都得来学校。'
            y '……'
        '别凡尔赛了……':
            a '（呃……真想给他一拳。）'
            a '……'
            a '你知道吗？我今天救了个人！'
            y '什么人？'
            a '就在刚才，我制止了自己把拳头打在你的脸上……'
    y '其实还有一个原因，校服t恤的领子工艺太差，总觉得它扎脖子，所以没必要的话就不穿了。'
    a '……突然感觉自己的脖子开始痒了。'
    return

    

























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