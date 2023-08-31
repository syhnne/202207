
init offset = -2



python early:

    import re

    ## 精心筛选了这个字体能显示出来的东西（
    nonunicode = '¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŃńŌōŎŏŐő'
    erererer = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    def glitchtext(length):
        if not isinstance(length, int):
            raise TypeError('glitchtext要输入int，你是不是想写_p')
        output = ""
        for x in range(length):
            output += renpy.random.choice(nonunicode+erererer)
        return output
    gtext_mainmenu = glitchtext(12)

    ## 输入字符串！！！
    def glitchtext_p(origin):
        output = ''
        if not isinstance(origin, str):
            return ''
        for x in origin:
            if x in '，。？！…（）：“”':
                output += x
            else:
                output += renpy.random.choice(nonunicode+erererer)
        return output
    
    def glitch_ansi(s):
        if not isinstance(s,str):
            return s
        else:
            s = s.encode('utf-8')
            s = s.decode('ansi', 'ignore')
            return s








    _glitch_text = True

    def parse_glitchtext(l):
        global _glitch_text
        if not _glitch_text:
            return l.renpy_statement()
        else:
            ## 注意：我实在没辙了，glitch text开启的时候id和文本标签之类都是不可用的。
            state = l.checkpoint()
            # Try for a single-argument say statement.
            what = l.triple_string() or l.string()
            if l.eol():
                l.expect_noblock('say statement')
                l.advance()
                print('who:', '', 'what:', what)
                return ('', what)
            l.revert(state)
            # Try for a two-argument say statement.
            who = l.say_expression()
            what = l.triple_string() or l.string()
            if (who is not None) and (what is not None):
                l.expect_eol()
                l.expect_noblock('say statement')
                l.advance()
                return (who, what)
            # This reports a parse error for any bad statement.
            l.error('expected statement--01-definitions.rpy')

    def execute_glitchtext(say_obj):
        global _glitch_text
        if not _glitch_text:
            pass
        else:
            who, what = say_obj
            if who != '':
                who = str(eval(who))
            print('【who】', who, '【what】', what)
            renpy.say(who, glitch_ansi(what))

    def next_glitchtext(l):
        global _glitch_text
        if not _glitch_text:
            return l
        else:
            pass

    renpy.register_statement(
        name='_',
        parse=parse_glitchtext,
        execute=execute_glitchtext,
        next=next_glitchtext,
    )
















