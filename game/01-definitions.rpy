
init offset = -2



python early:

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





    ## 实时文字乱码

    say_glitch = False

    ## 感谢大自然的馈赠：parser.py line 1537
    def parse_say_glitch(l):
        state = l.checkpoint()
        # Try for a single-argument say statement.
        what = l.triple_string() or l.string()
        if l.eol():
            l.expect_noblock('say statement')
            l.advance()
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
  
    
    def execute_say_glitch(say_obj):
        global say_glitch
        who, what = say_obj
        if who != '':
            who = str(eval(who))
        if say_glitch:
            renpy.say(who, glitchtext_p(what))
        else:
            renpy.say(who, what)


    # 坏消息：重新定义这个statement会导致id不可用，也就是不能方便地切换角色立绘，所以我要寻找别的方法了。。ng应该也是不可用了
    renpy.register_statement(
        name='',
        parse=parse_say_glitch,
        execute=execute_say_glitch,
    )

    ## 语句前面加入ng，表示这句话在任何情况下都显示为原文字
    def execute_nonglitch(say_obj):
        who, what = say_obj
        if who != '':
            who = str(eval(who))
        renpy.say(who, what)
    
    renpy.register_statement(
        name='ng',
        parse=parse_say_glitch,
        execute=execute_nonglitch,
    )
















init python:



    renpy.add_layer('map', above='master', menu_clear=False)


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














    import functools

    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper




    import random

    class Chr():
        
        def __init__(self, *e):
            self.__e = list(e)

        def random_event(self):
            if len(self.__e) <= 0:
                return False
            else:
                random.shuffle(self.__e)
                return self.__e[0]

        def del_event(self):
            
            print('delete:--', self.__e[0])
            del self.__e[0]
            
            print(self.__e)

        def add_event(self, ev):
            if isinstance(ev, tuple):
                self.__e.append(ev)
            else:
                raise TypeError('bad event on add_event()')


        def ev(self):
            return self.__e


    yc = Chr(('y_1',1), ('y_2',3), ('y1',1), ('y2',5), ('y3',7))
    cc = Chr(('c_1',2), ('c_2',1), ('c1',2), ('c2',3), ('c3',6))
    bc = Chr(('b_1',3), ('b_2',2), ('b1',1), ('b2',6), ('b3',3))

    ## 他吗的。我是傻逼，要给事件按顺序排，我在y_1那里加个append函数把_2加进列表里不就完事了吗？？？
    ## 这比我写的那个傻逼方法好多了，想加事件随时都能加，我……唉……
    
    def e():
        return yc.ev() + cc.ev() + bc.ev()









    class MapEvent():

        def __init__(self):
            self.current_opt = None
            self.spot_name = {
                1:'操场',
                2:'高中楼',
                3:'食堂',
                4:'p40',
                5:'p50',
                6:'p60',
                7:'p70',
                8:'p80',
                9:'p90',
            } 
            self.spot_label = {
                1:'playground',
                2:'building',
                3:'cafeteria',
                4:'p4',
                5:'p5',
                6:'p6',
                7:'p7',
                8:'p8',
                9:'p9',
            }
            self.spot_pos = {
                1:(100,100),
                2:(200,100),
                3:(300,100),
                4:(400,100),
                5:(500,100),
                6:(600,100),
                7:(700,100),
                8:(800,100),
                9:(900,100),
            }
            self.spot_available = {
                1:True,
                2:True,
                3:True,
                4:True,
                5:True,
                6:True,
                7:True,
                8:True,
                9:True,
            }

        def get_options(self):
            global out_of_events
            opt_dict = {}
            for chr in {yc,cc,bc}:
                if chr.random_event() != False:
                    opt_dict[chr] = chr.random_event()
            if opt_dict == {}:
                out_of_events= True
            return opt_dict

        def opt_init(self):
            self.current_opt = None
            self.current_opt = self.get_options()
        
        def show_spot(self, number):
            name, label, pos, chr = self.spot_name[number], self.spot_label[number], self.spot_pos[number], None
            if self.spot_available[number]:
                ## showspot
                if self.current_opt and self.current_opt != {}:
                    for k,v in self.current_opt.items():
                        if v[1] == number:
                            label = v[0]
                            chr = k
                        elif v[1] >= 9:
                            raise ValueError('Invalid location number on map.show_spot()')
                return [name, label, pos, chr]
            else:
                return None
        def action(self, l4):
            print('on map.action():')
            if l4[3]:
                print('chr')
                l4[3].del_event()
            else:
                print('--')
            renpy.call(l4[1])

    map = MapEvent()































    renpy.add_layer('effects', above='master', below=None, menu_clear=False)
    effects = 'effects'

    
        
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
    if not in_map:
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

