default name = ""

init:
    image bg warmdark:
        "images/warmdark/bg_warmdark.png"
        zoom 1.1
init python:
    import random
    def change_name(newstring):                                               #Functions that allow us to store the input
        store.name = newstring


image namebox_caret:                                                                 #This is for that flashing line thingy next to your input :>
    Text("|", color="#323232",size=20)
    ypos -3
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat
style namebox_button:                                                                #Some styles..
    background Frame("images/name_input_textbox.png")
    xsize 400
    xpadding 10

style namebox_text:
    size 20
    hover_color "#323232"
    idle_color "#b6a699"
    selected_color "#323232"

style namebox_input:
    size 20
    caret "namebox_caret"
    
screen button_input():
    default input_on = False                                                    #Screen variable for input
    # add "images/overlay.png"                                                    #I like it, okay?
    modal True                                                                  #Prevents user from accidentally clicking out of the screen
    key "a" action NullAction()
    key "b" action NullAction()
    key "c" action NullAction()
    key "d" action NullAction()
    key "e" action NullAction()
    key "f" action NullAction()
    key "g" action NullAction()
    key "h" action NullAction()
    key "i" action NullAction()
    key "j" action NullAction()
    key "k" action NullAction()
    key "m" action NullAction()
    key "n" action NullAction()
    key "o" action NullAction()
    key "p" action NullAction()
    key "q" action NullAction()
    key "r" action NullAction()
    key "s" action NullAction()
    key "t" action NullAction()
    key "u" action NullAction()
    key "v" action NullAction()
    key "w" action NullAction()
    key "x" action NullAction()
    key "y" action NullAction()
    key "z" action NullAction()
    frame:
        background Frame("images/name_input_frame.png")
        xpadding 256
        top_padding 90
        bottom_padding 40
        xalign 0.5
        yalign 0.5
        has vbox:
            text "Welcome to your dream vacation!" xalign 0.5 bold True size 25 color "#2c948e" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
            text "" size 25
            text "Before we get started, what shall we" xalign 0.5 bold True size 25 color "#2e1d15" 
            text "call you?" xalign 0.5 bold True size 25 color "#2e1d15"
            text ""  size 25
            xalign 0.5
            button style_prefix "namebox":
                if input_on:                                                #Only activate input after the user has clicked the button
                    input default name length 8 exclude u'{ }' changed change_name color "#323232" bold True xalign 0.5
                    action SetScreenVariable("input_on", False)             #Pressing enter turns input back off
                else:
                    if name == "":
                        text "ENTER YOUR NAME..." bold True xalign 0.5
                    else:
                        text name color "#323232" bold True xalign 0.5
                    action SetScreenVariable("input_on", True)              #Activate input


                xalign 0.5 
            text "" size 25
            if name == "":
                imagebutton:
                    idle "images/ui_button_hover.png"
                    selected "images/ui_button_idle.png"
                    selected_idle "images/ui_button_idle.png"
                    selected_hover "images/ui_button_selected.png"
                    hover "images/ui_button_selected.png"
                    xalign 0.5
                text _("CONFIRM") size 25 xalign 0.5 yoffset -50 outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
            else:
                imagebutton:
                    idle "images/ui_button_hover.png"
                    selected "images/ui_button_idle.png"
                    selected_idle "images/ui_button_idle.png"
                    selected_hover "images/ui_button_selected.png"
                    hover "images/ui_button_selected.png"
                    xalign 0.5
                    action Hide("button_input") 
                text _("CONFIRM") size 25 xalign 0.5 yoffset -50 outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
label naming:
    show screen button_input

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg warmdark

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy
    show screen button_input
    pause
    python:
        while name == "":
            renpy.jump("naming")
        name = name.strip() or "Bill"
    # scene bg washington with fade
    name " 1"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
