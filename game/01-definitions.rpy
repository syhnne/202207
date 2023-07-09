
init python:

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

