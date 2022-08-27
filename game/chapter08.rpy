label chapter08:
    call towelscene
    call event_dinner
    nrr "What a fun day you've been having! I can see it written all over you face. You're shining! And that's not just the remaining anxious sweat from spending an afternoon counting a psycho killer."
    nrr "No no, you ask really feeling this whole romantic experience. Don't worry, I'll keep your dirty little secrets."
    nrr "But enough gentle ribbing it's time to get back to business! All the... ahem... appetizing singles have arrived for dinner, including Trickster."
    nrr "Wraith is here too."
    nrr "We're not going to do the gag where we cram them all on screen at the same time again, so just believe me... they're all here, and they're just as sexy and demented as you remember them."
    nrr "With your love on the line, everyone is being very careful not to offend you by saying the wrong thing."
    nrr "Congrats, by the way, on getting this far. I'm as surprised as you are that these four are falling for you. No, not because of your personality--but because you just met them {i}yesterday{/i}!"
    nrr "However, since Wraith seems like the biggest longshot to end up holding your heart, he throws caution to the wind and speaks up."
    nrr "It's a pretty small consolation prize for being the least-lover Killer on Murderer's Island, but hey, letting them have this one moment in the spotlight is the least we can do--and heaven knows they won't do any better than that."
    $ wraithObj.change("emote", "dread")
    $ wraithObj.change("pose", "pose01")
    $ wraithObj.change("emotion", "disgusted")
    show wraith with dissolve
    tw "I'm sick of watching everyone else gorge themselves while I'm preoccupied with, you know, trying to get to the bottom of this never-ending nightmare. So tonight, none of that."
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("pose", "close03")
    tw "I'm not really hungry, anyway. So I say we just do a simple salad? Or something? The green kind, not the mayo kind. Mayo is gross."
    tw "I'm fine with just lettuce, it doesn't have to be fancy."
    $ wraithObj.change("emote", "sweat")
    $ wraithObj.change("emotion", "sad")
    tw "Not iceberg though, it has no nutritional value."
    $ wraithObj.change("emote", "none")
    hide wraith with dissolve
    nrr "Letting Wraith choose was a mistake. That's on all of us."
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "sad")
    show clauddwight with dissolve
    dw "Dinner will be served shortly. But certain... power brokers... would like to know about your day."
    $ clauddwightObj.change("emotion", "happy")
    cl "Would you like to share your day with the rest of the group?"
    nrr "You've had an interesting day, that's for sure. But how will you describe it to the others? Say too much or too little and it could affect your standing with the group."
    mc "..."
    hide clauddwight with dissolve
    menu:
        cho "Ok, but don't just sit there saying nothing. Nothing is not an option."
        "Be coy":
            mc ""
        "Gush about your date":
            $ spiritObj.change("pose", "pose03")
            $ spiritObj.change("emotion", "disgusted")
            show spirit with dissolve
            mc "I wish you could all get to meet the real Spirit. She has a beautiful soft side and you'd all get to see it if you were a bit nicer to her."
            $ spiritObj.change("pose", "close03")
            nrr "Spirit looks totally horrified. I promise she doesn't want people paying her any more attention. She's just trying to do her own thing, not fit into this Killer Club."
            $ spiritObj.change("pose", "pose03")
            $ spiritObj.change("emotion", "mad")
            ts "Seriously? Did you listen to a single thing I said today?"
            $ spiritObj.change("emote", "anger")
            ts "{i}IT SEEMS CLEAR TO ME THAT YOU DID NOT{/i}!"
            $ spiritObj.change("emote", "none")
            hide spirit with dissolve
    
    $ clauddwightObj.change("emotion", "idle")
    $ clauddwightObj.change("pose", "pose01")
    show clauddwight with dissolve
    nrr "Dwight and Claudette bring out dinner. Everyone eats in silence. No one trusts anyone now, and they are all very tired. Oh, wait. No. Sorry. That's a dreary supernatural horror thriller set in Antarctica, not a charming parody dating sim set in... an undisclosed tropical paradise."
    $ clauddwightObj.change("emotion", "sad")
    cl "Boney appetite."
    mc "Don't you mean \"bon\"?"
    $ clauddwightObj.change("emotion", "disgusted")
    $ clauddwightObj.change("emotion", "close02")
    dw "No. Almost everything we serve has a lot of bones in it. Even the vegetables."
    $ clauddwightObj.change("emotion", "mad")
    cl "Impossible to avoid on this island."
    hide clauddwight with dissolve
    nrr "Everyone eats without speaking."
    nrr "Tensions are rising. Both of the sexual and deadly variety."
    $ clauddwightObj.change("emotion", "sad")
    $ clauddwightObj.change("pose", "pose02")
    show clauddwight with dissolve
    nrr "When everyone finishes, Dwight and Claudette come back to clean up the table. They linger around you as they pick up your plate, take your napkin, and dust crumbs off of the table."
    $ clauddwightObj.change("emotion", "pose01")
    menu:
        cho "What would you like to say to the servants?"
        "Thank them":
            $ clauddwightObj.change("emotion", "happy")
            $ clauddwightObj.change("emote", "stars")
            mc "Your top-notch service is much appreciated."
            $ clauddwightObj.change("emote", "none")
        "Ignore them":
            mc "..."
    
    $ clauddwightObj.change("emotion", "idle")
    $ clauddwightObj.change("emotion", "pose02")
    cl "Everyone, if you would please be so kind as to follow us to the fire pit, we'd greatly appreciate it. We're been told something big is going to happen. Something that will change everything."
    $ clauddwightObj.change("emotion", "happy")
    dw "You can go willingly or you can go unwillingly. You have no choice. Tough cookies."
    $ clauddwightObj.change("emotion", "sad")
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("emotion", "pose01")
    $ trapperObj.change("emote", "anger")
    show trapper behind clauddwight at moveleft with dissolve
    tt "Did you have a choice on how you said that, dweeb?"
    $ trapperObj.change("emote", "none")
    dw "... Yes, and I immediately regret how I did."
    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose03")
    $ spiritObj.change("emotion", "idle")
    show spirit at movecenterright with dissolve
    ts "Good. Something needs to change around here. Fire is rebirth."
    $ huntressObj.change("pose", "pose03")
    $ huntressObj.change("emotion", "idle")
    show huntress behind spirit at moveleft with dissolve
    th "Fire illuminates the soul."
    $ wraithObj.change("pose", "pose03")
    $ wraithObj.change("emotion", "scared")
    $ wraithObj.change("emote", "sweat")
    $ huntressObj.change("emotion", "disgusted")
    $ trapperObj.change("emotion", "disgusted")
    $ spiritObj.change("emotion", "disgusted")
    show wraith behind spirit at movecenterleft with dissolve
    $ wraithObj.change("emote", "none")
    tw "I hope the firs isn't too smoky. Smoke hurts my eyes. I have pretty sensitive eyes. I'm also horribly afraid of it. The fire, I mean--not my eyes. Because of childhood trauma. Involving fire."
    $ wraithObj.change("emotion", "disgusted")
    $ huntressObj.change("emotion", "idle")
    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    nrr "And finally everyone starts moving toward the Fire Pit, if only to get away from Wraith's complaining."
    call blackscene
    call campfirescene
    $ renpy.music.set_volume(0,3.0,"music")
    nrr "You take a seat on a comfortable log, feeling the fire's heat against your skin, and wait for other Killers to take their places, wondering who will want to tell a story this time."
    nrr "Will Narrator tell a story? I bet they're got a stunningly creative mind. \"Hey,\" you think. \"Are they allowed to simple place thoughts in my mind like this? Doesn't seem fair.\""
    nrr "Everyone makes their way in, but something unexpected happens: nothing. Nothing happens. Something almost always seems to be happening here, so nothing is probably not a great sign."
    $ huntressObj.change("emotion", "idle")
    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    $ wraithObj.change("emotion", "idle")
    $ huntressObj.change("pose", "pose01")
    $ trapperObj.change("pose", "pose01")
    $ wraithObj.change("pose", "pose01")
    $ spiritObj.change("pose", "pose01")
    show huntress
    show wraith
    show trapper
    show spirit
    with Dissolve(0.25)
    mc "..."
    $ renpy.music.set_volume(1,3.0,"music")
    call event_speeddating
    nrr "Oh, cool. And now everyone is looking at you."
    nrr "So, ya know, do something."
    $ trapperObj.change("emotion", "disgusted")
    $ spiritObj.change("emotion", "disgusted")
    mc "Should I pick someone to tell a story? Or we could play charades? Boggle?!"
    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    $ wraithObj.change("emotion", "happy")
    $ wraithObj.change("emote", "question")
    tw "Um, well... we were actually thinking... why don't {i}you{/i} tell us a story?"
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("pose", "pose02")
    nrr "Wraith points his spine and skull-staff-thingamajig at you."
    nrr "You duck out of its way. Who knows what that thing can do. Probably shoots lasers."
    hide wraith with dissolve
    $ trapperObj.change("emotion", "disgusted")
    tt "Try not to bore us."
    hide trapper with dissolve
    $ huntressObj.change("emotion", "happy")
    th "We're just VERY interested in you!"
    $ spiritObj.change("emote", "anger")
    $ spiritObj.change("emotion", "disgusted")
    ts "Don't speak for me, Huntress."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    hide spirit with dissolve
    nrr "How you can't tell if you're warm from the fire or if it's your nerves heating up."
    $ wraithObj.change("emotion", "scared")
    show wraith at movecenterleft with dissolve
    tw "I know that the fire is... {i}right here{/i}, but maybe if we stop talking about it all the time we can start to pretend it's not here and doesn't, you know... threaten to burn us all alive."
    hide wraith with dissolve
    menu:
        nrr "He's... not supposed to hear me. Get out of here, Wraith. [mc_name] was about to make an important decision about telling a story or not."
        "\"Fine, I'll tell a story\"":
            mc "Sure! I'm game to tell a story."
        "\"I'm not the storytelling type\"":
            mc ""
    play sound "sounds/sfx_signature_trickster01.ogg"
    $ tricksterObj.change("emotion", "happy")
    $ tricksterObj.change("pose", "pose01")
    show trickster with dissolve
    tt "I hope it's a mystery!"
    hide trickster with dissolve 
    
    menu:
        nrr "Uh, Ok? So what type of story do you want to tell?"
        "Romance":
            mc "I'll tell a romantic story."
            $ spiritObj.change("pose", "pose01")
            $ spiritObj.change("emotion", "happy")
            $ spiritObj.change("emote", "question")
            show spirit at movecenterright with dissolve
            ts "About two lovers who take poison together and die foaming at the mouth?"
            $ spiritObj.change("emotion", "idle")
            $ spiritObj.change("emote", "none")
            $ huntressObj.change("pose", "pose02")
            $ huntressObj.change("emotion", "happy")
            $ huntressObj.change("emote", "question")
            show huntress at moveleft with dissolve
            $ huntressObj.change("emote", "none")
            th "Or about two strong hunters who meet when they both try to bludgeon the same wily wolverine?"
            $ huntressObj.change("emotion", "idle")
            mc "Not quite. It's about my parents. they met at a party in college. He was hosting, she'd been dragged there by some friends."
            $ huntressObj.change("pose", "pose01")
            mc "They couldn't have been more different. And yet... as the night went on, they were drawn to each other."
            mc "She made fun of his taste in music and he took an interest in her major, Women's Studies!"
            mc "They were married within two months."
            $ trapperObj.change("emotion", "disgusted")
            $ trapperObj.change("pose", "pose01")
            show trapper behind spirit at moveright with dissolve
            tt "Bit soon to know if you can trust someone, don't you think?"
            $ wraithObj.change("emotion", "happy")
            $ wraithObj.change("pose", "pose03")
            $ wraithObj.change("emote", "stars")
            show wraith behind spirit at movecenterleft with dissolve
            tw "It's so sweet."
            $ wraithObj.change("emote", "none")
            mc "Exactly. I learned a lot about love from them. If you know, you know. Some people don't need years to get acquainted with their partner."
            $ wraithObj.change("emotion", "idle")
            $ spiritObj.change("pose", "pose03")
            $ trapperObj.change("emotion", "mad")
            $ trapperObj.change("pose", "pose03")
            mc "Love could spark from a mere look across a campfire."
            nrr "Now you've got their attention. Each Killer is furiously attempting to catch your eye from across the firepit."
            nrr "Except for Trickster, who has wandered over to the bar and is loudly playing his own music on headphones to drown you out."
        "Adventure":
            mc ""
        "Action":
            mc ""

    $ huntressObj.change("emotion", "idle")
    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    $ wraithObj.change("emotion", "idle")
    $ huntressObj.change("pose", "pose01")
    $ trapperObj.change("pose", "pose01")
    $ wraithObj.change("pose", "pose01")
    $ spiritObj.change("pose", "pose01")
    nrr "Ok, that was not a very good story. I don't mean to insult you, but it was actually quite bad. Sorry, but this Narrator keeps it real. We can't just end there."
    nrr "So who else would you like to hear a story from tonight?"
    call event_storytime
    $ diamondchoice = True
    menu:
        cho "You look from killer to killer, trying to decide who might be the most entertaining."
        "gui/button_spirit_idle.png¦gui/button_spirit_hover.png¦gui/button_spirit_select.png":
            $ diamondchoice = False
            call storytime_spirit
        "gui/button_trapper_idle.png¦gui/button_trapper_hover.png¦gui/button_trapper_select.png":
            $ diamondchoice = False
            call storytime_spirit
        "gui/button_wraith_idle.png¦gui/button_wraith_hover.png¦gui/button_wraith_select.png":
            $ diamondchoice = False
            call storytime_spirit
        "gui/button_huntress_idle.png¦gui/button_huntress_hover.png¦gui/button_huntress_select.png":
            $ diamondchoice = False
            call storytime_spirit

    stop eventloop fadeout 3.0
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    show clauddwight with dissolve
    dw "How was storytime? A lot of people like to take pot-shots at sequels, but I think every good story deserves a follow-up."
    $ clauddwightObj.change("pose", "pose01")
    cl "When you think it's the end, the sequel is almost never as rewarding as the original... that's why I'm much more a fan of the episodic style of storytelling."
    cl "Knowing it's a series takes a lot of pressure off of any individual installment, and builds a greater sense of community between audience and creator."
    $ clauddwightObj.change("pose", "close01")
    $ clauddwightObj.change("emotion", "idle")
    dw " Tell me, [mc_name] if you could delete any sequel from existence, what would it be?"
    call event_tikitiki
    $ clauddwightObj.change("emotion", "disgusted")
    cl "Don't answer that, we don't actually care. We're just here to make sure that we seamlessy move on to the next segment of the evening."
    dw "God forbid my small talk get in the way of a romantic twilight moment!"
    $ clauddwightObj.change("emotion", "mad")
    cl "Dwight, I'm gonna need you to shut your yap-trap. You know that we need to get back to... that thing we do whenever we're not on screen."
    $ clauddwightObj.change("emotion", "disgusted")
    dw "OK OK! You have fun tonight, and try not to--\"wink wink\"--end up dead!"
    mc "Why did you say the words \"wink wink\" out loud and what kind of double entendre are you getting at with the \"end up dead\" thing?"
    $ clauddwightObj.change("emotion", "idle")
    cl "Dwight is physically incapable of winking. Not since... the accident. And you {i}do{/i} know that all of these people are despicable criminals with double-digit kill counts, right?"
    $ clauddwightObj.change("emotion", "sad")
    $ clauddwightObj.change("pose", "pose01")
    dw "Well, except for Spirit. She really doesn't belong here. She's strictly a victim, not a perpetrator! No wonder she's pissed."
    hide clauddwight
    $ trapperObj.change("emotion", "happy")
    $ spiritObj.change("emotion", "disgusted")
    $ trapperObj.change("pose", "pose01")
    $ spiritObj.change("pose", "pose01")
    show spirit at movecenterright
    show trapper behind spirit at moveright
    with dissolve
    tt "Did I hear somebody trash-talking Spirit? Deal me in."
    $ trapperObj.change("emotion", "mad")
    $ spiritObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose03")
    $ trapperObj.change("emote", "stars")
    tt "What do you say we take this talk to the hot tub so I can soak this bod while I roast that ghost with some killer hot takes?"
    $ trapperObj.change("emote", "none")
    $ trapperObj.change("emotion", "disgusted")
    $ wraithObj.change("emote", "sweat")
    $ wraithObj.change("pose", "pose02")
    $ wraithObj.change("emotion", "scared")
    show wraith behind spirit at movecenterleft with dissolve
    tw "Please, enough talk of \"burns,\" things that are \"lit,\" or getting \"blazed.\" It enough that these activities have to be set next to a literal fire, must I be surrounded by figurative flames as well?"
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("emotion", "idle")
    tw "What if we turned and ran as far away from this place as we could, just you and me?"
    $ wraithObj.change("emotion", "disgusted")
    $ huntressObj.change("emotion", "disgusted")
    $ trapperObj.change("emotion", "idle")
    $ huntressObj.change("pose", "pose01")
    $ trapperObj.change("pose", "pose01")
    show huntress behind wraith at moveleft with dissolve
    th "On those spindly legs? You'd probably tire before you got too far. If it's running away to someplace more secluded [mc_name] is after, they should obviously join me. Have you seen these legs? Pure power."
    $ huntressObj.change("emotion", "happy")
    th "Not that my walk speed really reflects my giant stature... but that's because I choose to move slowly for stealthy reasons. It's my own choice and it's completely logical!"
    $ huntressObj.change("emotion", "disgusted")
    $ spiritObj.change("emotion", "disgusted")
    $ wraithObj.change("emotion", "idle")
    $ spiritObj.change("emote", "question")
    ts "Why is everyone so obsessed with comparing themselves to each other and creating drama? I'm so over all that."
    $ spiritObj.change("emote", "none")
    ts "Why is everyone so obsessed with comparing themselves to each other and creating drama? I'm over all that."
    ts "Don't you get it? Society wants to trick you into fighting with each other so that corporations can swoop in and sell you fake solutions to all your fabricated problems!"
    $ spiritObj.change("pose", "pose03")
    $ spiritObj.change("emotion", "idle")
    ts "I'll be sitting in the shade and drinking something locally sourced while thumbing through a public domain novella printed on recycled paper because I refuse to play {i}their{/i} game anymore!"
    $ huntressObj.change("emotion", "idle")
    $ trapperObj.change("emotion", "happy")
    $ spiritObj.change("emotion", "disgusted")
    $ wraithObj.change("emotion", "disgusted")
    $ huntressObj.change("pose", "pose01")
    tt "It's like she's actively trying to be as unappealing as possible. Does it REALLY turn anyone else on or just me?"
    nrr "Despite Trapper's... insatiable appetite, it seems his attention--along with the attention of everyone else--is still on you. For the moment."
    $ wraithObj.change("emote", "question")
    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    $ wraithObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose01")
    tw "If you could, I dunno, just pick one of us maybe we could all move on with our lives, or, um, you know... some special projects we might have going?"
    $ wraithObj.change("emote", "none")
    nrr "You heard him. Who will it be? Who will you head off with for an evening activity?"
    nrr "I'm just saying... you may not get a ton of chances to date around like this before your time on Murderer's Island comes to a close."
    nrr "And no, I'm not satisfied with that name, either, but with this streaming reality TV dating show boom happening, it's pretty much all that wasn't taken."
    
    $ diamondchoice = True
    menu:
        cho "Which Killer will you pick? And yes, we're back to excluding Trickster, because, ugh, that guy."
        "gui/button_spirit_idle.png¦gui/button_spirit_hover.png¦gui/button_spirit_select.png":
            $ diamondchoice = False
            call finaldate_spirit
        "gui/button_trapper_idle.png¦gui/button_trapper_hover.png¦gui/button_trapper_select.png":
            $ diamondchoice = False
            call finaldate_spirit
        "gui/button_wraith_idle.png¦gui/button_wraith_hover.png¦gui/button_wraith_select.png":
            $ diamondchoice = False
            call finaldate_spirit
        "gui/button_huntress_idle.png¦gui/button_huntress_hover.png¦gui/button_huntress_select.png":
            $ diamondchoice = False
            call finaldate_spirit
    call blackscene
    return 


