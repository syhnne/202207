
init python:

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

















    def len0(list):
        if len(list)>0:
            return len[0]
        else:
            return None
    
    ## 家人们谁懂啊，cpu最烧的一集，从特么放学修到半夜1点。
    ## 方便起见，我用整数来代表地点，这里是它对应的标签。函数的最后一步，或者直接写screen那里，得来这地方查一下地点标签叫啥
    list_ = []

    class CharacterEvents():
        
        def __init__(self, e1, e2):
            self.__e1 = e1
            self.__e2 = e2 

        ## Return a tuple if available. If not, returns None.
        def random_event(self):
            # global list_
            list_ = []
            if len(self.__e1)+len(self.__e2) <= 0:
                return False
            else:
                list_ = self.__e2
                if len(self.__e1)>0:
                    if not self.__e1[0] in list_:
                        list_.append(self.__e1[0])
                if list_ == []:
                    return False
                else:
                    return renpy.random.choice(list_)
    
        def del_event(self, event):
            if event in self.__e1:
                self.__e1.remove(event)
            elif event in self.__e2:
                self.__e2.remove(event)
            else:
                pass
            ## 都找不着的话就是没有，不管了

        def ev(self):
            return self.__e1 + self.__e2




    y = CharacterEvents([('y_1',1), ('y_2',3),], [('y1',1), ('y2',5), ('y3',7)])
    c = CharacterEvents([('c_1',2), ('c_2',1),], [('c1',2), ('c2',3), ('c3',6)])
    b = CharacterEvents([('b_1',3), ('b_2',2),], [('b1',1), ('b2',6), ('b3',3)])






    def e():
        s = list_
        q = y.ev() + c.ev() + b.ev()
        return [s,q]











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
            opt_dict = {}
            for chr in {y,c,b}:
                choice = chr.random_event()
                if choice != False:
                    opt_dict[chr] = choice
            if opt_dict == {}:
                raise ValueError('你选项用完了,这倒霉催的for循环怎么他妈不干活啊，你嘛死了')
            return opt_dict

        def opt_init(self):
            self.current_opt = None
            self.current_opt = self.get_options()
        
        def show_spot(self, number):
            name, label, pos = self.spot_name[number], self.spot_label[number], self.spot_pos[number]
            if self.spot_available[number]:
                ## showspot
                if self.current_opt:
                    for i in self.current_opt.values():
                        if i[1] == number:
                            label = i[0]
                        elif i[1] >= 9:
                            raise ValueError('Invalid location number on map.show_spot()')
                return [name, label, pos]
            else:
                return None
        
        def action(self, tuple_):
            if self.current_opt:
                pass
                ## 日你妈，是你逼我写屎山的，我本来想写的干净整洁一点，谁他妈知道这倒霉催的比玩意报了两天两夜的错
                y.del_event(tuple_)
                c.del_event(tuple_)
                b.del_event(tuple_)
            else:
                raise ValueError('我真的服，你tm什么时候把我列表吞了')

    map = MapEvent()
































    renpy.add_layer('effects', above='master', below=None, menu_clear=False)
    effects = 'effects'

    ## 感谢ddlc，我直接对代码进行一个照搬。
    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
    erererer = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    def glitchtext(length):
        output = ""
        for x in range(length):
            output += renpy.random.choice(nonunicode+erererer)
        return output
    gtext_mainmenu = glitchtext(12)
        
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

