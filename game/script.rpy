##https://youtu.be/DPFXHoIBmAo
# Declare the characters.
init python:
    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.sound.play("sounds/sfx_tap.ogg",channel="sound")
    def callbackchoice(ctc, **kwargs):
        if ctc == "end":
            renpy.sound.play("sounds/sfx_ui_choice_appear.ogg",channel="sound")
    renpy.music.register_channel("hauntloop", "music", loop=True)
    renpy.music.register_channel("choiceloop", "music", loop=True)
    renpy.music.register_channel("moodloop", "music", loop=True)
    renpy.music.register_channel("eventloop", "music", loop=True)

define nrr = Character(None, window_style="window_narrator", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define cho = Character(None, window_style="window_narrator",  callback=callbackchoice, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)

define oc = Character("", window_style="window_ocean", namebox_style="namebox_ocean", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define mc = DynamicCharacter('mc_name', color="#3e3458", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
##define look = Character(None,window_background=None, button_style = "say_button_none", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define dw = Character("DWIGHT", window_style="window_killer", color="#cb8830", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define nb = Character("NOBODY", window_style="window_killer", color="#cb8830", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define cl = Character("CLAUDETTE", window_style="window_killer", color="#cba530",  callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define th = Character("THE HUNTRESS", window_style="window_killer", color="#d94b2a", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define ts = Character("THE SPIRIT", window_style="window_killer", color="#ee496a", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define tt = Character("THE TRAPPER", window_style="window_killer", color="#385b8d", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define tw = Character("THE WRAITH", window_style="window_killer", color="#5f9b2a", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define tr = Character("THE TRICKSTER", window_style="window_killer", color="#ae6cdd", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define everyone = Character("EVERYONE", window_style="window_killer", color="#d94b2a", callback=callbackcontinue, show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
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

label event_dinner:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play eventloop("audio/sfx_red_sauce.ogg") fadein 3.0 loop
    return 

label event_bloodconfident:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play eventloop("audio/sfx_blood_confident.ogg") fadein 3.0 loop
    return 

label event_speeddating:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play eventloop("audio/sfx_slash_speed_dating.ogg") fadein 3.0 loop
    return 

label event_storytime:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play eventloop("audio/sfx_boarding_pass.ogg") fadein 3.0 loop
    return 

label event_papercutbolsa:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play eventloop("audio/sfx_papercut_bolsa.ogg") fadein 3.0 loop
    return 

label namePlayer:
    # No quick menu in name input screen
    $ quick_menu = False

    call warmdarkscene

    while user_input == "":
        call screen name_input
    python:
        user_input = user_input.strip() or "Player"
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
    call prologue
    call chapter1
    call chapter2
    call chapter3
    call chapter4
    nrr "<<<<<<<Ends here for now>>>>>>>>"
    # This ends the game.
    return
