################################################################################
## Initialization
################################################################################

init offset = -1

default pullout = True

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

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
    thumb_offset 23.5
    left_gutter 23
    right_gutter 23
    left_bar Frame("gui/slider/horizontal_left_bar.png")
    right_bar Frame("gui/slider/horizontal_[prefix_]bar.png")
    

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

#define config.skip_delay = 300

transform namebox_rotate():
    anchor (0.5, 0.5) transform_anchor 1
    rotate -3.5
    
screen say(who, what, slow_effect = slow_typewriter, slow_effect_delay = 0, always_effect = None):
    style_prefix "say"

    window:
        id "window"
        if who is not None:


            window:
                id "namebox"
                style "namebox"
                text who id "who" at namebox_rotate 
                #background Frame("gui/frame.png")

        #text what id "what"
        fancytext what id "what" slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect
        button:
            id "button"
            action Skip()
            if renpy.get_screen("skip_indicator"):
                unhovered Skip() alternate Skip(fast=True, confirm=True)
            else:
                unhovered NullAction()

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')
    config.character_id_prefixes.append('button')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign - 0.06
    ysize gui.textbox_height 

    background Image("gui/gui_dialoguebox_default.png", xalign=0.5, yalign=1.0)

style window_ocean:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign - 0.06
    ysize gui.textbox_height 

    background Image("gui/gui_dialoguebox_ocean.png", xalign=0.5, yalign=0.3)

style window_narrator:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign - 0.06
    ysize gui.textbox_height 

    background Image("gui/gui_dialoguebox_leaf.png", xalign=0.5, yalign=1.0)

style window_killer:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign - 0.06
    ysize gui.textbox_height 

    background Image("gui/gui_dialoguebox_black.png", xalign=0.5, yalign=1.0)

