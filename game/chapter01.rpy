define lastchance = False
label icecream_warning:
    nrr "You got a reading comprehension problem? I just told you mint chip was where it's at!"
    nrr "You almost bought youself a Game Over there, buddy. That's right. I can end your life whenever I want to. I'm in control, so don't you forget it. If I say you like mint chip, you like mint clip. Now try it again."
    $ lastchance = True
    call choice_icecream
    return

label icecream_death:
    nrr "In case it wasn't clear who is in charge, it's me."
    oc "You have to understand, it feels very good to end someone else's game. You should try it sometime…"
    play sound "sounds/sfx_gameover.ogg"
    call screen game_over("choice_icecream")
    return

label choice_icecream:
    menu:
        nrr "Tell me, what's the best flavor of ice cream?"
        "Vanilla":
            mc "The best flavor is… vanilla!"
            if not lastchance:
                call icecream_warning
            else:
                call icecream_death
        "Chocolate":
            mc "The best flavor is… chocolate!"
            if not lastchance:
                call icecream_warning
            else:
                call icecream_death
        "Horseflesh":
            mc "The best flavor is… horseflesh!"
            if not lastchance:
                call icecream_warning
            else:
                call icecream_death
        "Mint Chip":
            mc "The best flavor is… mint chip!"
            oc "So obedient…"
            nrr "I think you're gonna do juuuuust fine."
    return

