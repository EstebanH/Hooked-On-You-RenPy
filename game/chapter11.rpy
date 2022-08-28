label chapter11:
    call beachdayscene
    nrr "Soft sunlight warms your skin, nudging you awake. Also you're using a killer crab as a pillow, which it's sort of OK with."
    nrr "What's that? You don't know about the killer crabs? Oh, right. You didn't go on that Huntress date. You really missed out. It was thrilling. Or, I guess it {i}would've been{/i}. You'll have to play the game again to get that reference, I suppose."
    nrr "You pull on your beach attire and splash water on your face. Dwight and Claudette approach. Is that look on their faces excitement? Terror?"
    nrr "You notice your stomach flutters with butterflies. Sommmmmeone's in loooooove."
    nrr "Or you've been infected with zombie butterflies in your sleep. It has happened here before. But it's probably the love thing."
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    show clauddwight with dissolve
    cl "It's time!"
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "idle")
    call event_tikitiki
    nrr "Claudette gestures over to the beach where the Killers all stand flanked by tiki torches. It's a scene very reminiscent of a TV show you used to hate-watch with your ex."
    nrr "Suddenly the message is clear. You are going to declare your affections for a Killer in front of several other Killers. Hey, isn't Trickster supposed to be here? We paid him good money to make some half-assed cameos in this show. I'm gonna chew his agent out."
    nrr "But before they walk you over for your big moment..."
    $ clauddwightObj.change("pose", "close01")
    $ clauddwightObj.change("emotion", "happy")
    $ clauddwightObj.change("emote", "heart")
    dw "Don't think we haven't noticed how kind you've been to us, [mc_name]."
    $ clauddwightObj.change("emote", "none")
    $ clauddwightObj.change("emotion", "sad")
    cl "It can't be easy, being thrown into a mysterious island for seemingly no reason, surrounded by terrifying Killers, trying to manage your most primal impulses-"
    dw "Murder and making out!"
    $ clauddwightObj.change("emotion", "happy")
    cl "And you've kept a cool head and treated us, your friendly island hosts, with dignity and respect. So don't tell anyone we told you this, but..."
    nrr "Claudette and Dwight look around conspiratorially."
    $ clauddwightObj.change("emotion", "idle")
    $ clauddwightObj.change("pose", "close02")
    dw "Just a little hint for you, going forward: Don't try to go all the way with a Killer who isn't into you."
    cl "Relationships are two-way streets, and if you don't have a green light in the other direction, you might end up in the Friend Zone."
    mc "The Friend Zone? That doesn't sound so bad."
    $ clauddwightObj.change("emotion", "disgusted")
    cl "Where do you think you are, exactly?"
    dw "Dead by Daylight doesn't do \"friends.\" There are Killers and there are Survivors and... I'm afraid we can't say more."
    mc "Ok, so... who's into me?"
    nrr "Claudette and Dwight look around conspiratorially, again."
    $ clauddwightObj.change("emotion", "happy")
    $ clauddwightObj.change("pose", "close01")
    cl "Well..."
    dw "I've never seen Spirit open up to anyone like she has opened up to you."
    $ clauddwightObj.change("emotion", "sad")
    cl "I've seen her open up the insides of plenty of people. But, thankfully for you and for us, that's in a different type of game."
    nrr "So, are you ready? Of course you're not! But too bad, we're on a schedule..."
    call blackscene
    call beachtikiscene(withDissolve=False)
    $ renpy.music.set_volume(0,3.0,"music")
    play sound "sounds/sfx_signature_clauddwight04.ogg"
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
    #show wraith at movecenterleft
    show spirit at movecenterright
    with dissolve
    nrr "You make your way over to the row of hotties. Claudette and Dwight stand off to the side, hands behind their backs."
    hide huntress
    hide spirit
    hide trapper
    hide wraith
    $ clauddwightObj.change("emotion", "idle")
    $ clauddwightObj.change("pose", "close01")
    show clauddwight
    with dissolve
    dw "It's been quite the 48 hours, but there are clearly sparks in the air. And I'm not just talking about this rusty chainsaw! Though I do recommend staying away from those sparks."
    call event_confess
    $ clauddwightObj.change("emotion", "happy")
    $ renpy.music.set_volume(0,3.0,"music")
    cl "It's time for our newcomer to confess their love!"
    $ clauddwightObj.change("emotion", "scared")
    dw "Wait! I have to do a drum roll for this!"
    $ clauddwightObj.change("emotion", "disgusted")
    cl "No. You don't. But who cares. [mc_name], who do you choose for your solo date?"
    $ clauddwightObj.change("emotion", "happy")
    dw "Can we at least do the flower thing?"
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "mad")
    cl "Dwight! I thought we agreed to keep that between us!"
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "scared")
    dw "No, not {i}that{/i} flower thing. The thing where the suitor gets a flower as a symbol of the contestant's love and affection!"
    $ clauddwightObj.change("emotion", "disgusted")
    cl "Oh, right, right... I {i}suppose{/i}. But no roses. They're such a cliche at this point."
    $ clauddwightObj.change("emotion", "idle")
    dw "Well that's good, because I tried to pick a rose but I got an ouchie so I settled for these!"
    call mood_warmdark(image_name="images/flowers.png", ismovefrombottom = True, withDissolve = True)
    pause 1
    nrr "Beautiful!"
    cl "You've done good, Dwight. This is a lovely bouquet."
    call beachtikiscene(withDissolve=False)
    nrr "I hope Dwight saved some of these for Claudette. They're a thing, right? You're getting that vibe too? Just me? Sorry, sorry, you've got other things to think about right now."
    $ clauddwightObj.change("pose", "close01")
    $ clauddwightObj.change("emotion", "idle")
    show clauddwight with dissolve

    
    $ diamondchoice = True
    menu flower_choice:
        cl "[mc_name]... Who do you select to receive these flowers and spend the day with you today?"
        "gui/button_spirit_idle.png¦gui/button_spirit_hover.png¦gui/button_spirit_select.png":
            $ diamondchoice = False
            call flowers_spirit
        "gui/button_trapper_idle.png¦gui/button_trapper_hover.png¦gui/button_trapper_select.png":
            $ diamondchoice = False
            call flowers_spirit
        #"gui/button_wraith_idle.png¦gui/button_wraith_hover.png¦gui/button_wraith_select.png":
        #    $ diamondchoice = False
        #    call flowers_spirit
        "gui/button_empty_idle.png¦gui/button_empty_idle.png¦gui/button_empty_idle.png¦Disable":
            jump flower_choice
        "gui/button_huntress_idle.png¦gui/button_huntress_hover.png¦gui/button_huntress_select.png":
            $ diamondchoice = False
            call flowers_spirit
    call blackscene
    return
