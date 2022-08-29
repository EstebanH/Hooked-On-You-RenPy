label chapter03:
    call campfirescene
    call event_speeddating
    nrr "Once everyone has gathered at the firepit, Dwight and Claudette quickly make an announcement."
    $ clauddwightObj.change("pose", "close01")
    $ clauddwightObj.change("emotion", "idle")
    show clauddwight
    with Dissolve(0.25)
    dw "We're not going to blame anyone in particular..."
    $ clauddwightObj.change("emotion", "disgusted")
    cl "...But someone--and we're not going to say who, so don't worry, you--hasn't been sticking to the schedule."
    $ clauddwightObj.change("emotion", "idle")
    dw "That means that we're behind on time for evening activities!"
    cl "And we'll only have time for one person to share their special spooky nighttime story."
    hide clauddwight with dissolve
    show wraith at movecenterleft 
    $ wraithObj.change("emotion", "sad")
    $ wraithObj.change("emote", "question")
    $ wraithObj.change("pose", "pose02")
    tw "Just one story?? But storytime is my favorite activity! This is a narrative-heavy experience!!"
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("emotion", "disgusted")
    $ huntressObj.change("emotion", "disgusted")
    $ huntressObj.change("pose", "pose01")
    show huntress at moveleft 
    show wraith behind huntress
    with dissolve
    th "You're telling us that only person gets to share? How will we decide who?"
    $ wraithObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "disgusted")
    show spirit at movecenterright
    with dissolve
    ts "Oh great, we have to decide as a group? that never goes well..."
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("emote", "anger")
    $ trapperObj.change("pose", "pose02")
    show trapper behind spirit at moveright
    with dissolve
    tt "Whoever did this, step up now. I swear I won't be angry. I'll merely chop your head clean off. No fuss. No muss."
    $ trapperObj.change("emote", "none")
    nrr "Voice trembling, you realize this is probably it for you, but you embrace your fate."
    $ trapperObj.change("pose", "pose01")
    $ wraithObj.change("emotion", "idle")
    $ trapperObj.change("emotion", "idle")
    $ huntressObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    mc "S-S-Sorry, everyone, I think they're talking about me. To be honest, I still don't understand how this whole schedule thing works... I guess I lost track of time? While I was passed out?"
    $ wraithObj.change("emotion", "happy")
    tw "Been there before. Even though it's taking some pressure off of me, which is an absolute dream come true, is it really fair to pick on the newbie?"
    hide wraith with dissolve
    $ spiritObj.change("emote", "question")
    $ spiritObj.change("emotion", "disgusted")
    ts "Seriously, has anything here ever happened on schedule, even once?"
    hide spirit with dissolve
    $ spiritObj.change("emote", "none")
    $ trapperObj.change("emote", "anger")
    $ trapperObj.change("pose", "pose02")
    $ trapperObj.change("emotion", "mad")
    $ huntressObj.change("emotion", "disgusted")
    tt "Damnit Donald, if you try to flex that authority gimmick one more time, so help me, I'll snap your head off so quick, and then I'll drown you in his blood, Cynthia. Fuss and muss are back on! You two know I love to hack, slash, and slice."
    $ trapperObj.change("emote", "none")
    $ huntressObj.change("pose", "pose04")
    $ huntressObj.change("emote", "exclamation")
    th "We all know you love to kill. It's almost all you talk about."
    $ huntressObj.change("emote", "none")
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose01")
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "sad")
    show clauddwight
    cl "Nobody named any names! Who even knows any names? Not us!"
    $ clauddwightObj.change("emotion", "scared")
    dw "I renounce my name! Who's Donald? Who's Dwight? Who even knows anymore? Call me Nobody!"
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "disgusted")
    $ dwight_name = "NOBODY"
    dw "But we still gotta get started on storytime so..."
    $ dwight_name = "DWIGHT"
    $ clauddwightObj.change("emotion", "idle")
    cl "[mc_name], who do you think should go? Ahhh damnit, that's a name."
    hide clauddwight
    hide trapper
    hide huntress
    with Dissolve(0.25)
    $ diamondchoice = True
    menu:
        nrr "Please, pick somebody quickly so that this tropical vacation doesn't turn into a bloodbath."
        "gui/button_spirit_idle.png¦gui/button_spirit_hover.png¦gui/button_spirit_select.png":
            $ diamondchoice = False
            mc "I choose you, Spirit!"
            call storytime_spirit
        "gui/button_wraith_idle.png¦gui/button_wraith_hover.png¦gui/button_wraith_select.png":
            $ diamondchoice = False
            mc "I choose you, Wraith!"
        "gui/button_trapper_idle.png¦gui/button_trapper_hover.png¦gui/button_trapper_select.png":
            $ diamondchoice = False
            mc "I choose you, Trapper!"
        "gui/button_huntress_idle.png¦gui/button_huntress_hover.png¦gui/button_huntress_select.png":
            $ diamondchoice = False
            mc "I choose you, Huntress!"

    nrr "On that note, everyone decides it's time to take a break and split up for a little bit so that they can all have a moment alone before bed."
    nrr "Everyone leaves and you're alone by the fire. The only thing you hear is the ocean slowly lapping against the shore."
    nrr "This is nice."
    nrr "A true moment of peace and tranquility that lasts for all of seven seconds because Trickster shows up. And he's blaring his latest song."
    play sound "sounds/sfx_signature_trickster01.ogg"
    $ tricksterObj.change("pose", "pose02")
    $ tricksterObj.change("emotion", "idle")
    tr "Hey, baby. You look lonely. Mind if I join you?"
    nrr "He doesn't wait for an answer."
    $ tricksterObj.change("pose", "close01")
    $ tricksterObj.change("emotion", "happy")
    tr "I know you've been hearing from these guppies all day. But I want you to hear something from a big fish like me. Something special those in charge of this island don't want you to hear."
    $ tricksterObj.change("emotion", "mad")
    $ tricksterObj.change("emote", "sparks")
    tr "I am the ultimate catch on this island. The only lobster in an ocean of sardines."
    $ tricksterObj.change("emote", "none")
    tr "No one can give you what I can."
    $ tricksterObj.change("emotion", "happy")
    tr "You just have to find me."
    $ tricksterObj.change("pose", "pose02")
    tr "Come find me, baby."
    hide trickster with dissolve
    nrr "Trickster leaves. You're a bit confused about what to make of his cryptic clues, but you aren't going to get any time to yourself to think about them just yet."
    nrr "Spirit approaches you..."
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    show spirit
    with Dissolve(0.25)
    call event_bloodconfident
    ts "You know, I was watching you while I told my story."
    ts "I could tell it was having an effect on you."
    ts "This fog that follows me around... I could feel you breathing heavily, taking me in."
    nrr "You {i}and I{/i} are both absolutely flabbergasted at that piece of information. Legit, you learn something new every day, even when you're a god--I mean, a narrator."
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("emote", "sweat")
    ts "You're doing it again, right now. You need to calm down. You should come to the hot tub with me."
    $ spiritObj.change("emote", "none")
    stop eventloop fadeout 3.0
    call oceanhaunting
    oc "Dipping in hot tubs with The Spirit? You've come a long way in a single day. I'm not saying you shouldn't follow her. An offer like that..."
    oc "Just don't forget our little talk."
    stop hauntloop fadeout 3.0 
    call blackscene
    return

