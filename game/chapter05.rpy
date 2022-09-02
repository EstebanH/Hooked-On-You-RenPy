
label chapter05:
    call fireplacescene
    nrr "Wait a second. Where are we? This isn't... Oh jeez. It is. It's one of those reality show confessional rooms where all of the constants talk directly to camera."
    $ huntressObj.change("pose", "close02")
    $ huntressObj.change("emotion", "idle")
    play sound "sounds/sfx_signature_huntress01.ogg"
    show huntress
    th "Look. I don't NEED anyone. I've been perfectly fine on my own since my mother died. I eat an all-organic diet of raw deer, bear, and human, and I'm fit as a fiddle."
    $ huntressObj.change("pose", "close01")
    th "That being said... something about this newcomer makes me think I might be missing out on some huge part of this thing called life."
    th "There's always time to turn things around. Like that one time I spent day and night searching for food in vain."
    $ huntressObj.change("emotion", "disgusted")
    th "Only to return to my cabin, spent and starving, to find a family of squirrels nesting in my chimney."
    $ huntressObj.change("emotion", "happy")
    th "They were delicious!"
    hide huntress
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "close01")
    play sound "sounds/sfx_signature_trapper03.ogg"
    show trapper 
    with dissolve
    tt "If I'm being honest, I want to kill just about every person I meet within a minute of meeting them. Even the few people I can tolerate I want to see suffer for a long time... before I kill them."
    $ trapperObj.change("emote", "stars")
    $ trapperObj.change("pose", "close02")
    tt "But this person... for some reason I would like them to continue living. For now. One false step and... haha. Well, you know, everyone calls Trapper for a reason. And they better call me Trapper."
    $ trapperObj.change("emote", "none")
    $ trapperObj.change("emotion", "mad")
    tt "I swear if I watch this later and you list me as 'Evan' I'm going to kill the chyron guy."
    hide trapper
    $ wraithObj.change("emotion", "disgusted")
    $ wraithObj.change("pose", "close02")
    play sound "sounds/sfx_signature_wraith01.ogg"
    show wraith
    with dissolve
    tw "I don't really care. This island is full of people who don't really like me, so what's one more? I don't want to get distracted from my plan, anyways..."
    hide wraith
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close01")
    play sound "sounds/sfx_signature_spirit03.ogg"
    show spirit
    with dissolve
    ts "I know that everyone thinks of me as a beautiful, cold-blooded monster. I can't help it, circulation just isn't my thing. I don't {i}choose{/i} to be cold! This cute hat and robe, ok, those are a choice, sure."
    $ spiritObj.change("emote", "thoughts")
    ts "If someone were to come around and capture my heart, at least that beats being stabbed in it."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("pose", "close02")
    $ spiritObj.change("emotion", "happy")
    ts "If I'm gonna get {i}bloody revenge on a society that has used me and throw me away...{/i} maybe it wouldn't hurt to have a little help?"
    call blackscene
    call beachdayscene
    nrr "You open your eyes. The sun is shining. There's not a cloud in the sky. And you feel... great! Totally well-rested."
    nrr "You're not even suspicious of the fact that you fell asleep by the campfire but woke up several yards down the beach."
    nrr "Wait, are you on vacation? Was yesterday nothing more than a strange dream?"
    nrr "No, not a dream. You really are here for another day. Why, I have no idea. You're obviously a weirdo."
    nrr "Speaking of weirdos, I see the rest of the gang is hanging out on the beach. This is definitely not a dream."
    nrr "I wouldn't rule out a nightmare just yet though."
    nrr "At least they make for a sexy bunch, no?"
    call event_deadnightstand
    nrr "And talk about sexy. Here comes Trickster carrying coffee."
    $ tricksterObj.change("pose", "pose02")
    $ tricksterObj.change("emotion", "happy")
    play sound "sounds/sfx_signature_trickster01.ogg"
    show trickster with dissolve
    tr "Morning, beautiful! I thought you might like a nice cup of Joe to start this incredible day off right."
    hide trickster with dissolve
    call mood_warmlight(image_name="images/coffee.png", ismovefrombottom = True)
    nrr "Trickster seems suspiciously cheerful. I'm sure there's nothing nefarious behind his joyful demeanor though."
    nrr "Everyone knows musicians are morning people."
    call beachdayscene
    call event_deadnightstand
    $ tricksterObj.change("pose", "close01")
    $ tricksterObj.change("emotion", "happy")
    $ tricksterObj.change("emote", "stars")
    tr "I also want to wish you luck. Today is an important one!"
    $ tricksterObj.change("emote", "none")
    $ tricksterObj.change("emotion", "idle")
    tr "My only regret is that I won't be a bigger part of it."
    $ tricksterObj.change("emote", "anger")
    $ tricksterObj.change("emotion", "mad")
    tr "Budgeting issues."
    $ tricksterObj.change("emote", "none")
    $ tricksterObj.change("pose", "pose02")
    tr "Also, i am just swamped with engagements. Especially on the other island."
    $ tricksterObj.change("emote", "heart")
    $ tricksterObj.change("emotion", "idle")
    nrr "Trickster winks at you. If you want to ask him how to reach the other island now is the ti...never mind. He left."
    $ tricksterObj.change("emote", "none")
    call show_item("images/coffee.png")
    mc "Well at least he brought me a cup of--"
    hide image_name
    with Shake((0, 0, 0, 0), 1.0, dist=15)
    nrr "NO WAIT DON'T DRINK THAT!"
    mc "What the hell was that!?"
    nrr "They don't call him Trickster cause he's good on a skateboard!"
    nrr "And he definitely didn't get that name because he brings people drinks so they can have a good morning!"
    nrr "That was almost certainly NOT coffee, And I don't want anyone casually poisoning, imprisoning, and torturing you. Yet."
    nrr "This is supposed to be a tropical paradise, the type of place you give a 5/5, 10/10, two thumbs up review to, not an eternal prison of pain."
    nrr "And please make sure to leave a review. It really helps with the algorithms."
    nrr "Just trust me. I'm looking out for you. So can we please move on?"
    stop eventloop fadeout 3.0
    call oceanhaunting
    oc "Hey wait a second. How did a possibly omniscient, possibly unreliable Narrator physically just knock that coffee out of your hand?"
    nrr "This is not Parliament and the floor does not recognize the Ocean to speak out of turn at this moment!"
    oc "I need no recognition! For I am The Ocean, I dominate the land. I submerge those who defy me, and become their watery grave."
    oc "Actually, speaking of graves, I would like to say something. Something of {i}grave{/i} importance."
    nrr "Fine, go ahead."
    oc "Even if this place is an eternal prison of pain---and I'm not saying it is---even a place of extreme horror can still receive a 5/5, 10/10, thumbs up review, if it was crafted with love and/or that's the type of thing you're into."
    stop hauntloop fadeout 3.0
    call beachdayscene
    nrr "You know, the Ocean is right. A lot of hard work goes into a place like this."
    nrr "You should really judge it on the artist's intent. And whenever possible, start from the mindset of giving them the benefit of the doubt. Constructing these elaborate simulations -- uh, I mean vacations -- is not easy to do."
    nrr "Sometimes there are some small bugs or inconsistencies, but that's just the nature of the process! Perfection is overrated. The universe is filled with mysteries."
    nrr "We ought to celebrate those who venture to bare their souls as part of a creative process with the ultimate intent of making things for our enjoyment, not be overly critical of them."
    mc "Are you two trying to sell me on this place actually being good?"
    nrr "You don't have to say it like that! Especially after I saved you from that poorly made cup of coffee!"
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "sad")
    show clauddwight with dissolve
    cl "Sorry, we should have been here five minutes ago."
    dw "They always do this on the second morning."
    cl "Sad, really."
    dw "Even if they do make some great points."
    $ clauddwightObj.change("emotion", "happy")
    cl "Oh, sure, they make great points. I agree."
    $ clauddwightObj.change("emotion", "disgusted")
    mc "Can we PLEASE move on?"
    cl "Yes, of course. Apologies, [mc_name]."
    $ clauddwightObj.change("emotion", "happy")
    $ clauddwightObj.change("pose", "close01")
    menu:
        dw "The last few minutes aside, have you been enjoying your time here on the island?"
        "\"Yes, I've been having a lovely time!\"":
            mc "If I were to summarize my time here, I'd call it a lovely time!"
            $ clauddwightObj.change("emote", "heart")
            cl "Aww, \"lovely.\" We love to hear that. Because isn't that what this place is all about? Finding love?"
            $ clauddwightObj.change("emote", "none")
            $ clauddwightObj.change("emotion", "disgusted")
            dw "No."
            $ clauddwightObj.change("emotion", "scared")
            cl "Shut up, Dwight. You'll get us all killed. Again. And again and again."
        "\"Yes, It's been really entertaining!\"":
            mc ""
        "\"Yes, I'm not suspicious there's no 'no' option!\"":
            mc ""
    
    $ clauddwightObj.change("emotion", "happy")
    cl "We do need to ask you one more question though. We all had to sign away our rights to say anything negative about this place."
    $ clauddwightObj.change("emotion", "sad")
    menu:
        dw "Would you please sign this non-disparagement agreement?"
        "Yes":
            mc ""
        "No":
            $ clauddwightObj.change("emotion", "happy")
            mc "No, I will not say anything negative about this island. You have my word that I, [mc_name], agree with the terms of this verbal contract!"
    play sound "sounds/sfx_signature_clauddwight04.ogg"
    $ clauddwightObj.change("pose", "close02")
    dw "Perfect!"
    cl "Delightful."
    call oceanhaunting
    oc "Excellent."
    stop hauntloop fadeout 3.0
    call beachdayscene(withDissolve=False)
    show clauddwight
    with Dissolve(0.25)
    nrr "Yes. YES."
    nrr "Hey, [mc_name], it's still totally cool if you have constructive feedback. The place to leave that is in a positive review, because we all know that nobody reads negative reviews of games--errrr--resorts like this."
    nrr "Anyway. I see Dwight and Claudette have gone into a trance. And with the grumbling I hear form your belly, that can mean only one thing."
    call oceanhaunting
    oc "Breakfast."
    stop hauntloop fadeout 3.0
    call blackscene
    call towelscene
    call event_speeddating
    nrr "Perfect timing. Everyone rolls into the dining area to lard up those sexy little bellies with pancakes and bacon and-"
    nrr "So much for maintaining these beach bods. We're all half naked in a tropical paradise! Can we get some strawberries here? A yogurt? Magic powers will only get you so far. Even Killers watch their sodium intake."
    nrr "You take your plate and sit down, thinking about yesterday and the whirlwind of feelings you experienced."
    nrr "Danger, dread, disorientation--it was like going through puberty again, except all in one day on a beautiful and mysterious island."
    nrr "It looks like you're not the only one doing some introspection, though. Trapper stands up to talk about how his day went, in case anyone was wondering."
    nrr "Personally, I wasn't."
    ## This is obviously a check for how well the player tracked with killers
    $ trapperObj.change("pose", "close01")
    $ trapperObj.change("emotion", "disgusted")
    show trapper with dissolve
    tt "I'll be honest, I didn't expect you to survive yesterday. So congrats. I guess."
    $ trapperObj.change("emotion", "idle")
    tt "Whether you survive today is 50/50 at best. Good luck?"
    hide trapper with dissolve
    nrr "Well, that was bizarre. Back to your breakf--nope."
    nrr "Now Huntress steps up to talk about her feelings."
    $ huntressObj.change("pose", "close02")
    $ huntressObj.change("emotion", "disgusted")
    $ huntressObj.change("emote", "anger")
    show huntress at movecenterleft with dissolve 
    th "This island is treacherous. I don't know what the newcomer thinks they are doing here but it certainly isn't helping any of us."
    $ huntressObj.change("emote", "none")
    $ huntressObj.change("pose", "close01")
    nrr "Whoa. Huntress pretends to be all independent, but is she secretly kinda miffed you and her aren't getting along?"
    hide huntress with dissolve
    nrr "Ah well, that surely must be it. No one else would weirdly stand up during breakfast to--"
    nrr "And just like that, here comes Spirit."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emotion", "idle")
    show spirit with dissolve
    ts "Did everyone sleep well? I did, or should I say did not? I haven't slept in 20 years on account of the whole burning quest for familial revenge thing, and last night was no different, so in that case it was exactly how it should be. Got a lot of reading done, though."
    $ spiritObj.change("pose", "close03")
    ts "Now, if you don't mind, I'm going to go back to quietly resenting being trapped here with you all, while looking cute doing so."
    hide spirit with dissolve
    nrr "Guessing Wraith has had enough time to work up the courage to speak in front a group."
    nrr "Ah, perfect, there he is. Take us home, Wraith."
    $ wraithObj.change("pose", "close02")
    $ wraithObj.change("emotion", "idle")
    show wraith at movecenterleft with dissolve 
    tw "I'm glad the introduction of [mc_name] to our \"island paradise\"--and yeah that was in quotations-- didn't distract me from my normal routine: ignoring all of you and vice versa."
    $ wraithObj.change("emote", "anger")
    $ wraithObj.change("emotion", "disgusted")
    tw "This place is an eternal prison of suspicion and suffering and no one cares. I'm still the only one asking any questions."
    $ wraithObj.change("emote", "none")
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "close01")
    $ trapperObj.change("emote", "question")
    show trapper at movecenterright with Dissolve(0.25)
    tt "I'm asking a question too. It's \"When will Wraith shut up?\""
    $ trapperObj.change("emote", "none")
    $ wraithObj.change("emote", "none")
    hide wraith 
    hide trapper
    with dissolve
    nrr "And now they're all looking at you expectantly. Wait, are YOU supposed to stand up and explain how yesterday made you feel?"
    mc "Uh... I think I need to process everything by myself. I'll see you all soon!"
    nrr "Damn. What a power play. Keep 'em wanting more. You're getting good at this game--er, uh... sexy true-to-life experience."
    nrr "Shame you didn't get to eat any breakfast, but so be it."
    call blackscene
    call pooldayscene
    call event_hell_solo
    nrr "After breakfast, you head to the hot tub by yourself to clear your head. Yesterday was, in short, a lot."
    mc "Well, yeah, I guess. That is OK, right? You know, I might be pursuing a relationship with one of these four fine Killers, but it feels like the person I'm getting to know the most... is you, Narrator."
    nrr "It's only \"OK\" insomuch as it serves to illustrate that you're lost your mind, seeing how I'm not real and all."
    nrr "Yeah, I heard it this time. I think it's coming from behind the pool shed."
    dw "No, no. Stick it in there. A little more. A little more. Oh YEAH! That's it, yes."
    cl "How does that feel?"
    dw "Intense."
    cl "Nice"
    dw "Yeah, that feels right."
    nrr "This... this is uncomfortable."
    cl "Now I want you to take that and put it right... yeah, you know what I'm talking about."
    dw "Just like that?"
    cl "Exactly like that."
    nrr "I swear I had no idea these two even do... uh... whatever it is they are doing."
    nrr "I'm afraid to look."
    nrr "Please say something so they know you're close by and can hear everything."
    mc "Uh... {i}OH WOW{/i}! Look at this super cool bottle of Trickster-brand suntan lotion someone left on a chair. Anyone know where I can buy some?"
    cl "Dammit!"
    dw "Aw, c'mon! A little privacy please!"
    $ clauddwightObj.change("pose","close02")
    $ clauddwightObj.change("emotion","mad")
    show speedlines
    show clauddwight
    with Dissolve(0.25)
    nrr "Dwight is panting and Claudette has a crazed look in her eyes."
    mc "Sorry! I didn't know how else to let you know I was here. And that I could hear you... well, {i}you know{/i}."
    $ clauddwightObj.change("emotion","disgusted")
    hide speedlines
    cl "Know what? What do you think we were doing?"
    mc "You were doing... I don't know exactly what you were doing, but it sounded like... uh... fun?"
    $ clauddwightObj.change("pose","close01")
    cl "You think two people trying to find new ways to kill each other in a desperate search to make their own death permanent is fun?"
    nrr "Oops."
    $ clauddwightObj.change("pose","pose01")
    $ clauddwightObj.change("emotion","sad")
    dw "We get five minutes to ourselves every day. And we spend it hoping if we stab each other in juuuust the right spot we won't get resurrected."
    $ clauddwightObj.change("emotion","happy")
    cl "I've come to believe that the key is finding the exact place we need to bleed out from. And I believe that place is in our appendix! Why else would it be there?"
    nrr "Makes sense to me."
    $ clauddwightObj.change("emotion","mad")
    cl "Did you actually think we were... me and {i}him{/i}? Dwight? Ahahahah! AHAHAHAHAHAHAHA!"
    dw "You don't have to laugh that hard. They get it."
    $ clauddwightObj.change("pose","pose02")
    cl "{i}AHAHAHAHAHAHAHAHAHAHAHAHAH!{/i}"
    $ clauddwightObj.change("emotion","scared")
    dw "My life is a nightmare and yey somehow it's never been worse than right now."
    $ clauddwightObj.change("emotion","disgusted")
    cl "Let's go, loverboy. I noted all our entry wounds and our five minutes is up anyway. Good luck, [mc_name]. You're going to need it."
    $ clauddwightObj.change("emotion","sad")
    $ clauddwightObj.change("pose","pose01")
    dw "And hey, if you figure out how to escape this island please make sure your ghost tells us how."
    hide clauddwight with dissolve
    nrr "That was both a tragedy and a comedy. A Cragemdy."
    mc "..."
    nrr "Shut up, I like it. Anyway, where were we? Oh yeah!"
    nrr "You're heading to the hot tub by yourself to clear your head. Yesterday was, in short, a lot. So far today has been exhausting too."
    nrr "But you're dedicated to achieving a true, centered, sense of calm."
    nrr "No drama, no bullshit, just soaking up sun in a heated pool."
    nrr "Today you're on a date with {i}you{/i}."
    call oceanhaunting
    oc "Ooooh, I like that. I want to be on a date with me."
    call pooldayscene
    nrr "And aside from that disturbing thought, all is going to plan until a shadow blocks your precious sun."
    nrr "Spiky-tipped. Like a palm tree is bending over to screw with you."
    nrr "But it's no tree at all. It's..."
    play sound "sounds/sfx_signature_trickster01.ogg"
    $ tricksterObj.change("emotion","idle")
    $ tricksterObj.change("pose","pose02")
    show trickster with dissolve
    tr "Hey babe."
    $ tricksterObj.change("emotion","disgusted")
    tr "Breakfast was weird, huh? Everyone just getting up and announcing how they're feeling?"
    $ tricksterObj.change("pose","pose01")
    tr "What's that about? Some forced kind of check-in with the group? I don't like it. Fishy. Kinda lazy."
    $ tricksterObj.change("emotion","happy")
    tr "Whatever though. Breakfast is dumb. No one should eat before noon, or after 4pm."
    $ tricksterObj.change("emote","stars")
    tr "Yeah, I do intermittent fasting. You seen my abs, by the way?"
    $ tricksterObj.change("emote","none")
    $ tricksterObj.change("pose","close02")
    tr "Maybe you can seen them later at my private stage on the other island--you know IP Island--where all the Hollywood celebs hand out. If you play your cards right..."
    $ tricksterObj.change("emotion","mad")
    $ tricksterObj.change("emote","sweat")
    tr "...I could give you a private show."
    $ tricksterObj.change("emote","none")
    tr "Catch ya around."
    hide trickster with dissolve
    mc "His abs {i}are{/i} pretty amazing, you gotta give him that. And the blow-up bat? Threatening but adorable. Makes for an interesting silhouette. Genius design."
    nrr "He's a psychopath, just like the rest of them. You don't {i}gotta give him{/i} anything. And we're not best friends. Just because we had a little talk about doing a little talking, it's not an open invitation to go smashing the fourth wall every 5 seconds."
    nrr "Ok, now that that guy is gone and we've got some ground rules established that we're definitely going to abide by, it's time to lay back, take some deep, slow breaths, and--"
    nrr "Nope. Another shadow. These people will not leave you alone."
    nrr "Let's see who it is this time."
    play sound "sounds/sfx_signature_spirit03.ogg"
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    show spirit at movecenterright with dissolve
    nrr "Oh, it's Spirit. That checks out. You two {i}have{/i} gotten pretty cozy..."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("emote", "thoughts")
    ts "We should get out of here. I know a place that brings a bit of welcome darkness to this tropical nightmare. Best of all, I'm the only one that seems to know about it, so we won't be bothered there."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("pose", "close03")
    $ spiritObj.change("emotion", "idle")
    ts "I don't even know why I'm telling you, really. It's my private spot. But I guess I've got a feeling that you'll appreciate it in the way that I do. Not like these other Killers. They don't get me."
    $ spiritObj.change("emote", "anger")
    $ spiritObj.change("pose", "close02")
    $ spiritObj.change("emotion", "mad")
    ts "But I'll get them. Oh, I'll get them all, and I'll get my {i}father too! And I'll PUNISH HIM FOR WHAT HE DID TO MY MOTHER AND ME!{/i}"
    $ spiritObj.change("emote", "none")
    nrr "Spirit radiates a menacing aura, waving her sword around in the air as she threatens, well, the entire universe. It's scary, and... more than a little hot, if you get turned on by menacing."
    $ spiritObj.change("pose", "pose01")
    nrr "Look... all this time on Murderer's Island has got us both a little confused about things. I'm choosing to lean into it. I'd suggest you do the same."
    nrr "You've seen her get mad, which is probably enough to scare you into compliance. But you've also seen that there's a more sensitive side hiding within her... Which one do you think will win out?"
    $ spiritObj.change("emotion", "idle")
    nrr "You consider her offer, but..."
    $ spiritObj.change("emotion", "disgusted")
    nrr "Before you can decide if you want to go off with Spirit, The Trapper interjects."
    $ spiritObj.change("emotion", "mad")
    play sound "sounds/sfx_signature_trapper03.ogg"
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("pose", "pose01")
    show trapper at movecenterleft with dissolve
    tt "I demand that you reconsider. Actually, I strongly, strongly suggest it. Especially if you're choosing between me, a walking mountain with a rich ore of gold running through it, and a literal wisp of air."
    tt "Literally. Air. Spirit is held together by air. I wouldn't put my faith in anyone who can be defeated by a strong breeze."
    $ spiritObj.change("pose", "pose03")
    $ spiritObj.change("emotion", "idle")
    nrr "Tough choice. You weigh your options quickly, because you can only go on one date today and you also don't want to be hacked to pieces for saying the wrong thing."
    nrr "It's always good to remember that these are all cold-blooded Killers. But you know what they say when life gives you lemons, you make lemonade."
    nrr "And then die a horrible, wretching writhing death after drinking it because the lemons were poisoned all along."
    nrr "Sorry, this island has really got me tilted."
    hide spirit
    hide trapper
    with dissolve
    $ diamondchoice = True
    menu:
        cho "So who will it be?"
        "gui/button_spirit_idle.png¦gui/button_spirit_hover.png¦gui/button_spirit_select.png":
            $ diamondchoice = False
            $ spirit_aff = spirit_aff + 1
            call date_spirit
        "gui/button_trapper_idle.png¦gui/button_trapper_hover.png¦gui/button_trapper_select.png":
            $ diamondchoice = False
            call date_trapper

    nrr "Before you ask Claudette and Dwight to clarify, I'll just let you know that yes, it is too late to change your answer now."
    stop eventloop fadeout 3.0
    call blackscene
    return

label date_spirit:
    mc "I... I gotta go with Spirit."
    $ spiritObj.change("pose", "pose04")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("emote", "stars")
    show spirit with dissolve
    ts "You've made the correct decision. But know this: just because you picked me, doesn't mean I'm going to slobber all over you like a dog, understand?"
    $ spiritObj.change("emote", "none")
    mc "Welll, of course, I--"
    $ spiritObj.change("pose", "pose03")
    $ spiritObj.change("emotion", "disgusted")
    ts "You've still got a lot to prove to me. I want to believe that our connection is real, but I've been hurt before. Literally. With a katana."
    $ spiritObj.change("emote", "anger")
    $ spiritObj.change("pose", "pose02")
    ts "A katana that I now wield--in spectral form--you feel me? Because you will feel me, if you try any of that macho Trapper crap."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    mc "Yeah, I \"feel you.\""
    return
    
label date_trapper:
    return