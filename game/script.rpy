default name = ""


init python:
    import random
    def change_name(newstring):                                               #Functions that allow us to store the input
        store.name = newstring


image namebox_caret:                                                                 #This is for that flashing line thingy next to your input :>
    Text("|", color="#323232",size=30)
    ypos -5
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat
style namebox_button:                                                                #Some styles..
    background Frame("images/button.png")
    xsize 400

style namebox_text:
    size 30
    hover_color "#323232"
    idle_color "#b6a699"
    selected_color "#323232"

style namebox_input:
    size 30
    caret "namebox_caret"
    
screen button_input():
    default input_on = False                                                    #Screen variable for input
    add "images/overlay.png"                                                    #I like it, okay?
    modal True                                                                  #Prevents user from accidentally clicking out of the screen

    frame:
        background Frame("images/frame.png")
        xpadding 30
        xalign 0.5
        yalign 0.5
        has vbox:
            text "Welcome to your dream vacation!" xalign 0.5
            text "Before we get started, what shall we" xalign 0.5
            text "call you?" xalign 0.5
            xalign 0.5
            button style_prefix "namebox":
                if input_on:                                                #Only activate input after the user has clicked the button
                    input default name length 8 exclude u'{ }' changed change_name
                    action SetScreenVariable("input_on", False)             #Pressing enter turns input back off
                else:
                    if name == "":
                        text "ENTER YOUR NAME..." bold True
                    else:
                        text name color "#323232"
                    action SetScreenVariable("input_on", True)              #Activate input


                xalign 0.5 
            if name == "":
                textbutton "CONFIRM" xalign 0.5
            else:
                textbutton "CONFIRM" xalign 0.5 action Hide("button_input") 
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

    scene bg room

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
    name " 1"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