label flowers_spirit:
    hide clauddwight 
    $ spiritObj.change("pose", "pose03")
    $ spiritObj.change("emotion", "idle")
    show spirit
    with dissolve
    nrr "You approach Spirit, peering below the brim of her impressively large hat and into her haunting eyes."
    mc "Spirit. Since I met you, I've been enchanted by your presence. You've challenged me to be a better person and resisted the urge to show me the sharp end of your katana. For that, I thank you."
    mc "I'm ready to take our relationship to the next level."
    $ spiritObj.change("pose", "close04")
    $ spiritObj.change("emotion", "happy")
    ts "And we shall. Up to the eye of the dark storm that is our reality. To the lantern room... of the Black Lighthouse."
    $ spiritObj.change("emote", "sparks")
    ts "It's time to see what you're made of, [mc_name]."
    $ spiritObj.change("emote", "none")
    call blackscene
    call yachtdayscene(withDissolve=False)
    call event_monkeybytes
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    show spirit
    with Dissolve(0.25)
    ts "I thought it might be nice to start the day out on Trapper's yacht before we head up to the Black Lighthouse."
    ts "Even if I kinda hate this basic tropical vacation stuff like yachts and snorkeling or whatever, it's good for you to see me in the sun a little bit, at least. There's more to me than what you've already gotten to experience."
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("emote", "dread")
    ts "I know my whole vibe can be... a little dark."
    $ spiritObj.change("emote", "none")
    ts "The hat, the swimsuit, the plume of floating hair."
    $ spiritObj.change("emotion", "idle")
    ts "This wasn't always who I was. I was a normal young woman, once. Went to school. Hung out with friends."
    $ spiritObj.change("pose", "close03")
    ts "I even had a part-time job working at a restaurant in town."
    mc "And then... well, I know what happened. You father, he--"
    $ spiritObj.change("emotion", "disgusted")
    ts "Yeah, yeah, he murdered me and I awoke as an undead avenger. That's not what I was getting at."
    $ spiritObj.change("emotion", "happy")
    ts "Something {i}else{/i} happened to me."
    ts "I realized I needed to be seen. I don't even know by whom. I just..."
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emotion", "idle")
    ts "A lot of time, when you think about ghosts, they're these kind of see-through flickering spectres. You imagine reaching out and having your hand go right through them."
    $ spiritObj.change("emotion", "disgusted")
    ts "OOOoooOOooooohhhhh, like that sort of thing. Maybe there's some warpy effect on the world around you, I dunno, depends on which movie you're watching."
    $ spiritObj.change("emotion", "idle")
    ts "But when I died, well, I dare you to try and reach your hand through me."
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "close02")
    ts "Not {i}really{/i}. That's not an invitation. It's rhetorical."
    $ spiritObj.change("emotion", "idle")
    ts "Why did I end up this way? Who brought me here to this Island? Who knows. I sure don't."
    ts "I've got my ideas."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "close03")
    ts "But I'm not exactly out there digging around in caves or dusting off antiques and trying to find clues and analyze their meanings."
    ts "I do want to take this experience seriously, though. I want to give the process a chance."
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("emote", "dread")
    ts "It may be a dumb process, and one that I have extremely little respect for as a person..."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    ts "But you just woke up on this beach with no memory of who are or where you came from, and rather than freak out and simply try and swim away... you're giving this a chance."
    mc "I actually didn't know that swimming away was an option."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "close01")
    ts "It's not. However, the fact that you never even tried. I think that means you've got courage. Or an open mind. Or, I dunno, maybe you stuck around..."
    $ spiritObj.change("emote", "stars")
    ts "...because you like someone you met here..."
    $ spiritObj.change("emote", "none")
    mc "Maybe."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose01")
    nrr "While the two of you were getting all deep and philosophically flirty, the yacht pulled up to the shore next to the Black Lighthouse."
    show spirit at slidetomovecenterright
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "mad")
    show clauddwight behind spirit at movecenterleft
    with dissolve
    dw "Last stop! Everybody off!"
    $ clauddwightObj.change("emotion", "idle")
    mc "There were other stops?"
    $ clauddwightObj.change("emotion", "happy")
    $ clauddwightObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "disgusted")
    cl "Oh, no, not of this trip. Of {i}your life{/i}."
    mc "..."
    nrr "Spirit rolls her eyes and leaves for the shore."
    $ spiritObj.change("emotion", "sad")
    hide spirit
    show clauddwight at slidetomovecenter
    with dissolve
    cl "I'm just messin' with ya. This was the only stop. Nobody here is really looking out for {i}our{/i} fun, so we have to make it for ourselves."
    $ spiritObj.change("emotion", "disgusted")
    $ clauddwightObj.change("pose", "close01")
    dw "But no, there are no other stops. Seriously. Go."
    $ spiritObj.change("emotion", "happy")
    $ clauddwightObj.change("pose", "close02")
    cl "Race you to the poop deck, Dwight!"
    dw "This shop doesn't even have a poop deck!"
    cl "Oh it will!"
    hide clauddwight with dissolve
    nrr "As you disembark, you see Dwight and Claudette run giggling across the ship. Too bad you can't date those two, they seem like they know how to have a good time."
    call blackscene
    return