
################################################################################
## spinthebottle_minigame
################################################################################

init 15 python:
    spinthebottle_position = 0
    spinthebottle_section = 0
init:
    transform spinthebottle_arrow_move(cur_arrow):
        subpixel True
        rotate_pad True
        rotate cur_arrow
    image spinthebottle_arrow:
        "images/minigames/spinthebottle/spinthebottle_arrow.png"
        align(0.5,0.5)
        yoffset -40
    image spinthebottle_bg:
        "images/minigames/spinthebottle/bg_spinthebottle.png"
        align(0.5,0.5)
screen spinthebottle_minigame:
    add "spinthebottle_bg"
    add "spinthebottle_arrow" at spinthebottle_arrow_move(spinthebottle_position)
    button:
        xalign .5
        yalign .9
        xysize (194, 66)
        idle_background "gui/gui_button_idle.png"
        hover_background "gui/gui_button_hover.png"
        selected_idle_background "gui/gui_button_idle.png"
        selected_hover_background "gui/gui_button_hover.png"
        selected_background "gui/gui_button_selected.png"
        activate_sound "sounds/sfx_tap.ogg"
        text "STOP":
            style "menubutton"
            size 30
            outlines [ (1, "#000", absolute(0), absolute(0)) ]
        if spinthebottle_position >= 0 and spinthebottle_position <= 90:
                action [SetVariable("spinthebottle_section", 1),Hide("spinthebottle_timer"), Call("results_spinthebottle_minigame")]
        elif spinthebottle_position >= 91 and spinthebottle_position <= 180:
                action [SetVariable("spinthebottle_section", 2),Hide("spinthebottle_timer"), Call("results_spinthebottle_minigame")]
        elif spinthebottle_position >= 181 and spinthebottle_position <= 270:
                action [SetVariable("spinthebottle_section", 3),Hide("spinthebottle_timer"), Call("results_spinthebottle_minigame")]
        elif spinthebottle_position >= 271 and spinthebottle_position <= 360:
                action [SetVariable("spinthebottle_section", 4),Hide("spinthebottle_timer"), Call("results_spinthebottle_minigame")]
        else:
            ## If somehow over 360, assume it's within 0 to 90
            action [SetVariable("spinthebottle_section", 1),Hide("spinthebottle_timer"), Call("results_spinthebottle_minigame")]

    if spinthebottle_position >= 0 and spinthebottle_position <= 90:
        key "K_SPACE" action [SetVariable("spinthebottle_section", 1),Hide("spinthebottle_timer"), Call("results_spinthebottle_minigame")]
    elif spinthebottle_position >= 91 and spinthebottle_position <= 180:
        key "K_SPACE" action [SetVariable("spinthebottle_section", 2),Hide("spinthebottle_timer"), Call("results_spinthebottle_minigame")]
    elif spinthebottle_position >= 181 and spinthebottle_position <= 270:
        key "K_SPACE" action [SetVariable("spinthebottle_section", 3),Hide("spinthebottle_timer"), Call("results_spinthebottle_minigame")]
    elif spinthebottle_position >= 271 and spinthebottle_position <= 360:
        key "K_SPACE" action [SetVariable("spinthebottle_section", 4),Hide("spinthebottle_timer"), Call("results_spinthebottle_minigame")]
    else:
        ## If somehow over 360, assume it's within 0 to 90
        key "K_SPACE" action [SetVariable("spinthebottle_section", 1),Hide("spinthebottle_timer"), Call("results_spinthebottle_minigame")]

screen spinthebottle_timer:
    timer 0.0001 repeat True action [If(spinthebottle_position <= 360, SetVariable("spinthebottle_position", spinthebottle_position + 3)),If(spinthebottle_position >= 360, SetVariable("spinthebottle_position", 0))]

################################################################################
label start_spinthebottle_minigame:
    show screen spinthebottle_timer
    call screen spinthebottle_minigame with Dissolve(0.25)
    return
################################################################################
label end_spinthebottle_minigame: #End minigame.
    hide screen spinthebottle_minigame
    hide screen spinthebottle_timer
    return
label results_spinthebottle_minigame:
    show screen spinthebottle_minigame
    pause 1
    hide screen spinthebottle_minigame
    with Dissolve(0.25)
    return

################################################################################
## meatcarving_minigame
################################################################################

init 15 python:
    meatcarving_position = 0
    meatcarving_section = 0
    meatcarving_barpos = 0
    meatcarving_speed = 1
    meatcarving_bar_start_offset = 64
    startpos_meatcarving = meatcarving_bar_start_offset
    endpos_perfect_meatcarving = (meatcarving_bar_start_offset+30)
    endpos_meatcarving = (meatcarving_bar_start_offset+80)
