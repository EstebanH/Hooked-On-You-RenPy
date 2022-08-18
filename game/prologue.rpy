label prologue:
    mc "*cough* *cough* *cough*"
    nrr "You wake up on the beach, soaking wet, saltwater stinging the inside of your throat, as if you'd nearly drowned."
    nrr "Water falls from your mouth as you open it to gasp for air."
    nrr "You have no memory of how you got here. In fact, you can only remember your own name, but not where you came from, or a single fact about your life."
    nrr "What you do know is that, despite the outrageous beauty of the landscape around you, you feel incredibly sick to your stomach--"
    nrr "Wow, really went down the wrong pipe, huh? You need a minute, or can I go on?"
    mc "..."
    nrr "Because I can give you a minute. We've got plenty of time. Endless time, really."
    call oceanhaunting
    oc "An eternity, if you catch my drift."
    stop hauntloop fadeout 3.0
    nrr "Woah, not now, Ocean! Sorry, [mc_name]. May I continue?"
    call beachdayscene

    nrr "OK then. As I was--"
    mc "*cough* *cough*"
    nrr "AS I WAS SAYING."
    nrr "You look down at your feet, ankle-deep in the crystal blue water of a newly arrived wave."
    nrr "As the water recedes back into the ocean, it reveals a grotesque discovery!"

    call mood_inner_monologuescene("images/head_idle.png", ismovefrombottom = True)

    nrr "A decomposing face stares up at you from beneath the sand. All you can do is vomit--a stream of dark bile, bugs, worms, and other... ick."
    nrr "Questions race through your mind. Where are you? How did you get here? {i}Who is behind this incredibly charming and well-spoken voice in your head?{/i} However, answers don't come easy. Your mind... is completely blank."
    stop moodloop fadeout 3.0
    window hide
    scene bg beach_day with dissolve

    call event_choices
    menu:
        cho "What will you do?"
        "Run":
            scene black with dissolve
            nrr "You turn away from this wretched sight, and begin to run. But the beach, it's... endless. Despite how far you run, you get nowhere."
            scene bg beach_day with dissolve
            nrr "Exhausted, you stop and look behind you, your footsteps erased by soft blue waves. You turn inland, considering your lack of options, you've got no choice but to walk into the brush."
            nrr "However, the beauty of the beach is not shared by the darkness of the palmy woods before you. There's nothing inviting about that shadowy forest. Terror freezes you in your steps."
            stop choiceloop fadeout 3.0
            call oceanhaunting
            oc "Why are you trying to run away? This is paradise!"
            oc "You're here to enjoy yourself, don't you know? Have a little bit of fun. Take charge of your own experience."
            call beachdayscene
            stop hauntloop fadeout 3.0
            nrr "Well that was sure weird, that voice again. Do oceans normally talk? Your memory isn't right, but you're pretty sure you remember learning as a child that oceans do not speak directly to people in spooky terms."

        "Close your eyes":
            nrr "You close your eyes. This must be a nightmare, right?"
            scene black with dissolve
            mc "This is not happening. This is not happening."
            nrr "This mantra centers you, and you're briefly able to find peace."
            nrr "The lapping waves go silent, and for the first time in your entire life, it feels like you're in control."
            nrr "When you open your eyes..."
            stop choiceloop fadeout 3.0
            call mood_inner_monologuescene("images/head_coin.png", ismovefrombottom = True)
            nrr "You're in the exact same place. Except now, that disgusting corpse face is--is smiling at you?"
            stop moodloop fadeout 3.0
            call oceanhaunting
            oc "Even the dead have a wonderous time on your Island. I promise, you will too."
            oc "Don't worry, You're going to do just fine... We wouldn't want anyone else."
            call beachdayscene
            stop hauntloop fadeout 3.0
            nrr "Well that was sure weird, that voice again. Do oceans normally talk? Your memory isn't right, but you're pretty sure you remember learning as a child that oceans do not speak directly to people in spooky terms."

        "Dig up that face!":
            window hide
            call mood_inner_monologuescene("images/head_idle.png")
            pause 1
            nrr "You brush the sand away from the half-buried human head-embedded in the ground before you."
            window hide
            call mood_inner_monologuescene("images/head_coin.png")
            pause 1
            nrr "There is no body, just this head. As you pick it up, flakes of skin fall to the ground. The jaw falls open, revealing a gold coin sitting on the rotting tongue of this poor dead soul."
            
            stop choiceloop fadeout 3.0
            
            call oceanhaunting
            oc "Getting your hands dirty, I see. I like that... You're a take charge type."
            stop hauntloop fadeout 3.0
            window hide
            call oceanhaunting("images/coin.png", ismovefrombottom = True)
            pause 1
            stop hauntloop fadeout 3.0

            call beachdayscene(keep_images=True)
            call mood_speedlines("images/coin.png")

            nrr "You examine the gold coin briefly, happily distracted from what has otherwise been an extremely.... confusing morning."
            nrr "The sun beats down on you, drying your clothes. You check your pockets, but they're empty. Plenty of room for a gold coin, you suppose, and so you deposit it."
            hide speedlines
            stop moodloop fadeout 3.0
            call beachdayscene

            call event_choices
            menu:
                cho "Why that's a nice coin you've got there! What if you were to spend it right now?"
                "\"No, thanks\"":
                    ""

                "\"Why not?\"":
                    mc "Why not?"
            stop choiceloop fadeout 3.0

            call event_clauddwight
            show clauddwight
            $ clauddwightObj.change("pose", "close02")
            $ clauddwightObj.change("emotion", "happy")
            dw "Well hello, there! I'm Dwight!"
            cl "And I'm Claudette!"
            $ clauddwightObj.change("pose", "close01")
            play sound "sounds/sfx_signature_clauddwight01.ogg"
            cl "We'll take that!"
            $ clauddwightObj.change("emotion", "idle")
            nrr "Claudette quickly relieves you of your gold coin and tosses it to Dwight, who bites down on it like an old-timey prospector before handing it back to her."
            cl "And this..."
            dw  "...is for you!"
            window hide
            #scene bg excitement with dissolve
            stop eventloop fadeout 3.0

            call mood_excitement("images/skull.png", ismovefrombottom = True)
            pause 1
            nrr "Claudette presents you with a tropical drink."
            nrr "When you take a sip, you find that it's incredible. Money well spent, in your estimation."
            stop moodloop fadeout 3.0
            call beachdayscene
            call event_clauddwight
            menu:
                cho "But I gotta ask: Could somebody maybe design the next one of these dating sims to be all-inclusive? It really takes some of the fun out of a fantasy vacation to be watching your wallet the entire time."
                "Thank them for the delicious drink":
                    mc "Thanks for the drink. It's quite delicious!"

                "This is suspicious, spit that out!":
                    ""
            $ clauddwightObj.change("emotion", "happy")
            $ clauddwightObj.change("emote", "heart")
            $ clauddwightObj.change("pose", "far01")
            show clauddwight with Dissolve(0.2)
            pause 1
            cl "You're... welcome!"
            $ clauddwightObj.change("emote", "none")
            $ clauddwightObj.change("emotion", "sad")
            dw "Did someone just thank us?"
            cl "Go with it, Dwight. It's normal to be thanked for doing a good job. Trust me on this one."
            hide clauddwight with dissolve
            stop eventloop fadeout 3.0
            $ renpy.music.set_volume(1,3.0,"music")

    nrr "Your mind doesn't have a chance to linger any longer on your current situation, as you feel something soft bump into your foot."
    window hide
    call speedlinesredscene("images/volleyball.png", ismovefrombottom = True)
    pause 3
    nrr "When you look down, you find a volleyball sitting in the sand there next to you."
    nrr "You stare down, frozen. A voice calls out from behind you."
    th "Little help, please?"
    window hide
    stop moodloop fadeout 3.0
    call beachdayscene
    nrr "You turn around, and when you see what's waiting for you, your jaw just about hits the ground."
    window hide
    call mood_happy(scenedissolve = False)
    $ huntressObj.change("pose", "close01")
    show huntress
    with dissolve
    pause 4
    call mood_excitement(scenedissolve = False)
    $ wraithObj.change("pose", "close01")
    show wraith 
    with dissolve
    pause 4
    call mood_warmlight(scenedissolve = False)
    $ spiritObj.change("pose", "close01")
    show spirit
    with dissolve
    pause 4
    call mood_warmdark(scenedissolve = False)
    $ trapperObj.change("pose", "close01")
    show trapper
    with dissolve
    pause 4
    stop moodloop fadeout 3.0
    scene bg beach_day with dissolve
    pause 1
    window hide
    $ wraithObj.change("pose", "pose04")
    $ trapperObj.change("pose", "pose04")
    $ huntressObj.change("pose", "pose04")
    $ spiritObj.change("pose", "pose04")
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright
    with dissolve
    nrr "Four gorgeous monsters stand halfway between you and a well-tended volleyball court."
    nrr "Each of them oozes with undead energy, a magical aura reaching out and penetrating you. Via your eyes."
    nrr "Your heart begins to race. Curiousity. Fear. Desire. You can't help but stare at these casually dressed... let's call them Killers--I dunno, not to be judgemental but that's just the energy they put out there."
    nrr "So many competing feelings rush through your mind at once you are completely paralyzed."
    $ wraithObj.change("pose", "pose01")
    $ trapperObj.change("pose", "pose01")
    $ huntressObj.change("pose", "pose01")
    $ spiritObj.change("pose", "pose01")
    $ trapperObj.change("emote", "question")
    tt "Hello?"    
    $ trapperObj.change("emote", "none")
    show bg beach_day at Transform(matrixcolor=TintMatrix('#737373ff'))
    call show_item(image_name="images/volleyball.png", ismovefrombottom = True)
    hide huntress
    hide trapper
    hide wraith
    hide spirit
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright
    nrr "There are weird days, and then there's this. All you can do is look down at the ball and back up at this monstrous line-up of, wll, literal monsters. Sexy ass monsters, though."
    stop moodloop fadeout 3.0
    show bg beach_day at Transform(matrixcolor=TintMatrix('#ffffffff'))
    hide dreadnoise
    hide image_name
    with dissolve
    $ renpy.music.set_volume(1,3.0,"music")
    call event_hell
    menu:
        nrr "What do you do?"
        "Toss it back":
            nrr "You bend down and grab the ball. It's warm from sitting in the sand on this beautiful day."
            nrr "When you give the ball a toss, it arcs beautifully through the air and lands right in Huntress's hands."
            hide trapper
            hide wraith
            hide spirit
            $ huntressObj.change("pose", "close01")
            $ huntressObj.change("emotion", "happy")
            $ huntressObj.change("emote", "stars")
            show huntress at slidetocenter
            with Dissolve(0.25)
            th "Not bad, stranger."
            $ huntressObj.change("emote", "none")
            nrr "Huntress's muscles ripple as she grips it in her hand. You look her up and down and consider what it might be like to be held tightly in those strong arms. Warm, perhaps. Maybe a little sweaty, but that's OK--it's natural."
            $ huntressObj.change("emotion", "idle")
            $ huntressObj.change("pose", "pose01")
            $ spiritObj.change("emotion", "disgusted")
            show trapper at moveright
            show wraith at movecenterleft
            show spirit at movecenterright
            show huntress at slidetoleft
            with Dissolve(0.25)
            ts "Try hard much? Blech."
            nrr "They're speaking directly to you, but you still can't bring yourself to reply. You're entranced."
            call beachdayscene
            nrr "When you snap out of it, you realize that everyone has gone back to the volleyball court."
        "Kick it back":
            nrr "You swing your foot and awkwardly strike the volleyball, sending it bouncing across the sand towards Huntress."
            $ wraithObj.change("emotion", "disgusted")
            $ trapperObj.change("emotion", "disgusted")
            $ huntressObj.change("emotion", "disgusted")
            $ spiritObj.change("emotion", "disgusted")
            nrr "It.. doesn't make it all the way. Everyone stares at you, silently observing your unsportsmanlike shame."
            nrr "They must be wondering, have you ever even seen a volleyball before? That's surely what I'm wondering right now. It's not a soccer ball."
            hide huntress
            hide wraith
            hide spirit
            $ trapperObj.change("pose", "close01")
            $ trapperObj.change("emote", "spark")
            with Dissolve(0.25)
            tt "What a dork."
            $ trapperObj.change("emote", "none")
            $ trapperObj.change("pose", "pose01")
            $ wraithObj.change("emotion", "idle")
            $ trapperObj.change("emotion", "idle")
            $ huntressObj.change("emotion", "idle")
            $ spiritObj.change("emotion", "idle")
            show trapper at moveright
            show wraith at movecenterleft
            show spirit at movecenterright
            show huntress at moveleft
            $ wraithObj.change("emote", "stars")
            with Dissolve(0.25)
            nrr "You feel so awkward that you can barely see straight, but through the haze of your embarassment you catch Wraith looking at you from the corner of your eye."
            $ wraithObj.change("emote", "none")
            hide huntress with dissolve
            nrr "Huntress jogs the rest of the way to grab the volleyball, and they all turn and head back to the court."
            hide trapper
            hide wraith
            hide spirit
            with Dissolve(0.25)

        "Say \"No, thanks!\"":
            $ wraithObj.change("emotion", "disgusted")
            $ huntressObj.change("emotion", "disgusted")
            $ spiritObj.change("emotion", "disgusted")
            mc "No, thanks."
            nrr "Damn, what an alpha move. You just became the type of person who says \"no thanks\" to group of actual killers."
            hide huntress
            hide wraith
            hide spirit
            hide trapper
            call oceanhaunting
            with Dissolve(0.25)
            oc "No one tells you what to do..."
            call beachdayscene
            stop hauntloop fadeout 3.0
            $ huntressObj.change("pose", "close01")
            $ huntressObj.change("emote", "anger")
            show huntress at slidetocenter
            with Dissolve(0.25)
            th "Thanks for nothing, I guess?"
            $ huntressObj.change("emote", "none")
            $ wraithObj.change("emotion", "idle")
            $ trapperObj.change("emotion", "idle")
            $ huntressObj.change("emotion", "idle")
            $ spiritObj.change("emotion", "idle")
            show trapper at moveright
            show wraith at movecenterleft
            show spirit at movecenterright
            hide huntress
            with Dissolve(0.25)
            nrr "Huntress jogs over to collect the ball from the ground next to you. For someone so large, she moves deftly and silently across the sand."
            $ trapperObj.change("emotion", "happy")
            nrr "It's hard to make out his expression from behind the mask, but it seems like Trapper might be... smirking?"
            $ trapperObj.change("emotion", "idle")
            $ trapperObj.change("pose", "close01")
            hide wraith
            hide spirit
            show trapper at slidetocenter
            with Dissolve(0.25)
            nrr "As you try and read Trapper's face, you realize that the two of you have been staring into each other's eyes for a really long time, even though everyone else has headed back to the volleyball court."
            hide trapper with dissolve
            nrr "Finally, you can't take the tension, and you look down, breaking his gaze. As soon as you do, he turns to follow them."

        "Say nothing. Do nothing.":
            mc "..."
            $ wraithObj.change("emotion", "disgusted")
            $ huntressObj.change("emotion", "disgusted")
            $ trapperObj.change("emotion", "disgusted")
            nrr "You stand, frozen, in complete silence. It's... can I be honest with you? It's kind of a weird move."
            $ trapperObj.change("emotion", "mad")
            nrr "It's as if you truly don't care that someone asked you politely. You're doing you, despite how much of a weirdo or just a jerk it might make you look like. Clearly you don't even care!"
            nrr "Is this some kind of display of confidence? Confusion? Sheer awkwardness? You feel judged, but you're not sure how."
            $ spiritObj.change("emotion", "happy")
            $ spiritObj.change("emote", "sweat")
            $ spiritObj.change("pose", "pose03")
            nrr "Spirit cuts the silence with a giggle that she quickly swallows when she sees that it caught your attention."
            $ spiritObj.change("emote", "none")
            $ spiritObj.change("emotion", "idle")
            hide huntress
            hide wraith
            hide trapper
            with Dissolve(0.25)
            nrr "Huntress jogs over to collect the ball from the ground next to you before heading back to the volleyball court with everyone else."
            $ trapperObj.change("pose", "close03")
            $ spiritObj.change("emotion", "mad")
            show spirit at slidetocenter
            with Dissolve(0.25)
            nrr "Except for Spirit. She's really staring you down, her expression hardening as you watch her. The longer you hold her gaze, the more angry she seems to become before turning with a huff and floating off to join the others."

    nrr "Alone again, you look across the beach at these strange residents who casually bat a volleyball back and forth, happily ignoring your intrusion onto their private beach."
    nrr "Should you be frightened? Worried? Excited? I did refer to them as Killers, not to give too much away."
    nrr "But at the same time, damn, they are looking very appealing in their own way, and nobody so much as lifted a blood-soaked finger in your direction."
    call oceanhaunting
    oc "Don't be scared, [mc_name]. You were made for this."
    nrr "Well jeez. If the spooky Ocean-voice says not to be scared, I'm sure it's all going to work out."
    call beachdayscene
    stop hauntloop fadeout 3.0
    nrr "With no good reason not to, you decide to head over and see what happens next."
    
    $ quick_menu = False
    scene black with dissolve
    pause 1
    return