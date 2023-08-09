
init offset = -1
style default:
    properties gui.text_properties()
    language gui.language
    font FontGroup().add("font.ttf", 0x0020, 0x007f).add("zpix.ttf", 0x0000, 0xffff)
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
style gui_text:
    properties gui.text_properties("interface")
style button:
    properties gui.button_properties("button")
style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
style prompt_text is gui_text:
    properties gui.text_properties("prompt")
style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


style ruby_style is default:
    size 15
    yoffset -35































################################################################################
## 游戏内界面
################################################################################

## 输入密码 ########################################################################

screen roof_code():
    modal True
    frame:
        style_prefix 'code'
        align (0.5, 0.5)
        has vbox

        text roofcode.refresh() xalign 0.5
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
            
style code_button_text:
    font gui.text_font









































################################################################################
## gui界面
################################################################################


screen developer_options():
    tag menu
    use game_menu('开发者选项'):
        has vbox
        text '天台密码：[persistent.HEYWHATAREYOUDOING]'
        text 'persistent.playthrough = [persistent.playthrough]'
        text 'persistent.firstrun = [persistent.firstrun]'
        # text '[tt.history_get()]'
        textbutton '清除游戏数据' action Confirm('确认重置全部游戏数据？', Function(reset_game_data))


## 对话界面 ########################################################################

screen say(who, what):
    style_prefix "say"
    key 'dismiss' action Return()
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

        ## 复杂的操作（指在地图界面上推进对话），往往只需要简单的办法
        button:
            xalign 0.5 ypos 0 xysize (1400,1400)
            action Return()



    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background At("gui/textbox.png", pixelzoom11, center)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    adjust_spacing False
    line_leading 7
    ruby_style style.ruby_style

## 输入界面 ########################################################################

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择界面 ########################################################################

screen choice(items):
    modal True
    style_prefix "choice"
    vbox:
        ypos 780-len(items)*43-len(items)*gui.choice_spacing+gui.choice_spacing
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

transform choicemove:
    easeout 0.4 xoffset 5
    easein 0.4 xoffset 0
    repeat



style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_background At('gui/button/choice_hover_background.png', pixelzoom11)
    idle_background At('gui/button/choice_idle_background.png', pixelzoom11)
    hover_foreground At('gui/button/choice_fg.png', pixelzoom11, choicemove, leftcenter)
    idle_foreground At('gui/button/choice_fg.png', pixelzoom11, leftcenter)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## 快捷菜单界面 ######################################################################

screen quick_menu():

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.96

            textbutton _("历史") action MenuHideInterface('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action MenuHideInterface('save')
            textbutton _("设置") action MenuHideInterface('preferences')


init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


## 导航界面 ########################################################################


screen navigation():

    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("开始游戏") action Start()

        else:
            textbutton _("历史") action ShowMenu("history")
            textbutton _("保存") action ShowMenu("save")

        textbutton _("读取游戏") action ShowMenu("load")
        textbutton _("设置") action ShowMenu("preferences")
        if config.developer:
            textbutton '开发者选项' action ShowMenu('developer_options')

        if _in_replay:
            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("标题界面") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        #     textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text
style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单界面 ######################################################################


screen main_menu():
    tag menu
    add gui.main_menu_background

    frame:
        style "main_menu_frame"

    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"
style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
style main_menu_title:
    properties gui.text_properties("title")
style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单界面 ######################################################################

default menuscrsdata = None

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    elif menuscrsdata:
        $ s = im.Data(menuscrsdata, "screenshot.png")
        add Transform(s, zoom=6, blur=15)

    frame:
        style "game_menu_outer_frame"
        background "gui/overlay/game_menu.png"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if not main_menu:
        key 's' action Return()
    key 'K_ESCAPE' action Return()


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## 关于界面 ########################################################################

screen about():
    tag menu

    use game_menu(_("关于"), scroll="viewport"):
        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
style about_label_text:
    size gui.label_text_size


## 读取和保存界面 #####################################################################

screen save():
    tag menu
    use file_slots(_("保存"))

screen load():
    tag menu
    use file_slots(_("读取游戏"))


screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))
    use game_menu(title):

        fixed:
            order_reverse True
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot) alternate FileDelete(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5 xoffset 10

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) 给出 1 到 9 之间的数字。
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    background At('gui/button/slot_idle_background.png', pixelzoom11)

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## 设置界面 ########################################################################

