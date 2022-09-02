label chapter04:
    call poolnightscene
    call event_papercutbolsa
    nrr "It's just the right temperature for an eventing dip. Plus, if some jealous shark comes along and manages to jump from the ocean into the pool, you're also pretty sure your Killer companion could handle it."
    $ spiritObj.change("pose","pose01")
    $ spiritObj.change("emotion","disgusted")
    $ spiritObj.change("emote","dread")
    show spirit with dissolve
    ts "I just want to be totally clear, even through that story bore {i}some{/i} similarities to my life, it was not about me in any way, shape, or form. Not symbolically, not metaphorically, not any other-ically"
    $ spiritObj.change("emote","none")
    mc "I believe you, completely. Sure, you were cut into pieces in your life, and so was the person in the story."
    $ spiritObj.change("emotion","idle")
    ts "A perfectly normal coincidence."
    mc "Sure, you're on this island, trapped one might say, in a most puzzling place."
    $ spiritObj.change("emotion","happy")
    ts "Also a completely regular coincidence."
    $ spiritObj.change("emotion","idle")
    mc "And sure, his lips were blue, your lips are blue."
    $ spiritObj.change("emote","question")
    $ spiritObj.change("pose","close03")
    $ spiritObj.change("emotion","happy")
    ts "Really? You'd call this blue?"
    $ spiritObj.change("emote","none")
    mc "Searching for answers. Hoping to find..."
    $ spiritObj.change("emote","sparks")
    $ spiritObj.change("pose","close02")
    $ spiritObj.change("emotion","mad")
    ts "... {i}Revenge{/i}"
    $ spiritObj.change("emote","none")
    mc "Ok, so the similarities stop there,, I guess."
    ts "Coincidences."
    mc "Sorry, the coincidences."
    $ spiritObj.change("emotion","disgusted")
    ts "Get this through your head, whoever you are:"
    ts "Samurai blood runs through my veins. Or, well, maybe it has coagulated by now... No need to sweat the details. REGARDLESS. I'm a descendent of noble warriors."
    $ spiritObj.change("emotion","idle")
    ts "Thousands of years of training with bladed weapons preceded my entrance into this world."
    ts "Do you know many many swords that is? A lot. You've gotta figure that with that many sharp edges, a person is bound to get disconnected from a body part here and there."
    ts "The {i}truth{/i} is, and I wouldn't typically share this so don't go blabbing about it..."
    $ spiritObj.change("emotion","sad")
    $ spiritObj.change("pose","close01")
    ts "I dreamt that story, like watching a movie in my sleep, when I was just a little girl. Years before my father sunk his blade into my skin."
    ts "I've never been able to shake it..."
    mc "That's a very adult story for a child to dream."
    $ spiritObj.change("emotion","idle")
    $ spiritObj.change("pose","pose01")
    menu:
        ts "Do you believe me?"
        "Yes":
            mc "I know we just met, but... yes, I do believe you. The way you told that story, it clearly came from someplace deep."
            $ spiritObj.change("emotion","mad")
            $ spiritObj.change("emote","sparks")
            ts "{i}FOOL!{/i}"
            $ spiritObj.change("emote","none")
            $ spiritObj.change("emotion","disgusted")
            ts "Who taught you to trust a stranger?! You're going to get hurt if you don't learn to take better care of yourself."

        "No":
            mc ""
        "Who cares?":
            $ spirit_aff = spirit_aff + 1
            mc ""
    nrr "Now you've got me wondering, do I believe you if you believe her or not?"
    nrr "And if I know everything, because trust me I do know everything, don't I already know the answer to my own question about if I believe your answer to Spirit's question?"
    nrr "... woah..."
    nrr "Ocean air got me {i}trippin'{/i}."
    nrr "Sorry, I didn't mean to distract us both. What's important is that a certain corpse cutie floating in a cloud of magical mist might still be waiting for you to say the right thing and free her from her puzzle box... if you believe that she is the--damnit, got me going again!"
    nrr "Unfortunately, before you can follow this conundrum to what will surely be a mind-numbing cycle of new questions..."
    nrr "...you find a certain two someones standing before you with a fresh towel, ready to dry you off."

    show spirit at slidetomovecenterright
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    show clauddwight behind spirit at movecenterleft
    with Dissolve(0.25)
    cl "Sorry, kids."
    dw "But it's time for bed!"
    $ clauddwightObj.change("emotion", "idle")
    $ clauddwightObj.change("pose", "pose01")
    $ spiritObj.change("emotion","idle")
    ts "I might be the youngest one here, but I'm no kid! I do, however, love being wrapped up in a fresh clean towel."
    ts "My mother used to help me wash my hair when I was young. She'd comb out all of the tangles and tie a ribbon around it before sending me on my way. I miss her."
    $ spiritObj.change("emotion","sad")
    $ spiritObj.change("pose","close01")
    nrr "You watch as Spirit stares off into the distance, her hand gripping into a tight fist. She doesn't notice you're watching her, at first."
    hide spirit with dissolve
    nrr "When she catches you looking, she turns away, roughly grabs a towel from Dwight and then pushes him and Claudette aside as she floats off."
    $ spiritObj.change("emote","none")
    call blackscene
    call campfirescene
    nrr "You head over to the campfire. The heat is comforting on this chilly night."
    nrr "Looking into the crackling embers, you think about Spirit's story about the prisoner in the puzzle box."
    nrr "If you manage to escape this place, will you leave with your life? Or has it already been taken from you and it's just a matter of time until you make a gruesome discovery?"
    nrr "Before you can dwell too much on your fate, Claudette and Dwight arrive, their now familiar creepy smiles stretching from ear to ear. It's a bit menacing to see a smile like that lit by firelight."
    call mood_unsettling
    $ clauddwightObj.change("emotion", "happy")
    $ clauddwightObj.change("pose", "close01")
    show clauddwight
    cl "We must apologize for the accommodations!"
    $ clauddwightObj.change("emotion", "idle")
    dw "We weren't prepared for another guest, but we're going to make you comfortable, or die trying!"
    $ clauddwightObj.change("emotion", "happy")
    nrr "They hand over a pillow and blanket and welcome you to snuggle up by the fire."
    call campfirescene
    $ clauddwightObj.change("pose", "pose01")
    with Dissolve(0.25)
    cl "Perhaps some music will put you at ease?"

    menu:
        dw "Just try to keep the volume to a minimum. Our other guests aren't the types you'll want to rob of their beauty sleep."
        "Ready":
            mc "Ready!"
            nrr "Away we go!"
            nrr "As you relax and look into the fire, the radio begins to fuzz and flicker. You examine it and decide that you might adjust the dial and fix it."
            call start_radio_minigame
        "Repeat the instructions":
            mc "Would you please repeat the instructions?"
            nrr "My pleasure!"
            call instructions_meatcarving
    $ tuning = True
    call tune_radio

    nrr "No matter how many things you listen to, you still can't sleep. You decide to ask one of the killers to spend a little more time with you until you're sleepier."
    
    $ diamondchoice = True
    menu:
        nrr "Who would you like to summon to your side as you lay by the fire?"
        "gui/button_spirit_idle.png¦gui/button_spirit_hover.png¦gui/button_spirit_select.png":
            $ diamondchoice = False
            $ spirit_aff = spirit_aff + 1
            call summon_spirit
        "gui/button_trapper_idle.png¦gui/button_trapper_hover.png¦gui/button_trapper_select.png":
            $ diamondchoice = False
            call summon_trapper
        "gui/button_wraith_idle.png¦gui/button_wraith_hover.png¦gui/button_wraith_select.png":
            $ diamondchoice = False
            call summon_wraith
        "gui/button_huntress_idle.png¦gui/button_huntress_hover.png¦gui/button_huntress_select.png":
            $ diamondchoice = False
            call summon_huntress

    nrr "You finally start to feel sleepy. Except... maybe this isn't really a \"sleepy\" feeling... maybe you're paralyzed. You try to keep your eyes open but you can't."
    nrr "Darkness overtakes you."
    call oceanhaunting
    nrr "The dark voice from earlier speaks to you again. It shouldn't still be as spooky, by now you've had a whole day of strange voices in your head, but this one's still undeniably odd."
    oc "The human body is made up of 60% water, did you know that? Of course you did. Everyone knows that, even amnesiac video game protagonists."
    oc "Well guess what? Drink as much as you'd like, you'll never get to 100%. You hear me? Don't think I don't see what you're up to."
    stop hauntloop fadeout 3.0
    call campfirescene
    nrr "You awake suddenly to see someone looming over you..."
    call mood_murder(withDissolve = False)
    $ wraithObj.change("emotion", "idle")
    $ wraithObj.change("pose", "close04")
    show wraith
    with Dissolve(0.25)
    nrr "Wraith stares at you, awkwardly. He says nothing, just stares. You look around to see if there's something going on behind you or on either side, but nope. Just staring."
    $ wraithObj.change("emote", "exclamation")
    $ wraithObj.change("pose", "close03")
    tw "Oh! You're awake!"
    $ wraithObj.change("emote", "none")
    tw "I saw you with The Spirit right before bedtime. Are you making some sort of uh... alliance? Are you with..."
    nrr "Wraith scans the horizon..."
    $ wraithObj.change("emote", "question")
    tw "{i}Them?{/i}"
    $ wraithObj.change("emote", "none")
    tw "I'm just making sure you are who you say you are. I've been burned before, and something seems off on this island since you've arrived. Even more off than usual..."
    call campfirescene(withDissolve = False)
    $ wraithObj.change("pose", "pose04")
    show wraith
    with Dissolve(0.25)
    tw "Um... maybe we could talk more about that tomorrow? It's just, since you got here, I... I just... I think we could have a really nice day tomorrow. Together."
    tw "It's just, you have no idea how long I've been here with these monsters. To be honest, I have no idea either. They're just awful. Boring and loud and stupid."
    $ wraithObj.change("emotion", "happy")
    tw "You're different. There's finally someone here on my level. You're thoughtful, interesting, gentle. I think we could uh.. you know. Have fun."
    $ wraithObj.change("emotion", "idle")
    tw "I could show you some cool stuff. If you want. If you don't, that's totally cool, I get it. No pressure."
    $ wraithObj.change("emote", "dread")
    $ wraithObj.change("emotion", "disgusted")
    tw "In fact, probably just forget I was here. Goodnight."
    $ wraithObj.change("emote", "none")
    hide wraith with Dissolve(0.25)
    nrr "Finally alone, for real this time (maybe), you drift off to sleep, again. Hopefully, you're not poisoned!"
    call blackscene
    return
    
