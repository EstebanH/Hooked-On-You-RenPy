label chapter02:
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
    call mood_excitement(withDissolve = False)
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
        if meatcarving_section == 1:
            call end_meatcarving_minigame
            $ meatcarving_perfects = meatcarving_perfects + 1
            nrr "Perfect!"
        elif meatcarving_section == 2:
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
    $ clauddwightObj.change("pose", "close01")
    $ clauddwightObj.change("emotion", "disgusted")
    dw "For real."
    hide clauddwight with Dissolve(0.25)
    nrr "The sounds, especially coming from the masked killers while they eat (which involves lifting their masks and shoving food up behind them) are {i}nasty{/i}."
    nrr "Spirit, meanwhile, doesn't even eat. She's the only one who seems to really be embracing being dead. They're all dead, right? This is obviously hell? I mean--"
    call oceanhaunting
    oc "Come on. We're still trying to be mysterious, here. You think mystery comes easy? Claudette and Dwight aren't the only ones who've been working their asses off to make this night perfect."
    stop hauntloop fadeout 3.0
    nrr "Well, at least they're lifting their masks. This is only 99% as disgusting as it could be if they just tried to mash stuff through there."
    mc "Spirit, why aren't you hungry?"
    $ spiritObj.change("pose","pose03")
    $ spiritObj.change("emotion","idle")
    show spirit
    ts "The two best things about being dead is not having to eat."
    mc "That's only one thing."
    $ spiritObj.change("pose","close03")
    $ spiritObj.change("emotion","disgusted")
    $ spiritObj.change("emote","lightbulb")
    ts "Think about it, [mc_name]. Number two... is no number two. One less thing to think about in the afterlife."
    $ spiritObj.change("emote","none")
    ts "Even if I wanted to eat I have no idea what would actually follow."
    ts "You might have noticed, but I'm mostly just a brunch of dismembered body part floating in a spectral form."
    $ spiritObj.change("emote","sweat")
    $ spiritObj.change("emotion","happy")
    ts "Do you see how deep this cut on my abdomen is? I don't think my digestive tract connects anymore."
    $ spiritObj.change("emote","none")
    show spirit at slidetomovecenterright, fadeaway
    nrr "Between the food and the behavior of the group this might be the worst meal in history."
    hide spirit
    $ wraithObj.change("emotion", "disgusted")
    $ trapperObj.change("emotion", "disgusted")
    $ huntressObj.change("emotion", "disgusted")
    $ spiritObj.change("emotion", "disgusted")
    $ wraithObj.change("pose", "pose01")
    $ trapperObj.change("pose", "pose01")
    $ huntressObj.change("pose", "pose01")
    $ spiritObj.change("pose", "pose01")
    show huntress at moveleft
    show trapper at moveright
    show wraith at movecenterleft
    show spirit at movecenterright
    nrr "But evem worse is they're staring at you. You're not eating. They don't like that."
    menu:
        nrr "I think they want an explanation why. What do you want to tell them?"
        "\"This is gross.\"":
            mc "This is gross."
        "\"I'm sorry.\"":
            mc "I'm sorry."
        "\"Look at that seagull!\"":
            mc "Wow! You ever see a seagull that big? I haven't! That's incredible! Anyway, what were we talking about?"
            th "Lame misdirect."
            ts "Yeah, she's right, [mc_name]. Pretty lame. Own who you are. Never compromise."
            $ trapperObj.change("emotion", "idle")
            $ trapperObj.change("emote", "question")
            tt "Didn't you wash up on this island with no memory of who you are and how you got here?"
            $ trapperObj.change("emote", "none")
            $ wraithObj.change("emotion", "sad")
            tw "Yes. You did. Poor thing."
            $ trapperObj.change("emotion", "disgusted")
            tt "You have no idea the last time you ate a real meal. And you've been standing in the sun."
            mc "But the seagull..."
    nrr "Uh oh. He just made a lot of good points."
    mc "I swear..."
    nrr "You're beginning to feel light headed."
    mc "It waved at me..."
    show bg towel_day at Transform(matrixcolor=TintMatrix('#737373ff'))
    nrr "Maybe you need to eat to survive here."
    nrr "Either that or someone poisoned you."
    stop moodloop fadeout 3.0
    stop eventloop fadeout 3.0
    scene black with dissolve
    nrr "No, wait. You haven't eaten, so you can't be poisoned. Hmm... Whatever the answer, you're cleatly about to pass out."
    call oceanhaunting
    oc "Oh hey, it's me again!"
    oc "Your friend, mentor, and guide. Narrator to The Narrator, {i}The Ocean{/i}."
    nrr "Not sure how I feel about that characterization, but I'll allow it."
    oc "I brought you here. And I might be the only one who can help you now."
    oc "There's only one thing you must do to survive: you have to figure out why you're really here."
    oc "No one can tell you. Not unless you follow the right path. Or at least \"a\" right path."
    oc "There's too many of those to count. Hopefully you pick at least one of them."
    oc "Because there are even more wrong paths. Many of them lead to your demise. Others lead to something even worse."
    nrr "Starting scenes over and having to fast-forward back to where you were, amiright???"
    oc "For this place holds many secrets. Even from itself. But the one that truly matters can only be learned if you answer the most important question:"
    oc "Why are you here?"
    oc "{i}Why are you here?{/i}"
    oc "Answer that and you'll learn the truth."
    oc "The ultimate truth."
    stop hauntloop fadeout 3.0
    scene black with dissolve
    nrr "Vague. Mysterious. I gotta give it up to this Ocean character. That's some quality early-game storytelling."
    call oceanhaunting
    oc "Hold on, I'm back."
    oc "One more piece of advice. You've made many choices by now. Some of them I liked, some of them I did not."
    oc "It's in your best interest to make more choices that I like."
    stop hauntloop fadeout 3.0
    call beacheveningscene 
    with dissolve
    nrr "You wake up to find Spirit holding your limp body, gingerly pouring cool water into your mouth."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close03")
    call mood_romantic(withDissolve = False)
    show spirit
    with dissolve
    ts "Don't you just love the ocean at night? I do..."
    $ spiritObj.change("emotion", "mad")
    $ spiritObj.change("emote", "sparks")
    ts "Staring out over the vast darkness of the ocean really validates the feelings inside me that we're all truly insignificant AND THE ONLY THING WORTH PURSUING IS REVENGE."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    ts "I have to wonder, how could anyone believe anything else?"
    nrr "You look out into the darkness of night and ponder her question."
    $ spiritObj.change("emote", "question")
    $ spiritObj.change("emotion", "happy")
    menu:
        ts "Well? It's a simple question. How could they? How could anyone not feel small and alone in the face of such massive nothingness?"
        "You're always been alone":
            $ spiritObj.change("emote", "none")
            mc ""
        "You found someone special":
            $ spiritObj.change("emote", "none")
            mc "I used to feel that way. Small, unimportant, alone. But lately, I'm not so sure."
            mc "I've started to feel different. I've started to actually think that maybe this island is where I might meet someone special."
            nrr "You look at Spirit, who has turned from the ocean to look at you while you speak on this topic she's clearly so passionate about."
            mc "A friend, perhaps something more? I don't know what this island has planned for me."
            $ spiritObj.change("emote", "exclamation")
            $ spiritObj.change("emotion", "digusted")
            ts "Hah! A \"friend?\" Friends are just cowards who seek comfort in numbers!"
            $ spiritObj.change("emote", "none")
    call beacheveningscene 
    stop moodloop fadeout 3.0
    with dissolve
    ts "I had friends, once. Back before I was chopped into a bunch of pieces by my father!"
    $ spiritObj.change("emote", "sparks")
    $ spiritObj.change("pose", "close02")
    $ spiritObj.change("emotion", "mad")
    ts "Friends aren't what's keeping me held together, I'm floating in a cloud of rage!"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "digusted")
    $ spiritObj.change("pose", "close03")
    call event_bloodconfident
    ts "Ugh, I was so dumb! So busy trying to please everyone and be the perfect student, the perfect employee, the perfect daughter, I didn't take care of myself! And now I'm all I've got."
    ts "Worse of all, I got distracted from my true purpose. My destiny! The purpose that was sitting inside me my whole life."
    $ spiritObj.change("emotion", "idle")
    ts "Ok, so, this might sound a bit silly, but..."
    nrr "Spirit looks around to see if there's anyone else on the beach. When she's convinced that it's only you two, she continues."
    $ spiritObj.change("pose", "pose03")
    ts "There's a dragon that lives inside me. I've always known, but I've tried to ignore it. When I couldn't ignore it, I tried to push it down. I'm so stupid!"
    mc "You're not stupid, that sounds badass!"
    $ spiritObj.change("emotion", "happy")
    ts "Right??? But I didn't let it out, and then I, ya know... CHOP CHOP... and now that dragon is pretty much a one-track revenge beast."
    $ spiritObj.change("pose", "pose01")
    menu:
        ts "But enough about me... what's inside of you, stranger?"
        "Nothing but darkness":
            mc "I'd kill to have a dragon--"
            nrr "Maybe not the best choice of words."
            mc "I mean, a dragon sounds {i}awesome{/i}. Honestly, though, I don't feel like I've got anything inside me at all. Just... darkness, never ending darkness."
            nrr "And here I thought Spirit was the biggest goth on the island until YOU arrived!"
            $ spiritObj.change("emotion", "happy")
            $ spiritObj.change("emote", "stars")
            ts "Perhaps I could light a torch and search through that darkness..."
            $ spiritObj.change("emote", "none")

        "No dragon, just a lot of fire":
            mc ""
    hide spirit with Dissolve(0.25)
    nrr "Just as things are really heating up, you hear a flurry of footsteps behind you and you quickly spin around, ready to fend off whatever new danger has popped up on this strange island..."
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "disgusted")
    show clauddwight
    show speedlines
    with dissolve
    nrr "...only to find that it's Dwight and Claudette sprinting across the beach, clipboards in hand which they're waving in the air above their heads."
    dw "It's very important that we stick to the itinerary!"
    $ clauddwightObj.change("emotion", "happy")
    cl "And attend each event as scheduled!"
    $ clauddwightObj.change("pose", "close01")
    $ clauddwightObj.change("emotion", "disgusted")
    dw "Playing sick for cute flirt points was {i}not{/i} a part of this evening's activites."
    $ clauddwightObj.change("emotion", "mad")
    cl "That's strictly slotted in for {i}after{/i} campfire storytime. At this rate we'll be late!"
    mc "Playing sick? No, I was--"
    $ clauddwightObj.change("emotion", "happy")
    dw "No time for excuses."
    cl "Well, there is, but that's scheduled for after what comes after the flirting."
    $ clauddwightObj.change("pose", "close02")
    dw "GO GO GO GO!"
    call blackscene
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