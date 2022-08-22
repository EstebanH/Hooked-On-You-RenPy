label chapter2:
    call towelscene
    call event_dinner
    mc "Seems like the next activity is...meal-time? How quaint."
    nrr "You were expecting, what? Capture the flag? Do you know how complicated it is to run a game like that? Much moreso than sitting and talking."
    nrr "You arrive at the cookout area to find an assortment of picnic tables scattered around."
    nrr "What were you expecting, some kind of grand hall with a huge banquet table? This ain't some prestigious fantasy epic like you'd find on cable."
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "idle")
    show clauddwight with dissolve
    nrr "Dwight and Claudette usher you to your seat, but there's very limited seating directly around you."
    nrr "And--ohh great--{i}terrific{/i}. It seems that everyone wants to sit next to you."
    $ wraithObj.change("pose", "pose01")
    $ trapperObj.change("pose", "pose01")
    $ huntressObj.change("pose", "pose01")
    $ spiritObj.change("pose", "pose01")
    $ wraithObj.change("emotion", "idle")
    $ trapperObj.change("emotion", "idle")
    $ huntressObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    $ wraithObj.change("emote", "none")
    $ trapperObj.change("emote", "none")
    $ huntressObj.change("emote", "none")
    $ spiritObj.change("emote", "none")
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright
    with Dissolve(0.25)
    nrr "Even better is that they don't want to sit next to certain other people either."
    $ trapperObj.change("emotion", "disgusted")
    nrr "To start, no one wants to sit next to Trapper."
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("emote", "anger")
    $ wraithObj.change("emotion", "disgusted")
    nrr "Meanwhile, he refuses to sit next to Wraith or Trickster."
    call speedlinebg_blue
    $ tricksterObj.change("emotion", "idle")
    $ tricksterObj.change("pose", "close02")
    show trickster
    nrr "Oh yeah, Trickster is here. Surprised? Yeah well, they don't call him... Expected-ster? I'm sorry, even I get nervous around crowds (of Killers) and my whole schtick gets a little flustered."
    $ tricksterObj.change("emote", "heart")
    $ tricksterObj.change("emotion", "happy")
    $ tricksterObj.change("pose", "close01")
    tr "Hey there. You're looking good, Esteban. Real good."
    $ tricksterObj.change("emote", "none")
    $ tricksterObj.change("emotion", "idle")
    $ tricksterObj.change("pose", "pose01")
    $ huntressObj.change("emotion", "disgusted")
    $ trapperObj.change("emotion", "disgusted")
    $ wraithObj.change("emotion", "idle")
    hide trickster
    stop moodloop fadeout 3.0
    call towelscene
    call event_dinner
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright
    show trickster
    with Dissolve(0.25)
    nrr "And we literally can't let Huntress and Trapper sit together."
    nrr "No, seriously. Their arms are too big. They can't fit at the table if they sit side-by-side."
    $ huntressObj.change("emotion", "idle")
    $ trapperObj.change("emotion", "idle")
    nrr "Look at this. We can't even fit everyone on screen at the same time. You probably think it was an error, but it's not. It was completely intentional."
    nrr "Let that be a lesson to you: Every error you {i}think{/i} you see is a choice. Got that?"
    hide huntress
    hide trapper
    hide wraith
    hide spirit
    hide trickster
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    show clauddwight
    with Dissolve(0.25)
    nrr "Okay, Dwight and Claudette are directing traffic. You sit on one side. The rest of them will sit opposite you."
    nrr "Huntress and Trapper can sit at the ends with their enormous sexy arms."
    $ clauddwightObj.change("pose", "close01")
    dw "Now that everyone is seated, we can begin dinner."
    $ clauddwightObj.change("emotion", "sad")
    cl "Tonight's meal was prepared slowly and carefully with both love and hate for 12 hours over a spit."
    dw "We hope you all enjoy. We really, really hope you do."
    $ spiritObj.change("emote", "exclamation")
    ts "Hey! You didn't actually tell is what you're serving. What are we eating?"
    $ spiritObj.change("emote", "none")
    $ clauddwightObj.change("emotion", "idle")
    call mood_excitement(scenedissolve = False)
    show clauddwight
    with Dissolve(0.25)
    dw "It's meat."
    cl "Seasoned with a {i}specific number{/i} of special herbs and spices that we simply can't divulge."
    stop moodloop fadeout 3.0
    $ trapperObj.change("emote", "heart")
    $ huntressObj.change("emotion", "happy")
    $ trapperObj.change("emotion", "happy")
    $ wraithObj.change("emotion", "disgusted")
    tt "My favorite!"
    $ trapperObj.change("emote", "none")
    $ huntressObj.change("pose", "pose03")
    th "Meat is good."
    $ wraithObj.change("emote", "dread")
    $ huntressObj.change("emotion", "disgusted")
    $ trapperObj.change("emotion", "disgusted")
    tw "Meat is murder."
    $ wraithObj.change("emote", "none")
    $ spiritObj.change("emote", "question")
    $ spiritObj.change("emotion", "disgusted")
    ts "Which you'd know, considering what you've been up to. Who are you to get judgey now?"
    tw "I'm just... I'm just sharing... facts. And you need to murder something to eat its meat, so that's, like, technically true."
    $ trapperObj.change("emote", "exclamation")
    $ trapperObj.change("emotion", "happy")
    $ spiritObj.change("emotion", "idle")
    tt "Technically true is the best kind of true."
    $ trapperObj.change("emote", "none")
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("emote", "sparks")
    $ wraithObj.change("pose", "pose03")
    $ wraithObj.change("emotion", "idle")
    th "Okay, enough yapping! Let's eat!"
    $ trapperObj.change("emote", "none")
    $ trapperObj.change("emotion", "idle")
    nrr "Hey, Esteban, you thinking what I'm thinking?"
    nrr "It's gonna be a person on that spit, right? Or several parts of overlapping people, perhaps..."
    nrr "I haven't seen many pigs wearing palm-tree button down prints, you know?"
    nrr "When you look closely at the spit, you spot what definitely appears to be scraps of fabric sandwiched between some layers of meat."
    $ huntressObj.change("emotion", "disgusted")
    $ trapperObj.change("emotion", "disgusted")
    mc "I'm going to be sick. Is there anything else to eat?"
    $ clauddwightObj.change("emotion", "disgusted")
    $ clauddwightObj.change("pose", "pose01")
    show clauddwight
    cl "This took 12 hours."
    dw "And we do literally everything on this island."
    hide clauddwight
    $ trapperObj.change("emotion", "happy")
    $ trapperObj.change("pose", "pose02")
    with Dissolve(0.25)
    tt "Actually, there's one thing you're not doing today. You're not carving up this delectable meal."
    hide huntress
    $ trapperObj.change("emotion", "idle")
    $ huntressObj.change("emotion", "happy")
    $ huntressObj.change("pose", "close02")
    show huntress at moveleft
    show huntress at slidetomovecenterleft
    th "Wow, he's right for a change. Cause {i}I{/i} am with my broad axe. It's the perfect tool for easily chopping anything in twain."
    $ trapperObj.change("emote", "question")
    $ trapperObj.change("emotion", "disgusted")
    $ huntressObj.change("emotion", "disgusted")
    $ huntressObj.change("pose", "pose02")
    show huntress behind wraith at slidetomoveleft
    hide trapper
    $ trapperObj.change("pose", "close02")
    show trapper at moveright
    show trapper at slidetocenter
    tt "First, who says twain? Sometimes I swear it's like we're all from completely different historical eras. Second, I'll handle this with my cleaver. Fast, powerful, and clean. At least it's clean when the meat is cooked. No blood."
    hide spirit
    $ trapperObj.change("emote", "none")
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emote", "sparks")
    show trapper at slidetomoveright
    show spirit
    ts "Ugh! You two and your ridiculous bicep-swinging contest. Enough! GROW UP!"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close02")
    ts "Obviously my gorgeous katana is the ONLY OPTION. Obvs."
    $ trapperObj.change("emote", "anger")
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("pose", "pose01")
    tt "The hell it is!"
    $ trapperObj.change("emote", "none")
    $ spiritObj.change("emotion", "mad")
    ts "Oh I'll show you both my katana and send you to actual hell if you'd like."
    hide wraith
    $ spiritObj.change("pose", "pose02")
    show spirit at slidetomovecenterright
    $ wraithObj.change("pose", "close01")
    $ wraithObj.change("emote", "sweat")
    $ wraithObj.change("emotion", "disgusted")
    show wraith at movecenterleft
    show wraith at slidetocenter
    tw "Please stop. Please. I hate when we fight. Or talk. Or even when we look at each other in the eye."
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("pose", "close02")
    $ wraithObj.change("emotion", "mad")
    tw "I can do it. I have the skull of Azarov."
    $ huntressObj.change("emote", "anger")
    $ wraithObj.change("emotion", "disgusted")
    th "Great, instead of slicing it up you can club it to a second death."
    $ huntressObj.change("emote", "none")
    hide huntress
    show huntress at moveleft
    hide trapper
    show trapper at moveright
    hide wraith
    show wraith
    show wraith at slidetomovecenterleft
    hide spirit
    show spirit at movecenterright
    nrr "Hey, Esteban, I know this isn't what you want to eat. But hurry up and volunteer to carve up Felix... I mean\"dinner.\""
    nrr "Otherwise this will go on for hours. No hyperbole. They once argued who had the most effective weapons for 72 straight hours. "
    nrr "And it doesn't matter which one does it. When they're done they will take even longer cleaning their weapon, all while explaining the value in maintaining your tools."
    nrr "Despite being a brunch of cold-blooded Killers, for some reason they're always terrified of tetanus."
    mc "Hey, why don't you just let me carve up... dinner."
    hide huntress
    hide trapper
    hide wraith
    hide spirit
    show clauddwight
    with Dissolve(0.25)
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "happy")
    dw "Splendid idea. We'd hate for it to get cold."
    $ clauddwightObj.change("emotion", "sad")
    cl "He hated when it got cold."
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "idle")
    dw "Here's a machete. Freshly sharpened."
    call instructions_meatcarving
    nrr "Away we go!"
    nrr "Slice!"
    while (int(meatcarving_turn) < 5):
        call start_meatcarving_minigame
        if spinthebottle_section == 1:
            call end_meatcarving_minigame
            $ meatcarving_perfects = meatcarving_perfects + 1
            nrr "Perfect!"
        elif spinthebottle_section == 2:
            call end_meatcarving_minigame
            $ meatcarving_good = meatcarving_good + 1
            nrr "Not bad..."
        else:
            call end_meatcarving_minigame
            nrr "You missed completely!"
        $ meatcarving_turn = meatcarving_turn + 1
        $ meatcarving_speed = meatcarving_turn + 1
    if meatcarving_perfects == 5:
        ##Perfect
        call mood_excitement
        $ trapperObj.change("pose", "pose03")
        $ trapperObj.change("emotion", "disgusted")
        $ trapperObj.change("emote", "stars")
        show trapper
        tt "{i}Shit.{/i} Flawless. That was possibly the sexiest thing I've ever seen that didn't involve a dismemberment. Maybe we should skip dinner."
        $ trapperObj.change("emote", "none")
        stop moodloop fadeout 3.0
        call oceanhaunting
        oc "Settle down... Let's not get ahead of ourselves. And remember OHM, don't show all yours cards just yet. You don't want them to expect anything..."
        stop hauntloop fadeout 3.0
    elif meatcarving_good > 1:
        ##Good
        call mood_warmlight
        $ spiritObj.change("pose", "pose02")
        $ spiritObj.change("emotion", "idle")
        $ spiritObj.change("emote", "stars")
        show spirit
        ts "That was pretty good. I'd like to see what you could do with a less clumsy weapon. Yeah. I said it. Machetes are dumb!"
        $ spiritObj.change("emote", "none")
        stop moodloop fadeout 3.0
    elif (meatcarving_good == 1) and (meatcarving_perfects == 0):
        ##Bad 1/5
        call mood_mystery
        $ wraithObj.change("pose", "close01")
        $ wraithObj.change("emotion", "idle")
        show wraith
        tw "It's okay. At least you tried. A little. Sometimes trying a little takes a lot of effort."
        hide wraith
        $ huntressObj.change("pose", "close01")
        $ huntressObj.change("emotion", "mad")
        $ huntressObj.change("emote", "anger")
        show huntress
        with Dissolve(0.25)
        th "What the hell was that? You ruined dinner! Your swinging was so poorly aimed, you hacked it to pieces. The bad kind of pieces, too. I hope you're drunk."
        $ huntressObj.change("emote", "none")
        hide huntress at slidetomoveleft, fadeaway
        stop moodloop fadeout 3.0
    else:
        ##Missed Completely
        call oceanhaunting
        oc "Perfect! You know just when to play the part of harmless. They'll never see you coming..."
        stop hauntloop fadeout 3.0
        stop moodloop fadeout 3.0
        call event_dinner
        call towelscene
        $ clauddwightObj.change("pose", "close02")
        $ clauddwightObj.change("emotion", "idle")
        show clauddwight
        cl "Dinner is finally served."
        dw "For real."

    return

init python:
    meatcarving_perfects = 0
    meatcarving_good = 0
    meatcarving_turn = 0

label instructions_meatcarving:
    show emptyspin at top
    nrr "Minigames consist of two parts! On top, a pointer which rotates in a clockwise direction."
    hide emptyspin
    show targetspin at top
    nrr "And on the bottom, a target you're going to be pointing at."
    nrr "Sometimes the target is immediately visible, sometimes it's hidden until the pointer arrives."
    nrr "Press the spacebar to stop the pointer while over the target to win! Fail to land on the target and you will lose."
    nrr "To achieve a {i}perfect{/i} success, land on the start of the target area, not the end."
    hide targetspin
    menu:
        cho "Ok, ready to play? Or would you like me to repeat that?"
        "Ready":
            mc "Ready!"
        "Repeat the instructions":
            mc "Would you please repeat the instructions?"
            nrr "My pleasure!"
            call instructions_spinbottle
    return