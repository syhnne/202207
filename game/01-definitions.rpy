
init python:

    from functools import reduce

    ## 这个东西是为了天台的那个门而写的，但是可以用作一切六位数的密码。
    ## 它也告诉我一个道理：任何运算都应该打包成函数，而不是搞一个屎山label反复横跳……我最好把时间表也做成这种形式的，天呐，那是多少bug要修……
    class Roofcode():
        def __init__(self, code) -> None:
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


    ## 家人们谁懂啊，cpu最烧的一集，从特么放学修到半夜1点。
    
    import random

    ## 方便起见，我用整数来代表地点，这里是它对应的标签。函数的最后一步，或者直接写screen那里，得来这地方查一下地点标签叫啥
    spotdict = {
        1:'playground',
        2:'building',
        3:'cafeteria',
    }

    class CharacterEvents():
        
        def __init__(self, e1, e2):
            self.e1 = e1
            self.e2 = e2 

        ## Return a tuple if available. If not, returns None.
        def random_event(self, exclude=None):
            if len(self.e1)+len(self.e2) <= 0:
                return False
            else:
                choice = set(self.e2)
                if len(self.e1)>0:
                    choice.add(self.e1[0])

                if exclude:
                    choice = set(filter(lambda x: not x[1] in exclude, choice))
                if list(choice) == []:
                    return None
                else:
                    return random.choice(list(choice))

        def del_event(self, event):
            if event in self.e1:
                self.e1.remove(event)
            elif event in self.e2:
                self.e2.remove(event)
            # else:
            #     print('bad event')
            ## 都找不着的话就是没有，不管了



    class Timetable():

        def __init__(self):

            self.history = []
            self.banned = None
            self.characters = {y,c,b}

        def get_options(self):
            if self.banned:
                self.characters.remove(self.banned)

            dict = {}
            except_location = []
            for chr in self.characters:
                choice = chr.random_event(except_location)
                if choice:
                    dict[chr] = choice
                    except_location.append(choice[1])
                
            
                
            if self.banned:
                self.characters.add(self.banned)
            return dict

        def choose(self, choice, opt):
            if not isinstance(choice, CharacterEvents):
                raise TypeError('输入角色！！')
            if self.banned != None:
                self.banned = None
            if opt == {}:
                return 'running out of all options!'
            elif choice in opt.keys():
                target = opt[choice]
                self.history.append(choice)
                self.banned = choice
                choice.del_event(target)
                return target[0]
            else:
                return 'running out of options of your character.'



    y = CharacterEvents([('y_1',1), ('y_2',3),], [('y1',1), ('y2',5), ('y3',7)])
    c = CharacterEvents([('c_1',2), ('c_2',1),], [('c1',2), ('c2',3), ('c3',6)])
    b = CharacterEvents([('b_1',3), ('b_2',2),], [('b1',1), ('b2',6), ('b3',3)])


    tt = Timetable()



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

