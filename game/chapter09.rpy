label chapter09:
    call barnightscene
    call event_bloodconfident
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    show clauddwight at movecenterleft
    nrr "You arrive at the bar to find Dwight and Claudette both holding cocktail shakers, surrounded by a bevy of bottles for assorted boozes."
    dw "Who's ready..."
    cl "To get waaaaaaasted?!?!"
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    show spirit behind clauddwight at movecenterright with dissolve
    ts "Well, I don't drink, so... not me."
    mc "You really don't drink? Ever? Is that a like... because it will just fall out a hole in your stomach thing, or..."
    $ spiritObj.change("emotion", "mad")
    $ spiritObj.change("emote", "sparks")
    ts "I don't drink alcohol because alcohol is poison of the body and the mind, and I don't need to act like a fool to have a good time thing."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "disgusted")
    dw "Then why did you choose a mixology lesson as your romantic nighttime activity?"
    $ clauddwightObj.change("emotion", "happy")
    cl "Everyone knows this kind of date is just an excuse to get loaded up on booze and make terrible decisions."
    dw "It's true, not a single person has ever learned {i}anything{/i} at one of these things."
    cl "Dwight, now that's not true. You learned how to tie a cherry knot in a stem using only your tongue..."
    dw "Woaaah woah. Who ordered the soda with a splash of my private business? Because that's off-menu!"
    $ clauddwightObj.change("emotion", "idle")
    nrr "Welp, I know what I'm drinking to forget tonight."
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "pose02")
    ts "Mixology is a real thing, and it doesn't require alcohol to be interesting. I'll have you all know that I worked at a restaurant before I was violently executed."
    $ clauddwightObj.change("emotion", "sad")
    cl "...by your father..."
    $ spiritObj.change("emote", "dread")
    dw "...on whom you will have your bloody vengeance. Right, right. Well, so be it."
    $ spiritObj.change("emote", "none")
    $ clauddwightObj.change("emotion", "happy")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose01")
    menu:
        cl "How about you, [mc_name]? Do you drink?"
        "Booze it up":
            mc ""
        "Stay sober":
            $ clauddwightObj.change("emotion", "idle")
            $ spiritObj.change("pose", "pose03")
            mc "I've got the impression that tonight will be a night I want to remember perfectly, so I'm gonna pass on the alcoholic drinks."
            $ spiritObj.change("emote", "exclamation")
            $ spiritObj.change("emotion", "happy")
            ts "{i}Here, here{/i}!"
            $ spiritObj.change("emote", "none")
            ts "Alcohol is a false escape. Besides, it's not like sober people can't have fun."
            nrr "You watch as Spirit picks up a plump cherry and roughly stabs a little plastic sword through it."
            nrr "Cherry juice splatters everywhere and its little fruity guts flop out onto Spirit's lap."
            ts "Oopsie!"
            $ spiritObj.change("emote", "thoughts")
            ts "One of the upsides of wearing black: it hardly shows stains!"
            $ spiritObj.change("emote", "none")
            nrr "No take-backsies."
    $ clauddwightObj.change("emotion", "happy")
    $ spiritObj.change("pose", "pose03")
    $ spiritObj.change("emotion", "idle")
    menu:
        dw "So, lovebirds, what drink shall we make?"
        "Fancy Beer":
            mc ""
        "Zombie":
            mc ""
        "Bloody Mary":
            mc ""
        "Dark & Stormy":
            mc "How about a dark and stormy drink for my dark and stormy date?"
            call mood_excitement(withDissolve = False)
            show clauddwight at movecenterleft
            $ spiritObj.change("emote", "heart")
            $ spiritObj.change("emotion", "happy")
            $ spiritObj.change("pose", "close03")
            show spirit at slidetomovecenter
            with dissolve
            ts "Ok, that one is cute."
            $ spiritObj.change("emote", "none")
            call barnightscene(withDissolve = False)
            $ clauddwightObj.change("pose", "pose02")
            show clauddwight at movecenterleft
            show spirit at movecenter
            with dissolve
            dw "Please, allow us to demonstrate how to dark and stormy is made!"
            cl "First, rum--or in this case rum extract and a bit of apple juice--is poured over ice..."
            dw "And then fresh ginger beer is added in..."
            cl "Garnish with a lime wheel..."
            dw "And drink. The end."
            $ clauddwightObj.change("pose", "pose01")
            cl "Do you think you're up to the challenge of replicating this recipe, [mc_name]?"
            mc "Replicating... rum-substitute and ginger beer over ice?"
            $ clauddwightObj.change("emotion", "mad")
            dw "DON'T FORGET THE LIME WHEEL!"
            $ clauddwightObj.change("emotion", "sad")
            mc "Rum-substitute and ginger beer over ice... with a lime wheel."
            $ clauddwightObj.change("emotion", "idle")
            cl "Not sure I appreciated your tone, but yes, you got it! You're a natural. A sassy natural. You and Dwight might have more in common than--"
            mc "Don't you dare."
            hide clauddwight with dissolve
            nrr "Spirit seems to be in a lovely mod as she sips her dark and stormy. She's not even rolling her eyes at your pretty behaviour."
            nrr "On cue, a literal dark storm begins to make its way in from the ocean. You taste your own dark and stormy as you watch the clouds approach. It's quite refreshing."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close04")
    ts "Isn't this fun?"
    mc "Honestly... it's the most drama-free fun I've had since I got here."
    ts "And since you picked a simple but delicious drink, we've got plenty of time left to relax."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("emote", "sweat")
    ts "Wanna make out a little?"
    $ spiritObj.change("emote", "none")
    nrr "You breath in a sip of your drink and immediately begin coughing. Before you can get a \"YES\" out..."
    $ spiritObj.change("emotion", "scared")
    $ spiritObj.change("pose", "pose04")
    nrr "Lightning strikes a palm tree on the beach and it immediately starts a fire. The activity ends abruptly as Claudette and Dwight usher the two of you away from the bar."
    call blackscene
    call volleyballsunsetscene
    nrr "The gangs all together again on the volleyball court. Seems like only yesterday you were sitting on the sidelines watching everyone get sweaty."
    nrr "That's because it was? Oy. Feels like I've been here a lot longer than that actually."
    nrr "It's so late that the sun is already beginning to rise. Better get this over with quickly so that I--I mean you--can get some beauty rest."
    nrr "I do not recommend the eternal damnation of perpetual narratordom."
    nrr "Good thing you've really used your time well since then."
    nrr "Really getting to know the gang. The brain, the mogul, the basket case, the psychotic bunny girl. You know, the four types of people."
    nrr "Anyway, everyone is gathered on the volleyball court for a NEW type of game: Pitch your dream and see who [mc_name] chooses!"
    call event_quiz
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    show clauddwight at movecenterleft with dissolve
    dw "Who's ready for a round robin?"
    $ huntressObj.change("emotion", "happy")
    $ huntressObj.change("pose", "pose01")
    show huntress behind clauddwight at movecenterright with dissolve
    th "How round are we talking?"
    $ huntressObj.change("emotion", "scared")
    $ huntressObj.change("emote", "sweat")
    $ clauddwightObj.change("emotion", "mad")
    dw "No, not to eat, Huntress."
    $ huntressObj.change("emote", "none")
    hide huntress
    $ clauddwightObj.change("pose", "close01")
    $ clauddwightObj.change("emotion", "happy")
    with dissolve
    cl "Each Killer gets two minutes to tell you all about the dream date they have planned for you tomorrow!"
    $ clauddwightObj.change("emotion", "idle")
    dw "In no particular order! Which is a weird thing to mention, right? Almost like the order DOES matter. Wraith, why don't you go first. You look like you'd hate that."
    $ clauddwightObj.change("emotion", "disgusted")
    $ clauddwightObj.change("pose", "pose01")
    cl "Stop talking."
    $ clauddwightObj.change("emotion", "idle")
    dw "Sorry. Anyway, Wraith?"
    $ wraithObj.change("emotion", "happy")
    $ wraithObj.change("pose", "close03")
    $ wraithObj.change("emote", "sweat")
    show wraith at movecenterright with dissolve
    $ wraithObj.change("emote", "none")
    tw "Well... uh, I don't know, I'd really prefer to just tell [mc_name] privately."
    $ wraithObj.change("emotion", "disgusted")
    $ clauddwightObj.change("emotion", "happy")
    dw "Umm... I don't really know how that's going to work with these game mechanics."
    cl "What if you just whispered it to [mc_name]?"
    nrr "Wraith considers this for a long moment. Too long."
    $ clauddwightObj.change("emotion", "idle")
    $ wraithObj.change("pose", "close01")
    tw "That's fine."
    hide clauddwight with dissolve
    nrr "Without moving, Wraith lowers his voice to a barely audible whisper."
    $ clauddwightObj.change("emotion", "disgusted")
    $ wraithObj.change("pose", "close02")
    tw "Tomorrow we have to find my bell."
    tw "And then I can finally tell you about what I've been working on."
    tw "It's going to be really special. The kind of thing where we will really bond."
    tw "And maybe finally get off this island."
    $ clauddwightObj.change("emotion", "happy")
    tw "And maybe then we can go on a real date."
    $ wraithObj.change("emote", "thoughts")
    tw "..."
    $ wraithObj.change("emote", "none")
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "disgusted")
    show clauddwight behind wraith at movecenterleft with dissolve
    dw "...uhh... you done? Is that it?"
    nrr "Wraith nods, proud."
    hide wraith with dissolve
    $ clauddwightObj.change("emotion", "idle")
    cl "Great. Huntress, why don't you take it from here?"
    hide clauddwight
    show huntress at movecenterright 
    with dissolve
    $ huntressObj.change("emotion", "idle")
    $ huntressObj.change("pose", "close03")
    th "Tomorrow morning I'm planning on a nice atmospheric breakfast on the yacht. Don't worry, Trapper won't even know it's gone."
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose01")
    show trapper at moveleft with dissolve
    tt "What was that?"
    $ trapperObj.change("emotion", "disgusted")
    $ huntressObj.change("emotion", "scared")
    $ huntressObj.change("emote", "sparks")
    th "Nothing. Go away."
    $ huntressObj.change("emote", "none")
    $ huntressObj.change("emotion", "happy")
    th "Then... boy oh boy! I've got such an adventure planned. It involves hunting for treasure."
    show clauddwight behind huntress at movecenterleft with dissolve
    $ clauddwightObj.change("emotion", "happy")
    $ clauddwightObj.change("pose", "pose01")
    $ huntressObj.change("emotion", "idle")
    $ huntressObj.change("pose", "close02")
    $ huntressObj.change("emote", "stars")
    dw "What kind of treasure we lookin' for?"
    $ huntressObj.change("emote", "none")
    th "Guess you'll have to pick me to find out. Let me tell ya', it's primo stuff."
    $ clauddwightObj.change("emotion", "idle")
    $ huntressObj.change("emotion", "happy")
    th "Now if you don't mind, I've got to start preparing, because it's clear already that you're going to pick me."
    cl "Confident. Mysterious. I like it."
    $ huntressObj.change("emotion", "sad")
    cl "Trapper, without further ado, would you like to make us all uncomfortable by pushing the boundaries of what's acceptable not only in polite society but within the narrative of this in-world event and also the larger meta-narrative of a Dead by Daylight dating experience?"
    dw "Sometimes you just gotta say it."
    hide clauddwight
    $ trapperObj.change("emotion", "happy")
    $ trapperObj.change("pose", "close01")
    show trapper at movecenterright
    with dissolve
    tt "Why yes, thank you, I'd love to."
    $ trapperObj.change("emotion", "mad")
    tt "So, [mc_name], you're thinking of picking me? Well, this is your final warning. Pick me and be punished... and rewarded?"
    $ trapperObj.change("emotion", "disgusted")
    $ trapperObj.change("pose", "close03")
    $ trapperObj.change("emote", "sweat")
    tt "Tomorrow will suck. Probably. I'm not an easy guy to get along with. I know that."
    $ trapperObj.change("emote", "none")
    $ trapperObj.change("emotion", "mad")
    tt "But I can tell you this much: I'm hiding a secret on this island that will make fans shit themselves with excitement."
    tt "If you like Trapper you're gonna love it. And if not you're a maggot. Also, everyone, even confident sexy ladies in rabbit masks, better stay the hell away from my yacht!"
    hide trapper
    $ clauddwightObj.change("emotion", "happy")
    show clauddwight at movecenterleft
    with dissolve
    dw "Hit us, Spirit!"
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close03")
    show spirit behind clauddwight at movecenterright with dissolve
    cl "Figuratively! Damnit, Dwight. You gotta watch your words with these people."
    $ spiritObj.change("pose", "close02")
    $ spiritObj.change("emote", "sparks")
    ts "Tomorrow, you'll spit in the face of god, die, and be reborn anew."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "disgusted")
    $ clauddwightObj.change("emotion", "sad")
    show clauddwight behind spirit at movecenterleft with dissolve
    dw "That's it?"
    ts "If you're not intrigued by that... I don't want you. Go draw crayon art with Trapper or dig up whatever mysteries with Wraith, I don't know what those guys do all day."
    $ clauddwightObj.change("emotion", "disgusted")
    cl "Do you want to at least specify which god you'll be spitting in the face of?"
    $ spiritObj.change("emote", "anger")
    $ spiritObj.change("emotion", "mad")
    ts "{i}All of them.{/i}"
    $ spiritObj.change("emote", "none")
    $ clauddwightObj.change("emotion", "sad")
    dw "Ok then, so hydrate tonight if you intend to hang with Spirit."
    hide spririt with dissolve
    $ clauddwightObj.change("emotion", "happy")
    $ clauddwightObj.change("pose", "pose02")
    cl "Annnnnnd time's up everyone! Gosh, you'll need to dream about these options so you're ready to choose in the morning."
    show clauddwight at slidetomovecenter
    dw "Now go dream about all these swoon-worthy options so that you're ready to make a choice come dawn."
    cl "Have a swell night!"
    $ clauddwightObj.change("emotion", "disgusted")
    $ clauddwightObj.change("pose", "close02")
    nrr "Um. Did you two forget to mention something?"
    $ clauddwightObj.change("emotion", "sad")
    dw "Haha, oh gosh. How could we forget? Before you run off to slumber peacefully there's sone more thing to do..."
    $ clauddwightObj.change("pose", "close01")
    call event_choices
    cl "No reality survival dating competition parody would be complete without singling out one of our contestents who is already teetering on the edge of a psychological break..."
    $ clauddwightObj.change("emotion", "happy")
    dw "...and giving them a little push!"
    $ clauddwightObj.change("emotion", "idle")
    mc "Hold up, this has been a survival dating competition parody this entire time and I'm just now finding out about it?"
    nrr "Come on, the signs were there. You just didn't read them."
    $ clauddwightObj.change("emotion", "happy")
    dw "{i}Welcome to Murderer's Island{/i}!"
    $ clauddwightObj.change("emotion", "disgusted")
    cl "It's now time... to eliminate one of the Killers!"
    nrr "Oof! It's like butchering, but it hurts even worse!"
    call oceanhaunting
    oc "You can't kill a Killer, but can you break their heart?"
    oc "...Do you dare to even try?"
    stop hauntloop fadeout 3.0
    $ clauddwightObj.change("emotion", "idle")
    $ clauddwightObj.change("pose", "pose01")
    call volleyballsunsetscene(withDissolve=False)
    show clauddwight
    with dissolve
    mc "You mean..."
    dw "That's right. Tomorrow one of these sexy slicers will not be eligible to take you on a date. Who's it gonna be?"
    mc "But why?"
    $ clauddwightObj.change("emotion", "disgusted")
    cl "Uh, because it's dramatic?"
    dw "Because it's surprising?"
    cl "Because it's a classic reversal of fate?"
    $ clauddwightObj.change("pose", "close02")
    $ clauddwightObj.change("emotion", "happy")
    dw "And it will hurt someone's feelings! Someone {i}dangerous{/i}!"
    $ clauddwightObj.change("emotion", "idle")
    nrr "What's it gonna be champ? What's your thought process here?"
    nrr "Trapper seems like he might throttle you in your sleep if you eliminate him."
    nrr "That being said, at least you'd see him coming. Spirit could be anywhere. She floats. And I hear she can disappear. Hard to track."
    nrr "Eek, if you get rid of Wraith he might cry. And although I totally support normalizing men crying and being vulnerable, it just seems like he might be an ugly crier."
    nrr "Huntress? She might pretend to be OK with it but then you'll start seeing her behind every tree."
    hide clauddwight with dissolve
    $ diamondchoice = True
    menu:
        cho "What I'm trying to say is... I don't envy you, boss. So which sociopath are you eliminating?"
        "gui/button_spirit_idle.png¦gui/button_spirit_hover.png¦gui/button_spirit_select.png":
            $ diamondchoice = False
            call eliminate_wraith
        "gui/button_trapper_idle.png¦gui/button_trapper_hover.png¦gui/button_trapper_select.png":
            $ diamondchoice = False
            call eliminate_wraith
        "gui/button_wraith_idle.png¦gui/button_wraith_hover.png¦gui/button_wraith_select.png":
            $ diamondchoice = False
            call eliminate_wraith
        "gui/button_huntress_idle.png¦gui/button_huntress_hover.png¦gui/button_huntress_select.png":
            $ diamondchoice = False
            call eliminate_wraith
    
    $ clauddwightObj.change("pose", "close01")
    $ clauddwightObj.change("emotion", "idle")
    show clauddwight with dissolve
    dw "Now that you've broken the heart of someone heartless, you should go get some shut eye!"
    cl "And don't worry too much about the broken heart you've left behind..."
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    dw "...because, of course, they'll be receiving a consolation prize! They might not get to go home with [mc_name] when this is all over, but they'll never sleep alone again."
    cl "That's right! We're sending our eliminated player home with..."
    stop eventloop fadeout 3.0
    call mood_excitement(image_name="images/bodypillow.png",ismovefrombottom = True)
    play sound "sounds/sfx_signature_trickster01.ogg"
    dw "Their own mostly-new Trickster Body Pillow! The next best thing to the real Trickster, it might not hug you back but it definitely won't try and stab you! And how do we know? Because I've tried it! That's right, it's Dwight tested..."
    cl "Claudette approved!"
    stop moodloop fadeout 3.0
    call volleyballsunsetscene(withDissolve=False)
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "happy")
    show clauddwight
    with Dissolve(0.25)
    cl "I hope you sleep well tonight, [mc_name]. You're my hero for what you've accomplished."
    hide clauddwight with dissolve
    nrr "How can you sleep tonight knowing what you've done? No, not because of guilt. I mean knowing that there's a legit homicidal maniac who hates you so close by?"
    call oceanhaunting
    oc "How can you sleep tonight... knowing what you'll do tomorrow?"
    nrr "I dunno know you'll do it, but you better go before Dwight and Claudette come back and put you to sleep themselves. You know those two, schedule, schedule, schedule!"
    call blackscene
    return