label summon_spirit:
    mc "Spirit? Are you around? I was wondering if I could get a little company..."
    $ spiritObj.change("emotion","idle")
    $ spiritObj.change("pose","pose03")
    show spirit with dissolve
    nrr "Spirit tells you her secret for falling asleep when she's feeling restless."
    $ spiritObj.change("pose","close03")
    $ spiritObj.change("emote","stars")
    ts "I like to listen to flute music, dab on some essential oils, and steam my pores."
    $ spiritObj.change("emote","none")
    mc "Really?"
    $ spiritObj.change("emotion","disgusted")
    ts "What? Even the dead like to relax."
    mc "I don't really have any of those things around..."
    call mood_warmdark(image_name="images/comb.png", ismovefrombottom = True, withDissolve = True)
    pause 1
    nrr "Spirit reaches out and presents you with a unique item. It's a small comb, carved from bamboo."
    ts "I guess you could hold onto this. It was a gift from my mother. I will want it back, though. And if you lose it... well..."
    call campfirescene(withDissolve=False)
    $ spiritObj.change("emotion","idle")
    show spirit
    with Dissolve(0.25)
    mc "You'll get your revenge on me?"
    $ spiritObj.change("emotion","mad")
    ts "If it's the last thing I do."
    hide spirit with dissolve
    return
label summon_wraith:
    return
label summon_trapper:
    return
label summon_huntress:
    return
label tune_radio:
    while tuning:
        if radio_section == 1:
            call event_papercutbolsa
        elif radio_section == 2:
            call event_papercutbolsa
        elif radio_section == 3:
            call event_papercutbolsa
        elif radio_section == 4:
            call event_papercutbolsa
        elif radio_section == 5:
            call event_papercutbolsa
        elif radio_section == 6:
            call event_papercutbolsa
        elif radio_section == 7:
            call event_papercutbolsa
        elif radio_section == 8:
            call event_papercutbolsa
        else:
            call event_papercutbolsa
        menu:
            nrr "Let's see what's on this station."
            "Listen more?":
                call start_radio_minigame
            "Turn it off":
                stop eventloop fadeout 3.0
                $ tuning = False

    return