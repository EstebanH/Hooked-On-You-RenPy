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
            ""

        "Close your eyes":
            ""

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
    $ trapperObj.change("emote", "none")
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
            nrr "Huntress's muscles ripple as she grips it in her hand. You look her up and down and consider what it might be like to be held tightly in those strong arms. Warm, perhaps. Maybe a little sweaty, but that's OK--it's natural."
            $ huntressObj.change("emote", "none")
            $ huntressObj.change("emotion", "idle")
            $ huntressObj.change("pose", "pose01")
            $ spiritObj.change("emotion", "disgusted")
            show trapper at moveright
            show wraith at movecenterleft
            show spirit at movecenterright
            show huntress at slidetoleft
            with Dissolve(0.25)
            ts "Try hard much? Blech."
        "Kick it back":
            ""
        "Say \"No, thanks!\"":
            ""
        "Say nothing. Do nothing.":
            ""
    nrr "They're speaking directly to you, but you still can't bring yourself to reply. You're entranced."
    call beachdayscene
    nrr "When you snap out of it, you realize that everyone has gone back to the volleyball court."
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