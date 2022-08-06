
# Declare the characters.

# define e = Character(_('Eileen'), color="#c8ffc8")
define nrr = Character(None, style_prefix="window", window_background="gui/gui_dialoguebox_leaf.png", color="#3a2e55", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define oc = Character("OCEAN", style_prefix="window", window_background="gui/gui_dialoguebox_leaf.png", color="#3a2e55", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define mc = DynamicCharacter('mc_name', color="#3a2e55", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define dw = Character("DWIGHT", color="#bb7d31", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define cl = Character("CLAUDETTE", color="#b4992e", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define th = Character("THE HUNTRESS", color="#c64631", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])

default name = ""

transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 10 rotate 360    
    repeat

init:
    image bg warmdark:
        "images/warmdark/bg_warmdark.png"
        zoom 1.1
    image bg loading:
        "images/bg_loading.png"
    image bg inner_monologue:
        "images/bg_inner_monologue.png"
    image bg haunting:
        "images/bg_haunting.png"
    image bg excitement:
        "images/bg_excitement.png"
        zoom 1.11
    image bg warmlight:
        "images/bg_warmlight.png"
    image bg happy:
        "images/bg_happy.png"
    image bg speedlinebg_re2d:
        Tile("images/bg_speedlinebg_red.png")
        xtile 5
        ytile 5
        zoom .5
    image bg speedlinebg_red:
        xoffset -3920
        yoffset -1250
        zoom 2
        rotate -45
        anchor (0, 0) transform_anchor 1
        contains:
            parallel:
                Tile("images/bg_speedlinebg_red.png")
                ytile 3
                xtile 3
                xpan -5400
                linear 8 xpan 180
                xalign 1
                yalign 1
                repeat

    define loadIn = ImageDissolve("images/bg_loading.png", 5.0)
    define loadOut = ImageDissolve("images/bg_loading.png", 5.0, reverse=True)
    image bg beach0:
        "images/bg_beach_0.png"

init python:
    import random
    def change_name(newstring):                                              
     #Functions that allow us to store the input
        store.name = newstring





image namebox_caret:                                                                
 #This is for that flashing line thingy next to your input :>
    Text("|", color="#323232",size=20)
    ypos -2
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat
style namebox_button:                                                               
 #Some styles..
    background Frame("images/name_input_textbox.png")
    xsize 430
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
    #Screen variable for input
    default input_on = False
    # add "images/overlay.png"    
    #Prevents user from accidentally clicking out of the screen                                                
    modal True              
    zorder 100                                                    
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
            #Only activate input after the user has clicked the button
            if input_on:                                                
                input default name length 8 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" changed change_name color "#323232" bold True xalign 0.5
                action SetScreenVariable("input_on", False)             
                #Pressing enter turns input back off
            else:
                if name == "":
                    text "ENTER YOUR NAME..." bold True xalign 0.5
                else:
                    text name color "#323232" bold True xalign 0.5        
                #Activate input
                action SetScreenVariable("input_on", True)     
            xalign 0.5 
        text "" size 25
        if name == "":
            imagebutton:
                idle "images/ui_button_hover.png"
                xalign 0.5
                action SetScreenVariable("input_on", False)
            text _("CONFIRM") size 25 xalign 0.5 yoffset -50 outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        else:
            imagebutton:
                idle "images/ui_button_hover.png"
                selected "images/ui_button_idle.png"
                selected_idle "images/ui_button_idle.png"
                selected_hover "images/ui_button_selected.png"
                hover "images/ui_button_selected.png"
                xalign 0.5
                action [Hide("button_input"), Return()]
            text _("CONFIRM") size 25 xalign 0.5 yoffset -50 outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
label naming:
    show screen button_input

# The game starts here.
label start:
    $ mc_name = "Bill"
    scene bg warmdark
    show screen button_input
    pause
    python:
        while name == "":
            renpy.jump("naming")
        name = name.strip() or "Bill"
    hide screen button_input
    scene bg loading with dissolve
    pause 2
    scene bg beach0 with Dissolve(1.0)
    $ mc_name = name
    mc "*cough* *cough* *cough*"
    nrr "You wake up on the beach, soaking wet, saltwater stinging the inside of your throat, as if you'd nearly drowned."
    nrr "Water falls from your mouth as you open it to gasp for air."
    nrr "You have no memory of how you got here. In fact, you can only remember your own name, but not where you came from, or a single fact about your life."
    nrr "What you do know is that, despite the outrageous beauty of the landscape around you, you feel incredibly sick to your stomach--"
    nrr "Wow, really went down the wrong pipe, huh? You need a minute, or can I go on?"
    mc "..."
    nrr "Because I can give you a minute. We've got plenty of time. Endles time, really."
    scene bg haunting with dissolve
    oc "An eternity, if you catch my drift."
    scene bg beach0 with dissolve
    nrr "Woah, not now, Ocean! Sorry, [mc_name]. May I continue?"
    nrr "OK then. As I was--"
    mc "*cough* *cough*"
    nrr "AS I WAS SAYING."
    nrr "You look down at your feet, ankle-deep in the crystal blue water of a newly arrived wave."
    nrr "As the water recedes back into the ocean, it reveals a grotesque discovery!"
    scene bg inner_monologue with dissolve
    nrr "A decomposing face stares up at you from beneath the sand. All you can do is vomit--a stream of dark bile, bugs, worms, and other... ick."
    nrr "Questions race through your mind. Where are you? How did you get here? {i}Who is behind this incredibly charming and well-spoken voice in your head?{/i} However, answers don't come easy. Your mind... is completely blank."
    scene bg beach0 with dissolve
    nrr "What will you do?"
    menu:
        nrr "What will you do?"
        "Run":
            ""

        "Close your eyes":
            ""

        "Dig up that face!":
            window hide
            scene bg inner_monologue with dissolve
            pause 1
            window show
            nrr "You brush the sand away from the half-buried human head-embedded in the ground before you."
            window hide
            pause 1
            window show
            nrr "There is no body, just this head. As you pick it up, flakes of skin fall to the ground. The jaw falls open, revealing a gold coin sitting on the rotting tongue of this poor dead soul."
            scene bg haunting with dissolve
            oc "Getting your hands dirty, I see. I like that... You're a take charge type."
            window hide
            pause 1
            window show
    scene bg beach0 with dissolve
    nrr "You examine the gold coin briefly, happily distracted from what has otherwise been an extremely.... confusing morning."
    nrr "The sun beats down on you, drying your clothes. You check your pockets, but they're empty. Plenty of room for a gold coin, you suppose, and so you deposit it."
    nrr "Why that's a nice coin you've got there! What if you were to spend it right now?"
    menu:
        nrr "Why that's a nice coin you've got there! What if you were to spend it right now?"
        "\"No, thanks\"":
            ""

        "\"Why not?\"":
            mc "Why not?"
    dw "Well hello, there! I'm Dwight!"
    cl "And I'm Claudette!"
    cl "We'll take that!"
    nrr "Claudette quickly relieves you of your gold coin and tosses it to Dwight, who bites down on it like an old-timey prospector before handing it back to her."
    cl "And this..."
    dw  "...is for you!"
    window hide
    scene bg excitement with dissolve
    window show
    nrr "Claudette presents you with a tropical drink."
    nrr "When you take a sip, you find that it's incredible. Money well spent, in your estimation."
    nrr "But I gotta ask: Could somebody maybe design the next one of these dating sims to be all-inclusive? It really takes some of the fun out of a fantasy vacation to be watching your wallet the entire time."
    menu:
        nrr "But I gotta ask: Could somebody maybe design the next one of these dating sims to be all-inclusive? It really takes some of the fun out of a fantasy vacation to be watching your wallet the entire time."
        "Thank them for the delicious drink":
            mc "Thanks for the drink. It's quite delicious!"

        "This is suspicious, spit that out!":
            ""
    cl "You're... welcome!"
    dw "Did someone just thank us?"
    cl "Go with it, Dwight. It's normal to be thanked for doing a good job. Trust me on this one."
    nrr "Your mind doesn't have a chance to linger any longer on your current situation, as you feel something soft bump into your foot."
    window hide
    scene bg speedlinebg_red with dissolve
    window show
    nrr "When you look down, you find a volleyball sitting in the sand there next to you."
    nrr "You stare down, frozen. A voice calls out from behind you."
    th "Little help, please?"
    scene bg beach0 with dissolve
    nrr "You turn around, and when you see what's waiting for you, your jaw just about hits the ground."
    window hide
    scene bg happy with dissolve
    pause 1
    scene bg excitement with dissolve
    pause 1
    scene bg warmlight with dissolve
    pause 1
    scene bg warmdark with dissolve
    pause 1
    scene bg beach0 with dissolve
    pause 1
    window show
    nrr "Four gorgeous monsters stand halfway between you and a well-tended volleyball court."
    nrr "Each of them oozes with undead energy, a magical aura reaching out and penetrating you. Via your eyes."
    nrr "Your heart begins to race. Curiousity. Fear. Desire. You can't help but stare at these casually dressed... let's call them Killers--I dunno, not to be judgemental but that's just the energy they put out there."
    nrr "So many competing feelings rush through your mind at once you are completely paralyzed."
    # This ends the game.
    return
