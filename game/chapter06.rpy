label chapter06:
    call lighthouse_day
    nrr "You and Spirit arrive at the coast, overlooking the Black Lighthouse. It's old and decrepit, but still impressive. There's something magnetic about it. You can see why Spirit would be drawn to such a place."
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    show spirit with dissolve
    nrr "You look Spirit up and down and notice that she's wearing all black, just like the lighthouse."
    mc "I'm noticing a bit of a theme... Is black your favorite color?"
    ts "Black isn't really a color at all, it's absence of color. It's a void."
    mc "Like me."
    $ spiritObj.change("emotion", "happy")
    nrr "Spirit smiles."
    ts "Nature abhors a vacuum."
    nrr "You're not sure if that's a good thing... or a bad thing."
    nrr "The lapping waves on the shore of the coast set a romantic tone. The fog that surrounds Spirit everywhere she goes blends perfectly with the mist rolling up over the rocky shoreline. She's at one with this place, and so are you."
    call event_frunkyzombie
    nrr "The peace doesn't last too long, however, as the Lighthouse lets out an eerie howl, like a monster dying. A spiraling black light stretches out across the sky."
    nrr "Spirit has to yell at you just to be heard."
    $ spiritObj.change("emote", "sparks")
    $ spiritObj.change("pose", "pose03")
    ts "{i}OH YEAH, IT DOES THAT.{/i}"
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("emote", "none")
    nrr "The light and sound recede and the two of you sit in silence."
    nrr "Spirit lays a towel down and then pats on it gently. Clearly she wants your company, so you oblige."
    nrr "When you do, she takes out some sunscreen and hands it to you."

    menu:
        nrr "You're not exactly sure what to do. Is this an invitation to get in a little hands-on action? What else could it be?"
        "\"Thanks\"":
            $ spirit_aff = spirit_aff + 1
            mc ""
        "\"Now we're talking\"":
            mc "Now we're talking, where should I start? Your back? They always start there in the movies..."
            $ spiritObj.change("emotion", "disgusted")
            $ spiritObj.change("emote", "dread")
            nrr "Woah sailor, slow your role. She doesn't actually need help reaching behind her, haven't you noticed that her hands float in the air?"
            $ spiritObj.change("emote", "none")
            $ spiritObj.change("pose", "pose01")
            ts "I'm good. The lotion is for you."




        "\"No, thanks\"":
            mc ""
    $ spiritObj.change("pose", "close04")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("emote", "question")
    ts "You need any help reaching those difficult spots?"
    $ spiritObj.change("emote", "none")
    menu:
        nrr "You see a hand float around your back."
        "\"Sure, why not?\"":
            $ spirit_aff = spirit_aff + 1
            mc "Sure, why not."
            nrr "Spirit's hand on your back is ice cold, but she has a soft touch. When she's done, she takes care of herself."
        "*GULP*":
            mc ""
    $ spiritObj.change("pose", "close03")
    $ spiritObj.change("emotion", "idle")
    menu:
        nrr "You watch as Spirit applies sunscreen to herself in the most unique way... by floating her own hand around her back to spread it on."
        "Comment on her floating hands ability":
            mc "The fact that your hands just float out around you like that, you can reach things way easier than I can. It's almost like you're some kind of superhero."
            $ spiritObj.change("pose", "pose03")
            $ spiritObj.change("emotion", "disgusted")

        "Say nothing":
            mc ""
        "Ask about the shards of glass sticking out from her":
            $ spirit_aff = spirit_aff + 1
            mc ""
    menu:
        ts "I'm glad you get a kick out of it, but floating severed limbs isn't exactly the type of super power you think to wish for as a kid. I'd much rather be able to read minds. Maybe then I'd understand why some people act the way they do..."
        "Tell her you're actually jealous":
            mc ""
        "Apologize":
            mc "I'm truly sorry. I clearly hadn't thought through what your experience was like."
    nrr "Sometimes humor is how you deal with uncomfortable situations, but clearly you read the room wrong."
    $ spiritObj.change("pose", "close03")
    $ spiritObj.change("emotion", "idle")
    mc "I was just thinking about what you must've gone through to end up like that. It had to have been horrible."
    $ spiritObj.change("emotion", "disgusted")
    ts "It was worse than death. At least death ends, eventually."
    $ spiritObj.change("emotion", "idle")
    ts "But I wouldn't want to forget it. It literally made me who I am right now."
    $ spiritObj.change("pose", "close01")
    ts "Truth is, I could pull all of these bits of glass that are stuck in my flesh out right now, if I wanted to. But I don't want to."
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("emote", "dread")
    ts "Each shard is a reminder of what my father did to me... and what the world did to him."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "mad")
    ts "That's why I refuse to play the universe's game. I hate the idea that I'll be forced to succumb to pressure the way he did in the end!"
    $ spiritObj.change("emote", "anger")
    $ spiritObj.change("pose", "close02")
    ts "The way that fear and anger filled him up and then came bursting out. The way his misery flooded our home and drowned us all..."
    $ spiritObj.change("emote", "none")
    nrr "{i}Yeesh.{/i}"
    $ spiritObj.change("emotion", "disgusted")
    ts "It's hard not to think about revenge. The dragon inside me, it's doing to me what the world did to him. I have to fight it, even though it gives me strength. I must maintain control."
    $ spiritObj.change("emotion", "idle")
    mc "You're stronger than he ever was. I'm sure of it."
    $ spiritObj.change("emote", "stars")
    $ spiritObj.change("pose", "close03")
    ts "I appreciate that, [mc_name]."
    $ spiritObj.change("emote", "none")
    ts "I suppose a little help isn't a bad thing. In life. In love... This world is a lot to endure alone."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "pose03")
    ts "Maybe I could use a little assistance reaching my toes for a bit of lotion... You know, having your body contorted into these vengeful poses, it really does a number on my joints."
    
    menu:
        cho "It rubs the lotion on its skin..."
        "Ready":
            $ sunscreen_turn = 0
        "Repeat the instructions":
            mc "Would you please repeat the instructions?"
            nrr "My pleasure!"
            call instructions_meatcarving

    while (int(sunscreen_turn) < 5):
        call start_sunscreen_minigame
        if sunscreen_section == 1:
            call end_sunscreen_minigame
            $ sunscreen_perfects = sunscreen_perfects + 1
            nrr "Perfect!"
        elif sunscreen_section == 2:
            call end_sunscreen_minigame
            $ sunscreen_good = sunscreen_good + 1
            nrr "Not bad..."
        else:
            call end_sunscreen_minigame
            nrr "You missed completely!"
        $ sunscreen_turn = sunscreen_turn + 1
        $ sunscreen_speed = sunscreen_turn + 1
    if sunscreen_perfects == 5:
        ##Perfect
        $ spirit_aff = spirit_aff + 1
        show spirit
    elif sunscreen_good > 1:
        ##Good
        $ spirit_aff = spirit_aff + 1
        stop eventloop fadeout 3.0
        call mood_warmlight
        $ spiritObj.change("pose", "pose01")
        $ spiritObj.change("emotion", "happy")
        show spirit
        ts "Well, I suppose that the lotion made it to where it was supposed to be going, eventually."
        $ spiritObj.change("emotion", "idle")
        ts "And you weren't too incredibly wasteful. I'm not a women who believes in rushing through things just to get them done."
        $ spiritObj.change("pose", "pose03")
        ts "If there is a next time, I'm sure you'll do even better."
        call event_frunkyzombie
        stop moodloop fadeout 3.0
    elif (sunscreen_good == 1) and (sunscreen_perfects == 0):
        ##Bad 1/5
        show spirit
    else:
        ##Missed Completely
        show spirit

    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    nrr "You look up at the Lighthouse, its ominous dark form hovering above this moment between Spirit and yourself."
    nrr "Evil as it clearly is, in this case it does you a solid by blurting out another ominous moan and burst of black light that rescues you from this awkward silence."
    call mood_inner_monologuescene("images/ghostship.png")
    nrr "From seemingly out of nowhere, an ancient-looking ship appears in the water. It glows, itself a thing of death, a spirit of a ship that once sailed these seas, centuries ago."
    nrr "A tattered black flag whips in the ocean air above the ship as it careens toward the shore..."
    nrr "...before crashing on the rocks! It must've been drawn in by the Lighthouse."
    stop moodloop fadeout 3.0
    call lighthouse_day(withDissolve=False)
    show spirit
    with dissolve
    nrr "You hear the distant shouting of sailors as the old wooden ghost ship breaks up and sinks into the water."
    $ spiritObj.change("emotion", "disgusted")
    ts "Oh, right. It does {i}that{/i} sometimes, too."
    mc "Should we, uhhh, do something?"
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose03")
    ts "Nah. The sharks will take care of it."
    nrr "Within a minute, the ocean is quiet again except for the waves. Note to self: hungry sharks."
    nrr "But these time-travelling pirates (or whoever they were... you're half sure you saw one of those skull and crossbone flags) aren't the only ones drawn here today."
    play sound "sounds/sfx_signature_wraith01.ogg"
    hide spirit
    $ wraithObj.change("emotion", "idle")
    $ wraithObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "disgusted")
    show wraith at movecenterleft with dissolve
    show spirit
    show spirit at slidetomovecenterright
    nrr "It's Wraith! He has emerged from the palm trees behind you."
    $ wraithObj.change("emotion", "scared")
    tw "I didn't come here to break up your fate, or something..."
    $ wraithObj.change("emotion", "idle")
    $ wraithObj.change("pose", "pose03")
    $ wraithObj.change("emote", "exclamation")
    tw "I came here... for {i}THAT{/i}!"
    $ wraithObj.change("emote", "none")
    hide wraith
    hide spirit
    with dissolve
    nrr "Wraith points to the lighthouse. It is indifferent to his attention."
    show wraith at movecenterleft
    show spirit at movecenterright
    with dissolve
    $ wraithObj.change("pose", "pose02")
    $ wraithObj.change("emotion", "disgusted")
    tw "I've been seeing it, in my dreams. Shining its strange light on me. I can't avoid it, through woods and walls, nothing seems to stop it from reaching out to me."
    $ spiritObj.change("emote", "sparks")
    $ spiritObj.change("pose", "pose01")
    $ wraithObj.change("pose", "pose01")
    ts "Duh. It's a haunted Lighthouse. It does that to {i}everyone{/i} at some point. You're no more special than me, those dead pirates, or that mermaid I saw washed up on shore that one time."
    $ spiritObj.change("emote", "none")
    nrr "Eww."
    $ wraithObj.change("pose", "pose03")
    $ spiritObj.change("pose", "pose03")
    ts "Mermaids, by the way, aren't even close to as beautiful in person as they are in movies. More sea witch than underwater princess, if you get my drift."
    $ wraithObj.change("emote", "dread")
    $ wraithObj.change("emotion", "scared")
    tw "It's all part of a vast conspiracy. An epic river of lies that runs beneath the island. Or something."
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("emotion", "idle")
    tw "I'm pretty sure I've figured it out. The basics, anyhow. If you come with me, I can--"
    $ wraithObj.change("emotion", "scared")
    $ wraithObj.change("pose", "pose01")
    $ spiritObj.change("emote", "anger")
    $ spiritObj.change("emotion", "mad")
    $ spiritObj.change("pose", "pose02")
    ts "{i}You can get cut{/i}!"
    nrr "Spirit waves her katana, nearly trimming a couple buttons off of Wraith's tropical top. He takes the hint and backs away a few steps slowly."
    $ spiritObj.change("emote", "none")
    ts "For the \"quiet guy\" he never really shuts up."
    $ wraithObj.change("emotion", "disgusted")
    $ wraithObj.change("pose", "pose02")
    tw "Ok, be that way! You'll see..."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose01")
    hide wraith with dissolve
    show spirit at movecenter
    nrr "Alone at last, tension broken, deathly moans quiet, and Wraith banished back to... wherever he hangs out, you scooch closer to Spirit, breathing in the damp foggy air that seems to emanate from her."
    nrr "It's not quite clear how that whole fog thing works, but you don't even care. You're feeling this moment."
    $ spiritObj.change("emote", "stars")
    $ wraithObj.change("pose", "close04")
    nrr "Spirit seems to be feeling it too. She starts to adjust her robe, and you get a peek at the bathing suit beneath."
    $ spiritObj.change("emote", "none")
    nrr "For someone who seems intent on proving how little she cares about what everyone else thinks, she put a lot of work into getting into that suit-- it's got straps for days."
    nrr "However, you're so focused on what's happening with Spirit you don't see the next interruption coming..."
    stop eventloop fadeout 3.0
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "pose03")
    show spirit at slidetomovecenterright
    $ clauddwightObj.change("emotion", "idle")
    $ clauddwightObj.change("pose", "pose02")
    show clauddwight at movecenterleft with dissolve
    nrr "... and Claudette and Dwight burst in on you and interrupt whatever you were doing! It doesn't seem like they were worried they'd bump into much..."
    dw "We're here to make..."
    play sound "sounds/sfx_signature_clauddwight04.ogg"
    $ clauddwightObj.change("emotion", "happy")
    $ clauddwightObj.change("pose", "close02")
    $ spiritObj.change("emotion", "idle")
    cl "...{i}a very dramatic announcement{/i}!"
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "sad")
    dw "Well, technically, we're here to invite you to join us back at the beach."
    play sound "sounds/sfx_signature_clauddwight04.ogg"
    $ clauddwightObj.change("emotion", "happy")
    $ clauddwightObj.change("pose", "close02")
    cl "Where we'll be making {i}a very dramatic announcement{/i}!"
    $ clauddwightObj.change("emotion", "disgusted")
    $ clauddwightObj.change("pose", "pose01")
    $ spiritObj.change("pose", "pose01")
    dw "It's hard being the producers and the hosts."
    $ clauddwightObj.change("emotion", "sad")
    cl "Aren't Survivors suppose to work in groups of four?"
    call blackscene
    return

    
init python:
    sunscreen_perfects = 0
    sunscreen_good = 0
    sunscreen_turn = 0