init:
    transform meatcarving_arrow_move(cur_arrow):
        subpixel True
        rotate_pad True
        rotate cur_arrow
    image meatcarving_arrow:
        "images/minigames/meatcarving/meatcarving_arrow.png"
        align(0.5,0.5)
        yoffset -40
    image meatcarving_bg:
        "images/minigames/meatcarving/bg_meatcarving.png"
        align(0.5,0.5)
    image meatcarving_bar:
        "images/minigames/meatcarving/meatcarving_bar.png"
        align(0.5,0.5)
        yoffset -40
    image meatcarving_meat:
        "images/minigames/meatcarving/meatcarving_meat.png"
        align(0.5,0.5)
        
screen meatcarving_minigame:
    add "meatcarving_arrow" at meatcarving_arrow_move(meatcarving_position)
    #text "[meatcarving_section]\nSection" align(0.5,0.1)
    #text "[meatcarving_position]\nPosition" align(0.5,0.2)
    #text "[meatcarving_barpos]\nBarPos" align(0.4,0.2)
    #text "[startpos_meatcarving]\nStart" align(0.6,0.2)
    #text "[endpos_meatcarving]\nEnd" align(0.7,0.2)
    #text "[endpos_perfect_meatcarving]\nPerEnd" align(0.8,0.2)
    button:
        xalign .5
        yalign .9
        xysize (194, 66)
        idle_background "gui/gui_button_idle.png"
        hover_background "gui/gui_button_hover.png"
        selected_idle_background "gui/gui_button_idle.png"
        selected_hover_background "gui/gui_button_hover.png"
        selected_background "gui/gui_button_selected.png"
        activate_sound "sounds/sfx_tap.ogg"
        text "STOP":
            style "menubutton"
            size 30
            outlines [ (1, "#000", absolute(0), absolute(0)) ]
        if meatcarving_position >= startpos_meatcarving and meatcarving_position <= endpos_perfect_meatcarving:
                action [SetVariable("meatcarving_section", 1),Hide("meatcarving_timer"), Call("results_meatcarving_minigame")]
        elif meatcarving_position >= endpos_perfect_meatcarving and meatcarving_position <= endpos_meatcarving:
                action [SetVariable("meatcarving_section", 2),Hide("meatcarving_timer"), Call("results_meatcarving_minigame")]
        else:
            action [SetVariable("meatcarving_section", 0),Hide("meatcarving_timer"), Call("results_meatcarving_minigame")]

    if meatcarving_position >= 0 and meatcarving_position <= 90:
        key "K_SPACE" action [SetVariable("meatcarving_section", 1),Hide("meatcarving_timer"), Call("results_meatcarving_minigame")]
    else:
        key "K_SPACE" action [SetVariable("meatcarving_section", 1),Hide("meatcarving_timer"), Call("results_meatcarving_minigame")]
screen meatcarving_bar_background:
    add "meatcarving_bg"
    add "meatcarving_bar" at meatcarving_arrow_move(meatcarving_barpos)

screen meatcarving_timer:
    timer 0.01 repeat True action [If(meatcarving_position <= 360, SetVariable("meatcarving_position", meatcarving_position + meatcarving_speed)),If(meatcarving_position >= 360, SetVariable("meatcarving_position", 0))]


################################################################################
label start_meatcarving_minigame:
    #Get a new bar position at startup
    $ meatcarving_barpos = renpy.random.randint(0, 216)
    #Start of bar
    $ startpos_meatcarving = (meatcarving_barpos + meatcarving_bar_start_offset)
    #End of Perfect on bar
    $ endpos_perfect_meatcarving = (startpos_meatcarving+30)
    #End of bar
    $ endpos_meatcarving = (startpos_meatcarving+80)
    
    show screen meatcarving_timer
    show screen meatcarving_bar_background
    call screen meatcarving_minigame with Dissolve(0.25)
    return
################################################################################
label end_meatcarving_minigame: #End minigame.
    hide screen meatcarving_minigame
    hide screen meatcarving_timer
    hide screen meatcarving_bar_background
    return
label results_meatcarving_minigame:
    show screen meatcarving_bar_background
    show screen meatcarving_minigame
    pause 1
    hide screen meatcarving_minigame
    hide screen meatcarving_bar_background
    with Dissolve(0.25)
    return
################################################################################
## Radio
################################################################################
init 15 python:
    radio_position = 0
    radio_section = 0