label chapter1:
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
    $ trapperObj.change("pose", "close01")
    show spirit behind trapper 
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
            mc "I've never thought of myself as attractive."
            nrr "Woah, watch it. That's bullshit. You're beautiful, you hear me?"
            $ trapperObj.change("pose", "pose01")
        "Average":
            mc "I'm pretty average, I think."
            $ trapperObj.change("pose", "pose01")
            $ spiritObj.change("emotion", "disgusted")
            ts "Just another face in the crowd, another normal, meaningless life in an endless cycle…"
            $ huntressObj.change("pose", "pose03")
            th "I think you're quite cute, myself. Like a chipmunk! Or a grizzly bear!"
            $ huntressObj.change("pose", "pose01")
            $ spiritObj.change("emotion", "idle")
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
            mc "Umm… invisibility?"
            $ wraithObj.change("emote", "disgusted")
            $ wraithObj.change("pose", "pose03")
            tw "Same. Although sometimes I think I already am…"
            $ wraithObj.change("emote", "idle")
            $ wraithObj.change("pose", "pose01")
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
            ts "Technically I suppose I can fly. Honestly? It's not all that it's cracked up to be. As far as I go… I'm still not where I want to be."
        "Super strength":
            $ wraithObj.change("emote", "none")
            mc "Super strength would be cool."
            $ trapperObj.change("emotion", "happy")
            tt "Strength isn't all about muscles. True strength is up here."
            nrr "You expect Trapper to point to his head, but instead he taps one of his bulging shoulders."
            $ trapperObj.change("emotion", "disgusted")
            tt "It's specifically in these muscles. Nobody gives a shit about your calves."
            $ trapperObj.change("emotion", "idle")

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
            $ spiritObj.change("pose", "pose01")
            mc "Probably math."
            $ wraithObj.change("pose", "pose03")
            $ wraithObj.change("emote", "exclamation")
            $ wraithObj.change("emotion", "happy")
            tw "It's the only thing that makes sense, when you think about it."
            $ wraithObj.change("pose", "pose01")
            $ wraithObj.change("emote", "none")
            $ wraithObj.change("emotion", "idle")
        "History":
            $ spiritObj.change("emote", "none")
            $ spiritObj.change("pose", "pose01")
            mc "History?"
            $ spiritObj.change("emote", "exclamation")
            mc "Nice. It's important to know what came before so that we are not doomed to repeat humanity's mistakes. I mean… we will always, but still."
            $ spiritObj.change("emote", "none")
        "Skipping Class":
            $ spiritObj.change("emote", "none")
            mc "You could say I majored in skipping class, hah!"
            $ huntressObj.change("emotion", "happy")
            th "If I had ever gone to school, I'm sure I would've done great in skipping class. I prefer skipping over walking almost always."
            $ spiritObj.change("pose", "pose01")
            $ huntressObj.change("emotion", "idle")
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
            $ huntressObj.change("pose", "pose01")
            mc "Dog?"
            $ huntressObj.change("emote", "heart")
            $ huntressObj.change("pose", "pose03")
            th "You'd look absolutely adorable in a little puppy mask!"
            $ huntressObj.change("emote", "none")
            $ huntressObj.change("pose", "pose01")
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
            $ spiritObj.change("emote", "sparks")
            $ spiritObj.change("emotion", "disgusted")
            ts "What? Why is everyone looking at me? You think just because I'm the typical cute goth girl I have some specific love of all things cats, and more specifically, black cats? Well I do but you can all go to hell anyway."
            $ spiritObj.change("emote", "none")
            $ spiritObj.change("emotion", "idle")
        "Mustelid":
            $ huntressObj.change("pose", "pose01")
            mc "Mustelids, 100%"
            nrr "Be honest, you have no idea what a mustelid is and you're just hoping it's some secret answer that results in a hilarious Easter egg, right?"
            nrr "Because there is no Easter egg… it's just another word for ferrets and stuff like that."
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
            $ wraithObj.change("pose", "pose01")
            mc "Blue."
            $ trapperObj.change("emotion", "disgusted")
            tt "Blue isn't good for productivity. Makes people want to be lazy."
            $ trapperObj.change("emotion", "idle")
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
            $ wraithObj.change("pose", "pose01")
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
    $ spiritObj.change("pose", "close01")
    hide spirit
    show spirit at movecenterright
    menu:
        ts "What's your dream job?"
        "Astronaut":
            $ spiritObj.change("emote", "none")
            $ spiritObj.change("pose", "pose01")
            mc "It'd be pretty amazing to be an astronaut, I think."
            tw "It's hard to imagine being farther away from anyone than floating in space. The cold, inky vastness of nothing, forever."
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
            tt "Luring folks into the dark? Not just anyone can do that…"
            $ wraithObj.change("emotion", "idle")
            $ trapperObj.change("emotion", "idle")
            $ huntressObj.change("emotion", "idle")
            $ spiritObj.change("emotion", "idle")
        "Not working at all":
            $ spiritObj.change("emote", "none")
            $ spiritObj.change("pose", "pose01")
            mc "If we get to do what we really want, why work at all?"
            ts "It takes a lot of courage to break free from society's expectations to climb the ladder."
            $ trapperObj.change("emote", "anger")
            $ trapperObj.change("emotion", "mad")
            tt "Only she could spin laziness into some kind of grand crusade. These damned millenials…"
            $ trapperObj.change("emote", "none")
            $ trapperObj.change("emotion", "idle")
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
            mc "Vanilla?"
        "Chocolate":
            mc "Chocolate."
        "Horseflesh":
            mc "Horse… flesh?"
            call oceanhaunting
            oc "MMMMmmmmm, horseflesh."
            stop hauntloop fadeout 3.0
            $ trapperObj.change("pose", "pose01")
    hide huntress
    hide trapper
    hide wraith
    hide spirit
    $ trapperObj.change("emote", "exclamation")
    $ trapperObj.change("pose", "pose02")
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright
    tt "My favorite flavor is Pain."
    $ trapperObj.change("emote", "none")
    $ huntressObj.change("emotion", "happy")
    th "Same."
    $ spiritObj.change("emotion", "happy")
    ts "Same here."
    $ wraithObj.change("emotion", "disgusted")
    $ trapperObj.change("emote", "thoughts")
    tw "…"
    $ wraithObj.change("emotion", "idle")
    tw "…Mine is vanilla. Swiriled with Pain."
    $ wraithObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    $ huntressObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose01")
    nrr "I think mint chip is the greatest flavor ever conceived, myself. But enough about ice cream, am I right?"
    nrr "Hold on a second, this reminds me… I am right. Always. It's a lesson you should learn before we go too much further. Do what I say if you want to survive. Pick mint chip."
    hide huntress
    hide trapper
    hide wraith
    hide spirit
    call oceanhaunting
    oc "We're teaching lessons now, Narrator? You rascal… Kill or be killed is the rule on this island, even for faceless voices."
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
    show wraith at movecenterleft, noalpha
    tt "I don't like losers. If you want to know what a loser is say hello to Wraith."
    play sound "sounds/sfx_signature_wraith01.ogg"
    $ trapperObj.change("emote", "none")
    $ wraithObj.change("emotion", "happy")
    $ wraithObj.change("pose", "close03")
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose01")
    show trapper at slidetomoveright, fadeaway
    show wraith at slidetocenter, fadenear
    with dissolve
    hide trapper
    tw "Hi, I'm Wraith. I'm nothing like everyone else."
    $ wraithObj.change("emote", "sweat")
    $ wraithObj.change("emotion", "idle")
    show spirit at movecenterright, noalpha
    tw "I like nice people and loathe big dumb idiots."
    $ wraithObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close03")
    $ wraithObj.change("emotion", "idle")
    $ wraithObj.change("pose", "pose01")
    play sound "sounds/sfx_signature_spirit03.ogg"
    show wraith at slidetomovecenterleft, fadeaway
    show spirit at slidetocenter, fadenear
    with dissolve
    hide wraith
    ts "Hey what's up? I'm Spirit. I don't like… most things."
    $ spiritObj.change("emote", "dread")
    $ spiritObj.change("emotion", "disgusted")
    ts "I don't really hate most things either. It's not worth my time. But the things I do hate I really hate, you know?"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "happy")
    ts "Based on my personal observations, life is nothing but suffering, and society is a carefully calculated lie to keep everyone subserviant to those in power. It's better to choose to just not take part."
    $ spiritObj.change("emotion", "idle")
    nrr "Jeez, it's like she was downright murdered by society, she hates it so much."
    show huntress at moveleft, noalpha
    nrr "Oh, no, wait--I'm remembering Spirit's story now, and that's almost exactly what happened."
    play sound "sounds/sfx_signature_huntress01.ogg"
    $ huntressObj.change("emotion", "happy")
    $ huntressObj.change("pose", "close02")
    $ spiritObj.change("pose", "pose03")
    show spirit at slidetomovecenterright, fadeaway
    show huntress at slidetocenter, fadenear
    with dissolve
    hide spirit
    th "Hey! I'm Huntress. Don't let these bummers get you down."
    $ huntressObj.change("emote", "sparks")
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
    hide huntress
    hide trapper
    hide wraith
    hide spirit
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright
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
    $ trapperObj.change("emote", "sparks")
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
    $ trapperObj.change("emote", "none")
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
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("emotion", "sad")
    tw "I find the water calming. Simple. Beautiful."
    $ huntressObj.change("emote", "exclamation")
    $ huntressObj.change("pose", "pose02")
    $ wraithObj.change("emotion", "disgusted")
    th "Hey! What about our volleyball game?"
    $ huntressObj.change("emote", "none")
    th "We can exercise and have some fun as a group!"
    ts "Are you all serious? There's a perfectly good lounge to chill out at right here."
    $ spiritObj.change("emotion", "disgusted")
    ts "I'm tired. And besides, I hate being in the sun."
    $ imagechoice = True
    menu:
        nrr "Where do you want to go?"
        "gui/menu_choice_bar_idle.png¦gui/menu_choice_bar_hover.png¦gui/menu_choice_bar_select.png":
            mc "It'd be great to relax for a second at the lounge."
            hide huntress
            hide trapper
            hide wraith
            $ spiritObj.change("emotion", "idle")
            $ spiritObj.change("pose", "close01")
            show spirit at slidetocenter
            ts "To kick up your feet, look out over the ocean, and relax on your own terms…"
            $ spiritObj.change("emotion", "happy")
            ts "Who would want anything else? Dry, comfortable, enjoying a cool drink on a hot day. It's the best."
            $ spiritObj.change("pose", "close03")
            $ spiritObj.change("emotion", "idle")
            ts "I mean, what kind of fool, what kind of monster, what kind of mask-wearing psychopath would finally be granted a break from the constant grind of chasing and fighting to get ahead, and then choose to exert themselves in, quite frankly, any way whatsoever?"
            $ spiritObj.change("emotion", "mad")
            $ spiritObj.change("emote", "anger")
            ts "Why am I the only one who gets it?! It’s time to stop living by THEIR RULES! I WON’T DO IT ANY LONGER!"
            nrr "Yeah, we should probably give her a second to calm down."
            show spirit at slidetomovecenterright, fadeaway
            with dissolve
            hide spirit

        "gui/menu_choice_beach_idle.png¦gui/menu_choice_beach_hover.png¦gui/menu_choice_beach_select.png":
            mc "I'd be down for a dip in the pool?"
            hide huntress
            hide spirit
            hide trapper
            $ wraithObj.change("emotion", "happy")
            $ wraithObj.change("emote", "question")
            $ wraithObj.change("pose", "close01")
            show wraith at slidetocenter
            tw "Whoa. The pool? You…you actually want to go to the pool?"
            $ wraithObj.change("emote", "none")
            $ wraithObj.change("emotion", "disgusted")
            $ wraithObj.change("pose", "close01")
            tw "I, uh, well, I mean, sure, why not?"
            tw "I've got good ideas. What's wrong with my ideas?"
            $ wraithObj.change("emotion", "idle")
            $ wraithObj.change("pose", "close03")
            tw "The pool is great, everyone knows that. All over the world, if people agree on one thing, it's that pools are great."
            $ wraithObj.change("emotion", "happy")
            tw "Look, we've got a whole ocean right here and they still put in a pool because pools are just, ya know, great. It's a real special treat."
            $ wraithObj.change("emotion", "idle")
            $ wraithObj.change("emote", "sweat")
            nrr "And you thought it was bad when he stayed quiet."
            $ wraithObj.change("emote", "none")
            show wraith at slidetomovecenterleft, fadeaway
            with dissolve
            hide wraith
            
        "gui/menu_choice_volleyball_idle.png¦gui/menu_choice_volleyball_hover.png¦gui/menu_choice_volleyball_select.png":
            mc "I hate that I interrupted your game. You should finish it."
            hide wraith
            hide spirit
            hide trapper
            $ huntressObj.change("emotion", "happy")
            $ huntressObj.change("pose", "close02")
            show huntress at slidetocenter
            th "Yay! I love to play outdoors! I also love to meet new people!"
            th "I also love to bring them home to play!"
            $ huntressObj.change("pose", "close01")
            th "I'm sort of a big kid at heart. Obviously you are too, I like you already."
            $ huntressObj.change("emotion", "disgusted")
            th "I hate people who are too serious. They ruin everything."
            $ huntressObj.change("emote", "stars")
            $ huntressObj.change("emotion", "idle")
            $ huntressObj.change("pose", "close03")
            th "Well, they do if you don't handle them. Swiftly."
            show huntress at slidetomoveleft, fadeaway
            with dissolve
            hide huntress

        "gui/menu_choice_yacht_idle.png¦gui/menu_choice_yacht_hover.png¦gui/menu_choice_yacht_select.png":
            mc "How about the yacht?"
            hide huntress
            hide spirit
            hide wraith
            $ trapperObj.change("emotion", "happy")
            $ trapperObj.change("pose", "close01")
            show trapper at slidetocenter
            tt "Perfect. You obviously have a modicum of taste and good judgement."
            tt "At least I hope you do. Guess we'll find out."
            $ trapperObj.change("emotion", "idle")
            $ trapperObj.change("pose", "close03")
            tt "Worst case, we'll find out how strong your bones are, how heavy you are pick up and throw, and how fast your lifeless body sinks. Should be pretty chill day, regardless."
            show trapper at slidetomoveright, fadeaway
            with dissolve
    $ imagechoice = False

    $ clauddwightObj.change("emotion", "scared")
    $ clauddwightObj.change("pose", "close02")
    show clauddwight with Dissolve(0.75)
    cl "Hold on…"
    dw "…for just one moment!"
    $ clauddwightObj.change("emotion", "idle")
    $ clauddwightObj.change("pose", "close01")
    nrr "This is Dwight and Claudette, our Activities Coordinators."
    nrr "They're also the cooks, waiters, bartenders, janitors, and every other job."
    $ clauddwightObj.change("emotion", "sad")
    nrr "They're the only help remaining on the island."

    nrr "This place we call… Murderer's Island. Cue dramatic musical flourish."
    play sound "sounds/sfx_signature_clauddwight04.ogg"
    $ clauddwightObj.change("pose", "pose01")
    nrr "None of the others survived-"
    nrr "Ahem, survived the interview process, I mean."
    $ clauddwightObj.change("emotion", "idle")
    nrr "Hence why we shall heretofore refer to them as Survivors with a capital \"S\"."
    nrr "These two have worked here a long time. So very long. I don't actually know how long it's been…"
    nrr "Sorry. Anyway, I should probably let Dwight and Claudette do their mandated jobs. They sure look happy, but they're vibrating with a nervous energy that is starting to give me the creeps."
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    dw "We will now escort the group to the venue of your choosing."
    $ clauddwightObj.change("emotion", "idle")
    cl "However, in the future we recommend waiting for us to present you with your options whenever possible, and don't just run off to various activities unsupervised."
    dw "We don;t have much autonomy around here."
    cl "The least you can do is allow us to do our job."
    
    $ clauddwightObj.change("emotion", "scared")
    dw "The most you could do is help us get off this isl-"
    $ clauddwightObj.change("pose", "pose01")
    cl "Dwight!"
    $ clauddwightObj.change("emotion", "happy")
    dw " Yes. Pardon me. Please follow us."
    show clauddwight with dissolve
    mc "Hey, Narrator?"
    nrr "Yes? Something I can help you with?"
    mc "Those two, Claudetter and Dwight… did they just start to mention something about wanting to escape? Is escape an option? Should I be trying to escape?"
    nrr "Escape? Them? Oh, no, no no no. I think you're mistaken."
    mc "It seemed like Dwight was asking for help to \"get off this island\" though."
    nrr "Oh, right, that. Yes, that's true, he was. But he just meant that he wanted to get to the other vacation island getaway. A couple miles south of here. It has much fancier accommodations than this island."
    nrr "It's one of those big corporate outfits, quite exclusive, where all the famous celebrities hang out. Very luxurious. Doesn't quite have the charm that this island has, though. Trust me, you wouldn't want to go there. With all that money comes a lot of restrictions."
    nrr "This is where you belong. Now now, off you go. It's time for an activity! On this island, your decisions matter–mostly. When I agree with them. Not like that other island…"
    
    $ imagechoice = True
    menu:
        nrr "So what'll it be?"
        "gui/menu_choice_bar_idle.png¦gui/menu_choice_bar_hover.png¦gui/menu_choice_bar_select.png":
            $ imagechoice = False
            call spiritch1
        "gui/menu_choice_beach_idle.png¦gui/menu_choice_beach_hover.png¦gui/menu_choice_beach_select.png":
            $ imagechoice = False
            call wraith_ch1
        "gui/menu_choice_volleyball_idle.png¦gui/menu_choice_volleyball_hover.png¦gui/menu_choice_volleyball_select.png":
            $ imagechoice = False
            call huntress_ch1
        "gui/menu_choice_yacht_idle.png¦gui/menu_choice_yacht_hover.png¦gui/menu_choice_yacht_select.png":
            $ imagechoice = False
            call trapper_ch1