label finaldate_spirit:
    hide trapper
    hide wraith
    hide huntress
    with Dissolve(0.25)
    mc "Spirit?"
    show spirit at slidetocenter
    $ spiritObj.change("emotion", "disgusted")
    ts "Oh... you picked me... yaaay..."
    $ spiritObj.change("emotion", "scared")
    $ spiritObj.change("emote", "sweat")
    ts "Sorry, that was rude of me. I despite phoniness, so I should be honest with you."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    ts "You make for interesting company, and I love the idea of winning over these other Killers at all costs, even when I hate the game and the price... but I had a long day."
    ts "Floating, subverting expectations, grinding my teeth as I imagine sweet sweet revenge--it takes a lot out of me."
    $ spiritObj.change("pose", "pose03")
    ts "So don't stop bringing your A-game, alright? It might seem like I hate everything, and getting to really know who I am is an impossible task not worth trying, but too bad."
    ts "You won't know unless you search deep inside yourself and bring everything you've got."
    ts "Or just say the extract right thing at the right time and melt my cold heart in an instant. I don't know the rules here any better than you do."
    $ spiritObj.change("emote", "thoughts")
    ts "See you at the bar, I guess."
    $ spiritObj.change("emote", "none")
    return 

label storytime_spirit:
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("emote", "dread")
    ts "I suppose I could tell a story. I don't really want to, but anything I say is sure to be better than whatever you get out of anyone else in this group."
    $ spiritObj.change("emote", "none")
    hide trapper
    hide wraith
    hide huntress
    with Dissolve(0.25)
    $ spiritObj.change("emote", "happy")
    $ spiritObj.change("pose", "close01")
    show spirit at movecenter
    ts "Like all good stories, I stole this one from someone in the past who is dead now and can't do anything about it."
    $ spiritObj.change("emote", "scared")
    ts "It's called the \"The Bride\"--err, technically, I suppose, \"The Fiancée\""
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close03")
    ts "One winter, a young couple decided that the next spring they would be married."
    $ spiritObj.change("emote", "stars")
    $ spiritObj.change("emotion", "happy")
    ts "The two were madly in love, and could not wait for the snow to melt, so they could join in matrimony and unite their souls for eternity."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    ts "Per the latest bridal trends, they decided to have their webbing ceremony at the edge of the woods by a beautiful shabby-chic farmhouse."
    ts "Together they spent months planning the details of the wedding. The two created invitations figured out seating arrangements, and tasted one hundred cakes before settling on the perfect one."
    $ spiritObj.change("emote", "exclamation")
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "close01")
    ts "They chose lilikoi, by the way. So fancy."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    ts "When it came time to figure out the decorations, however, the bride--err, the fiancée, I guess, since she wasn't actually married yet--wanted to take the lead and set the style."
    $ spiritObj.change("emotion", "disgusted")
    ts "After all, her boyfriend had been wearing cargo shorts and open-toe sandals for pretty much their entire relationship, so he was definitely not to be trusted."
    $ spiritObj.change("emotion", "happy")
    ts "Having decided on such a lovely natural setting for the ceremony, the fiancée decided that she would create unique floral arrangement from the local wildflowers that surrounded the farmhouse."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close03")
    ts "As soon as the sun rose on the first day of spring, she set off into the woods."
    ts "Each dat, she spent hours mapping out where the best blooms could be found, and prepared to pick them herself the morning of the wedding, so that they'd be at the height of their freshness and beauty."
    $ spiritObj.change("emotion", "happy")
    ts "Enamored with the incredible variety of flowers in the woods she surveyed, the bride--err, the fiancée, since they had not yet been married--became obsessed with knowing just how many there were, so that she could choose the absolute best."
    $ spiritObj.change("emotion", "idle")
    ts "When the fateful morning of her big day finally came, the fiancée told her husband-to-be that she had one final errand before the wedding."
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emotion", "happy")
    ts "Excited for the ceremony to come, she dressed in her beautiful white gown and set off into the woods to gather flowers. Treading carefully, she followed her route, selecting only the best stems and collecting them in a basket."
    $ spiritObj.change("emote", "dread")
    $ spiritObj.change("emotion", "disgusted")
    ts "However, when she came upon a once familiar clearing, something was not as she expected."
    $ spiritObj.change("emote", "none")
    ts "Somehow, it was more beautiful now than it had ever been before. And just on the edge of her view, was a new bush filled with blossoms so vibrant and colorful, she became dizzy just looking at them."
    $ spiritObj.change("emotion", "idle")
    ts "But the fiancée ignored her sudden spell and pressed ahead, scooping up flower after flower. And every time she did, she noticed just further ahead, impossibly, even more beautiful blossoms."
    ts "Carried by the sweet fragrance of spring air, the bride--err, the fiancée--crept farther and farther into the woods, until she turned a corner, stepped over a mossy fallen tree trunk and realized... she had been here before."
    $ spiritObj.change("pose", "close03")
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("emote", "dread")
    ts "But this wasn't the clearing she remembered, or, at least, not how she remembered it. The flowers were suddenly overripe, decaying, falling from their stems into festering moldy piles on the floor."
    $ spiritObj.change("emote", "none")
    ts "Where bees had been, now only flies buzzed. Where the scene of flowers had once intoxicated her, the odor of mildew now made her sick."
    $ spiritObj.change("emotion", "sad")
    ts "She turned and looked back, but the path was dark."
    ts "Into a shadowy glen she walked, and walked, and walked..."
    ts "That day, as guests gathered at the farmhouse, the fiancée was nowhere to be seen. Her friends, family, and love began to look for her, but to no avail."
    ts "They searched the pasture, the tree line, and into the forest, but there were no beautiful wildflowers or young lovers to be seen..."
    ts "...just old dead trees, trampled vines, and moss-covered rocks."
    $ spiritObj.change("pose", "close01")
    ts "The fiancée stayed a fiancée, for eternity. Always wandering, looking for fresher blooms to clip, but never finding them."
    $ spiritObj.change("emotion", "idle")
    mc "Distracted by a never-ending search for perfection, unable to see that you are loved for who you are..."
    hide spirit with dissolve
    mc "Out there all alone..."
    mc "I thought it was beautiful and sad."
    nrr "Just like someone we know..."
    return