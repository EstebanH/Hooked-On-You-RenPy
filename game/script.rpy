##https://youtu.be/DPFXHoIBmAo
# Declare the characters.
define nrr = Character(None, window_style="window_narrator", color="#3a2e55",callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define cho = Character(None, window_style="window_narrator", color="#3a2e55",  callback=callbackchoice, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)

define oc = Character("", window_style="window_ocean", namebox_style="namebox_ocean", color="#3a2e55", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define mc = DynamicCharacter('mc_name', color="#3a2e55", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define look = Character(None,window_background=None, button_style = "say_button_none", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define dw = Character("DWIGHT", color="#bb7d31", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)

define cl = Character("CLAUDETTE", color="#b4992e",  callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define th = Character("THE HUNTRESS", window_style="window_killer", color="#c64631", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define ts = Character("THE SPIRIT", window_style="window_killer", color="#d94464", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define tt = Character("THE TRAPPER", window_style="window_killer", color="#3d567b", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define tw = Character("THE WRAITH", window_style="window_killer", color="#58902c", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
## Character Example
#p = Character('Protagonist', what_prefix="\"", what_suffix="\"", what_size=26, who_outlines=[(4, "#004035", -5, 3),(2, "#0a9e9a", -5, 3), (3, "#252118", absolute(-2), absolute(0)), (absolute(1), "#FFF", absolute(0), absolute(0))],what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ], show_two_window=True, color="#000000", ctc = anim.Blink("ctc.png", xpos=600, ypos=450), ctc_position= "fixed", callback=callbackcontinue)

label event_choices:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play choiceloop("audio/sfx_time_to_kill.ogg") fadein 3.0 loop
    return

label event_clauddwight:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play eventloop("audio/sfx_banana_hammak.ogg") fadein 3.0 loop
    return

label event_hell:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play eventloop("audio/sfx_welcome_to_hell_nosolo.ogg") fadein 3.0 loop
    return

label event_tikitiki:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play eventloop("audio/sfx_tikitiki_youredead.ogg") fadein 3.0 loop
    return

label event_quiz:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play eventloop("audio/sfx_killer_flirt.ogg") fadein 3.0 loop
    return

define lastchance = False
label icecream_warning:
    nrr "You got a reading comprehension problem? I just told you mint chip was where it's at!"
    nrr "You almost bought youself a Game Over there, buddy. That's right. I can end your life whenever I want to. I'm in control, so don't you forget it. If I say you like mint chip, you like mint clip. Now try it again."
    $ lastchance = True
    call choice_icecream
    return

label icecream_death:
    nrr "In case it wasn't clear who is in charge, it's me."
    oc "You have to understand, it feels very good to end someone else's game. You should try it sometime..."
    play sound "sounds/sfx_gameover.ogg"
    call screen game_over("choice_icecream")
    return

label choice_icecream:
    menu:
        nrr "Tell me, what's the best flavor of ice cream?"
        "Vanilla":
            mc "The best flavor is... vanilla!"
            if not lastchance:
                call icecream_warning
            else:
                call icecream_death
        "Chocolate":
            mc "The best flavor is... chocolate!"
            if not lastchance:
                call icecream_warning
            else:
                call icecream_death
        "Horseflesh":
            mc "The best flavor is... horseflesh!"
            if not lastchance:
                call icecream_warning
            else:
                call icecream_death
        "Mint Chip":
            mc "The best flavor is... mint chip!"
            oc "So obedient..."
            nrr "I think you're gonna do juuuuust fine."
    return

label namePlayer:
    # No quick menu in name input screen
    $ quick_menu = False

    call warmdarkscene

    while user_input == "":
        call screen name_input
    python:
        user_input = user_input.strip() or "Bill"
        mc_name = user_input
        save_name = user_input
    return

# The game starts here.
label start:
    # Initialize important variables
    $ mc_name = "PlayerName"
    $ save_name = mc_name
    $ clauddwightObj = ClauddwightClass()
    $ entityObj = EntityClass()
    $ grandmaObj = GrandmaClass()
    $ huntressObj = HuntressClass()
    $ momObj = MomClass()
    $ oniObj = OniClass()
    $ spiritObj = SpiritClass()
    $ trapperObj = TrapperClass()
    $ dadObj = DadClass()
    $ tricksterObj = TricksterClass()
    $ wraithObj = WraithClass()
    call namePlayer
    call loadingscene

    #call prologue
    call chapter1


    #scene bg volleyball_day with dissolve
 
    nrr "<<<<<<<Ends here>>>>>>>>"
    # This ends the game.
    return