screen preferences():

    tag menu

    use game_menu(_("设置"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("") action Preference("display", "fullscreen")

                    vbox:
                        style_prefix "radio"
                        label '窗口大小'
                        textbutton '1920*1080' action Function(renpy.set_physical_size,(1920,1080))
                        textbutton '1600*900' action Function(renpy.set_physical_size,(1600,900))
                        textbutton '1280*720' action Function(renpy.set_physical_size,(1280,720))

                vbox:
                    style_prefix "check"
                    label _("快进")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后继续") action Preference("after choices", "toggle")
                    textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))

                if config.developer:
                    vbox:
                        
                        label ''
                        textbutton '低配模式' action gui.TogglePreference("low_performance_mode", True, False) style_prefix "check"
                        textbutton '清除截屏缓存' action SetVariable('menuscrsdata', None) 

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字速度")

                    bar value Preference("text speed")

                    label _("自动前进时间")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("音乐音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("音效音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("语音音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    background At("gui/button/check_[prefix_]background.png", pixelzoom4, leftcenter5)
    foreground At("gui/button/check_[prefix_]foreground.png", pixelzoom4, leftcenter5)

style check_button_text:
    properties gui.button_text_properties("check_button")
    xoffset 10

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## 历史界面 ########################################################################

screen history():

    tag menu

    ## 避免预缓存此界面，因为它可能非常大。
    predict False

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
                
            null height 20

        if not _history_list:
            label _("尚无对话历史记录。")



define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    font gui.text_font
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    font gui.text_font
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    line_leading 7
    ruby_style style.ruby_style

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 确认界面 ########################################################################


screen confirm(message, yes_action, no_action):

    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:
        at ctc_appear
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复 no（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## 快进指示界面 ######################################################################

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“▸”（黑色右旋小三角）字形的字体。
    font "DejaVuSans.ttf"


## 通知界面 ########################################################################

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式界面 ####################################################################


screen nvl(dialogue, items=None):
    tag phone
    if contact.enable_phone_mode:
        use phone_dialogue(dialogue, items)



## 消息出现的动态效果。因为可能是收也可能是发
## 用direction来决定出现的方向。
transform message_appear(direction):
    alpha 0.0
    xoffset 100 * direction
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0



screen phone_base(yinitial=0):
    zorder 10 
    frame:
        xcenter 0.3 yalign 0.5
        background "gui/mobile/phone_bg.png"
        viewport:
            offset (gui.phone_xoffset, gui.phone_yoffset) xysize (gui.phone_xsize, gui.phone_ysize)
            draggable True
            mousewheel True
            scrollbars 'vertical'
            yinitial yinitial
            transclude


screen phone_dialogue(dialogue, items=None):
    use phone_base(1.0):
        vbox:
            spacing 10
            xfill True

            null height 20
            
            use nvl_phonetext(dialogue, items)
            null height 20

            ## 负责显示选项的部分
            for i in items:
                button:
                    action i.action
                    pos (0,0)
                    xysize (gui.phone_xsize-30, 60)
                    background Solid(gui.idle_color)
                    hover_background Solid(gui.hover_color)
                    text i.caption align (0.5,0.5) text_align 0.5 color "#000"




screen nvl_phonetext(dialogue, items=None):

    ## dialogue 是对话，items是负责选项的部分。
    for d in dialogue:
        ## 如果是旁白，这样显示。
        if d.who == None:
            text d.what:
                pos (0,0) ## 这是一句神奇的代码，不加上它，你就看不见自己做了什么东西出来
                text_align 0.5
                xalign 0.5
                color "#00000056"
                size gui.text_size*0.8
                xsize gui.phone_xsize - 170
                italic True
                slow_cps False
                id d.what_id
                if d.current:
                    at transform:
                        alpha 0.0
                        yoffset -50
                        parallel:
                            ease 0.5 alpha 1.0
                        parallel:
                            easein_back 0.5 yoffset 0
        else:
            hbox:
                xpos 18 spacing 10
                xsize gui.phone_xsize

                ## 判断现在说话的人是不是主角，因为主角的显示方式和其他人不同。比如主角头像的方向和其他说话人不同。
                if d.who == contact.mc.name:
                    $ message_frame = "gui/mobile/send_base.png"
                    $ direction = 1
                    ## 因为主角是先显示对话框再显示头像，所以这里用下面这个参数。
                    box_reverse True
                else:
                    $ message_frame = "gui/mobile/text_base.png"
                    $ direction = -1

                # $ message_icon = d.who + "_icon.png"
                $ message_icon = 'gui/mobile/common_icon.png'

                ## 有选择枝的时候，items不为空，但是current为True，会重新加载最后一句对话。为了避免重新加载，需要判断是否有选择枝。
                add message_icon:
                    if d.current and not items:
                        at transform:
                            zoom 0.0
                            ease_back 0.5 zoom 1.0
                # vbox:
                
                frame:
                    yalign 1.0
                    padding (10,10)
                    # xsize gui.phone_xsize - 150

                    if d.current and not items:
                        at message_appear(direction)

                    text d.what:
                        pos (0,0)
                        xsize gui.phone_xsize - 170
                        slow_cps False
                        color "#000"
                        id d.what_id




screen contact:
    zorder 1
    modal True
    tag phone
    $ contacts = contact.contacts.values()
    $ contacts = sorted(contacts, key=lambda x: x.sort_score(), reverse=True)

    # button xysize (1280, 720) action [Hide('contact'), Return()]
    use phone_base():
        vbox:
            spacing gui.phone_vsp
            for idx, npc in enumerate(contacts):
                button:
                    action [Hide('contact'), Jump(contact.get_message(npc.name))]
                    vbox:
                        text npc.name:
                            color '#000000'
                            hover_color gui.accent_color
                        if npc.has_new_message():
                            text "(New)" color gui.accent_color
                        text npc.bio color gui.idle_color
                        if idx != len(contacts) - 1:
                            add Solid("#0000001f", xsize=gui.phone_xsize-30, ysize=4)





# transform phone_appear:
#     on show:
#         yoffset 720
#         easein_back 1.0 yoffset -50

################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action MenuHideInterface()


style window:
    variant "small"
    background At("gui/phone/textbox.png", pixelzoom10)

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