style namebox:
    xanchor gui.name_xalign
    xpos gui.name_xpos - 238
    ypos gui.name_ypos - 85
    #xsize gui.namebox_width
    #ysize gui.namebox_height
    xsize 418
    ysize 159 

    background Frame("gui/gui_nameplate.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style namebox_ocean:
    xpos gui.name_xpos - 317
    xanchor gui.name_xalign
    #xsize gui.namebox_width
    xsize 490
    ypos gui.name_ypos - 120
    #ysize gui.namebox_height
    ysize 219

    background Frame("gui/gui_nameplate_ocean.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_button_none:
    xalign 0.877
    yalign 1.125
    xysize (149,120)
    idle_background None
    hover_background None
    selected_idle_background None
    selected_hover_background None
    selected_background None
    activate_sound None

style say_button:
    xalign 0.877
    yalign 1.125
    xysize (149,120)
    idle_background "gui/gui_button_skip_idle.png"
    hover_background "gui/gui_button_skip_hover.png"
    selected_idle_background "gui/gui_button_skip_idle.png"
    selected_hover_background "gui/gui_button_skip_hover.png"
    selected_background "gui/gui_button_skip_select.png"
    activate_sound "sounds/sfx_tap.ogg"

style say_label:
    #Putting outlines here applies to all characters, override with who_outlines
    outlines [(4, "#004035", -5, 3),(2, "#0a9e9a", -5, 3), (3, "#252118", absolute(-2), absolute(0)), (absolute(1), "#FFF", absolute(0), absolute(0))]
    properties gui.text_properties("name", accent=True)
    xsize 418
    ysize 159 
    xalign 0.6
    yalign 0.625

style say_dialogue:
    #Putting outlines here applies to all characters, override with what_outlines
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    size 26
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos - 70
    xsize gui.dialogue_width + 140
    ypos gui.dialogue_ypos 

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
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


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    $ count = 1
    vbox:
        for i in items:
            if count > 4:
                $ count = 4
            textbutton i.caption: 
                action i.action 
                hover_sound "sounds/sfx_ui_choice_hover0"+ str(count) + ".ogg"
                activate_sound "sounds/sfx_ui_choice_select.ogg"
            $ count = count + 1

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 357
    yanchor 0.4
    spacing gui.choice_spacing + 15

style choice_button is default:
    properties gui.button_properties("choice_button")
    ysize 79
    xsize 880

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

style choice_button_text is text:
    size 30
    color "#e4dfd8" 
    yalign 0.5
    outlines [ (2, "#0a5251", absolute(0), absolute(0)) ]

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
transform pull_out_ribbon:
    linear .4  xoffset -0 # take .4 seconds to move the menu to its default location
transform pull_in_ribbon:
    linear .4 xoffset -770
        
screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100

    #if renpy.get_screen("say"):
    if quick_menu:

        frame:
            if pullout:
                at pull_out_ribbon
            else:
                at pull_in_ribbon
            style_prefix "quick"
            has hbox:
                imagebutton:
                    ysize 47
                    xsize 47
                    if pullout:
                        hover "gui/gui_menu_pullout_button_select.png"
                    else:
                        hover "gui/gui_menu_pullout_button_hover.png"
                    idle "gui/gui_menu_pullout_button_idle.png"
                    selected "gui/gui_menu_pullout_button_select.png"
                    activate_sound "sounds/sfx_tap.ogg"
                    #hover "gui/gui_menu_pullout_button_hover.png"
                    if pullout:
                        action [SetVariable("pullout", False)]  
                    else:
                        action [SetVariable("pullout", True)] 
                #textbutton _("Back") action Rollback()
                #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                null width 20
                textbutton _("SAVE"):
                    action [[SetVariable("pullout", True)], ShowMenu('save')]
                    activate_sound "sounds/sfx_tap.ogg"
                #textbutton _("AUTO"): 
                #    action [[SetVariable("pullout", True)], Preference("auto-forward", "toggle")]  
                #    activate_sound "sounds/sfx_tap.ogg"
                textbutton _("LOAD"):
                    action [[SetVariable("pullout", True)], ShowMenu('load')]
                    activate_sound "sounds/sfx_tap.ogg"
                #textbutton _("Q.Save") action QuickSave()
                #textbutton _("Q.Load") action QuickLoad()
                textbutton _("SETTINGS"): 
                    action [[SetVariable("pullout", True)], ShowMenu('preferences')]
                    activate_sound "sounds/sfx_tap.ogg"
                textbutton _("MAIN MENU"): 
                    action [[SetVariable("pullout", True)], MainMenu()] 
                    activate_sound "sounds/sfx_tap.ogg"
                #textbutton _("HISTORY"): 
                #    action [[SetVariable("pullout", True)], ShowMenu('history')]  
                #    activate_sound "sounds/sfx_tap.ogg"


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    size 30
    
    color "#eedccb" 
    hover_color "099390"
    outlines [ (2, "#0e0505", absolute(0), absolute(0)) ]
    xalign 0.5
    #properties gui.button_text_properties("quick_button")

style quick_frame:
    background Frame("gui/gui_menu_pullout_ribbon.png")
    xalign 1.0
    yalign 0.06
    ysize 84
    xsize 871
    left_padding 40
    xoffset 770

style quick_hbox:
    yalign 0.4



################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.
transform rotateleft():
    anchor (0.5, 0.5) transform_anchor 1
    rotate -5

transform rotateleft2():
    anchor (0.5, 0.5) transform_anchor 1
    rotate -2

transform rotateleft3():
    anchor (0.5, 0.5) transform_anchor 1
    rotate -1

transform rotateright():
    anchor (0.5, 0.5) transform_anchor 1
    rotate 1

transform rotateright2():
    anchor (0.5, 0.5) transform_anchor 1
    rotate 2


screen the_img1(img):
    add img pos (938-80, 225)

screen the_img2(img):
    add img pos (885-90, 330)

screen the_img3(img):
    add img pos (921-80, 475)

screen the_img4(img):
    add img pos (885-90, 602)

screen the_img5(img):
    add img pos (941-80, 737)

screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            xalign -1.8
            button:
                xoffset 75
                action Start(),  Hide("the_img1") 
                idle_background "gui/gui_menu_button_new_game_idle.png"
                hover_background "gui/gui_menu_button_new_game_hover.png"
                hovered ShowTransient("the_img1", img="gui/window_icon.png") unhovered Hide("the_img1")
                selected_background "gui/gui_menu_button_new_game_select.png"
                text "NEW GAME":
                    style "menubutton"
                    yoffset 10
                    at rotateleft
                
            button:
                action ShowMenu("load"), Hide("the_img2")
                idle_background "gui/gui_menu_button_load_game_idle.png"
                hover_background "gui/gui_menu_button_load_game_hover.png"
                hovered ShowTransient("the_img2", img="gui/window_icon.png") unhovered Hide("the_img2")
                selected_background "gui/gui_menu_button_load_game_select.png"
                text "LOAD GAME":
                    style "menubutton"
                    yoffset 20
                    at rotateright
            button:
                xoffset 40
                action ShowMenu("preferences"), Hide("the_img3")
                idle_background "gui/gui_menu_button_settings_idle.png"
                hover_background "gui/gui_menu_button_settings_hover.png"
                hovered ShowTransient("the_img3", img="gui/window_icon.png") unhovered Hide("the_img3")
                selected_background "gui/gui_menu_button_settings_select.png"
                text "SETTINGS":
                    yoffset 20
                    style "menubutton"
                    at rotateleft3
            button:
                action ShowMenu("about"), Hide("the_img4")
                idle_background "gui/gui_menu_button_credits_idle.png"
                hover_background "gui/gui_menu_button_credits_hover.png"
                hovered ShowTransient("the_img4", img="gui/window_icon.png") unhovered Hide("the_img4")
                selected_background "gui/gui_menu_button_credits_select.png"
                text "CREDITS":
                    yoffset 20
                    xoffset -20
                    style "menubutton"
                    at rotateleft2
            button:
                xoffset 50
                action Quit(confirm=not main_menu)
                idle_background "gui/gui_menu_button_quit_idle.png"
                hover_background "gui/gui_menu_button_quit_hover.png"
                hovered ShowTransient("the_img5", img="gui/window_icon.png") unhovered Hide("the_img5")
                selected_background "gui/gui_menu_button_quit_select.png"
                text "QUIT":
                    yoffset 30
                    xoffset -20
                    style "menubutton"
                    at rotateright2

        else:
            xalign 0

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            textbutton _("Preferences") action ShowMenu("preferences")

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("Main Menu") action MainMenu()

            textbutton _("About") action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("Help") action ShowMenu("help")

            if renpy.variant("pc"):

                ## The quit button is banned on iOS and unnecessary on Android and
                ## Web.
                textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text
style menubutton is gui_button_text

style navigation_text:
    size_group "navigation"
    properties gui.button_properties("navigation_text")

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    xysize (447, 125)
    hover_sound "sounds/sfx_mainmenu_hover.ogg"
    activate_sound "sounds/sfx_mainmenu_hover.ogg"

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

style menubutton:
    layout "subtitle"
    hover_color "#0a9e9a"
    selected_color "#fff"
    size 63
    color "f3e3d4"
    text_align 0.5
    xalign 0.5
    outlines [ (1, "#000", absolute(0), absolute(0)) ]

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
init:
    transform menuslide:
        easein 1.0 xoffset 0
        linear 5.0 xoffset 0
        easeout 1.0 xoffset 1000
        linear 0.0 xoffset 1000
        repeat
    image slideshow1:
        zoom 1.005
        "gui/gui_menu_main_hunter.png"
        pause 7
        zoom 1.0125
        "gui/gui_menu_main_trapper.png"
        pause 7
        zoom 1.15
        "gui/gui_menu_main_spirit.png"
        pause 7
        zoom 1.01
        "gui/gui_menu_main_wraith.png"
        pause 7
        zoom 1.1975
        "gui/gui_menu_main_skull.png"
        pause 7
        repeat

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background
    add "slideshow1" at right, menuslide

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    #if gui.show_name:
    #
    #    vbox:
    #        style "main_menu_vbox"
    #
    #        text "[config.name!t]":
    #            style "main_menu_title"
    #
    #        text "[config.version]":
    #            style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 667
    ysize 940
    xalign 0.058
    yalign 0.45
    #yfill True

    background "gui/gui_menu_main_logo.png"
    #background "gui/overlay/main_menu.png"

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


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    #if main_menu:
    #    add gui.main_menu_background
    #else:
    #    add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"
        background None

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                background None
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

    #use navigation

    #textbutton _("Return"):
    #    style "return_button"
    #
    #    action Return()
    if not title == "Preferences":
        button:
            xalign 0.5
            yalign 0.9375
            action Return()
            xysize (194, 66)
            idle_background "gui/gui_button_idle.png"
            hover_background "gui/gui_button_hover.png"
            selected_background "gui/gui_button_select.png"
            activate_sound "sounds/sfx_tap.ogg"
            text "CLOSE":
                style "menubutton"
                size 30
                outlines [ (1, "#000", absolute(0), absolute(0)) ]
    #label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


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
    top_padding 0

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 0
    yfill True

style game_menu_content_frame:
    left_margin 0
    right_margin 0
    top_margin 0

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


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.
init -2:
    $ style.hyperlink_text = Style(style.say_dialogue) # inherits from the default dialog look, so it'll look like the rest of the dialogue, and we'll just have to change the look of the link hovered
    #$ style.hyperlink_text.hover_bold = True # make it bold when hovered.
    $ style.hyperlink_text.size = 18 # make size a bit smaller (? doesn't fix hover issue)
    $ style.hyperlink_text.color = "#0a9e9a";
    $ style.hyperlink_text.hover_color = "#0a9e9a"

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About")):

    #style_prefix "about"
        frame:
            xsize 1920
            ysize 1080
            background Image("images/bg_credits.png")
            vbox:
                xalign 0.5
                image "gui/gui_credits_dbd_logo.png":
                    xsize 795
                    ysize 431
                    xalign 0.5
                    yalign 0.1
                hbox:
                    xalign 0.5
                    image "gui/slider/horizontal_idle_thumb.png" xsize 47 ysize 51 xalign 0.0 yoffset -10 xoffset -5
                    null width (gui.pref_spacing)
                    text "DEVELOPMENT"  size 30 xalign 0.5 color "#0a9e9a"
                    null width (gui.pref_spacing)
                    image "gui/slider/horizontal_idle_thumb.png" xsize 47 ysize 51 xalign 1.0 yoffset -10
                image "gui/gui_credits_logo_psyop.png":
                    xsize 321
                    ysize 330
                    xalign 0.5
                vbox:
                    yoffset -170
                    text "[config.name!t]" color "#0a9e9a"
                    text _("Version [config.version!t]\n")

                    ## gui.about is usually set in options.rpy.
                    if gui.about:
                        text "[gui.about!t]\n" color "#0a9e9a"

                    text _("Made with {a=https://www.renpy.org/ }{color=#0a9e9a}Ren'Py{/color}{/a} [renpy.version_only].\n\n[renpy.license!t]")
        #key [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT', 'K_ESCAPE', 'K_MENU', 'K_PAUSE', 'mouseup_3','K_BACKSPACE' ] action Return()

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

define config.has_autosave = False
define config.has_quicksave = False
define config.autosave_on_quit = False
define config.autosave_on_choice = False
define gui.file_slot_cols = 1
define gui.file_slot_rows = 3
define gui.slot_button_width = 1041
define gui.slot_button_height = 214
define config.thumbnail_width = 272-20
define config.thumbnail_height = 173-20
define gui.slot_button_borders = Borders(15, 15, 15, 15)
# angled at 9 degrees

transform saves_rotate():
    #anchor (0, 0) transform_anchor 1
    rotate -9
    xoffset -8

image nav_previous_inactive:
    im.Flip("gui/gui_menu_next_inactive.png", horizontal=True) 

image nav_previous_idle:
    im.Flip("gui/gui_menu_next_idle.png", horizontal=True) 

image nav_previous_hover:
    im.Flip("gui/gui_menu_next_hover.png", horizontal=True) 

default playtime = 0

init 2 python:

    def save_playtime(d):
        renpy.store.playtime += renpy.get_game_runtime()
        renpy.clear_game_runtime()
        d["playtime"] = renpy.store.playtime

    config.save_json_callbacks = [save_playtime]

transform text_alpha:
    alpha 0.4
screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        frame:
            if title == "Save":
                image "gui/gui_file_save_icon.png":
                    xsize 224
                    ysize 109
                    xalign 0.5
                    yalign 0.09
            if title == "Load":
                image "gui/gui_file_load_icon.png":
                    xsize 224
                    ysize 109
                    xalign 0.5
                    yalign 0.09
            xsize 1920
            ysize 1080
            background Image("gui/game_menu.png")
            fixed:
                xsize 1188
                ysize 772
                xpos 366
                ypos 141
                ## This ensures the input will get the enter event before any of the
                ## buttons do.
                order_reverse True

                ## The page name, which can be edited by clicking on a button.
                #button:
                #    style "page_label"
                #
                #    key_events True
                #    xalign 0.5
                #    action page_name_value.Toggle()
                #
                #    input:
                #        style "page_label_text"
                #        value page_name_value

                ## The grid of file slots.

                grid gui.file_slot_cols gui.file_slot_rows:
                    

                    xalign 0.5
                    yalign 0.5

                    #spacing gui.slot_spacing
                    spacing -20
                    for i in range(gui.file_slot_cols * gui.file_slot_rows):
                        $ slot = i + 1
                        $ playtime = FileJson(slot, "playtime", empty=0, missing=0) 
                        $ minutes, seconds = divmod(int(playtime), 60)
                        $ hours, minutes = divmod(minutes, 60)
                        button:
                            xysize (1045+34,214)
                        #617
                            idle_background None
                            xoffset 0
                            yoffset -17
                            xalign 0.0
                            yalign 0.5
                            has hbox
                            key "save_delete" action FileDelete(slot)
                            style_prefix "slot"
                            hbox:
                                xysize (1045,214)
                                button:
                                    key "save_delete" action FileDelete(slot)
                                    activate_sound "sounds/sfx_tap.ogg"
                                    xysize (1045,214)
                                    if FileLoadable(slot):
                                        idle_background "gui/gui_file_save_slot_idle.png"
                                        hover_background "gui/gui_file_save_slot_hover.png"
                                        selected_background "gui/gui_file_save_slot_select2.png"
                                        selected_hover_background "gui/gui_file_save_slot_hover.png"
                                        action FileAction(slot)
                                    else:
                                        idle_background "gui/gui_file_save_empty_idle.png"
                                        hover_background "gui/gui_file_save_empty_hover.png"
                                        if title == "Save":
                                            action FileAction(slot)
                                        else:
                                            action NullAction()

                                    hbox:
                                        xysize (1045,214)
                                        xalign 0.0
                                        yalign 0.5
                                        hbox:
                                            xysize (303,214)
                                            xalign 0.0
                                            add FileScreenshot(slot) xalign 0.0 at saves_rotate
                                            if FileLoadable(slot):
                                                add "gui/gui_menu_save_pin.png" xoffset -160 yoffset 44 xsize 27 ysize 29
                                        hbox:
                                            xysize (635,143)
                                            yalign 0.5
                                            xalign 0.0
                                            xoffset -50
                                            vbox:  
                                                ysize 143
                                                yalign 0.5
                                                if FileLoadable(slot):
                                                    text FileSaveName(slot):
                                                        style "slot_time_text"
                                                        color "eedccb"
                                                        hover_color "#20130f"
                                                        size 37
                                                        yoffset 20
                                                    
                                                text FileTime(slot, format=_("{#file_time}%m/%d/%Y  %I:%M%p"), empty=_( "NEW FILE" if title == "Save" else "  EMPTY " )):
                                                    style "slot_time_text"
                                                    color "07807f"
                                                    if FileLoadable(slot) == False:
                                                        xoffset 125
                                            vbox:
                                                xysize (171,143)
                                                yalign 0.5
                                                xalign 1.0
                                                if FileLoadable(slot):
                                                    if hours > 999:
                                                        $ hours = 999
                                                    text "[hours:02d]:[minutes:02d]":
                                                        
                                                        color "000"
                                                        size 60
                                                        yalign 0.5
                                                        yoffset 10
                                                        text_align 1.0
                                                        xalign 1.0
                                                        at text_alpha
                                                    text "PLAYTIME":
                                                        
                                                        size 25
                                                        color "000"
                                                        yalign 0.5
                                                        yoffset -15
                                                        text_align 1.0
                                                        xalign 1.0
                                                        at text_alpha

                                            #text FileSaveName(slot):
                                            #    style "slot_name_text"

                                    
                            if FileLoadable(slot):
                                button:
                                    xysize (34,49)
                                    action FileDelete(slot)
                                    yalign 0.5
                                    yoffset -3
                                    idle_background "gui/gui_file_delete_idle.png"
                                    hover_background "gui/gui_file_delete_hover.png"
                                    #hovered ShowTransient("the_img5", img="gui/window_icon.png") unhovered Hide("the_img5")
                                    selected_background "gui/gui_file_delete_selected.png"
                                    activate_sound "sounds/sfx_tap.ogg"
                                    key "save_delete" action FileDelete(slot)
                ## Buttons to access other pages.
                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign .972

                    spacing gui.page_spacing 

                    #textbutton _("<") action FilePagePrevious()
                    imagebutton: 
                        #idle "nav_previous"
                        insensitive "nav_previous_inactive"
                        idle "nav_previous_idle"
                        hover "nav_previous_hover"
                        activate_sound "sounds/sfx_tap.ogg"
                        action FilePagePrevious()
                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")
                    button:
                        style "page_label"
                        #text FilePageName()
                        #key_events True
                        xalign 0.5
                        #action page_name_value.Toggle()
                        xpadding 30
                        #style "slot_time_text"
                        text FilePageName():
                            color "eedccb"
                            size 37
                            yoffset -4
                            outlines [ (2, "#187471", absolute(0), absolute(0)) ]
                    
                        #input:
                        #    style "page_label_text"
                        #    value page_name_value
                    ## range(1, 10) gives the numbers from 1 to 9.
                    #for page in range(1, 10):
                    #    textbutton "[page]" action FilePage(page)

                    imagebutton: 
                        insensitive "gui/gui_menu_next_inactive.png"
                        idle "gui/gui_menu_next_idle.png"
                        hover "gui/gui_menu_next_hover.png"
                        activate_sound "sounds/sfx_tap.ogg"
                        action FilePageNext()
                add "gui/window_icon.png" xoffset -75 yoffset 655 xsize 162 ysize 162

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
style slot_text is slot_button_text

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
    xsize 1045
    ysize 214
style slot_text:
    properties gui.button_text_properties("page_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    
    size 30
    xalign 0.0


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    tag menu
    use game_menu(_("Preferences")):
        frame:
            background Image("gui/gui_menu_settings.png")
            xysize(1920,1080)
            image "gui/gui_settings_icon.png":
                xsize 382
                ysize 107
                xalign 0.5
                yalign 0.09
            image "gui/gui_menu_settings_skull.png":
                xysize (211, 270)
                xalign 0.271
                yalign 0.59
            vbox:
                xalign 0.5
                yalign 0.3
                xysize(774,598)
                null height (2 * gui.pref_spacing)
                style_prefix "slider"
                vbox:
                    hbox:
                        xalign 1.0
                        if config.has_music:
                            label _("MUSIC VOLUME"):
                                text_color "#1f100b" 
                            null width (gui.pref_spacing)
                            vbox:
                                xysize(345, 51)
                                bar value Preference("music volume")
                                style_prefix "radio"
                                spacing (gui.pref_spacing)
                                textbutton _("MUTE"):
                                    ysize 21
                                    yalign 0.5
                                    xalign 0.05
                                    text_color "#0a9e9a"
                                    text_size 30
                                    action Preference("music mute", "toggle")
                                    activate_sound "sounds/sfx_tap.ogg"

                    hbox:
                        xalign 1.0
                        if config.has_sound:
                            label _("SFX VOLUME"):
                                text_color "#1f100b" 
                            null width (gui.pref_spacing)
                            vbox:
                                xysize(345, 51)
                                bar value Preference("sound volume")
                                style_prefix "radio"
                                spacing (gui.pref_spacing)
                                textbutton _("MUTE"):
                                    ysize 21
                                    yalign 0.5
                                    xalign 0.05
                                    text_color "#0a9e9a"
                                    text_size 30
                                    action Preference("sound mute", "toggle")
                                    activate_sound "sounds/sfx_tap.ogg"
                    hbox:
                        xalign 1.0
                        if config.has_voice:
                            label _("VOICE VOLUME"):
                                text_color "#1f100b" 
                            null width (gui.pref_spacing)
                            vbox:
                                xysize(345, 51)
                                bar value Preference("voice volume")
                                style_prefix "radio"
                                spacing (gui.pref_spacing)
                                textbutton _("MUTE"):
                                    ysize 21
                                    yalign 0.5
                                    xalign 0.05
                                    text_color "#0a9e9a"
                                    text_size 30
                                    action Preference("voice mute", "toggle")
                                    activate_sound "sounds/sfx_tap.ogg"
                    hbox:
                        xalign 1.0
                        label _("TEXT SPEED"):
                            text_color "#1f100b" 
                        null width (gui.pref_spacing)

                        bar value Preference("text speed")
                    hbox:
                        xalign 1.0
                        label _("AUTO SPEED"):
                            text_color "#1f100b" 
                        null width (gui.pref_spacing)

                        bar value Preference("auto-forward time")
                    null height (gui.pref_spacing)
                    hbox:
                        xalign 1.0
                        yalign .0
                        if renpy.variant("pc") or renpy.variant("web"):
                            vbox:
                                xsize 387
                                label _("DISPLAY"):
                                    text_color "#1f100b" 
                                    xalign 0.7
                                null height (gui.pref_spacing)
                                style_prefix "radio"
                                vbox:
                                    xalign 0.75
                                    textbutton _("WINDOW"):
                                        text_color "#1f100b"
                                        text_hover_color "#0a9e9a" 
                                        xalign 0.0
                                        text_xalign 1.0
                                        yoffset 10
                                        xoffset 100
                                        text_yoffset -12
                                        text_xoffset 10
                                        text_size 30 
                                        action Preference("display", "window")
                                        activate_sound "sounds/sfx_tap.ogg"
                                    textbutton _("FULLSCREEN"):
                                        text_color "#1f100b"
                                        text_hover_color "#0a9e9a" 
                                        xalign 0.0
                                        text_xalign 1.0
                                        yoffset 10
                                        xoffset 100
                                        text_yoffset -12
                                        text_xoffset 10
                                        text_size 30  
                                        action Preference("display", "fullscreen")
                                        activate_sound "sounds/sfx_tap.ogg"

                        vbox:
                            xsize 300
                            xalign 1.0
                            yalign .0
                            label _("SKIP"):
                                text_color "#1f100b" 
                                xalign 0.6
                                yoffset -5
                            style_prefix "radio"
                            textbutton _("UNSEEN TEXT"):
                                text_color "#1f100b"
                                text_hover_color "#0a9e9a" 
                                xalign 0.0
                                text_xalign 1.0
                                yoffset 10
                                xoffset 50
                                text_yoffset -12
                                text_xoffset 10
                                text_size 30
                                action Preference("skip", "toggle")
                                activate_sound "sounds/sfx_tap.ogg"
                            textbutton _("AFTER CHOICES"):
                                text_color "#1f100b"
                                text_hover_color "#0a9e9a" 
                                xalign 0.0
                                text_xalign 1.0
                                yoffset 10
                                xoffset 50
                                text_yoffset -12
                                text_xoffset 10
                                text_size 30
                                action Preference("after choices", "toggle")
                                activate_sound "sounds/sfx_tap.ogg"
                            textbutton _("TRANSITIONS"):
                                text_color "#1f100b"
                                text_hover_color "#0a9e9a" 
                                xalign 0.0
                                text_xalign 1.0
                                yoffset 10
                                xoffset 50
                                text_yoffset -12
                                text_xoffset 10
                                text_size 30 
                                action InvertSelected(Preference("transitions", "toggle"))
                                activate_sound "sounds/sfx_tap.ogg"
                

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.
            
            button:
                xalign .5
                yalign .75
                action Return()
                xysize (194, 66)
                idle_background "gui/gui_button_idle.png"
                hover_background "gui/gui_button_hover.png"
                selected_background "gui/gui_button_select.png"
                activate_sound "sounds/sfx_tap.ogg"
                text "CLOSE":
                    style "menubutton"
                    size 30
                    outlines [ (1, "#000", absolute(0), absolute(0)) ]
        if gui.show_name:
            vbox:
                yalign 0.98
                xalign 0.02
                text "Build: [config.version]":
                    color "#ffd600"
                    size 40
            

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
    size 35

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing -5

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    activate_sound "sounds/sfx_tap.ogg"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    activate_sound "sounds/sfx_tap.ogg"

style check_button_text:
    properties gui.button_text_properties("check_button")
style slider_slider:
    xsize 345
    yoffset 10

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
    activate_sound "sounds/sfx_tap.ogg"

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


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
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    #add "gui/overlay/confirm.png"
    fixed:
        add "gui/gui_input_name_frame.png" xalign .5 yalign .5
        frame:
            background None
            vbox:
                xalign .5
                yalign .5
                spacing 45
                label _("[message]"):
                    style "confirm_prompt"
                    xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 75        
                    button:
                        action yes_action
                        text "YES":
                            style "menubutton"
                            size 30
                            xalign 0.5
                            yalign 0.5
                    button:
                        action no_action
                        text "NO":
                            style "menubutton"
                            size 30
                            xalign 0.5
                            yalign 0.5

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    #background Frame([ "gui/gui_input_name_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    #background "gui/gui_input_name_frame.png"
    #padding gui.confirm_frame_borders.padding
    #left_padding 200
    xalign .5
    yalign .5
    #xoffset 30
    xysize(571,320)

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    color "#323232"

style confirm_button:
    properties gui.button_properties("confirm_button")
    xysize (194, 66)
    idle_background "gui/gui_button_idle.png"
    hover_background "gui/gui_button_hover.png"
    selected_background "gui/gui_button_select.png"
    activate_sound "sounds/sfx_tap.ogg"
    hover_sound "sounds/sfx_mainmenu_hover.ogg"

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"
    
    if renpy.get_screen("say"):
        image "gui/gui_button_skip_select.png":
            xpos 1547
            ypos 932
            xysize (149,120)

    #frame:

        #hbox:
            #spacing 9

            #text _("Skipping")

            #text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            #text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            #text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
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
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

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


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

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

################################################################################
## Name Input for PlayerName
################################################################################

init python:
    fadeconfirm = True
    def change_name(newstring):                                              
    #Functions that allow us to store the input
        store.user_input = newstring

image buttonidlefade:
    im.MatrixColor('gui/gui_button_idle.png', im.matrix.opacity(.5))
transform textalpha: 
    alpha 0.5

default user_input = ""

screen name_input():
    default input_on = False  
    style_prefix "userinputname"
    fixed:
        button:
            xysize(1920,1080)  
            action ToggleScreenVariable("input_on")   
        add "gui/gui_input_name_frame.png" xalign .5 yalign .5  
        frame:
            xoffset 35
            yoffset 10       
            vbox:
                text _("Welcome to your dream vacation!"):
                    color "#2c948e" 
                    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
                    size 33
                text "Before we get started, what shall we call you?":
                    size 33
                frame:
                    xysize(464,49)  
                    background "gui/gui_input_name_textbox.png"
                    if input_on:                                 
                        input default user_input length 8 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 " changed change_name          
                    else:
                        if user_input == "":
                            text "ENTER YOUR NAME...": 
                                color "#b1a195"
                                italic True
                            $ fadeconfirm = True
                        else:
                            text user_input: 
                                color "#323232" 
                            $ fadeconfirm = False
                button:
                    xysize (194, 66)
                    if fadeconfirm or input_on:
                        text "CONFIRM":
                            style "userinputname_button"
                            at textalpha
                            hover_color "#e4dfd8" 
                        idle_background "buttonidlefade"
                        hover_background "buttonidlefade"
                        selected_background "buttonidlefade"
                        action ToggleScreenVariable("input_on")  
                    else:
                        text "CONFIRM":
                            style "userinputname_button"
                            hover_color "#0a9e9a"
                        idle_background "gui/gui_button_idle.png"
                        hover_background "gui/gui_button_hover.png"
                        selected_background "gui/gui_button_selected.png"
                        action Return()
style userinputname_button is menubutton
style userinputname_input is gui_medium_button_text
style userinputname_text is gui_medium_button_text

style userinputname_vbox:
    spacing 15
    yalign .5  

style userinputname_frame:
    xysize(571,400)  
    yalign .5  
    xalign .5
    background None   

style userinputname_button:
    size 25
    xalign 0.5
    yalign 0.5
    selected_color "#e4dfd8" 
    outlines [ (1, "#000", absolute(0), absolute(0)) ]

style userinputname_input:
    size 25
    xalign 0.5
    yalign 0.5
    color "#323232" 
    caret "inputname_caret" 

image inputname_caret:                                              
    Text("|", color="#323232",size=25)
    ypos -1
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat
style userinputname_text:
    size 29
    color "#2e1d15"   
    xalign 0.5
    yalign 0.5
    text_align 0.5


screen game_over(yes_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 199

    style_prefix "confirm"

    #add "gui/overlay/confirm.png"
    frame:
        xysize(1920,1080)  
        background "gui/bg_gameover.png"
        xoffset 0
        vbox:
            xalign .5
            yalign .5
            spacing 45
            add "gui/gameover.png" xalign .5
            hbox:
                xalign 0.5
                spacing 75        
                button:
                    action Call(yes_action)
                    add "gui/gameover_flower.png" zoom 0.6 xoffset -20 yoffset -5
                    text "TRY AGAIN":
                        style "menubutton"
                        size 30
                        xalign 0.5
                        yalign 0.5
                button:
                    action MainMenu()
                    add "gui/gameover_skull.png" zoom 0.725 xoffset -20 yoffset -5
                    text "GIVE UP":
                        style "menubutton"
                        size 30
                        xalign 0.5
                        yalign 0.5
    #on "show" action renpy.sound.play("sounds/sfx_gameover.ogg")