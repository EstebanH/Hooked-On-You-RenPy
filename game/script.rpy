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
    call beachdayscene

    $ quick_menu = True
    call prologue
    $ quick_menu = True



    window hide
    scene bg volleyball_day with dissolve
    nrr "It seems like you've derailed the volleyball game just by showing up."
    tt "You derailed the game just by showing up, nitwit."
    nrr "And I guess you're also a nitwit."
    nrr "Look, it's best to just go with what Trapper says when he says it. That's a policy I hold for pretty much anyone who always seems to have fresh blood on their hands."
    ts "Hey, don't worry about it. It's all just a game. Existence, that is."
    th "Besides, you seem a lot more interesting than a silly game."
    th "What's your deal? What brings you here?"
    tt "You mean they're here to do more than distract from my total domination?"
    tw "*deep sigh*"
    nrr "That was Wraith. That sign means he was done with the game too."
    nrr "Either that or he saw a butterfly or something."
    tt "Look, I don't care why this slack-jawed moron is here."
    tt "I just want to know: can I kill them or not?"
    th "You know you can't."
    th "At least not yet."
    tt "Oh yeah. Not yet."
    nrr "Hey, [mc_name], you might want to, you know, say something."
    nrr "Actually, never mind. There'll be plenty of time for that soon enough."
    nrr "Right now this group has some questions for you."
    nrr "But be warned: answer quickly and answer well."
    nrr "This is a timed quiz. And it will be very important later."
    nrr "Very important."
    nrr "Orrrrrrr not important in any way whatsoever. Probably that one. I can't remember."

    menu:
        tt "How attractive would you say you are?"
        "Very":
            ""
        "Not at all":
            ""
        "Average":
            mc "I'm pretty average, I think."
            ts "Just another face in the crowd, another normal, meaningless life in an endless cycle..."
            th "I think you're quite cute, myself. Like a chipmunk! Or a grizzly bear!"

    menu:
        tw "If you could have any superpower what would it be?"
        "Invisibility":
            mc "Umm... invisibility?"
            tw "Same. Although sometimes I think I already am..."
        "Flight":
            ""
        "Super strength":
            ""

    menu:
        ts "What was your best subject in school?"
        "Math":
            mc "Probably math."
            tw "It's the only thing that makes sense, when you think about it."
        "History":
            ""
        "Skipping Class":
            ""

    menu:
        th "What's your favorite animal?"
        "Dog":
            mc "Dog?"
            th "You'd look absolutely adorable in a little puppy mask!"
        "Cat":
            ""
        "Mustelid":
            ""

    menu:
        tw "What's your favorite color?"
        "Blue":
            ""
        "Blood red":
            ""
        "There-day-old corpse":
            mc "Nobody would expect me to pick this, so I'm gonna say three-day-old corpse. That's a pretty edgy answer, right? I'm pretty dangerous. I talk about corpses. No biggie."
            th "Those are no good to me unless they've been frozen. You'd be surprised by how quick;y good meat can spoil. Or maybe you wouldn't be surprised? I'm still getting to know you."

    menu:
        ts "What's your dream job?"
        "Astronaut":
            ""
        "Nightclub promoter":
            ""
        "Not working at all":
            mc "If we get to do what we really want, why work at all?"
            ts "It takes a lot of courage to break free from society's expectations to climb the ladder."
            tt "Only she could spin laziness into some kind of grand crusade. These damned millenials..."

    menu:
        tt "Best flavor of ice cream?"
        "Vanilla":
            ""
        "Chocolate":
            mc "Chocolate."
            tt "My favorite flavor is Pain."
            th "Same."
            ts "Same here."
            tw "..."
            tw "...Mine is vanilla. Swiriled with Pain."
        "Horseflesh":
            ""
    nrr "I think mint chip is the greatest flavor ever conceived, myself. But enough about ice cream, am I right?"
    nrr "Hold on a second, this reminds me... I am right. Always. It's a lesson you should learn before we go too much further. Do what I say if you want to survive. Pick mint chip."
    window hide
    scene bg haunting with dissolve
    oc "We're teaching lessons now, Narrator? You rascal... Kill or be killed is the rule on this island, even for faceless voices."

    menu:
        nrr "Tell me, what's the best flavor of ice cream?"
        "Vanilla":
            ""
        "Chocolate":
            ""
        "Horseflesh":
            ""
        "Mint Chip":
            mc "The best flavor is... mint chip!"
            oc "So obedient..."
            nrr "I think you're gonna do juuuuust fine."
    window hide
    scene bg beach_day with dissolve
    nrr "Anyhoo, now that they know so much about you, I'm sure the group wants you to start getting to know them."
    tt "I'm Trapper. I pretty much run things around here. I'm the smartest, richest, strongest person on this whole island."
    tt "I don't like losers. If you want to know what a loser is say hello to Wraith."
    tw "Hi, I'm Wraith. I'm nothing like everyone else."
    tw "I like nice people and loathe big dumb idiots."
    ts "Hey what's up? I'm Spirit. I don't like... most things."
    ts "I don't really hate most things either. It's not worth my time. But the things I do hate I really hate, you know?"
    ts "Based on my personal observations, life is nothing but suffering, and society is a carefully calculated lie to keep everyone subserviant to those in power. It's better to choose to just not take part."
    nrr "Jeez, it's like she was downright murdered by society, she hates it so much."
    nrr "Oh, no, wait--I'm remembering Spirit's story now, and that's almost exactly what happened."
    th "Hey! I'm Huntress. Don't let these bummers get you down."
    th "There's lots of fun to be had on this island. Along with lots of love."
    tt "Yeah there is! If you know what I mean!"
    ts "Grow up."
    tt "Grow a body."
    ts "I've explained this a thousand times: I'm dead but I'm not a literal ghost. I just create a trail of fog, I'm not made for it."
    tt "Whatever, fogbody."
    tw "That's not nice."
    th "He's not nice."
    tt "You love it."
    th "Only sometimes."
    tw "Eww, really? That's disgusting."
    tt "That's why she likes it!"
    th "Don't speak for me. I also hate it."
    ts "Stop speaking entirely actually."
    nrr "For the first time ever I agree with Wraith. Let's move on, otherwise they'll do this all day."
    nrr "Besides, if I know this crew--and I do--they'll want to show off soon enough."
    tt "If we're done playing, let's do something else instead."
    ts "Wow, for once I actually agree with this meathead."
    tt "I say we go to my yacht. It's the massive boat docked nearby."
    tt "I'll give everyone a taste of true luxury and power."
    nrr "Wraith rolls his eyes."
    tt "Don't mind him, he just hates fun and happiness."
    tw "No, I hate the endless, desperate, soul-crushing pursuit of wealth, the way it's flaunted needlessly, and the cruelty it engenders."
    tw "What about hanging out by the pool?"
    tw "I find the water calming. Simple. Beautiful."
    th "Hey! What about our volleyball game?"
    th "We can exercise and have some fun as a group!"
    ts "Are you all serious? There's a perfectly good lounge to chill out at right here."
    ts "I'm tired. And besides, I hate being in the sun."
    menu:
        nrr "Where do you want to go?"
        "Vanilla":
            ""
        "Chocolate":
            ""
        "Horseflesh":
            ""
        "Mint Chip":
            ""

            
    nrr "<<<<<<<Ends here>>>>>>>>"
    # This ends the game.
    return