label storytime_spirit:
    nrr "Woah woah. This entire experience is being carefully crafted to avoid an IP infringement lawsuit. Let's be careful with the catchphrases, will ya?"
    $ spiritObj.change("emote", "question")
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "pose01")
    show spirit
    ts "Really? You want to hear from me?"
    $ spiritObj.change("emote", "none")
    nrr "Spirit huffs and dramatically rolls her eyes as she gets to her feet in front of the campfire."
    $ huntressObj.change("emote", "exclamation")
    $ huntressObj.change("emotion", "happy")
    $ huntressObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    show huntress behind spirit at moveleft
    with Dissolve(0.25)
    th "Don't let her talk you out of it, she's great with ghost-stories."
    $ huntressObj.change("emote", "none")
    $ wraithObj.change("emotion", "happy")
    $ wraithObj.change("pose", "pose01")
    show wraith behind spirit at movecenterleft
    with Dissolve(0.25)
    tw "I don't know where she gets it, but she comes up with the scariest stuff. Seriously disturbing, even to me, and I literally pulled a guy's skill and spine out once with my bare hands."
    $ wraithObj.change("emotion", "disgusted")
    $ huntressObj.change("emotion", "disgusted")
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "disgusted")
    show trapper behind spirit at moveright
    with Dissolve(0.25)
    tt "Talk about bullshit stories..."
    $ spiritObj.change("emote", "dread")
    ts "If everyone else is going to chit chat I guess I can just sit down and---"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    $ huntressObj.change("emotion", "mad")
    $ huntressObj.change("emote", "sparks")
    $ wraithObj.change("emotion", "scared")
    $ trapperObj.change("emotion", "disgusted")
    nrr "Huntress's eyes go red behind her mask and both Trapper and Wraith take their seat. They know it's worth fighting, and when it's not."
    $ huntressObj.change("emote", "none")
    hide trapper
    hide wraith
    hide huntress
    with Dissolve(0.25)
    $ spiritObj.change("emotion", "happy")
    call event_storytime
    ts "*Ahem* Well, I hate to break it to you, but tonight's story isn't scary. It's a {i}romance{/i}. Too late now, through. I was selected, and so I'm going to tell my story."
    $ trapperObj.change("pose", "close02")
    $ spiritObj.change("emotion", "idle")
    ts "I call it..."
    $ spiritObj.change("emote", "stars")
    ts "\"THE PRISONER'S KISS\""
    $ spiritObj.change("emote", "none")
    nrr "You notice that Huntress and Wraith are both sharing a giant tub of popcorn. Nobody offered you popcorn!"
    $ trapperObj.change("pose", "close03")
    ts "It was a dark summer night. Warm rain seeped from the sky like blood from an old wound."
    ts "Detective Hotta, a celebrated investigator and renowned hostage negotiator, was called to the scene of a strange occurrence, unlike anything she had ever seen before."
    $ spiritObj.change("emotion", "happy")
    ts "When she arrived, the scene was chaotic. Crowds had begun to gather. A dozen other officers were doing everything they could to keep curious onlookers away. But how could anyone resist wanting to know more?"
    call mood_mystery
    show spirit
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("emote", "dread")
    with Dissolve(0.25)
    ts "For there, in the middle of a busy market, had appeared a giant box. Strange, alien in its appearance, and massive in size."
    $ spiritObj.change("emote", "none")
    ts "No one knew how it got there. Was it delivered? Built on site? In such a busy area, how could something like this just appear? A mystery, it was as if conjured by magic."
    $ spiritObj.change("emotion", "happy")
    ts "But this was no illusion. The huge box was very real... and someone was trapped inside."
    $ spiritObj.change("pose", "close03")
    $ spiritObj.change("emotion", "idle")
    nrr "Spirit pauses her story to look from face to face of each audience member. She has no expression, but you feel her vibrating with energy. She's in her element."
    $ spiritObj.change("emote", "exclamation")
    ts "\"Help me!\" cried someone inside the box. It was a man. Terrified. Trapped. Imprisoned. His voice trembling."
    $ spiritObj.change("emote", "none")
    ts "By now it was if every detective in the city was there, looking this strange structure up and down, inspecting it on every side. It didn't make sense. There were no doors, no windows, no fasteners or seams. It was completely solid, and much too heavy to move by hand."
    $ spiritObj.change("emotion", "happy")
    ts "Solid, that is, except for a single small slit, just enough to see the bloodshot eyes of the prisoner trapped inside."
    $ spiritObj.change("emote", "sparks")
    ts "\"I don't know what happened! I woke up, and here I was! I'm so scared, please help me,\" cried the man, as if pleading for his life."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("pose", "close01")
    ts "No stranger to tense situations, Detective Hotta comforted the man. She used her training to calm him and buy time for the other investigators. However, time did not bring clarity, only anxiety, as the night dragged on with no progress opening the box."
    $ spiritObj.change("emotion", "sad")
    ts "And as the night grew longer, the seeping rain puddling on the ground, the man inside grew more desperate. More sad and lonely. More pathetic and in need of help."
    $ spiritObj.change("emote", "sweat")
    $ spiritObj.change("emotion", "disgusted")
    ts "But Detective Hotta was no help at all. Powerless to save him, guilt began to weigh on her, like it never had before. \"Don't let me die in here,\" the man begged. \"Don't let me die alone.\""
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    ts "\"Stay calm,\" instructed Detective Hotta. \"You're not alone. I'm here. Hell, half the town is here. We're all in this together, and we won't let this be the end of your story.\""
    $ spiritObj.change("emotion", "sad")
    $ spiritObj.change("pose", "close03")
    ts "Looking through that narrowest of passageways, Detective Hotta watched her own reflection in the tear-filled eyes of this strange, sad prisoner. Together they both wept in silence at the hopelessness of the moment."
    ts "\"Promise?\" asked the man. \"Promise that I'm not alone?\""
    $ spiritObj.change("emotion", "idle") 
    ts "\"Yes,\" she promised, \"I do.\" A simple pledge, she felt an instant connection like she had never felt before. Not to her family, not to her friends, not to any of the other hostages she had worked so hard to free before."
    $ spiritObj.change("pose", "close02")
    $ spiritObj.change("emotion", "idle")
    ts "And so, when the man's eyes closed and backed away, it didn't scare Detective Hotta, for she knew he would return, and he did, pressing his lips up the narrow slit in this horrible puzzle box, repeating his question again, steam flowing from his mouth as he asked..."
    $ spiritObj.change("emote", "question")
    ts "\"Promise? Promise that I'm not alone?\""
    $ spiritObj.change("emote", "none")
    ts "..."
    ts "\"Yes,\" she promised, \"I do.\" And pressing her palms against the cold outside of the box, without truly knowing why, Detective Hotta leaned forward and placed her own lips up to the opening, letting her breath creep into this strange structure, allowing her warm lips to fall on this man's."
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emotion", "idle")
    ts "It was a gentle kiss. A moment of compassion. She could feel in this brief contact the beating of her heart, pulsing blood through every inch of her body, matched beat for beat in this soft touch."
    ts "\"Thank you,\" said the man, no trace of fear remaining in his voice, and he backed away into the darkness, disappearing in a single moment of eerie calmness."
    $ spiritObj.change("pose", "close02")
    $ spiritObj.change("emotion", "mad")
    $ spiritObj.change("emote", "sparks")
    ts "\"Get back!\" yelled an officer, suddenly thrusting himself between Detective Hotta and the box, breaking a silence that would soon filled by a cacophony of whirring gears and clicking latches, a symphony of mechanical activity happening all at once."
    $ spiritObj.change("emote", "none")
    ts "Something had triggered, as if an unseen lever pulled, and the side of the giant box began to slide open."
    ts "Detective Hotta gripped her flashlight tightly and pushed forward into the foggy interior of the giant box. Her feet splashed in the puddled rainwater, her heart racing, as she swept her light from side to side."
    $ spiritObj.change("emotion", "sad")
    ts "And that's when her eyes landed on the man. Or at least, landed on what should have been him."
    $ spiritObj.change("pose", "close03")
    $ spiritObj.change("emote", "dread")
    ts "There, in the corner of the box, was a pile of... pieces. Like parts of a doll, almost, pulled apart, or..."
    $ spiritObj.change("emote", "none")
    ts "Perhaps that's just how Detective Hotta had to think of him in that moment to survive."
    ts "A collection of segments, limbs, pieces. Disconnected from one another. Cleanly severed and placed in a neat little pile."
    ts "And atop that pile, a head. Cold, pale. Eyes open. Lips an icy blue."
    $ spiritObj.change("pose", "pose01")
    stop moodloop fadeout 3.0
    call campfirescene(withDissolve=False)
    show spirit
    with Dissolve(0.25)
    nrr "Spirit stares at the fire, her own expression lifeless, her lips blue. Tears fall from her chin and soak into the sand at her feet."
    nrr "You're blown away by the story, and it's safe to say you're not alone. Everyone else is looking into the fire or up at the sky, anywhere but at Spirit."
    nrr "It was you who chose her, you who initiated this harrowing tale. So sad. So creepy. So... sensual? She really went into great detail when it came to describing that kiss. Too much detail, and now no one is sure to act."
    stop eventloop fadeout 3.0
    nrr "Dwight and Claudette are staring daggers at you. You have to do something."
    menu:
        nrr "This game was supposed to be a lighthearted romp. Please. I SAID DO SOMETHING."
        "Say nothing. Hug her":
            nrr "You stand and without saying anything approach Spirit, reaching your arms around her for a hug."
            $ spiritObj.change("pose", "close03")
            nrr "Her robe, hovering in the air, begins to wrap itself around you and squeeze you into her. It's kind of like being hugged back... but also like being tied up. It's certainly not what you expected."
            nrr "Instinctually, you pull yourself away, but it's an awkward movement and you nearly fall over into the fire."
            nrr "Spirit says nothing, and floats away without so much as a goodbye. You, meanwhile, realize everyone had just watched this truly strange interaction from the corners of their eyes."
            hide spirit with dissolve

        "Cool story.":
            mc "\"Cool story.\""
        "Stand up and try to start one of those slow claps":
            mc "Claps"
    return