return

label spirit_ch1:
    call blackscene
    call event_clauddwight
    call bardayscene
    $ spiritObj.change("pose", "close03")
    $ spiritObj.change("emotion", "happy")
    show spirit at slidetocenter
    ts "Finally! Freedom from the preposterous premise that the four of us would be engaged in some sort of thrilling two-on-two volleyball match."
    $ spiritObj.change("emotion", "idle")
    show spirit at slightzoom
    nrr "Spirit looks at you from beneath her gigantic sun hat. She takes a conspiratorial tone."
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("emote", "anger")
    ts "I don't know whose idea volleyball was in the first place, but I hate them."
    $ spiritObj.change("emote", "none")
    ts "I tried to feign a sprained ankle, but everyone already knows that I technically float above the foreund, so nobody believed I was even putting any pressure on my joints in the first place."
    ts "Then I tried to annoy everyone by not giving a crap, and when that didn;t work I tried whining, and when that didn't work…"
    $ spiritObj.change("emotion", "mad")
    $ spiritObj.change("emote", "sparks")
    $ spiritObj.change("pose", "close02")
    ts "I threatened to KILL EVERY SINGLE PERSON ON THIS ISLAND! But…"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    ts "It turns out I'm not the first to toss those kinds of threats around on this island."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("emote", "stars")
    ts "Sooooooooo thanks, I guess, for getting it called off."
    $ spiritObj.change("emote", "none")
    cl "Are we threatening to end each other again? Aha, ha, ha…"
    hide spirit
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "sad")
    show clauddwight
    with Dissolve(0.25)
    nrr "Now it's Dwight who takes on a conspiratorial tone, his eyes shifting as he slips into a loud whisper."
    $ clauddwightObj.change("pose", "close02")
    $ clauddwightObj.change("emotion", "scared")
    dw "Please! Just make it quick!"
    $ clauddwightObj.change("pose", "close01")
    cl "…"
    $ clauddwightObj.change("emotion", "sad")
    cl "…is what you'll be saying when we get behind the bar to make you the drink of your dreams!"
    $ clauddwightObj.change("emotion", "scared")
    dw "AHHHH!"
    $ clauddwightObj.change("emotion", "sad")
    cl "…"
    $ clauddwightObj.change("emotion", "happy")
    cl "…ahhhhhhhhhhhhhha ha ha ha! Hilarious, right? Right, Dwight?"
    $ clauddwightObj.change("pose", "close02")
    menu:
        dw "Yeah. Right. Right. So, what'll you be having?"
        "Vodka Soda":
            mc "Vodka Soda?"
            cl "Coming right up!"
            hide clauddwight
            $ huntressObj.change("emotion", "happy")
            $ huntressObj.change("pose", "close01")
            show huntress
            with Dissolve(0.25)
            th "Really takes me back home. You know, vodka is a very special drink to me. Warms the blood on a cold night in the woods. On occasion I would, hmmm, how do you say… bump into the occasional soldier while hiking acrss The Motherland."
            th "They always had a nip of vodka tucked away in a special little silver package in a special little hidden pocket."
            $ huntressObj.change("emotion", "idle")
            $ huntressObj.change("pose", "close02")
            th "…but no one hides from me."
            $ huntressObj.change("pose", "pose02")
            $ spiritObj.change("pose", "close02")
            $ huntressObj.change("emotion", "disgusted")
            $ spiritObj.change("emotion", "disgusted")
            show spirit at slidetomovecenterleft
            show huntress behind spirit at slidetomovecenterright
            ts "A bit basic to be drinking vodka on a tropical island, no? And you're mixing it with soda? Really?"
            ts "Being passionate about being passionless is so last year. It's also my thing and you're making it look bad. That's two strikes."
            hide spirit
            hide huntress
        "Sangria":
            mc "Something fruity, but refreshing. Hold the coconut rum. A sangria, maybe?"
            dw "My pleasure!"
            hide clauddwight
            $ wraithObj.change("emotion", "happy")
            $ wraithObj.change("pose", "close01")
            show wraith
            with Dissolve(0.25)
            tw "That sounds nice. We used to make drinks like that back home."
            tw "Well not, \"we,\" exactly. I watched someone drink a drink like that, once"
            $ wraithObj.change("emotion", "disgusted")
            $ wraithObj.change("emote", "dread")
            tw "They looked happy."
            $ wraithObj.change("emote", "none")
            mc "Now's your chance to be the one with the drink. What do you say?"
            $ wraithObj.change("pose", "pose01")
            $ huntressObj.change("emotion", "happy")
            $ huntressObj.change("pose", "pose01")
            show huntress at slidetomovecenterleft
            show wraith behind huntress at slidetomovecenterright
            th "This is some sort of juice for a child? Are there children hiding about?!"
            tw "No, it's for adults. The kind who like, you know, tropical fun."
            $ huntressObj.change("emotion", "sad")
            th "Oh… I see."
            nrr "Huntress really seemed to perk up at the idea of kids being around and is bummed to hear there aren't any, but I'm quite glad it's just grown-ups on this island, personally. Little ones should definitely not be exposed to this."
            $ huntressObj.change("emotion", "happy")
            th "Not my cup of tea, but OK, sure. We can still use it for a toast, yeah? To new adventures!"
            mc "To new friends!"
            $ wraithObj.change("pose", "pose02")
            $ wraithObj.change("emotion", "happy")
            tw "To, uhhh…"
            tw "*Clink*"
            $ huntressObj.change("emotion", "disgusted")
            $ huntressObj.change("emote", "question")
            th "Did you just say \"clink\"?"
            $ huntressObj.change("emote", "none")
            $ wraithObj.change("emotion", "disgusted")
            tw "No…"
            hide spirit
            hide huntress
        "Scotch, Rocks":
            mc "On a day like today? I could use something strong. Scotch on the rocks."
            nrr "Claudette uncorks a very expensive-looking bottle of top shelf liquor and pours you a glass."
            cl "Do enjoy!"
            hide clauddwight
            $ wraithObj.change("pose", "pose02")
            $ wraithObj.change("emotion", "disgusted")
            show wraith at movecenterleft
            with Dissolve(0.25)
            tw "Who would drink that? Smells like kerosene!"
            $ trapperObj.change("pose", "close01")
            $ trapperObj.change("emotion", "mad")
            $ trapperObj.change("emote", "exclamation")
            show trapper
            with Dissolve(0.25)
            tt "You need to embrace the burning!"
            $ trapperObj.change("emote", "none")
            $ wraithObj.change("emotion", "scared")
            $ wraithObj.change("emote", "sweat")
            tw "The… the burning?"
            $ wraithObj.change("emote", "none")
            $ trapperObj.change("pose", "pose01")
            $ trapperObj.change("emotion", "happy")
            tt "Oh yeah!"
            tw "Why would you embrace that? Burning is…"
            nrr "Wraith stifles a sob."
            $ wraithObj.change("emotion", "sad")
            tw "No… I can't even think about it…"
            $ wraithObj.change("emotion", "disgusted")
            $ trapperObj.change("emotion", "disgusted")
            tt "Well then don't. No skin off my back, you weirdo."
            $ trapperObj.change("pose", "close01")
            $ trapperObj.change("emotion", "idle")
            tt "Come to think of it…"
            $ trapperObj.change("pose", "close02")
            tt "Strong. Expensive. Better the longer you leave it locked in the basement…"
            $ trapperObj.change("emotion", "sparks")
            $ trapperObj.change("emotion", "happy")
            tt "Scotch is the best."
            $ trapperObj.change("emotion", "none")
            $ trapperObj.change("pose", "pose01")
            $ trapperObj.change("emotion", "idle")
            nrr "Trapper guzzles half the bottle and burps. It'd be disgusting if it wan't so… No, disgusting is exactly what it is." 

        "Virgin Daiquiri":
            mc "I didn't come here to party, I'm just trying to make the best of a… very strange situation. I dunno, how about a daiquiri?"
            dw "I know how to make that!"
            mc "But skip the liquor, I'll have mine virgin."
            hide clauddwight
            $ trapperObj.change("pose", "pose02")
            $ trapperObj.change("emotion", "happy")
            show trapper at moveright
            with Dissolve(0.25)
            nrr "Trapper snickers at your choice of words."
            tt "Sure you will, kid."
            $ spiritObj.change("emotion", "disgusted")
            $ spiritObj.change("emote", "dread")
            $ spiritObj.change("pose", "close01")
            show spirit at movebetweenmoveleftmovecenterleft with Dissolve(0.25)
            ts "Don't mind him, we don't need to soak ourselves in booze just to please someone else's expectations. If you ask me, there's enough Spirits here already."
            $ spiritObj.change("emote", "none")
            $ spiritObj.change("pose", "close02")
            $ spiritObj.change("emotion", "idle")
            ts "Besides, alchol just numbs you to the painful realities of the world--I choose to face them head-on."
            $ spiritObj.change("emotion", "disgusted")
            $ spiritObj.change("pose", "pose02")
            $ trapperObj.change("emotion", "question")
            $ trapperObj.change("pose", "pose01")
            tt "You'd never do something like, I don't know, hide from it all behind the world's largest hat, or anything."
            $ trapperObj.change("emote", "none")
            $ trapperObj.change("emotion", "disgusted")
            ts "Please allow me to ignore any fashion advice from the man wearing a doll's face as a mask."
            $ trapperObj.change("emotion", "mad")
            $ trapperObj.change("pose", "pose02")
            tt "…Not a doll's face. Jerk."
            hide spirit
            hide trapper
    show clauddwight
    with dissolve
    cl "Since we've fulfilled your requests…"
    $ clauddwightObj.change("pose", "close02")
    $ clauddwightObj.change("emotion", "happy")
    dw "It's time for you to return the favor!"
    mc "I should have known there was a catch…"
    cl "Ice-breaker time!"
    ts "I swear, had I known they'd pull this king of faux-enthusiastic community-building crap, I'd have suggested we attempt to walk to the lowest point of the ocean before I ever set foot near this bar."
    tw "You don't think it could be kinda fun? A little fun? Nevermind. I hate it. This sucks. But… it could be fine? Or whatever you say. Has anyone seen my hat?"
    nrr "I've literally never seen him in a hat."
    ts "If we must make small talk, I'm at least picking a topic before we end up being forced to do some lame improv game that nerds learn at their non-sports after-school activities that I definitely never did because I'm no nerd."
    nrr "Methinks a certain someone doth protest too much."
    ts "Sitting here on this beautiful sunny afternoon, warm sand beneath the fool fog beneath my severed feet…"
    ts "The topic I choose is books! Novels, comics, fiction or non. Reading is the only real escape from the inescapable horror of life–the escape into your own mind."
    nrr "A groan rolls through the crowd. Not a lot of readers here, I'd imagine, based on that response. They were much more enthusiastic about drinking."
    ts "Considering the situation we're in, it seems an appropriate time to ask you…"
    ts "[mc_name], what's your desert island book? The one book you'd bring with you if you were, well, on an island like this."
    ts "Oh, and it has to be classic horror. For reasons that should be obvious."
    nrr "She means because this is an island of horror villains. And also those books are all in the public domain."
    ts "Nothing too modern. Humanity has really gotten soft these past hundred years. So what's your favorite?"
        

return
label wraith_ch1:
    call blackscene
return
label huntress_ch1:
    call blackscene
return
label trapper_ch1:
    call blackscene
return