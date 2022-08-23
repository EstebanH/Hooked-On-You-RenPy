
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

    $ trapperObj.change("emote", "none")
    call blackscene
    return