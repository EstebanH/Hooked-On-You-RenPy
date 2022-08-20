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

    $ quick_menu = True
    #call prologue
    $ quick_menu = True



    window hide
    #scene bg volleyball_day with dissolve
    call volleyballscene
    nrr "It seems like you've derailed the volleyball game just by showing up."
    $ trapperObj.change("pose", "pose01")
    $ trapperObj.change("emote", "angry")
    $ trapperObj.change("emotion", "mad")
    show trapper at moveright
    with Dissolve(0.25)
    tt "You derailed the game just by showing up, nitwit."
    $ trapperObj.change("emote", "none")
    nrr "And I guess you're also a nitwit."
    nrr "Look, it's best to just go with what Trapper says when he says it. That's a policy I hold for pretty much anyone who always seems to have fresh blood on their hands."
    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "happy")
    show spirit at movecenterright
    with Dissolve(0.25)
    ts "Hey, don't worry about it. It's all just a game. Existence, that is."
    $ huntressObj.change("emotion", "happy")
    $ spiritObj.change("emotion", "idle")
    show huntress at moveleft
    with Dissolve(0.25)
    th "Besides, you seem a lot more interesting than a silly game."
    $ huntressObj.change("emote", "question")
    th "What's your deal? What brings you here?"
    $ huntressObj.change("emote", "none")
    $ huntressObj.change("emotion", "idle")
    $ trapperObj.change("emotion", "happy")
    tt "You mean they're here to do more than distract from my total domination?"
    tw "*deep sigh*"
    $ wraithObj.change("emotion", "disgusted")
    show wraith at movecenterleft
    nrr "That was Wraith. That sign means he was done with the game too."
    nrr "Either that or he saw a butterfly or something."
    $ trapperObj.change("emotion", "disgusted")
    tt "Look, I don't care why this slack-jawed moron is here."
    $ trapperObj.change("pose", "close02")
    $ trapperObj.change("emotion", "idle")
    show huntress behind trapper at moveleft
    show wraith behind trapper  at movecenterleft
    show spirit behind trapper  at movecenterright
    show trapper at slidetocenter
    call mood_speedlines
    tt "I just want to know: can I kill them or not?"
    hide speedlines
    stop moodloop fadeout 3.0
    $ trapperObj.change("pose", "pose03")
    $ trapperObj.change("emotion", "mad")
    $ huntressObj.change("emotion", "disgusted")
    th "You know you can't."
    $ wraithObj.change("emotion", "idle")
    $ huntressObj.change("pose", "pose02")
    $ huntressObj.change("emotion", "idle")
    show trapper at slidetomoveright
    hide spirit 
    hide wraith 
    show spirit at movecenterright
    show wraith at movecenterleft
    th "At least not yet."
    $ trapperObj.change("pose", "pose01")
    $ trapperObj.change("emotion", "happy")
    tt "Oh yeah. Not yet."
    $ huntressObj.change("pose", "pose01")
    $ trapperObj.change("emotion", "idle")
    nrr "Hey, [mc_name], you might want to, you know, say something."
    nrr "Actually, never mind. There'll be plenty of time for that soon enough."
    nrr "Right now this group has some questions for you."

    nrr "But be warned: answer quickly and answer well."
    nrr "This is a timed quiz. And it will be very important later."
    nrr "Very important."
    nrr "Orrrrrrr not important in any way whatsoever. Probably that one. I can't remember."
    hide trapper 
    $ trapperObj.change("pose", "close01")
    menu:
        tt "How attractive would you say you are?"
        "Very":
            "I'd say I'm \"very attractive.\""
            $ trapperObj.change("pose", "pose03")
            tt "That's what you think \"very attractive\" is? Compared to THIS?"
            $ trapperObj.change("emote", "stars")
            nrr "Trapper flexes and his muscles are so tight you can practically see the blood running through his veins."
            $ trapperObj.change("emote", "none")
        "Not at all":
            ""
        "Average":
            mc "I'm pretty average, I think."
            ts "Just another face in the crowd, another normal, meaningless life in an endless cycle..."
            th "I think you're quite cute, myself. Like a chipmunk! Or a grizzly bear!"
    hide huntress
    hide trapper
    hide spirit
    show huntress at moveleft
    show trapper at moveright
    show spirit at movecenterright

    hide wraith 
    $ wraithObj.change("pose", "close01")
    $ wraithObj.change("emote", "question")
    show wraith at movecenterleft
    menu:
        tw "If you could have any superpower what would it be?"
        "Invisibility":
            $ wraithObj.change("emote", "none")
            mc "Umm... invisibility?"
            tw "Same. Although sometimes I think I already am..."
        "Flight":
            $ wraithObj.change("emote", "none")
            $ wraithObj.change("emotion", "happy")
            $ wraithObj.change("pose", "pose03")
            hide huntress
            hide trapper
            hide wraith
            hide spirit
            show huntress at moveleft
            show trapper at moveright
            show wraith at movecenterleft
            show spirit at movecenterright
            mc "Flight, for sure."
            ts "Technically I suppose I can fly. Honestly? It's not all that it's cracked up to be. As far as I go... I'm still not where I want to be."
        "Super strength":
            $ wraithObj.change("emote", "none")
            mc "Not implemented"
    hide huntress
    hide trapper
    hide wraith
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft

    hide spirit
    $ spiritObj.change("emote", "question")
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "close01")
    show spirit at movecenterright
    menu:
        ts "What was your best subject in school?"
        "Math":
            $ spiritObj.change("emote", "none")
            mc "Probably math."
            tw "It's the only thing that makes sense, when you think about it."
        "History":
            $ spiritObj.change("emote", "none")
            $ spiritObj.change("pose", "pose01")
            mc "History?"
            $ spiritObj.change("emote", "exclamation")
            mc "Nice. It's important to know what came before so that we are not doomed to repeat humanity's mistakes. I mean... we will always, but still."
            $ spiritObj.change("emote", "none")
        "Skipping Class":
            $ spiritObj.change("emote", "none")
            mc "Not implemented"
    hide trapper
    hide wraith
    hide spirit
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright

    hide huntress
    $ huntressObj.change("pose", "close01")
    show huntress at moveleft
    menu:
        th "What's your favorite animal?"
        "Dog":
            mc "Dog?"
            th "You'd look absolutely adorable in a little puppy mask!"
        "Cat":
            hide huntress
            hide trapper
            hide wraith
            hide spirit
            $ huntressObj.change("pose", "pose01")
            show huntress at moveleft
            show trapper at moveright
            show wraith at movecenterleft
            show spirit at movecenterright
            mc "Definitely a cat."
            $ spiritObj.change("emote", "spark")
            $ spiritObj.change("emotion", "disgusted")
            ts "What? Why is everyone looking at me? You think just because I'm the typical cute goth girl I have some specific love of all things cats, and more specifically, black cats? Well I do but you can all go to hell anyway."
            $ spiritObj.change("emote", "none")
            $ spiritObj.change("emotion", "idle")
        "Mustelid":
            mc "Not implemented"
    hide huntress
    hide trapper
    hide spirit
    show huntress at moveleft
    show trapper at moveright
    show spirit at movecenterright

    hide wraith
    $ wraithObj.change("pose", "close01")
    $ wraithObj.change("emote", "question")
    $ wraithObj.change("emotion", "happy")
    show wraith at movecenterleft
    menu:
        tw "What's your favorite color?"
        "Blue":
            $ wraithObj.change("emote", "none")
            mc "Blue."
        "Blood red":
            $ wraithObj.change("emote", "none")
            hide huntress
            hide trapper
            hide wraith
            hide spirit
            $ wraithObj.change("pose", "pose01")
            show huntress at moveleft
            show trapper at moveright
            show wraith at movecenterleft
            show spirit at movecenterright
            mc "Red."
            $ wraithObj.change("emote", "dread")
            $ wraithObj.change("emotion", "sad")
            tw "Some call it the color of love. But love is just another word for pain."
            $ wraithObj.change("emote", "none")
        "There-day-old corpse":
            $ wraithObj.change("emote", "none")
            mc "Nobody would expect me to pick this, so I'm gonna say three-day-old corpse. That's a pretty edgy answer, right? I'm pretty dangerous. I talk about corpses. No biggie."
            th "Those are no good to me unless they've been frozen. You'd be surprised by how quick;y good meat can spoil. Or maybe you wouldn't be surprised? I'm still getting to know you."
    hide huntress
    hide trapper
    hide wraith
    $ wraithObj.change("emotion", "disgusted")
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft
    
    $ spiritObj.change("emote", "question")
    hide spirit
    show spirit at movecenterright
    menu:
        ts "What's your dream job?"
        "Astronaut":
            $ spiritObj.change("emote", "none")
            mc "Not implemented"
        "Nightclub promoter":
            $ spiritObj.change("emote", "none")
            hide huntress
            hide trapper
            hide wraith
            hide spirit
            $ spiritObj.change("pose", "pose01")
            show huntress at moveleft
            show trapper at moveright
            show wraith at movecenterleft
            show spirit at movecenterright
            mc "Definitely nightclub promoter."
            $ wraithObj.change("emotion", "disgusted")
            $ trapperObj.change("emotion", "disgusted")
            $ huntressObj.change("emotion", "disgusted")
            $ spiritObj.change("emotion", "disgusted")
            nrr "Everyone groans, and--let's be honest--they're right to do so."
            tt "Luring folks into the dark? Not just anyone can do that..."
            $ wraithObj.change("emotion", "idle")
            $ trapperObj.change("emotion", "idle")
            $ huntressObj.change("emotion", "idle")
            $ spiritObj.change("emotion", "idle")
        "Not working at all":
            $ spiritObj.change("emote", "none")
            mc "If we get to do what we really want, why work at all?"
            ts "It takes a lot of courage to break free from society's expectations to climb the ladder."
            tt "Only she could spin laziness into some kind of grand crusade. These damned millenials..."
    hide huntress
    hide wraith
    hide spirit
    $ wraithObj.change("emotion", "disgusted")
    show huntress at moveleft
    show wraith at movecenterleft
    show spirit at movecenterright
    
    hide trapper
    $ trapperObj.change("pose", "close01")
    show trapper at moveright
    menu:
        tt "Best flavor of ice cream?"
        "Vanilla":
            mc "Not implemented"
        "Chocolate":
            mc "Chocolate."

            hide huntress
            hide trapper
            hide wraith
            hide spirit
            $ spiritObj.change("emotion", "disgusted")
            $ trapperObj.change("emote", "exclamation")
            $ trapperObj.change("pose", "pose02")
            show huntress at moveleft
            show trapper at moveright
            show wraith at movecenterleft
            show spirit at movecenterright
            tt "My favorite flavor is Pain."
            $ huntressObj.change("emotion", "happy")
            th "Same."
            $ spiritObj.change("emotion", "happy")
            ts "Same here."
            $ wraithObj.change("emotion", "disgusted")
            $ trapperObj.change("emote", "thoughts")
            tw "..."
            $ wraithObj.change("emotion", "idle")
            tw "...Mine is vanilla. Swiriled with Pain."
            $ wraithObj.change("emote", "none")
            $ spiritObj.change("emotion", "idle")
            $ huntressObj.change("emotion", "idle")
            $ trapperObj.change("pose", "pose01")
        "Horseflesh":
            mc "Not implemented"
    
    hide huntress
    hide trapper
    hide wraith
    hide spirit
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright

    nrr "I think mint chip is the greatest flavor ever conceived, myself. But enough about ice cream, am I right?"
    nrr "Hold on a second, this reminds me... I am right. Always. It's a lesson you should learn before we go too much further. Do what I say if you want to survive. Pick mint chip."
    hide huntress
    hide trapper
    hide wraith
    hide spirit
    call oceanhaunting
    oc "We're teaching lessons now, Narrator? You rascal... Kill or be killed is the rule on this island, even for faceless voices."
    call choice_icecream
    stop hauntloop fadeout 3.0
    call beachdayscene
    call event_tikitiki
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright
    with dissolve
    nrr "Anyhoo, now that they know so much about you, I'm sure the group wants you to start getting to know them."
    hide huntress
    hide wraith
    hide spirit
    $ trapperObj.change("emotion", "happy")
    $ trapperObj.change("pose", "close03")
    show trapper at slidetocenter
    with Dissolve(0.25)
    play sound "sounds/sfx_signature_trapper03.ogg"
    tt "I'm Trapper. I pretty much run things around here. I'm the smartest, richest, strongest person on this whole island."
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("emote", "stars")
    tt "I don't like losers. If you want to know what a loser is say hello to Wraith."
    play sound "sounds/sfx_signature_wraith01.ogg"
    $ trapperObj.change("emote", "none")
    $ wraithObj.change("emotion", "happy")
    $ wraithObj.change("pose", "close03")
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose01")
    show trapper at slidetomoveright, fadeaway
    show wraith at slidetocenter
    with dissolve
    hide trapper
    tw "Hi, I'm Wraith. I'm nothing like everyone else."
    $ wraithObj.change("emote", "sweat")
    $ wraithObj.change("emotion", "idle")
    tw "I like nice people and loathe big dumb idiots."
    $ wraithObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close03")
    $ wraithObj.change("emotion", "idle")
    $ wraithObj.change("pose", "pose01")
    play sound "sounds/sfx_signature_spirit03.ogg"
    show wraith at slidetomovecenterleft, fadeaway
    show spirit at slidetocenter
    with dissolve
    hide wraith
    ts "Hey what's up? I'm Spirit. I don't like... most things."
    $ spiritObj.change("emote", "dread")
    $ spiritObj.change("emotion", "disgusted")
    ts "I don't really hate most things either. It's not worth my time. But the things I do hate I really hate, you know?"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "happy")
    ts "Based on my personal observations, life is nothing but suffering, and society is a carefully calculated lie to keep everyone subserviant to those in power. It's better to choose to just not take part."
    $ spiritObj.change("emotion", "idle")
    nrr "Jeez, it's like she was downright murdered by society, she hates it so much."
    nrr "Oh, no, wait--I'm remembering Spirit's story now, and that's almost exactly what happened."
    play sound "sounds/sfx_signature_huntress01.ogg"
    $ huntressObj.change("emotion", "happy")
    $ huntressObj.change("pose", "close02")
    $ spiritObj.change("pose", "pose03")
    show spirit at slidetomovecenterright, fadeaway
    show huntress at slidetocenter
    with dissolve
    hide spirit
    th "Hey! I'm Huntress. Don't let these bummers get you down."
    $ huntressObj.change("emote", "spark")
    th "There's lots of fun to be had on this island. Along with lots of love."
    $ huntressObj.change("emote", "none")
    $ huntressObj.change("pose", "pose01")
    $ trapperObj.change("emotion", "happy")
    $ huntressObj.change("emotion", "idle")
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright
    show huntress at slidetomoveleft
    with Dissolve(0.25)
    tt "Yeah there is! If you know what I mean!"
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "pose01")
    ts "Grow up."
    $ trapperObj.change("emotion", "disgusted")
    $ trapperObj.change("emote", "anger")
    tt "Grow a body."
    $ trapperObj.change("emote", "none")
    ts "I've explained this a thousand times: I'm dead but I'm not a literal ghost. I just create a trail of fog, I'm not made for it."
    $ trapperObj.change("emotion", "idle")
    $ huntressObj.change("emotion", "disgusted")
    tt "Whatever, fogbody."
    $ wraithObj.change("emotion", "disgusted")
    tw "That's not nice."
    th "He's not nice."
    $ trapperObj.change("pose", "pose03")
    tt "You love it."
    $ huntressObj.change("emotion", "happy")
    $ trapperObj.change("emotion", "happy")
    th "Only sometimes."
    $ wraithObj.change("emotion", "scared")
    tw "Eww, really? That's disgusting."
    $ trapperObj.change("pose", "pose01")
    $ trapperObj.change("emotion", "happy")
    $ trapperObj.change("emote", "spark")
    $ huntressObj.change("emotion", "idle")
    tt "That's why she likes it!"
    $ trapperObj.change("emote", "none")
    $ wraithObj.change("emotion", "disgusted")
    $ huntressObj.change("emotion", "disgusted")
    $ huntressObj.change("emote", "dread")
    $ trapperObj.change("emotion", "disgusted")
    th "Don't speak for me. I also hate it."
    $ huntressObj.change("emote", "none")
    $ spiritObj.change("pose", "pose03")
    ts "Stop speaking entirely actually."
    $ huntressObj.change("emotion", "idle")
    $ trapperObj.change("emotion", "idle")
    nrr "For the first time ever I agree with Wraith. Let's move on, otherwise they'll do this all day."
    nrr "Besides, if I know this crew--and I do--they'll want to show off soon enough."
    tt "If we're done playing, let's do something else instead."
    $ spiritObj.change("emote", "exclamation")
    $ wraithObj.change("emotion", "idle")
    ts "Wow, for once I actually agree with this meathead."
    $ spiritObj.change("emote", "none")
    $ trapperObj.change("emote", "lightbulb")
    $ trapperObj.change("emotion", "happy")
    tt "I say we go to my yacht. It's the massive boat docked nearby."
    $ wraithObj.change("emotion", "disgusted")
    $ wraithObj.change("pose", "pose03")
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("pose", "pose03")
    tt "I'll give everyone a taste of true luxury and power."
    nrr "Wraith rolls his eyes."
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose01")
    tt "Don't mind him, he just hates fun and happiness."
    tw "No, I hate the endless, desperate, soul-crushing pursuit of wealth, the way it's flaunted needlessly, and the cruelty it engenders."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose01")
    $ wraithObj.change("emotion", "happy")
    $ wraithObj.change("emote", "question")
    tw "What about hanging out by the pool?"
    $ wraithObj.change("emotion", "sad")
    tw "I find the water calming. Simple. Beautiful."
    $ huntressObj.change("emote", "exclamation")
    $ huntressObj.change("pose", "pose02")
    $ wraithObj.change("emotion", "disgusted")
    th "Hey! What about our volleyball game?"
    th "We can exercise and have some fun as a group!"
    ts "Are you all serious? There's a perfectly good lounge to chill out at right here."
    $ spiritObj.change("emotion", "disgusted")
    ts "I'm tired. And besides, I hate being in the sun."
    menu:
        nrr "Where do you want to go?"
        "{image=gui/menu_choice_bar_idle.png}":
            mc ""
        "{image=gui/menu_choice_beach_idle.png}":
            mc ""
        "{image=gui/menu_choice_volleyball_idle.png}":
            mc ""
        "{image=gui/menu_choice_yachet_idle.png}":
            mc ""

            
    nrr "<<<<<<<Ends here>>>>>>>>"
    # This ends the game.
    return