init python:



    renpy.add_layer('ef', above='overlay')


    import functools

    ## 这个东西是为了天台的那个门而写的，但是可以用作一切六位数的密码。
    ## 它也告诉我一个道理：任何运算都应该打包成函数，而不是搞一个屎山label反复横跳……我最好把时间表也做成这种形式的，天呐，那是多少bug要修……
    class Roofcode():
        def __init__(self, code):
            self.code = code
            self.current_code = ['', '', '', '', '', '', ]
        
        def refresh(self):
            x = ''
            for c in self.current_code:
                if c != '':
                    x = x + str(c)
                else:
                    x = x + '-'
            return x

        def clear(self):
            self.current_code = ['', '', '', '', '', '', ]

        def enter(self, number):
            current_number = 0
            for c in self.current_code:
                if c == '':
                    break
                else:
                    current_number += 1
                    continue
                    
            if current_number < len(self.current_code):
                self.current_code[current_number] = number
            # return self.refresh()
        

        def confirm(self):
            if '' in self.current_code:
                self.current_code = ['', '', '', '', '', '', ]
                return False
            else:
                x = reduce(lambda x,y: x*10+y,  self.current_code)
                self.current_code = ['', '', '', '', '', '', ]
                if x==self.code:
                    return True
                else:
                    return False
    ## 这是天台门口的密码
    roofcode = Roofcode(persistent.HEYWHATAREYOUDOING)






































    ## 焯，原来是我用对象当做dict的key导致的吗

    import random


    class Chr():
        
        def __init__(self, p, *e):
            self.__e = list(e)
            self.__p = p
            self.cond = True

        def random_event(self):
            rf = random.random()
            if len(self.__e) <= 0:
                return False
            elif rf >= self.__p:
                return False
            else:
                random.shuffle(self.__e)
                print(str(self), self.__e)
                return self.__e[0]

        ## renpy会在鼠标移动到按钮上，刷新screen状态的时候，直接调用这个函数，导致我手里的事件不知不觉地就被删掉了。
        ## 所以一切操作必须写在这个闭包函数g()里面，不然会出现“角色事件刷新概率为170%”之类的离谱事件。
        ## 要不要去github提个反馈。。。。
        def action(self):
            if len(self.__e)>0:
                e = str(self.__e[0])
                def f(self):
                    def g():
                        self.__p = self.__p + 0.1
                        del self.__e[0]
                    return g
                f_return = f(self)
                return f_return
                print('Chr.action():', str(self), '-deleted:', e)
                print('Chr.action():', str(self), '-remain:', str(self.__e))
            else:
                print('Chr.action():', 'chr'+str(self)+'out of events')

        def add_event(self, ev):
            if isinstance(ev, tuple):
                self.__e.append(ev)
            else:
                raise TypeError('bad event on add_event()')

        def ev(self):
            if len(self.__e)>0:
                return self.__e
            return None
        def p(self):
            return self.__p

    class Loc():

        def __init__(self, name, pos, label):
            self.name = name
            self.label = label ## 对于map来说，这是screen
            self.pos = pos
            self.chr = None

        def n(self):
            return self.name

        def l(self):
            return Call(self.label)

        def p(self):
            return self.pos



    class Map(Loc):

        def __init__(self, name, pos, label, list):
            Loc.__init__(self, name, pos, label)
            self.list = list

        def l(self):
            return ShowTransient(self.label, dissolve)


    def list_common(l1, l2):
        for i in l1:
            if i in l2:
                return True
        return False


    ## definitions ##################################################                

        ## Loc: name, pos, label
        ## Map: name, pos, label, list
    
    ## t_b_
    cls2_1 = Loc('高二1班', (100,100), 'cls2_1')
    cls2_2 = Loc('高二2班', (200,100), 'cls2_2')
    cls2_3 = Loc('高二3班', (300,100), 'cls2_3')

    ## s_b_
    sh01 = Loc('阶梯教室1', (100,100), 'sh01')
    sh04 = Loc('阶梯教室4', (300,100), 'sh04')

    ## libr
    sroom = Loc('自习室', (300,300), 'sroom')

    ## school_map
    ## 后面的list还是得手动写啊，甜腻腻的
    ## 新建一个地点：在screen，下面的list里面分别添加这个地点对象，然后再写个label
    playgr = Loc('操场', (100,100), 'playground')
    cafe = Loc('食堂', (300,100), 'cafeteria')
    t_building = Map('高中楼…', (500,100), 't_b_f1', ['cls2_1', 'cls2_2', 'cls2_3'])
    s_building = Map('实验楼…', (700,100), 's_b_f1', ['sh01', 'sh04'])
    libr = Map('图书馆楼…', (900,100), 'libr_map', ['sroom'])

    ## chr
    yc = Chr(0.2, ('y_1','cls2_1'), ('y1','playgr'), ('y2','cafe'), ('y3','sroom'))
    cc = Chr(0.3, ('c_1','sh01'), ('c1','cafe'), ('c2','sroom'), ('c3','sroom'))
    bc = Chr(0.4, ('b_1','sh01'), ('b1','cls2_1'), ('b2','cls2_1'), ('b3','sroom'))



    current_events = None

    def get_options():
        opt_dict = {}
        for chr in {'yc','cc','bc'}:
            x = eval(chr).random_event()
            if isinstance(x, tuple):
                opt_dict[x[1]] = (x[0], chr)  ## 放进去一个 地点：（label，角色） 的键值对
                ## 淦，一不小心写了个自动查重。。那就不改了，回去给chr.random_event加个概率，就说角色不一定会出来找你，这是游戏特性
        if opt_dict == {}:
            return None
        return opt_dict

    def get_allev():
        l = []
        for chr in {yc,cc,bc}:
            e = chr.ev()
            if e != None:
                for i in e:
                    l.append(i[0])
        if len(l)==0:
            return None
        else:
            return l

    def loc_action(locn):
        print('loc_action():',locn)
        if current_events:
            ev = current_events[locn]
            chr = ev[1]
            f = eval(chr).action()
            return [Function(f), Call(ev[0])]
        else:
            renpy.error('没事件了你怎么还能选啊')



































    ## 作者：黑凤梨BlackPineappl https://www.bilibili.com/read/cv17016134?spm_id_from=333.999.0.0 出处：bilibili
    ## 感谢大佬的代码，我直接用了（发出懒人的声音


    class NPC(object):
        
        def __init__(self, name, bio="", texting_default="texting_default", friendship=0):

            self.name = name
            self.img = name + "_icon.png"
            self.bio = bio
            self.friendship = friendship
            ## 点击联系人，有3种信息显示。
            ## 主角给联系人发信息的演出，联系人并不会提示有新信息。
            ## 主角收到了联系人发的信息，会有信息提示。
            ## 缺省信息演出，如果系统中并没有前两种信息，但是玩家点了联系人，就会演出一个缺省的信息对话。
            self.texting_send = []
            self.texting_recieved = []
            self.texting_default = texting_default

        ## 判断是否有新信息。
        def has_new_message(self):
            return len(self.texting_send) > 0

        ## 联系人列表的排列顺序，如果有新消息就排列在前面，除此之外按照友好度排列。假设没有友好度会达到10000
        def sort_score(self):
            score = 10000 if self.has_new_message() else 0
            return self.friendship + score

        ## 获得和联系人的信息的label的名字。
        def get_message(self):
            if self.texting_send:
                return self.texting_send[0]

            if self.texting_recieved:
                return self.texting_recieved[0]

            return self.texting_default

        ## 删掉已经演出过的短信剧本。
        def pop_message(self):
            if self.texting_send:
                self.texting_send.pop(0)

            if self.texting_recieved:
                self.texting_recieved.pop(0)

    NARUTO = NPC('naruto')
    IRUKA = NPC('iruka', "今天也要好好学习。", friendship=5)
    NAVI = NPC('navi', "通讯记录刷新中", friendship=1)
    KAKASHI = NPC('kakashi', "周刊征稿，请联系我。", friendship=2)
    C_1 = NPC('c1', "自我介绍")
    C_2 = NPC('c2', "关于我的关键字")
    C_3 = NPC('c3', "随便写写")
    C_4 = NPC('c4', "这个是我的网站")
    C_5 = NPC('c5', "小猫咪能有什么坏心眼")



    class Contact(object):
        def __init__(self, mc, npcs=[]):
            ## 主角的名字，因为主角在发短信的屏幕和别人的显示不同，这里记录下主角的名字。
            self.mc = mc

            ## 用字典储存联系人，键是人名字的字符串，值是NPC对象。
            self.contacts = dict()

            ## 是否在nvl mode启用这个phone的屏幕。如果不在游戏里使用nvl，可以直接改自带的nvl screen
            self.enable_phone_mode = True

            ## 初始化主角的通讯录，添加NPC到通讯录中。
            for npc in npcs:
                self.add(npc)

        ## 添加一个联系人到通讯录。参数是一个NPC对象。
        def add(self, npc):
            self.contacts[npc.name] = npc

        ## 从通讯录删掉一个联系人。参数是一个字符串，npc的名字。
        def remove(self, name):
            del self.contacts[name]

        ## 通过NPC名字的字符串获得NPC对应的头像，用于聊天对话显示。
        def get_icon(self, name):
            if name == self.mc:
                return self.mc.img

            return self.contacts[name].img

        ## 获得和联系人短信脚本的label的名字，是一个字符串。
        def get_message(self, name):
            return self.contacts[name].get_message() 

    contact = Contact(NARUTO, [IRUKA, NAVI, KAKASHI, C_1, C_2, C_3, C_4, C_5])

    # def fileclearfocus(slot_s):
    #     global gui.file_slot_rows, gui.file_slot_cols
    #     slot = int(slot_s)
    #     l = []
    #     for i in range(gui.file_slot_rows*gui.file_slot_cols):
    #         if i != slot:
    #             l.append(i)
        


    def nvl_adv_callback(mode, old_modes):
        global _history
        old = old_modes[0]

        if mode == "nvl" or mode == "nvl_menu":
            _history = False

        if mode == "say" or mode == "menu":
            _history = True

    config.mode_callbacks.append(nvl_adv_callback)








































    
        
    ## 需要在文件保存界面读取的内容。文档里抄的，不知道为啥能跑：https://www.renpy.cn/doc/config.html#var-config.save_json_callbacks
    def jsoncallback(d):
        d['test'] = 1
    config.save_json_callbacks.append(jsoncallback)

    ## 删存档
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    ## 重置游戏数据
    def reset_game_data():
        delete_all_saves()
        persistent._clear(True)
        renpy.quit(relaunch=True)

    ## 从头再来，但不重置游戏数据
    def game_utter_restart():
        delete_all_saves()
        renpy.quit(relaunch=True)

    ## 增加对话历史，修改who保证界面上出现灰色字体
    def add_history(what='', who='__add', kind='adv'):
        narrator.add_history(kind, who, what)


    # 打开菜单时存储一个二进制图片，用作模糊背景。renpy你就不能做一个不是二进制的函数吗？害得我每次打开菜单都要加载0.5秒，最后不得不写了个低功耗模式，我宣布这是整个工程中最粪的代码
    def menuscrs():
        global menuscrsdata
        menuscrsdata = renpy.screenshot_to_bytes((320,180))

    ## 这是打开菜单时实际使用的action，拿去替换所有的ShowMenu即可，名字起的不是很好，我懒得改了。
    def MenuHideInterface(menu):
        if gui.low_performance_mode:
            return ShowMenu(menu)
        else:
            return ShowMenuMod(menu)

    ## 为了修复【隐藏用户界面保证菜单上没有原先的用户界面，但是这个时候存档截屏也会看不到界面】这个问题，重新设置了showmenu的功能，
    ## 保证【存档的截屏】发生在【我手动隐藏用户界面并截屏拿去给菜单当背景】之前。
    ## 直接复制的，修改了最后一行，把'_game_menu'改成'_game_menu_mod'。
    class ShowMenuMod(Action, DictEquality):
        def __init__(self, screen=None, *args, **kwargs):
            self.screen = screen
            self.transition = kwargs.pop("_transition", None)
            self.args = args
            self.kwargs = kwargs
        def __call__(self):
            if not self.get_sensitive():
                return
            orig_screen = screen = self.screen or store._game_menu_screen
            if not (renpy.has_screen(screen) or renpy.has_label(screen)):
                screen = screen + "_screen"
            renpy.call_in_new_context("_game_menu_mod", *self.args, _game_menu_screen=screen, **self.kwargs)

    ## 重写的一个方法，我试过直接运行下面那个函数，好像不行，估计renpy在里面加了些什么东西
    class HideInterfaceMod(Action, DictEquality):
        def __call__(self):
            renpy.call_in_new_context("_hide_windows_mod")

