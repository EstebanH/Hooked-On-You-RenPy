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
            $ spirit_aff = spirit_aff + 1
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
    call lighthousedayscene
    call event_freshflesh
    nrr "You arrive at the beach near the majestic Black Lighthouse, it's imposing form towers above you."
    nrr "A flock of birds circle lazily, no sense of fear or urgency, as if circling a corpse that hasn't moved in ages."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "pose01")
    show spirit with dissolve
    ts "I'm excited about today. See?"
    nrr "Spirit places her wrist delicately in your hand and presses your fingers down against her skin. It's cool to the touch, but you feel... is that... the faintest of pulses?"
    $ spiritObj.change("pose", "close03")
    $ spiritObj.change("emote", "exclamation")
    ts "My blood is absolutely {i}pumping{/i}."
    $ spiritObj.change("emote", "none")
    mc "So... what happens now?"
    ts "Now I show you something that no one has ever seen up close before. Well, no one who has lived to tell about it."
    $ spiritObj.change("pose", "pose03")
    $ spiritObj.change("emotion", "idle")
    ts "We're going... there."
    nrr "Spirit points to the top of the lighthouse, amongst the circling birds."
    mc "What's actually up there? Have you seen it?"
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "disgusted")
    show spirit at slidetomovecenterright
    $ wraithObj.change("pose", "pose01")
    $ wraithObj.change("emotion", "happy")
    show wraith behind spirit at movecenterleft
    with dissolve
    tw "Hey y'all! How's everyone doin' today?!"
    nrr "Certainly seems to be taking the whole elimination thing well. Or... maybe this is the opposite of that. Better not bring it up at all and just hope he doesn't completely melt down."
    mc "Uhh... hi... Wraith. You sure seem chipper today..."
    $ wraithObj.change("pose", "pose03")
    nrr "Something strange is definitely going on with this guy. Well, something {i}else{/i} strange. Something different than what's usually going on."
    $ wraithObj.change("emotion", "idle")
    nrr "Wraith takes a deep breath, sucking in the ocean air like it's the greatest air has ever been sucked."
    $ wraithObj.change("emotion", "scared")
    $ spiritObj.change("emotion", "idle")
    tw "[mc_name], thank you. Thank you for choosing someone--anyone--else to go on a date with today."
    $ wraithObj.change("emotion", "happy")
    tw "Alone, again, forever... this is how I was meant to be! I feel ALIVE!"
    $ wraithObj.change("emotion", "disgusted")
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("emote", "question")
    ts "Are you done? We're kind of, you know, on that date you just mentioned?"
    $ spiritObj.change("emote", "none")
    mc "I'm glad you're feeling better, Wraith, but like she said... we're in the middle of something. You mind?"
    $ wraithObj.change("emotion", "scared")
    $ wraithObj.change("pose", "pose01")
    tw "Oh, right right right..."
    tw "So, whatcha doin? Heading up into the eye of the lighthouse? I love it up there! You can really see the whole island from up there. In fact--"
    $ wraithObj.change("emotion", "disgusted")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose03")
    mc "Spirit, I thought you said no one has been up there and lived to tell about it, but this sounds exactly like \"telling about it.\""
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "pose02")
    ts "Technically, I don't think Wraith counts as being alive. I mean, I don't maintain the canon, but..."
    nrr "Spirit waves her arms at Wraith from head to toe."
    $ wraithObj.change("emotion", "scared")
    $ wraithObj.change("pose", "pose02")
    $ spiritObj.change("emotion", "mad")
    $ spiritObj.change("emote", "sparks")
    ts "And if he's not dead now he's {i}GONNA BE WHEN I PUNISH HIM FOR INTERRUPTING OUT DATE{/i}!"
    $ spiritObj.change("emote", "none")
    tw "Hey now, we can solve our problems without hair floating up into any menacing shapes..."
    tw "I'll just be over here.... running away! Enjoy the viewwwwwwoooOOOoooOOooooohhhh."
    hide wraith 
    show spirit at slidetomovecenter
    with dissolve
    ts "You know, I think Wraith was kidding about that whole being up there. Honestly, the view isn't even of the island--what you can see is mostly ocean, on account of it being, you know, a lighthouse."
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    ts "However, that does bring up an interesting point..."
    ts "Regarding you, how do I say it..."
    nrr "Spirit's hand floats up as she scratches her head contemplatively. You don't usually see her at a loss for words like this."
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("emote", "question")
    ts "What's you... mortal status?"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "disgusted")
    ts "Because, despite what our lanky friend seems to think, the Lighthouse is not to be trifled with. It's a beacon of death and suffering that brings doom to it from all corners of this world... if not further..."
    $ spiritObj.change("emotion", "idle")
    nrr "Well, duh. You saw a freakin' pirate ship seeming travel through space and time only to crumble at the rocks beneath this spooky tower. But you decide not to point it out because that wouldn't be too romantic now would it?"
    mc "I think I'm... alive? I'm here, with you, walking this beach, feeling the water on my feet, feeling the sun on my skin."
    $ spiritObj.change("pose", "close03")
    ts "Here... with me, {i}The Spirit{/i}. Does that really make you alive?"
    mc "I guess I don't know."
    ts "If you come with me up into the eye of the Black Lighthouse, you may never return. Is that a risk you're willing to take?"
    $ spiritObj.change("emote", "sweat")
    $ spiritObj.change("emotion", "happy")
    ts "Because we have something. I won't deny it. I feel it. I'd hate for you to simply turn to ash..."
    $ spiritObj.change("emote", "none")
    ts "If we were to commit, right here and now, to figuring this out as friends, we could put that risk off for another time."
    $ spiritObj.change("emotion", "idle")
    nrr "Just be... friends? Ouch. Is this her way of letting you down easy?"
    mc "I don't know if I want that--friendship. I want you. That's why I chose you."
    menu:
        ts "I can't decide this for you. I can only warn you that it may not be safe. You might die up there and there's nothing I can do about it."
        "Stay down, live for sure":
            mc ""
        "Go up, maybe die":
            $ spirit_aff = spirit_aff + 1
            nrr "You take a deep breath and think about every particle of sea air as it travels into your body and fills your lungs. It may be the last time you have such a thought, but you feel strangely at peace with that information."
            $ spiritObj.change("pose", "close04")
            mc "I don't need another friend. I want something more. I'd risk my life for it."
            nrr "Spirit smiles a quirky, devilish smile."
            $ spiritObj.change("emote", "heart")
            $ spiritObj.change("emotion", "happy")
            ts "Right this way..."
            $ spiritObj.change("emote", "none")
    call darknessscene
    nrr "Inside the lighthouse is almost pitch-black. It was seemingly day when you stepped through the door, but inside this place is like a void."
    nrr "The last thing you see as the final rays of sun leave you is a horrible sight, a petrified body laying on the stairs, reaching not up, but down, as if it had been crawling."
    nrr "The things we do for love."
    call lighthouseinsidenightscene
    nrr "When you arrive in the lantern room at the top of the Black Lighthouse, you breathe a sigh of relief. The light is out, and seemingly defunct. Dust cakes the room, as though it hasn't been operated in a century."
    nrr "However, somehow..."
    mc "It was just morning, a moment ago, but now it's night?"
    $ spiritObj.change("emote", "question")
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "pose01")
    show spirit at movecenterright with dissolve
    call event_nextvictim
    $ renpy.music.set_volume(0,3.0,"music")
    ts "What do you mean, a moment ago? We've been standing here looking out over the ocean all day... I've really enjoyed the peaceful time together with you, taking in the view, standing in complete silence for hours. It was kinda my {i}perfect{/i} date."
    $ spiritObj.change("emote", "none")
    mc "Really? I don't remember that."
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "close01")
    ts "I just called it the perfect date and you can't be bothered to remember it? What kind of game are you playing with me?"
    mc "I {i}want{/i} to remember it, it's just that for some reason my mind is completely blank. But... Hey, I'm not dead!"
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "close03")
    ts "Or you're {i}already{/i} dead and have been this whole time."
    mc "Hmmm, that's true..."
    $ spiritObj.change("emotion", "idle")
    ts "Maybe we'll never know? It doesn't look like the light is working."
    nrr "Even turned off, the light has a power to it. The massive lens refracts moonlight through itself, a subtle sparkle that has a hypnotic effect. Maybe that's where the day went? Staring into this light as the sun fell and moon rose."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emote", "stars")
    ts "Thanks for spending the day with me. I really had a good time."
    $ spiritObj.change("emote", "none")
    mc "That's... it? Don't get me wrong, this is really cool and all, I just..."
    mc "I guess I don't know what I expected."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose02")
    ts "I suppose if you thought you were walking into your death, and nothing happened, it might feel a bit anti-climactic."
    $ spiritObj.change("emotion", "disgusted")
    ts "Sorry. Anyhow, it's time to go. Here, let me just flip on the light for the staircase so it's easier to get down."
    $ spiritObj.change("pose", "pose01")
    ts "Hmmm... the stairs still look pretty dark. Maybe it--"
    $ spiritObj.change("emotion", "scared")
    nrr "Spirit is interrupted by a strange hum, and then it becomes frighteningly clear to you: that switch wasn't for the stairs, it was for the main lantern--a lantern that is now beginning to power up."
    call lighthouseinsidenighteyescene(withDissolve=False)
    $ renpy.music.set_volume(0,3.0,"music")
    show spirit at movecenterright
    nrr "The faintest smell of burning begins to reach up to your nose."
    ts "Oopsie, looks like {i}maybe{/i} that switch wasn't for the stair lights at all..."
    nrr "Now we see who is really alive and who is really dead, I suppose. It was bound to happen sooner or later."
    $ spiritObj.change("emotion", "idle")
    nrr "You slam your eyes closed, hoping that somehow not looking at the light itself will protect you. Not sure I see the logic in that, but if it {i}is{/i} magic, it kinda defies logic."
    mc "I {i}want{/i} to see it... but, well, I'm a little scared!"
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close02")
    show spirit at slidetomovecenter
    $ spiritObj.change("emote", "sparks")
    menu:
        ts "Don't look directly into the light! Open your eyes and look only at me and I'll keep you safe!"
        "Ready":
            $ spiritObj.change("emote", "none")
            $ spirithideandseek_turn = 0
        "Repeat the instructions":
            $ spiritObj.change("emote", "none")
            mc "Would you please repeat the instructions?"
            nrr "My pleasure!"
            call instructions_meatcarving

    while (int(spirithideandseek_turn) < 5):
        call start_spirithideandseek_minigame
        if spirithideandseek_section == 1:
            call end_spirithideandseek_minigame
            $ spirithideandseek_perfects = spirithideandseek_perfects + 1
            nrr "Perfect!"
        elif spirithideandseek_section == 2:
            call end_spirithideandseek_minigame
            $ spirithideandseek_good = spirithideandseek_good + 1
            nrr "Not bad..."
        else:
            call end_spirithideandseek_minigame
            nrr "You missed completely!"
        $ spirithideandseek_turn = spirithideandseek_turn + 1
        $ spirithideandseek_speed = spirithideandseek_turn + 1
    if spirithideandseek_perfects == 5:
        ##Perfect
        show spirit
    elif spirithideandseek_good > 1:
        ##Good
        stop eventloop fadeout 3.0
        call mood_warmlight(withDissolve=False)
        $ spiritObj.change("pose", "pose03")
        $ spiritObj.change("emotion", "idle")
        show spirit
        with Dissolve(0.25)
        ts "Are you OK? You seem OK... I hope I haven't ruined this by pushing you to do something you weren't meant to do."
        $ spiritObj.change("emotion", "happy")
        $ spiritObj.change("emote", "stars")
        ts "You're so brave, maybe not so coordinated, but certainly brave."
        $ spiritObj.change("emote", "none")
        ts "I'm so lucky you'd put yourself through this for me. It shows that you're {i}real{/i}."
        stop moodloop fadeout 3.0
    elif (spirithideandseek_good == 1) and (spirithideandseek_perfects == 0):
        ##Bad 1/5
        show spirit
    else:
        ##Missed Completely
        show spirit

    call lighthouseinsidenighteyescene(withDissolve=False)
    show spirit
    with dissolve
    nrr "Despite your attempt to resist it, the incredible force of energy from the Black Lighthouse's lantern eye refuses to subside. No, it cannot be ignored. And it doesn't matter if you look directly at it or not."
    nrr "In the end, that was just a trivial game. This is real life. And real magic. You stare at it now, and its power penetrates your mind."
    call oceanhaunting
    oc "Hey. Been a while. How are things?"
    oc "Doing good? Feeling more dead, or more alive?"
    oc "Yeah... love will do that to a person."
    oc "Don't worry. It'll make sense soon."
    call blackscene
    call minescene
    nrr "You wake to hear Spirit's muffled voice. You've got a terrible taste in your mouth, like burnt hair. The air feels damp and smells like ash."
    call event_storytime
    nrr "It takes time for the sound to clear up, but eventually Spirit's words start to make sense to you. However, it's clear she's talking to someone else, not to you."
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emote", "anger")
    show spirit at movecenterright with dissolve
    ts "You know how sometimes people say \"It's not you, it's me?\" Well this time it is you and it's {i}also{/i} me!"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "mad")
    ts "I can't believe I thought you would change for me. I can't believe I thought what you were doing was a sacrifice. You never gave anything up for me. Well, today I saw what love looks like, and it looks a whole lot different than this!"
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("pose", "pose02")
    show trapper behind spirit at movecenterleft with dissolve
    tt "I don't think you're hearing me, which is weird, because I'm practically shouting."
    $ trapperObj.change("emote", "sparks")
    tt "Nobody breaks up with Trapper. {i}Nobody{/i}!"
    $ trapperObj.change("emote", "none")
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "pose03")
    ts "Oh yeah? Fine! Nobody breaks up with Trapper. But I'm not doing that. I'm dumping--"
    $ trapperObj.change("emotion", "disgusted")
    tt "Don't you say it..."
    call mood_speedlines
    $ spiritObj.change("emotion", "mad")
    $ spiritObj.change("pose", "pose02")
    ts "I'm dumping Evan MacMillan! And there's nothing you or he can do about it. It's over between us Evan!"
    $ trapperObj.change("emotion", "disgusted")
    $ trapperObj.change("pose", "pose01")
    $ trapperObj.change("emote", "sweat")
    hide speedlines
    stop moodloop fadeout 3.0
    tt "Rin, I--"
    $ trapperObj.change("emote", "none")
    nrr "Trapper turns from Spirit and looks directly at you. You realize that you're laying on the ground of some weird tunnel."
    tt "--I think your shouting woke up [mc_name]."
    $ spiritObj.change("emote", "question")
    menu:
        ts "MY SHOUTING?"
        "Say something":
            $ spirit_aff = spirit_aff + 1
            $ spiritObj.change("emote", "none")
            stop eventloop fadeout 3.0
            mc "I'm sorry, I think I interrupted something... very personal, and also quite scary."
            $ spiritObj.change("emotion", "idle")
            mc "I swear I wasn't trying to listen in, but.. I heard a lot. Probably not everything. I think I woke up in the middle."
            $ trapperObj.change("emotion", "idle")
            $ spiritObj.change("emotion", "idle")
            $ spiritObj.change("pose", "pose01")
            ts "What did you hear?"
            mc "Just you dumping Trapper."
            $ trapperObj.change("emotion", "mad")
            $ trapperObj.change("emote", "exclamation")
            tt "We were never together! I mean, we were... {i}together{/i}, wink-wink-wink--"
            $ trapperObj.change("emote", "none")
            $ trapperObj.change("emotion", "idle")
            $ spiritObj.change("emotion", "disgusted")
            ts "I know you're wearing a mask, but we can see your eyes. You don't need to say \"wink wink wink\" out loud. Another reason I'm right to have dumped you."
            $ trapperObj.change("emotion", "disgusted")
            tt "You did not! It was mutual."
        "Stay quiet":
            $ spiritObj.change("emote", "none")
            stop eventloop fadeout 3.0
        "Fake snore":
            $ spiritObj.change("emote", "none")
            stop eventloop fadeout 3.0

    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    call event_nextvictim
    nrr "The jig is, as they say, up. They know you're awake now, and you're going to have to deal with this awkward situation head-on."
    mc "Clearly I shouldn't be here. You two are having a very personal conversation that I don't need to be involved in. I don't even know how I got here. Not here on this island, or here in this creepy tunnel."
    show trapper at slidetomoveleft
    $ spiritObj.change("pose", "close03")
    ts "As far as this island goes, your guess is as good as mine. As far as this tunnel goes, we bought you here."
    mc "We? You and Trapper? But..."
    ts "After the lighthouse light came on, you blacked out. On your way down, I thought you might've hit your head or something. It's hard to tell what blood is new or old around here. Either way, I wanted to get you someplace safe and so I asked Trapper for help."
    $ trapperObj.change("emotion", "happy")
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "close01")
    ts "It's not that I can't carry you... I just didn't feel like it, you know? I hate anything messing with my shards. Trapper on the other hand, he loves nothing more than having an unconscious body draped over his shoulder."
    $ trapperObj.change("emotion", "idle")
    ts "I could've asked Claudette and Dwight for help but... I don't trust them."
    $ spiritObj.change("emotion", "idle")
    mc "But you trust Trapper?!"
    $ spiritObj.change("emotion", "disgusted")
    $ trapperObj.change("emotion", "disgusted")
    $ spiritObj.change("emote", "dread")
    ts "Like and trust are two different things. You might think Trapper can be a real jerk, and you'd be right. But you get what you see with him."
    $ spiritObj.change("emote", "none")
    $ trapperObj.change("emotion", "idle")
    ts "We brought you down here because we're the only ones who know about this place. It's part of an old tunnel network that connects different places on the island."
    $ wraithObj.change("emote", "question")
    $ wraithObj.change("emotion", "happy")
    $ wraithObj.change("pose", "pose03")
    $ trapperObj.change("emotion", "mad")
    $ spiritObj.change("emotion", "scared")
    $ spiritObj.change("pose", "pose01")
    show spirit at slidetomoveright
    show wraith behind spirit with dissolve
    $ wraithObj.change("emote", "none")
    $ spiritObj.change("emotion", "disgusted")
    tw "What's up, guys?!? Talking island mysteries? My favorite topic! I was just in the neighborhood so I thought I'd pop in."
    ts "Trapper, you said this place was private!"
    $ wraithObj.change("emotion", "disgusted")
    $ trapperObj.change("pose", "pose03")
    tt "Don't look at me, I didn't tell him about it. Half of the appeal of this port is getting {i}away{/i} from people like him."
    $ spiritObj.change("emote", "question")
    tw "Well jeez, I can see when I'm not wanted."
    $ spiritObj.change("emote", "none")
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("pose", "pose02")
    $ wraithObj.change("pose", "pose01")
    $ wraithObj.change("emotion", "happy")
    tw "So, you three a thruple now or...."
    tw "Because I gotta say, I really didn't get the whole Trapper-Spirit thing, but hey, if it's not my business, I don't stick my nose in it."
    $ trapperObj.change("emote", "sparks")
    $ wraithObj.change("emotion", "scared")
    $ trapperObj.change("emotion", "mad")
    tt "WE WERE NOT A THING! Nobody traps the Trapper. Not with traps, or with relationships."
    $ trapperObj.change("emote", "none")
    $ spiritObj.change("pose", "pose03")
    ts "And you do realize you're sticking your nose in our business right now, right?"
    $ wraithObj.change("emotion", "mad")
    $ wraithObj.change("pose", "pose03")
    tw "Wow, so hostile. If you don't want to talk about it, just say so!"
    $ wraithObj.change("emotion", "disgusted")
    tw "Anyhow, this tunnel has some very interesting features. If you head about 50 meters down that way you'll find--"
    $ trapperObj.change("emote", "anger")
    tt "GET OUT!"
    $ trapperObj.change("emote", "none")
    $ spiritObj.change("pose", "pose01")
    nrr "Wraith looks around, just to be double-y sure that Trapper is addressing him."
    tw "I was just leaving."
    hide wraith with dissolve
    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    show spirit at slidetomovecenterright
    show trapper behind spirit at slidetomovecenterleft
    ts "This island, it's a lonely place. Which is great, for me. I love to be alone. Trapper, on the other hand, he's quite needy."
    $ spiritObj.change("emotion", "disgusted")
    ts "And after a lot of pursuit, I finally let him catch up to me. And it became, well, I don't want to call it a relationship because {i}somebody{/i} really didn't want to have that talk. But we were more than friends."
    $ spiritObj.change("pose", "pose01")
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose01")
    tt "I dispute the events as told, for the record. I don't pursue, I stalk, and I lie in wait."
    $ spiritObj.change("emote", "dread")
    ts "Seeing eye to eye was not one of the things we were good at."
    $ spiritObj.change("emote", "none")
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    mc "So... I hate to ask, but I did just look into a refrigerator-sized death-lamp so I guess I'm more of a glutton for punishment than I thought. What were you good at?"
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose01")
    tt "Well, for starters--"
    show trapper at slidetomoveleft
    $ spiritObj.change("emotion", "scared")
    $ spiritObj.change("pose", "close01")
    ts "Excuse me, I'll take that question, thank you very much."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close03")
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("pose", "pose01")
    ts "If you know anything about me by now, it's that I'm on a quest--"
    $ trapperObj.change("emotion", "disgusted")
    everyone "For revenge."
    $ spiritObj.change("emotion", "happy")
    $ trapperObj.change("emotion", "idle")
    call event_badslinky
    ts "Exactly. What you might not know, Trapper is like a great classical maestro of revenge."
    $ trapperObj.change("emote", "stars")
    $ trapperObj.change("pose", "pose03")
    nrr "Trapper blushes behind the mask. That's one way to compliment a Killer."
    $ trapperObj.change("emote", "none")
    ts "Revenge against friends who had turned their back and betrayed him... revenge against his father, for making him into a monster... revenge against a barista who wrote \"Ewan\" on his cappuccino, knowing his nam was actually Evan."
    $ trapperObj.change("emotion", "happy")
    $ trapperObj.change("pose", "pose01")
    ts "For someone who thinks about revenge as much as I do, Trapper is an inspiration."
    $ spiritObj.change("emote", "sweat")
    $ spiritObj.change("emotion", "disgusted")
    $ trapperObj.change("emotion", "disgusted")
    ts "But they say to never date your heroes."
    $ spiritObj.change("emote", "none")
    nrr "Good advice, but I don't think that's the saying."
    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close04")
    ts "And then you came along, [mc_name]. You showed me that it's OK to be lost, to feel pathetic, to push on when you have nothing real to offer anyone."
    mc "I'm not sure where you got {i}all{/i} of that from, but OK."
    ts "You held a mirror up to my own doubts and fears and showed me that they aren't everything about me. That I can embrace those things but not be defined by them."
    $ trapperObj.change("emotion", "happy")
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("emote", "stars")
    ts "You showed me that life after death can be more than just an obsession with revenge and mind-blowing sex on the ground in a dark cave or a dusty old tunnel."
    $ spiritObj.change("emote", "none")
    nrr "Trapper nudges you in the ribs with his elbow. Gross. Clearly, appealing to Trapper's... better features has been a winning strategy for dumping his ass, because he seems to be taking it quite well."
    $ trapperObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "disgusted")
    ts "This whole half-ass dating show parody thing, at first I obviously thought it was a lame idea. What kind of moron thought there was an audience for this?"
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "close03")
    ts "But then we spent some time together, and I realized... There's something actually real here."
    ts "And I don't want to give up on it. I don't want to give up on us."
    $ spiritObj.change("emotion", "idle")
    show spirit behind trapper at slidetomoveright
    $ trapperObj.change("emotion", "disgusted")
    $ trapperObj.change("pose", "close02")
    show trapper at slidetomovecenterleft
    tt "Listen, [mc_name]. While you were knocked unconscious by some minor head trauma like a total weakling, Spirit confided in me that she has real feelings for you. I took it extremely well, naturally, because I trust her and value her opinions."
    $ trapperObj.change("emotion", "idle")
    $ trapperObj.change("emote", "anger")
    tt "That doesn't mean I trust {i}you{/i}."
    $ trapperObj.change("emote", "none")
    $ trapperObj.change("emotion", "mad")
    tt "If you want to get to her, you have to get through me, first."
    call speedlinesredscene(withDissolve=False)
    call event_confess
    show trapper at movecenterleft
    $ trapperObj.change("emotion", "happy")
    show trapper at slidetomovecenter
    $ trapperObj.change("pose", "close03")
    tt "By passing... Trapper's Test (TM). Coming BHVR TV, Sundays at 8PM."
    tt "Welcome to Trapper's Test. Answer My Questions Correctly Or Die By My Blade."
    call minescene(withDissolve=False)
    show trapper
    show spirit behind trapper at moveright 
    show trapper at slidetomovecenterleft
    $ trapperObj.change("emote", "exclamation")
    tt "QUESTION ONE!"
    $ trapperObj.change("emote", "none")
    $ trapperObj.change("pose", "close02")
    $ trapperObj.change("emotion", "disgusted")
    menu:
        tt "What is Spirit's real name? The one given to her by her murderous father, which she only lets her {i}real{/i} friends call her."
        "Yumi Koyama":
            show incorrect at center
            mc ""
        "Sachiko Yamaoto":
            show incorrect at center
            mc ""
        "Rin Yamaoka":
            $ spirit_aff = spirit_aff + 1
            show correct at center
            $ trapperObj.change("emote", "sweat")
            tt "Ok, you got that one. Don't celebrate yet."
            $ trapperObj.change("emote", "none")
    hide incorrect
    hide correct
    with dissolve
    tt "QUESTION TWO!"
    menu:
        tt "What lives inside Spirit?"
        "A Dragon":
            $ spirit_aff = spirit_aff + 1
            show correct at center
            tt "Sure, everyone knows that. They won't all be this easy."

        "A Demon":
            show incorrect at center

        "A Ghost":
            show incorrect at center
    hide incorrect
    hide correct
    with dissolve
    tt "QUESTION THREE!"
    menu:
        tt "Where did Spirit work back when she was a normal college girl, before she was hell-bent on revenge?"
        "Salon":
            show incorrect at center

        "Pet Store":
            show incorrect at center

        "Restaurant":
            $ spirit_aff = spirit_aff + 1
            show correct at center
            tt "I know, to think I would date a waitress. Don't tell my father I ever mingled with the help like that, he'd be so disappointed in me."
    hide incorrect
    hide correct
    with dissolve
    tt "QUESTION FOUR!"
    menu:
        tt "What's Spirit's favorite color?"
        "Purple":
            show incorrect at center

        "Black":
            $ spirit_aff = spirit_aff + 1
            show correct at center
            tt "Are these questions largely superficial? Sure. maybe I didn't get to know Spirit that well. Maybe that's why she dump--maybe that's why it didn't work out for us. Who knows."

        "Red":
            show incorrect at center
    hide incorrect
    hide correct
    with dissolve
    $ trapperObj.change("pose", "close03")
    $ trapperObj.change("emotion", "mad")
    $ trapperObj.change("emote", "sparks")
    tt "QUESTION FIVE: THE FINAL QUESTION"
    $ trapperObj.change("emote", "none")
    nrr "You got this, [mc_name]."
    menu:
        tt "According to Spirit, what's worse than being dead?"
        "Having unfinished business":
            show incorrect at center

        "Regretting parts of your life":
            show incorrect at center

        "Not being seen for who you are":
            $ spirit_aff = spirit_aff + 1
            show correct at center
            $ trapperObj.change("emotion", "disgusted")
    tt "When I pitched Trapper's Test to the suits at BHVR TV, they told me there was no room in the budget for a new car to be given as the final prize for winning."
    hide incorrect
    hide correct
    with dissolve
    $ trapperObj.change("pose", "close02")
    $ trapperObj.change("emotion", "happy")
    tt "So I killed them all, right there on the spot. While killing them didn't solve any of the budget problems, it sure did feel good."
    tt "I'm telling you this a.)to brag and b.)to explain why the only thing you're going to win is me saying \"CONGRATULATIONS FOR PASSING TRAPPER'S TEST!\""
    call event_badslinky
    $ trapperObj.change("pose", "close01")
    $ trapperObj.change("emotion", "disgusted")
    $ spiritObj.change("emotion", "disgusted")
    tt "Not that it was some huge challenge. I mean, the women obsessed with a giant light that shines in th dark has a chip on her shoulder about being seen? Go figure. You probably guessed, but rules are rules even if I literally just made them up, you got it right."
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    tt "So I guess I approve of you dating Spirit, or whatever. I never really cared in the first place, I was just hoping you'd slip up and give me a good excuse to wet my blade with your blood."
    $ spiritObj.change("emotion", "happy")
    tt "Maybe I'll find a reason tomorrow. For now, you two have fun. Wink-wink-wink Trapper out!"
    stop eventloop fadeout 3.0
    hide trapper
    show spirit at slidetomovecenter
    with dissolve
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emote", "sweat")
    ts "I'm sorry you had to endure that."
    $ spiritObj.change("emote", "none")
    mc "What, five measly questions? It was nothing."
    ts "Not even that, as ridicious and unnecessary as it was. The whole thing."
    ts "The waking up in a random tunnel, the overhearing our argument, the news that Trapper and I had something going on, and the stupid quiz. All of it. Especially the whole \"Trapper out!\" catchphrase."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close03")
    ts "It's only because I {i}actually{/i} like you. None of it would've happened if I didn't."
    mc "And I... I like you too, Spirit."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("emote", "heart")
    ts "Please... call me Rin."
    $ spiritObj.change("emote", "none")
    $ spirit_name = "RIN"
    mc "Rin."
    ts "I didn't really feel like our lighthouse experience was completed. There was someting else I wanted to show you..."
    ts "Alone up in the lantern room of the tower..."
    nrr "Get your mind out of the gutter, [mc_name]. It's not kind of game!"
    nrr "What's that? Hold on a moment. I'm being told, no, wait, it {i}is{/i} that kind of game. Disregard the gutter comment."
    $ spiritObj.change("emote", "thoughts")
    ts "Come back up there with me?"
    $ spiritObj.change("emote", "none")
    mc "There's no place I'd rather be."
    call blackscene
    call lighthouseinsidenightscene
    stop music
    nrr "You're excited to return to the lantern room of this lighthouse, despite all of the drama and worry that was previously a part of this place for you."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose01")
    show spirit
    nrr "More importantly, you're excited to be there with Spirit."
    nrr "Which makes it all the more crushing..."
    $ spiritObj.change("emotion", "disgusted")
    show spirit at slidetomovecenterright
    $ clauddwightObj.change("emotion", "sad")
    $ clauddwightObj.change("pose", "pose02")
    show clauddwight at movecenterleft behind spirit with dissolve
    nrr "When you're interrupted by the arrival of Claudette and Dwight."
    mc "Claudette, Dwight. Funny seeing you here. Wait, did I say funny? I meant tragic."
    $ clauddwightObj.change("emotion", "idle")
    cl "Tragic? I don't think so..."
    $ clauddwightObj.change("emotion", "happy")
    $ spiritObj.change("emotion", "idle")
    dw "What could be tragic about a family reunion?! Those are always joyous occasions, in my experience."
    $ clauddwightObj.change("emotion", "idle")
    nrr "Before they can explain what that's even suppose to mean, the lighthouse begins to howl a low, frightening sound."
    call lighthouseinsidenighteyescene(keep_images=True)
    nrr "The lens begins to glow in a now familiar way. You prepare to shield your eyes, in case something bad happens to you again."
    mc "Now isn't the time for any reality-show-adjacent shenanigans. Dwight! Claudette! Shield your eyes! We don't know what the lighthouse will--"
    $ clauddwightObj.change("emotion", "happy")
    dw "Now now, please don't interrupt."
    cl "You'd think after all of this time, you'd know that we've got your best interests in mind!"
    mc "Wait, what? No, of course I don't think that, I--"
    $ clauddwightObj.change("emotion", "disgusted")
    dw "Got wax in your ears, friend? I asked you not to interrupt."
    nrr "Too late. The black light flairs. In the darkness you see something horrible and strange. In the place of Claudette and Dwight are two ghoulish silhouettes."
    nrr "But before you can focus on them, the light passes and the two survivors are returned to their normal states."
    cl "It's breezy up here! Should've packed a sweater."
    mc "What in the hairy hell?"
    $ clauddwightObj.change("emotion", "mad")
    dw "HEY! Watch the language! You shouldn't speak that way..."
    play sound "sounds/sfx_signature_oni01.ogg"
    call mood_speedlines
    show oni behind spirit with dissolve
    show spirit at slidetomoveright
    show clauddwight at slidetomoveleft
    $ clauddwightObj.change("emotion", "happy")
    cl "...around your elders!"
    $ spirit_name = "THE SPIRIT"
    $ clauddwightObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "scared")
    $ spiritObj.change("emote", "sparks")
    ts "Grandpa?!"
    $ spiritObj.change("emote", "none")
    $ oniObj.change("emote", "heart")
    $ oniObj.change("emotion", "happy")
    to "My little Rin! You're such a woman now. They grow up so fast."
    $ oniObj.change("emote", "none")
    mc "Uhhh... wha?"
    $ spiritObj.change("emote", "sweat")
    $ spiritObj.change("emotion", "happy")
    call event_freshflesh
    ts "[mc_name], meet grandpa Kazan Yamaoka. Well, techically not just {i}grandpa{/i}. Technically he's my {i}great great great great great grandpa{/i}. But that's a lot of greats to say in a row."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    to "I haven't seen my little Rin since I watched over her from the afterlife when she was just a little girl."
    $ clauddwightObj.change("emotion", "sad")
    $ oniObj.change("emote", "sparks")
    $ oniObj.change("emotion", "mad")
    to "And I expect you all to say the greats. It's a matter of honor and respect! Expect Rin, she can do whatever she wants, my precious little angel. But you..."
    $ oniObj.change("emote", "none")
    nrr "Oni stares at you with his demonic red eyes. You're pretty sure even the decorative third eye on his mask is looking at you."
    $ oniObj.change("emote", "angry")
    $ oniObj.change("pose", "pose02")
    to "... you mongrel. You must treat me with respect! Or so help me, I'll be cleaning bits of your head off of my kanabo."
    $ oniObj.change("emote", "none")
    nrr "A knanbo is like a metal baseball bat covered in spikes, FYI."
    to "I'm not sure what a peasant like you is doing so close to a descendant of the noble Yamaoka bloodline in the first place!"
    $ oniObj.change("pose", "pose01")
    $ oniObj.change("emotion", "disgusted")
    to "Dirk, Claudine, explain what's going on to me!"
    $ clauddwightObj.change("emotion", "scared")
    dw "It's Dwight, sir. And Claudette. Remember? We explained to you that you were going to come meet with your great great great great granddaughter's suitor and to give or withhold your approval."
    $ oniObj.change("emote", "sparks")
    $ spiritObj.change("emote", "sweat")
    $ oniObj.change("emotion", "mad")
    $ spiritObj.change("emotion", "scared")
    $ oniObj.change("pose", "pose02")
    to "FIVE GREATS!"
    $ oniObj.change("emote", "none")
    $ spiritObj.change("emote", "none")
    dw "Great great great great great grandfather, sir, your honor, master... sir."
    $ clauddwightObj.change("emotion", "sad")
    $ spiritObj.change("emotion", "idle")
    cl "Dwight, he's a samurai, not a judge."
    $ oniObj.change("emotion", "idle")
    $ oniObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "happy")
    ts "Grandpa, they must've summoned you here because they think you have great judgement and because if they summoned my father I would be too distracted by torturing him for all of eternity to continue wiht the rest of the... whatever this is. Show? Game? Experience?"
    $ spiritObj.change("emotion", "idle")
    $ oniObj.change("emote", "stars")
    $ oniObj.change("emotion", "happy")
    to "Ah yes, that makes sense. Only a man of my own power and magnitude can help."
    $ oniObj.change("emote", "none")
    nrr "Self-important much?"
    mc "Nice to meet you, Kazan."
    $ oniObj.change("emotion", "disgusted")
    to "Only my friends and family call me Kazan! Those who tremble in fear at my presence call me Oni."
    nrr "You're seeing a serious resemblance to Trapper in not only the sheer size of the man that Oni is but also his attitude. Apparently Spirit has a type. You sure you can--or want to--measure up to that?"
    nrr "It dawns on you that, wait a second, maybe you DO resemble Oni. Every time you've tried to look at your own reflection, however, you've become dizzy and confused."
    nrr "This definitely deserves more thought, but now's not the time to consider the fact that you might be some kind of hulking vampire with the first-ever case of self-blindness. There's a massive samurai mad-dogging you from two steps away."
    mc "Well, you don't scare me at all, so I'll stick with Kazan."
    $ oniObj.change("emotion", "mad")
    $ oniObj.change("emote", "angry")
    $ spiritObj.change("emotion", "scared")
    $ oniObj.change("pose", "pose02")
    to "PEASANT! I realize now the true purpose of my visit is to extinguish your light!"
    $ oniObj.change("emote", "none")
    nrr "Oni waves his katana in the air at you menacingly. Like Great great great great great grandfather, like great great great great great granddaughter, apparently."
    $ spiritObj.change("emote", "exclamation")
    $ oniObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose03")
    ts "Hold up there, grandpops, not so fast. You're only supposed to kill 'em if they deserved it. First you should get to know them a little better."
    $ spiritObj.change("emote", "none")
    to "Young people these days! Always waiting to kill people, insisting they must \"deserve it.\" Back in my day, you did what needed to be done because your nobility depended on it!"
    nrr "In his day? For such an imposing presence, he sure is giving off serious \"old man yells at cloud\" vibes."
    $ oniObj.change("emotion", "disgusted")
    $ oniObj.change("emote", "thoughts")
    $ oniObj.change("pose", "pose01")
    $ spiritObj.change("pose", "pose01")
    to "You see, when I was a yound man, we didn't have foreigners in our land. Didn't need 'em! We had an abundance of culture already. A little too much, if you ask me, but I didn't make the rules, the rulers did--exactly how it should be!"
    $ oniObj.change("emote", "none")
    to "Literature. Art. Commerce. Theatre. Fashion. Poetry. Puppet shows. Ghost stories. Courtesans. Gambling. Fighting. Fine dining. Fast food. Public executions..."
    $ oniObj.change("emote", "question")
    $ oniObj.change("emotion", "idle")
    to "What were we talking about?"
    $ oniObj.change("emote", "none")
    $ oniObj.change("emotion", "happy")
    nrr "Spirit giggles at her great great--ok, I'm not saying all of those every time--at Oni's forgetfulness. You wonder, does she even like this guy? She sure hates her father, so..."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose03")
    mc "Listen up, old man. We don't have time for you to a list of every activity available to a samurai in the entirety of the Edo period."
    $ oniObj.change("emotion", "mad")
    to "Silence, peasant! You're showing your ignorance! Samurai were forbade from many activities that didn't befit the Bushido code! Such as attending certain theatrical performances, for instance. Sometimes, however, a samurai would put on a disguise in order to seek out entertainment..."
    $ oniObj.change("emotion", "happy")
    to "Now, I'm not saying I did that, because I had honor, and a body built like an entire castle that is quite hard to hide. But clearly you have neither my honor nor my physique! You don't even know about the ins andf outs of the shifting rules of traditional Japanese Samurai ettiquette! You fool!"
    $ oniObj.change("emotion", "disgusted")
    to "Rin, what would you want with such an uneducated admirer as this?"
    nrr "You find it hard to believe that any contemporary person knows all that much about who was and wasn't allowed to do what leisure activities over one hundred years ago. However, you're really not sure how to handle this massive, demonic old man."
    $ oniObj.change("emotion", "happy")
    to "Oh, wait, I get it. Sweet Rin, my beautiful descendent. You've invited me here to do what you're too kind to do..."
    $ oniObj.change("emote", "sparks")
    $ oniObj.change("pose", "pose02")
    $ spiritObj.change("emote", "sweat")
    $ spiritObj.change("emotion", "scared")
    to "Bash this jerk's head in!"
    $ oniObj.change("emote", "none")
    $ spiritObj.change("emote", "none")
    to "Claude, Dorris, fetch my kanabo! Rin, wrap your robe around this mongrel's hands and hold them still. We'll splatter their brains on the beach, togetherm as a family!"
    $ spiritObj.change("emotion", "idle")
    $ spirit_name = "RIN"
    ts "Grandpa, no! That's not why I invited you here at all! In fact, I didn't invite you. {i}Claudette{/i} and {i}Dwight{/i} did."
    $ oniObj.change("emote", "sweat")
    to "Ah, ha ha, yes, sure. Wink wink wink."
    $ oniObj.change("emote", "none")
    nrr "This whole \"saying wink out loud\" thing is getting out of hand. Him and Trapper really do have a lot in common don't they?"
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("emote", "thoughts")
    ts "I swear, [mc_name] has a good soul, and the heart of a warrior! They've fought for my love, in their own way. Faced down death, more than once, and put up with their fair share of nonsense."
    $ spiritObj.change("emote", "none")
    mc "Nonsense which seems to be endless. Can we, I dunno, wrap this up already?"
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose01")
    to "Of course, of course. Who am I to expect anyone to wait around for my approval. I've only been hanging out as a ghost and watching my bloodline be polluted bby cowards and quitters for five generations."
    $ oniObj.change("emotion", "idle")
    to "Just come give your ancestor-in-law a hug."
    nrr "Sword drawn, Oni beckons you closer. There's no way he has ever hugged anyone in his entire life."
    mc "I think I'm good over here, actually."
    $ oniObj.change("emotion", "mad")
    to "Rin! Now! Push them my way and I'll split them in half! Tha sacrifice of this usurper to the Yamaoka bloodline will surely bring us back to life and set us back on the course of honor!"
    $ spiritObj.change("emotion", "happy")
    ts "You're so silly, Grandpa. We both know that only one sacrifice can get our family back on track..."
    $ spiritObj.change("emote", "angry")
    $ spiritObj.change("emotion", "mad")
    ts "REVENGE ON MY FATHER, YOUR GREAT GREAT GREAT GREAT GREAT GRANDSON, TRAITOR TO THE YAMAOKA NAME!"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "sad")
    to "The lust for violence in your voice... it fills me with cheer."
    ts "I'll never forget who I am."
    $ oniObj.change("pose", "pose01")
    to "I suppose, if this is the person you want to be with, to go on your journey of bloody revenge with, I should trust your judgement. The strength inside of you blooms from the same cherry tree that was planted centuries ago by our shared ancestors."
    $ spiritObj.change("emote", "sparks")
    $ spiritObj.change("pose", "pose02")
    $ spiritObj.change("emotion", "happy")
    ts "And if [mc_name] ever treats me poorly, you have my word, on out family's honor, I will wield my katana and gut them like a fish."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "pose01")
    nrr "A tear rolls down from behind Oni's demonic mask."
    mc "You sure you want to marry into... this?"
    to "And one last word of advice, my dear girl. The father stuff? Don't forget it, but maybe stop focusing so specifically and obsessively on it."
    to "What he did, it was awful, but it was already done. Do something for yourself, now."
    to "Just my two cents."
    to "Be well, Rin. I will see you again soon."
    $ oniObj.change("pose", "pose02")
    $ oniObj.change("emotion", "idle")
    to "Now let's go, servants! Clint, Danice. Return me to the stables! I assume my dragon has been fed and tended to?"
    $ clauddwightObj.change("pose", "pose02")
    cl "Ummm, yes? Sure?"
    dw "I swear, this is still better than dealing with Trapper's dad."
    stop music
    hide oni
    hide clauddwight
    show spirit at slidetomovecenter
    with dissolve
    $ spiritObj.change("pose", "pose03")
    mc "I'm sorry if I was disrespectful to your great great great great great grandfather. He seemed like a... very special man."
    mc "I realize I will never measure up to someone likee that. A warrior with a hell of a fashion sense. I mean, that mask..."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "close03")
    ts "Don't worry, I would never expect you to. Or want you to, really. If all I wanted was the biggest brute alive, I'd be down in Trapper's cave right now avoiding his vintage bear traps."
    $ spiritObj.change("emotion", "idle")
    ts "But that's not the life I've imagined for myself."
    ts "This sense of abstract duty, anger at a world changing around me, a lust for blood... that's now way to live. And yet, as you now know, that {i}is{/i} the Yamaoka way of life."
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close04")
    ts "Forever, I'm cursed to battle against the dragon that lives inside me. Or at least, maybe, I was, until now..."
    mc "Call me the dragon tamer, baby."
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("emote", "sweat")
    ts "You haven't won this game yet. Please, don't ruin it."
    $ spiritObj.change("emote", "none")
    mc "Sorry, I havfe no idea where that came from."
    $ spiritObj.change("emotion", "idle")
    ts "I think we've spent enough time in this lantern room. We should get back to the beach."
    call lighthousenightscene
    stop music
    nrr "The moodlight sets a romantic mood as storm clouds roll in and surround the Black Lighthouse."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("pose", "pose04")
    ts "You know, the sun might've set, but if we wait long enough, it will rise again..."
    call mood_romantic
    call event_sex
    $ spiritObj.change("emotion", "idle")
    $ spiritObj.change("pose", "close04")
    $ spiritObj.change("swim", "True")
    show spirit
    nrr "Spirit removes her sheer robe, showing you her strappy black bikini. Her pale skin glows under the light of the moon."
    $ spiritObj.change("emotion", "happy")
    $ spiritObj.change("emote", "heart")
    ts "Maybe you could help me get a head start on applying tomorrow's sunscreen..."
    $ spiritObj.change("emote", "none")
    mc "Again? I mean, yeah, of course! Last time... well, I definitely felt more connected to you afterwards."
    ts "To be totally real with you, I kinda just asked you as a good, but... I really enjoyed it."
    ts "I swear, though... if you tell anyone about this. I will {i}not{/i} be labelled a foot freak. Not that there is anything wrong with feet, it's just that something about that kind of attention really get people talking."
    call lighthousenightscene(keep_images=True)
    show spirit
    $ sunscreen_turn = 0
    $ sunscreen_perfects = 0
    $ sunscreen_good = 0
    stop moodloop fadeout 3.0
    nrr "Steady... steady..."
    while (int(sunscreen_turn) < 9):
        call start_sunscreen_minigame
        if sunscreen_section == 1:
            call end_sunscreen_minigame
            $ sunscreen_perfects = sunscreen_perfects + 1
            ts "YES!"
        elif sunscreen_section == 2:
            call end_sunscreen_minigame
            $ sunscreen_good = sunscreen_good + 1
            ts "Almost..."
        else:
            call end_sunscreen_minigame
            ts "Close..."
        $ sunscreen_turn = sunscreen_turn + 1
        $ sunscreen_speed = sunscreen_turn + 1
    if sunscreen_perfects >= 5:
        ##Perfect
        show spirit
    elif sunscreen_good > 1:
        ##Good
        show spirit
        ts "{i}God that's so goddamn hot{/i}. I love feeling hands sliding up and down my feet and between my toes. My skin has never been more moist."
        $ spiritObj.change("emotion", "obsessed")
        ts "{i}Get up here right now{/i}!"
        nrr "Before you can find a towel to wipe off your lotioned hands, Spirit grabs you and pulls you in close."
        $ spiritObj.change("emotion", "sad")
        nrr "Her lips lock onto yours. They're surprisingly soft and warm. The sensation is..."
        mc "... incredible."
    elif (sunscreen_good == 1) and (sunscreen_perfects == 0):
        ##Bad 1/5
        show spirit
    else:
        ##Missed Completely
        show spirit
    scene black
    nrr "cover the moon and you find youself on the beach with Spirit in complete darkness."
    nrr "You can feel the narrow straps of her bathing suit come undone and come to life, snaking through the air, wrapping around your body, lifting you up off of your feet."
    ts "Come here, you."
    mc "So this is what it feels like..."
    mc "... to fly..."
    nrr "As Spirit pulls you close, you feel bits of glass press into your flesh. Pain and pleasure mix and wash over you like the oceam, salty air stinging your skin as you writhe against your undead lover."
    nrr "The lighthouse howls..."
    nrr "In the darkness, you're pretty sure that Spirit lets the dradon inside of her take over."
    nrr "If it kills you, you're sure it will have all been worth it."
    call lighthousenighteyescene
    $ renpy.music.set_volume(0,0,"music")
    nrr "The clouds part just as you manage to pull yourself, exhausted, away from Spirit."
    call mood_warmdark(image_name="images/shard.png", ismovefrombottom = True, withDissolve = True)
    nrr "A chunk of broken glass is lodged in your shoulder. When you pluck it from your skin, it drips blood."
    mc "Sorry, I... think this got stuck to me when we were... when I was... when... you know, I was having the best night of my life."
    nrr "Spirit drags her fingertip over the sharp end of the glass shard."
    stop moodloop fadeout 3.0
    $ spiritObj.change("emotion", "idle")
    ts "Keep it. Consider it a memento."
    $ spiritObj.change("emotion", "happy")
    ts "I've got plenty more where that came from."
    call blackscene
    call beachnightscene
    nrr "You arrive at the beach to find Claudette and Dwight waiting for you."
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    show clauddwight
    cl "Now is the time, [mc_name]..."
    call event_confess
    dw "...to face you destiny."
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "idle")
    $ spiritObj.change("emotion", "scared")
    $ spiritObj.change("pose", "pose04")
    $ spiritObj.change("emote", "sweat")
    show spirit at movecenterright with dissolve
    show clauddwight at slidetocenterleft
    ts "Actually, about that..."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("swim", "False")
    $ spiritObj.change("pose", "pose01")
    ts "[mc_name], can we talk? Privately? Maybe, ummm... not here. Maybe someplace else would be better for this talk."
    $ clauddwightObj.change("emotion", "disgusted")
    cl "You know how we feel about schedules, Spirit."
    dw "{i}Very strongly.{/i}"
    show clauddwight behind spirit
    $ spiritObj.change("emotion", "mad")
    $ spiritObj.change("pose", "close01")
    ts "And you know how I feel about you telling me what to do..."
    $ clauddwightObj.change("emotion", "scared")
    $ spiritObj.change("emote", "angry")
    ts "{i}Don't do it{/i}."
    $ spiritObj.change("emote", "none")
    call event_storytime
    ts "Like I said, I'd rather have this talk with [mc_name] privately. It's not right to do it here in front of everyone."
    hide clauddwight
    $ spiritObj.change("emotion", "disgusted")
    $ trapperObj.change("emotion", "happy")
    $ trapperObj.change("pose", "pose01")
    show trapper behind spirit at moveright 
    with dissolve
    tt "You know, from my experience in upper management at my father's mine, I learned that if you're going to fire someone, it's best to do it in public so they don't freak out."
    $ trapperObj.change("emotion", "disgusted")
    $ wraithObj.change("emotion", "scared")
    $ wraithObj.change("pose", "pose01")
    show wraith behind spirit at movecenterleft with dissolve
    tw "Please, enough of the fire talk!"
    $ wraithObj.change("emotion", "disgusted")
    $ huntressObj.change("emotion", "scared")
    $ huntressObj.change("pose", "pose01")
    $ trapperObj.change("emotion", "idle")
    show huntress behind wraith at moveleft with dissolve
    th "Wait, you think...  No! She couldn't be. They seemed so in love! Well, I mean, not rally, Spirit is still Spirit."
    $ huntressObj.change("emotion", "disgusted")
    th "But if I tried to imagine Spirit in love, I suppose... she hasn't attempted to murder [mc_name] yet? So..."
    th "OK, fine, your guess is as good as mine, really. That girl is {i}very{/i} hard to read."
    $ huntressObj.change("pose", "pose02")
    $ huntressObj.change("emotion", "idle")
    th "A word of advice, though. If you're going to end it, end it quickly. In my experience, the more pathetic the creature, the more annoying the final howls are."
    $ spiritObj.change("emotion", "mad")
    $ spiritObj.change("pose", "close02")
    $ huntressObj.change("emotion", "scared")
    $ wraithObj.change("emotion", "scared")
    $ trapperObj.change("emotion", "scared")
    $ spiritObj.change("emote", "sparks")
    ts "I don't need any advice! Every OUT! Except for [mc_name]."
    $ spiritObj.change("emote", "none")
    hide trapper
    hide huntress
    hide wraith
    $ tricksterObj.change("pose", "pose01")
    $ tricksterObj.change("emotion", "happy")
    show trickster behind spirit at movecenterleft
    with dissolve
    play sound "sounds/sfx_signature_trickster01.ogg"
    tr "Did someone say \"final howls\"? That kind of my whole jam. I can stay, right?"
    $ tricksterObj.change("pose", "pose02")
    $ tricksterObj.change("emotion", "sad")
    $ spiritObj.change("emote", "angry")
    ts "ESPECIALLY YOU! OUT!"
    $ spiritObj.change("emote", "none")
    tr "Lame."
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    show spirit at slidetomovecenter
    hide trickster with dissolve
    nrr "Alone with Spirit, you feel something awful hanging in the air. More awful een than the lingerin smell of that Cleaver Body Spray. (Ugh, that gag... I'm gagging. We're all gagging... for Cleaver Body Spray.)"
    mc "Spirit--Rin--I..."
    mc "I don't know what you plan on saying, but before you say anything, just know that I really, really enjoyed my time with you."
    mc "Getting to know you over the past few days helped me to get to know myself. For that, I just wanted to say thank you."
    $ spiritObj.change("pose", "close02")
    $ spiritObj.change("emotion", "happy")
    ts "That's sweet. You're welcome. And, you know what? It's that kind of thing that shows me you've got a good heart inside you. Too good for me to carve out and toss into the ocean. But also too good for me to love."
    $ spiritObj.change("emotion", "idle")
    ts "I need someone who shares my interests. Someone I can connect with. Someone jaded and dispassionate, only driven forward by a desire for revenge."
    $ spiritObj.change("pose", "close03")
    $ spiritObj.change("emotion", "happy")
    ts "I need someone who isn't so warm that I feel cold in comparison."
    $ spiritObj.change("emotion", "disgusted")
    ts "I need someone who... isn't you."
    $ spiritObj.change("emotion", "idle")
    ts "Can we just be friends?"
    mc "I don't know if--"
    $ spiritObj.change("pose", "close01")
    ts "Before you finish that, just know, if we're not friends we'll probably become enemies, and I will destroy you."
    mc "Friends it is!"
    ts "I'm glad to have you here for me when I need you, but also not too close to me when I don't."
    $ spiritObj.change("emotion", "happy")
    ts "So yeah, I'll see you around."
    nrr "Spirit starts to leave."
    mc "Wait. What? That's it? That's how this ends? You're just leaving me here?"
    $ spiritObj.change("emotion", "disgusted")
    ts "I'm not sure I'd use the word \"ends.\" And, for that matter, I wouldn't say that I'm \"leaving.\" But us? We're definitely through. The fact that you can't see that... well, it just proves that we never really belonged together anyhow. Good night, [mc_name]."
    mc "What the hell! I just spent all this time on this island, doing everything I can to get to know you, only to be told that I should just leave the chocolate factory through the side door?"
    $ spiritObj.change("emote", "dread")
    ts "I don't know what that means. Anyway, I {i}said{/i} good night, [mc_name]. See you around."
    $ spiritObj.change("emote", "none")
    nrr "Geez. I'm sorry. What a bummer."
    mc "Hey, why did she keep saying she'll see me around."
    nrr "Gosh, I have no idea..."
    call cgvolleyball
    call event_cooloutfit
    oc "And so, my precious Killers lived happily ever after. As they should, learning to love themselves, first and foremost..."
    oc "...whilst trapped in a never-ending cycle of torture, of my design."
    oc "Wait, did I just spoil my true identity? You made it this far, you should probably know that..."
    oc "...that you'll have to play again to find out more!"
    oc "Goodbye, [mc_name]! See you again later! And again, and again, and again..."
    oc "FOREVER!"
    return