init:
    transform radio_arrow_move(cur_arrow):
        subpixel True
        rotate_pad True
        rotate cur_arrow
    image radio_arrow:
        "images/minigames/radio/radio_arrow.png"
        align(0.5,0.5)
        yoffset -40
    image radio_bg:
        "images/minigames/radio/bg_radio.png"
        align(0.5,0.5)
screen radio_minigame:
    add "radio_bg"
    add "radio_arrow" at radio_arrow_move(radio_position)
    button:
        xalign .5
        yalign .9
        xysize (194, 66)
        idle_background "gui/gui_button_idle.png"
        hover_background "gui/gui_button_hover.png"
        selected_idle_background "gui/gui_button_idle.png"
        selected_hover_background "gui/gui_button_hover.png"
        selected_background "gui/gui_button_selected.png"
        activate_sound "sounds/sfx_tap.ogg"
        text "STOP":
            style "menubutton"
            size 30
            outlines [ (1, "#000", absolute(0), absolute(0)) ]
        if radio_position >= 0 and radio_position <= 45:
                action [SetVariable("radio_section", 1),Hide("radio_timer"), Call("results_radio_minigame")]
        elif radio_position >= 46 and radio_position <= 90:
                action [SetVariable("radio_section", 2),Hide("radio_timer"), Call("results_radio_minigame")]
        elif radio_position >= 91 and radio_position <= 135:
                action [SetVariable("radio_section", 3),Hide("radio_timer"), Call("results_radio_minigame")]
        elif radio_position >= 136 and radio_position <= 180:
                action [SetVariable("radio_section", 4),Hide("radio_timer"), Call("results_radio_minigame")]
        elif radio_position >= 181 and radio_position <= 225:
                action [SetVariable("radio_section", 2),Hide("radio_timer"), Call("results_radio_minigame")]
        elif radio_position >= 226 and radio_position <= 270:
                action [SetVariable("radio_section", 3),Hide("radio_timer"), Call("results_radio_minigame")]
        elif radio_position >= 271 and radio_position <= 315:
                action [SetVariable("radio_section", 4),Hide("radio_timer"), Call("results_radio_minigame")]
        elif radio_position >= 316 and radio_position <= 360:
                action [SetVariable("radio_section", 2),Hide("radio_timer"), Call("results_radio_minigame")]
        else:
            action [SetVariable("radio_section", 1),Hide("radio_timer"), Call("results_radio_minigame")]
    if radio_position >= 0 and radio_position <= 45:
            key "K_SPACE" action [SetVariable("radio_section", 1),Hide("radio_timer"), Call("results_radio_minigame")]
    elif radio_position >= 46 and radio_position <= 90:
            key "K_SPACE" action [SetVariable("radio_section", 2),Hide("radio_timer"), Call("results_radio_minigame")]
    elif radio_position >= 91 and radio_position <= 135:
            key "K_SPACE" action [SetVariable("radio_section", 3),Hide("radio_timer"), Call("results_radio_minigame")]
    elif radio_position >= 136 and radio_position <= 180:
            key "K_SPACE" action [SetVariable("radio_section", 4),Hide("radio_timer"), Call("results_radio_minigame")]
    elif radio_position >= 181 and radio_position <= 225:
            key "K_SPACE" action [SetVariable("radio_section", 2),Hide("radio_timer"), Call("results_radio_minigame")]
    elif radio_position >= 226 and radio_position <= 270:
            key "K_SPACE" action [SetVariable("radio_section", 3),Hide("radio_timer"), Call("results_radio_minigame")]
    elif radio_position >= 271 and radio_position <= 315:
            key "K_SPACE" action [SetVariable("radio_section", 4),Hide("radio_timer"), Call("results_radio_minigame")]
    elif radio_position >= 316 and radio_position <= 360:
            key "K_SPACE" action [SetVariable("radio_section", 2),Hide("radio_timer"), Call("results_radio_minigame")]
    else:
        key "K_SPACE" action [SetVariable("radio_section", 1),Hide("radio_timer"), Call("results_radio_minigame")]

screen radio_timer:
    timer 0.0001 repeat True action [If(radio_position <= 360, SetVariable("radio_position", radio_position + 3)),If(radio_position >= 360, SetVariable("radio_position", 0))]

################################################################################
label start_radio_minigame:
    show screen radio_timer
    call screen radio_minigame with Dissolve(0.25)
    return
################################################################################
label end_radio_minigame: #End minigame.
    hide screen radio_minigame
    hide screen radio_timer
    return
label results_radio_minigame:
    show screen radio_minigame
    pause 1
    hide screen radio_minigame
    with Dissolve(0.25)
    return
