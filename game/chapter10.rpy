label chapter10:
    call fireplacescene
    call event_papercutbolsa
    nrr "Wow, what a crazy way to end the day! An elimination? I didn't even know it was that kind of a game!"
    nrr "Let's check in with everyone, especially with out loser. Everyone deserves a send-off."
    play sound "sounds/sfx_signature_huntress01.ogg"
    $ huntressObj.change("pose", "close01")
    $ huntressObj.change("emotion", "idle")
    show huntress with dissolve
    th "We'll see how things go tomorrow, I suppose. I'm not expecting anything. I tend to shut my mind off during hard times."
    $ huntressObj.change("emotion", "disgusted")
    $ huntressObj.change("emote", "dread")
    th "I know I seem all excited and devil-may-care, but the truth is, I'm really a pessimist at heart."
    $ huntressObj.change("emote", "none")
    th "That tends to happen when-"
    nrr "Your mother is skewered by an elk when you were young?"
    $ huntressObj.change("emotion", "scared")
    $ huntressObj.change("emote", "question")
    th "Yeah, how'd you know?"
    $ huntressObj.change("emote", "none")
    nrr "Wild guess. It's also the only thing you talk about."
    $ huntressObj.change("emotion", "disgusted")
    $ huntressObj.change("pose", "close02")
    th "If you'll excuse me, I think I saw a raccoon over in that tree and I'm feeling peckish."
    hide huntress
    play sound "sounds/sfx_signature_wraith01.ogg"
    $ wraithObj.change("pose", "close01")
    $ wraithObj.change("emotion", "disgusted")
    $ wraithObj.change("emote", "sweat")
    show wraith
    with dissolve
    tw "I know I said some things when [mc_name] kicked me to the curb, and uh..."
    $ wraithObj.change("emote", "none")
    tw "I just want to say, I'm embarrassed for how I acted."
    $ wraithObj.change("pose", "close02")
    $ wraithObj.change("emotion", "mad")
    $ wraithObj.change("emote", "anger")
    tw "Not what I said though. I stand by it. I want everyone here to, uh... to burn."
    $ wraithObj.change("emote", "none")
    hide wraith
    $ trapperObj.change("pose", "close01")
    $ trapperObj.change("emotion", "idle")
    show trapper
    with dissolve
    play sound "sounds/sfx_signature_trapper03.ogg"
    tt "How would I say things are going? It's a matter of perspective."
    tt "If [mc_name]'s goal is to impress me things are going poorly."
    $ wraithObj.change("emotion", "mad")
    tt "But if [mc_name]'s goal is to get themselves killed they're doing an amazing job."
    play sound "sounds/sfx_signature_spirit03.ogg"
    hide trapper
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emotion", "idle")
    show spirit
    with dissolve
    ts "Did I think there was a chance I might get eliminated? Yeah, I did..."
    $ spiritObj.change("emotion", "disgusted")
    ts "Did I care if I got eliminated? Not even a little."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("emote", "question")
    ts "Does the volume of words I spend talking about how much I don't care about things signify a deeper yearning within me to be seen, heard, and validated by those around me?"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "happy")
    ts "Nah."
    play sound "sounds/sfx_signature_trickster01.ogg"
    hide spirit 
    $ tricksterObj.change("pose","close01")
    $ tricksterObj.change("emotion","idle")
    show trickster
    with dissolve
    nrr "What? No, you're not a part of this, you don't get a confessional."
    $ tricksterObj.change("emote","stars")
    $ tricksterObj.change("emotion","mad")
    tr "It's cool, man. I'm not a part of anything, you feel me? I'm not a cog in anyone's machine. I'm my own machine."
    $ tricksterObj.change("emote","none")
    $ tricksterObj.change("emotion","happy")
    tr "This whole thing is pretty cute though. Charmingly low budget, old school marketing vibes. Ngl, kinda wish I wasn't so busy right--I'd definitely be down with a reality-show-style dating competition with survival elements."
    tr "But I got my new album, upcoming tour, finalizing the new sneaker line, producing a limited series of my life, starting a new social media NFT crypto app, and doing these private gigs over on IP Island."
    $ tricksterObj.change("pose","close02")
    tr "My dudes, you gotta come check it out. IP Island, it's dope, it's where the {i}real{/i} killers are hanging out. Fully licensed, no legal drama. Lawyers? Take a hike."
    $ tricksterObj.change("emotion","idle")
    nrr "I'm gotta tell everyone that Trickster said that about them, don't worry."
    tr "I'm talking your favorite established characters from all over pop culture that can't be seen on this island--hell you probably can't even mention them, like Ghostf-"
    $ tricksterObj.change("emotion","sad")
    nrr "Don't you say it! Look, we get it, you're very popular and in demand. But we have a game to get back to and I don't want to get sued."
    tr "..."
    $ tricksterObj.change("emote","sparks")
    $ tricksterObj.change("emotion","happy")
    tr "... Ghostface."
    $ tricksterObj.change("emote","none")
    nrr "Come on!!"
    $ tricksterObj.change("pose","close01")
    $ tricksterObj.change("emotion","mad")
    tr "Whatever, I don't even care. I'm The Trickster!"
    $ tricksterObj.change("emote","heart")
    $ tricksterObj.change("emotion","happy")
    tr "See you around, [mc_name]. You too, Narrator."
    $ tricksterObj.change("emote","none")
    hide trickster with dissolve
    nrr "Um, I have a name, you know!"
    mc "You do?"
    nrr "YES! Seriously, they do not pay me enough to deal with you people."
    play sound "sounds/sfx_signature_entity01.ogg"
    call oceanhaunting
    oc "Is it my turn?"
    nrr "What? No! No, it's not your \"turn\"!!"
    nrr "You're sentient water, how are you even sitting in that chair?"
    oc "What's a chair?"
    nrr "It's the thing you're getting all wet. Now it's gonna smell like mildew!!"
    oc "Ok... rude."
    nrr "Fine, let's just get this over with. It's your turn, Ocean. Do your check-in."
    oc "Check-in? I was just looking for the bathroom."
    nrr "Bathroom? Are you serious? It's down the hall to the left!"
    oc "It's ok. Nevermind."
    stop hauntloop fadeout 3.0
    call fireplacescene
    nrr "NEVERMIND??? WHAT DOES THAT MEAN??"
    play sound "sounds/sfx_signature_clauddwight04.ogg"
    $ clauddwightObj.change("pose","close01")
    $ clauddwightObj.change("emotion","sad")
    show clauddwight with dissolve
    nrr "No, not you too. This wasn't meant to be confessional time for literally every character in this game."
    cl "It's ok, we don't have to confess anything, we've just been working our asses off for two days straight and wanted to sit down somewhere."
    $ clauddwightObj.change("emotion","disgusted")
    dw "This chair is wet!"
    nrr "Yeah, I think the ocean just peed on it."
    cl "How is tha poss- you know what, I don't care."
    $ clauddwightObj.change("emotion","sad")
    nrr "You two are looking pretty pleased with yourselves."
    dw "I've got something to confess."
    nrr "Oh great, what's it gonna be? You ate glue in the second grade? You cheated on an algebra test once?"
    call mood_murder(withDissolve=False)
    $ clauddwightObj.change("emotion","happy")
    show clauddwight
    dw "Watching Wraith get eliminated was the first time in this unending spiral staircase of pain that is my life that I've felt even a modicum of joy."
    $ clauddwightObj.change("emotion","mad")
    dw "Every minute that I'm alive is a nightmare. This place, this sun, these sweet sugary drinks, it sounds fun for a long weekend, but for {i}eternity{/i}?"
    dw "The unrelenting rhythm of crashing waves and wailing seagulls, it's like a crescendoing song of evil that makes me question the very foundation of the universe. Why am I here? Why are any of us here? What kind of sentient being would do this?!"
    $ clauddwightObj.change("emotion","scared")
    dw "Please, erase me from this existence. Make it so I was never born. Pull the plug on this experiment and let my soul be free! And please, {i}please{/i}, get me out of this polo shirt!!"
    cl "Ooooooooooooook, let's get you to bed, buddy."
    $ clauddwightObj.change("emotion","mad")
    dw "I don't want to go to bed. Going to bed means eventually... I'll have to wake up."
    hide clauddwight with dissolve
    nrr "Yikes huh? that was a weird way to end."
    nrr "Ah well, what are ya gonna do? You let the camera roll long enough, someone is bound to say something crazy."
    nrr "Anyways, seems like everyone's had their shot to annoy me tonight, so hit the hay and get some rest. Tomorrow is gonna be a doozy!"
    call blackscene
    return