label eliminate_wraith:
    mc "Look, I'm here and I'm horny, and I'm not really getting positive reinforcement from you, Wraithy-poo."
    $ wraithObj.change("pose", "pose01")
    $ wraithObj.change("emotion", "disgusted")
    show wraith with dissolve
    mc "Please don't take this personally, it's just my opinion of you and who you are and what you're about deep down as a person, and how I don't like it."
    mc "Like, give me something, you know? A kiss, a wink, hold my hand. Finish telling me about all this mysterious stuff you're obsessed with."
    $ wraithObj.change("emote", "dread")
    mc "Or better yet? Don't."
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("pose", "pose03")
    nrr "Wraith rises, taller than you've ever seen him, and calmly walks to the exit."
    nrr "Before he leaves, he turns to you."
    $ wraithObj.change("pose", "close03")
    tw "When you came here, I thought perhaps you would be different."
    tw "I don't know how my last bit of hope in humanity hadn't been snuffed out, but it wasn't."
    $ wraithObj.change("pose", "close02")
    tw "It is now. You are just like the rest of them. There is no hope of goodness here."
    tw "The only thing I can do is try to escape."
    $ wraithObj.change("emote", "anger")
    $ wraithObj.change("emotion", "mad")
    tw "Or burn everything and everyone to the ground."
    $ wraithObj.change("emote", "none")
    nrr "He leaves."
    hide wraith with dissolve
    nrr "Pretty badass exit, was not expecting that!"
    return