## 原label名为_hide_windows，删去了python语句块的第三句话，让用户无法使用点击事件，然后在ui.interact中加入pause参数，使隐藏ui事件自动结束（core.py line 3552）
label _hide_windows_mod:
    python:
        _windows_hidden = True
        voice_sustain()
        ui.interact(pause=0.01, suppress_overlay=True, suppress_window=True)
        _windows_hidden = False
    return

## 哦哦哦哦哦哦哦！！成功了！！！
label _game_menu_mod(*args, _game_menu_screen=_game_menu_screen, **kwargs):
    if not _game_menu_screen:
        return
    $ renpy.play(config.enter_sound)
    $ _enter_menu()
    ## 下面两行我加的，试了试，只有放在这个位置能保证两次截屏顺序正确
    ## 第一次截屏发生在_enter_menu()函数里面，我猜那个是给FileScreenshot用的，结果我猜对了
    ## 第二次截屏就是下文的menuscrs，我要保证他发生在我手动隐藏interface之后
    ## 20230713:地图变大了，变成了viewport，只好来这里改
    if not _in_map:
        $ renpy.run(HideInterfaceMod())
    $ menuscrs()

    $ renpy.transition(config.enter_transition)
    if renpy.has_label("enter_game_menu"):
        call expression "enter_game_menu" from _call_expression_4
    if config.game_menu_music:
        $ renpy.music.play(config.game_menu_music, if_changed=True)
    if renpy.has_label("game_menu"):
        jump expression "game_menu"
    if renpy.has_screen(_game_menu_screen):
        $ renpy.show_screen(_game_menu_screen, *args, _transient=True, **kwargs)
        $ ui.interact(suppress_overlay=True, suppress_window=True) ##这是关键
        jump _noisy_return
    jump expression _game_menu_screen

