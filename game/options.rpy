
define config.keymap = dict(
    # 除非明确禁用，各处都能使用的绑定快捷键。
    # 'mousedown_4'：鼠标滚轮上

    rollback = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK'],
    screenshot = [ ],
    toggle_afm = [ ],
    toggle_fullscreen = [ 'alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11', 'noshift_K_f' ],
    game_menu = [ 'K_ESCAPE' ],
    hide_windows = [ 'mouseup_2', 'h', 'noshift_K_h' ],
    launch_editor = [ 'E', 'shift_K_e' ],
    dump_styles = [ ],
    reload_game = [ 'R', 'alt_shift_K_r', 'shift_K_r' ],
    inspector = [ 'I', 'shift_K_i' ],
    full_inspector = [ 'alt_shift_K_i' ],
    developer = [ 'shift_K_d', 'alt_shift_K_d' ],
    quit = [ ],
    iconify = [ ],
    help = [ 'K_F1', 'meta_shift_/' ],
    choose_renderer = [ 'G', 'alt_shift_K_g', 'shift_K_g' ],
    progress_screen = [ 'alt_shift_K_p', 'meta_shift_K_p', 'K_F2' ],
    accessibility = [ "K_a" ],

    # 数据读取。
    self_voicing = [ ],
    clipboard_voicing = [ 'C', 'alt_shift_K_c', 'shift_K_c' ],
    debug_voicing = [ 'alt_shift_K_v', 'meta_shift_K_v' ],

    # say相关。
    rollforward = [ 'mousedown_5', 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],
    dismiss = [ 'mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT' ],
    dismiss_unfocused = [ ],

    # 暂停。
    dismiss_hard_pause = [ ],

    # 焦点相关。
    focus_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    focus_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    focus_up = [ 'K_UP', 'repeat_K_UP' ],
    focus_down = [ 'K_DOWN', 'repeat_K_DOWN' ],

    # 按钮。
    button_ignore = [ 'mousedown_1' ],
    button_select = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    button_alternate = [ 'mouseup_3' ],
    button_alternate_ignore = [ 'mousedown_3' ],

    # 输入。
    input_backspace = [ 'K_BACKSPACE', 'repeat_K_BACKSPACE' ],
    input_enter = [ 'K_RETURN', 'K_KP_ENTER' ],
    input_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    input_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    input_up = [ 'K_UP', 'repeat_K_UP' ],
    input_down = [ 'K_DOWN', 'repeat_K_DOWN' ],
    input_delete = [ 'K_DELETE', 'repeat_K_DELETE' ],
    input_home = [ 'K_HOME', 'meta_K_LEFT' ],
    input_end = [ 'K_END', 'meta_K_RIGHT' ],
    input_copy = [ 'ctrl_noshift_K_INSERT', 'ctrl_noshift_K_c', 'meta_noshift_K_c' ],
    input_paste = [ 'shift_K_INSERT', 'ctrl_noshift_K_v', 'meta_noshift_K_v' ],
    input_jump_word_left = [ 'osctrl_K_LEFT' ],
    input_jump_word_right = [ 'osctrl_K_RIGHT' ],
    input_delete_word = [ 'osctrl_K_BACKSPACE' ],
    input_delete_full = [ 'meta_K_BACKSPACE' ],

    # 视口。
    viewport_leftarrow = [ 'K_LEFT', 'repeat_K_LEFT' ],
    viewport_rightarrow = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    viewport_uparrow = [ 'K_UP', 'repeat_K_UP' ],
    viewport_downarrow = [ 'K_DOWN', 'repeat_K_DOWN' ],
    viewport_wheelup = [ 'mousedown_4' ],
    viewport_wheeldown = [ 'mousedown_5' ],
    viewport_drag_start = [ 'mousedown_1' ],
    viewport_drag_end = [ 'mouseup_1' ],
    viewport_pageup = [ 'K_PAGEUP', 'repeat_K_PAGEUP' ],
    viewport_pagedown = [ 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],

    # 这些按键控制跳过。
    skip = [ 'K_LCTRL', 'K_RCTRL' ],
    stop_skipping = [ ],
    toggle_skip = [  ],
    fast_skip = [ '>', 'shift_K_PERIOD' ],

    # Bar。
    bar_activate = [ 'mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    bar_deactivate = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    bar_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    bar_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    bar_up = [ 'K_UP', 'repeat_K_UP' ],
    bar_down = [ 'K_DOWN', 'repeat_K_DOWN' ],

    # 删除存档。
    save_delete = [ 'K_DELETE' ],

    # 可拖拽组件。
    drag_activate = [ 'mousedown_1' ],
    drag_deactivate = [ 'mouseup_1' ],

    # 调试控制台。
    console = [ 'shift_K_o', 'alt_shift_K_o' ],
    console_older = [ 'K_UP', 'repeat_K_UP' ],
    console_newer = [ 'K_DOWN', 'repeat_K_DOWN'],

    # 编导器
    director = [ 'noshift_K_d' ],

    # 忽略(保持后向兼容)。
    toggle_music = [ 'm' ],
    viewport_up = [ 'mousedown_4' ],
    viewport_down = [ 'mousedown_5' ],

    # Profile命令。
    performance = [ 'K_F3' ],
    image_load_log = [ 'K_F4' ],
    profile_once = [ 'K_F8' ],
    memory_profile = [ 'K_F7' ],

    )

define config.mouse = {}
define config.mouse['default']=[ ('gui/mouse/default.png',0,0) ]
define config.rollback_enabled = config.developer
define config.has_quicksave = False
define config.has_autosave = False
define config.save_json_callbacks = [ ]
# define config.narrator_menu = False
define config.log_gl_shaders = True

















## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

define config.name = _("202307")


## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = True


## 游戏版本号。

define config.version = "1.0"


## 放置在游戏内“关于”屏幕上的文本。将文本放在三个引号之间，并在段落之间留出空
## 行。

define gui.about = _p("""
""")


## 在构建的发布版中，可执行文件和目录所使用的短名称。此处仅限使用 ASCII 字符，并
## 且不能包含空格、冒号或分号。

define build.name = "202307"


## 音效和音乐 #######################################################################

## 这三个变量控制哪些内置的混音器会默认显示给用户。将其中一个设置为 False 将隐藏
## 对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 为了让用户在音效或语音轨道上播放测试音频，请取消对下面一行的注释并设置播放的
## 样本声音。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。

# define config.main_menu_music = "main-menu-theme.ogg"


## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve


## 载入游戏后使用的转场。

define config.after_load_transition = None


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = None


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 语句。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。若为 show，对话框将总是显示。若为 hide，对话框
## 仅在对话出现时显示。若为 auto，对话框会在 scene 语句前隐藏，并在有新对话时重
## 新显示。
##
## 在游戏开始后，可以用 window show、window hide 和 window auto 语句来改变其状
## 态。

define config.window = "auto"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 为瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 0


## 默认的自动前进延迟。数字越大，等待时间越长，有效范围为 0 - 30。

default preferences.afm_time = 15


## 存档目录 ########################################################################
##
## 控制 Ren'Py 放置游戏存档的特定操作系统目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该语句通常不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "game\saves"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"


## 构建配置 ########################################################################
##
## 此部分控制 Ren'Py 如何将您的项目转变为发行版文件。

init python:

    ## 以下函数接受文件模式。文件模式不区分大小写，并与基础目录的相对路径相匹
    ## 配，包括或不包括 /。如果多个模式匹配，则使用第一个模式。
    ##
    ## 在一个模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中的 txt 文件，“game/**.ogg”匹配游戏目录或任何子
    ## 目录中的 ogg 文件，“**.psd”匹配项目中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 若要封装文件，需将其列为“archive”。

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## 匹配为文档模式的文件会在 Mac 应用程序构建中被复制，因此它们同时出现在 APP
    ## 和 ZIP 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')


## 下载扩展文件和执行应用内购需要一个 Google Play 许可密钥。许可密钥可以在
## Google Play 开发者控制台的“服务和 API”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 项目相关的用户名和项目名，以 / 分隔。

# define build.itch_project = "renpytom/test-project"
