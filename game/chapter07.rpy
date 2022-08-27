label chapter07:
    $ renpy.music.set_volume(0,3.0,"music")
    call beachdayscene(withDissolve=False)
    $ clauddwightObj.change("emotion", "idle")
    $ clauddwightObj.change("pose", "pose01")
    show clauddwight
    with dissolve
    nrr "When you arrive at the beach, you realize you were set up! Despite promising an announcement, Dwight and Claudette simply stand quietly. This isn't at all what was promised."
    call event_choices
    mc "Wait a minute, there's no announcement here..."
    $ wraithObj.change("emotion", "happy")
    $ wraithObj.change("pose", "pose03")
    $ wraithObj.change("emote", "sparks")
    hide clauddwight with dissolve
    show wraith with Dissolve(0.25)
    tw "But there is... {i}a me{/i}!"
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("emotion", "idle")
    show wraith at slidetomovecenterleft
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "pose01")
    show spirit behind wraith at movecenterright with Dissolve(0.25)
    ts "You got mud in your ears, friend? I told you to GET LOST!"
    $ wraithObj.change("emotion", "happy")
    $ wraithObj.change("pose", "pose01")
    tw "Don't you see? Lost is what I am, and so are you! But I know the way out. I've got a map back in my secret lair. Literally. And figuratively. Yeah... I know that difference."
    $ wraithObj.change("pose", "close02")
    $ spiritObj.change("pose", "pose03")
    tw "That's why you should ditch Spirit and come spend the rest of the night with me, instead."
    mc "You've got a secret lair?"
    $ wraithObj.change("pose", "pose02")
    $ wraithObj.change("emote", "sweat")
    $ spiritObj.change("pose", "pose01")
    $ wraithObj.change("emotion", "disgusted")
    tw "Damnit!"
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("pose", "pose01")
    tw "Who said anything about a \"secret lair?\""
    $ wraithObj.change("emotion", "scared")
    $ wraithObj.change("pose", "pose03")
    tw "I said I've got, ummm, sap! Sap in my... secret... hair? There's a flap... on my secret chair?"
    $ wraithObj.change("emotion", "mad")
    $ wraithObj.change("emote", "sparks")
    $ spiritObj.change("emotion", "scared")
    tw "Don't change the subject!"
    $ wraithObj.change("emotion", "disgusted")
    $ wraithObj.change("emote", "none")
    mc "..."
    $ spiritObj.change("emotion", "disgusted")
    nrr "Don't ask me what he's talking about."
    $ spiritObj.change("pose", "pose02")
    $ spiritObj.change("emote", "anger")
    $ spiritObj.change("emotion", "mad")
    tw "You're trying to make a mess of the first nice day I've had in--I don't know how long because it's not even clear what year it is--but in... {i}a while{/i}!"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("emotion", "disgusted")
    ts "I'm not about to be ditched for the likes of you."
    $ wraithObj.change("pose", "pose02")
    $ wraithObj.change("emotion", "mad")
    tw "It's not me messing things up. Like I keep trying to tell you, it's this dang island!"
    $ wraithObj.change("emote", "dread")
    $ wraithObj.change("emotion", "idle")
    tw "I've come to accept a difficult truth. What's happening here, well, I'm convinced that it's our fate. It's not anyone's decision. It's simply the way it will be. There's no use fighting it."
    $ wraithObj.change("emote", "none")
    $ wraithObj.change("emotion", "disgusted")
    $ wraithObj.change("pose", "pose03")
    $ spiritObj.change("pose", "pose01")
    ts "What would you even know about fighting? All you know is hiding in your spooky little \"secret hair\" and crying like a baby while ringing your little bell."
    $ spiritObj.change("emotion", "mad")
    ts "So don't tell me what I can and can't fight back against. I was born a fighter. A dragon lives inside me! I can't not fight, even when all I might want to do is hide! Don't you see this giant hat?? It's a {i}metaphor{/i}!"    
    $ spiritObj.change("emote", "sparks")
    $ wraithObj.change("pose", "pose01")
    ts "If I do have a fate, my fate is to win every fight that comes my way, got it?!"
    $ spiritObj.change("emote", "none")
    show spirit at slidetomoveright
    show wraith at slidetomoveleft
    $ clauddwightObj.change("emotion", "idle")
    $ clauddwightObj.change("pose", "pose01")
    show clauddwight with dissolve
    cl "Folks..."
    $ wraithObj.change("emotion", "mad") 
    tw "Oh, you hide. I've seen you hide. You do your little... your phase-walking routine, what do you call that? It's basically cloaking. And we all know that cloaking is a type of hiding."
    $ clauddwightObj.change("emotion", "disgusted")
    dw "{i}Folks{/i}..."
    $ spiritObj.change("pose", "pose02")
    ts "You cloak, I don't cloak. I'm not a cloaker! I phase-walk out in the open, {i}you{/i} just can't {i}see{/i} me!"
    $ clauddwightObj.change("emotion", "sad")
    nrr "You have no idea what they're talking about, but this sure sounds like some video game community forum thread minutia if there ever was such a thing--not that you know about that, either."
    nrr "It sure doesn't seem like Dwight and Claudette are going to stop this, so it's on you."
    $ spiritObj.change("emotion", "disgusted")
    $ wraithObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "pose03")
    $ wraithObj.change("pose", "pose03")
    mc "*AH-HEM*"
    mc "I think I was brought here to make this choice, so I'm going to do that now."
    $ spiritObj.change("emotion", "idle")
    $ wraithObj.change("emotion", "idle")
    $ diamondchoice = True
    menu chosen_killer:
        mc "And I choose..."
        "gui/button_spirit_idle.png¦gui/button_spirit_hover.png¦gui/button_spirit_select.png":
            $ diamondchoice = False
            nrr "When it comes down to it, neither of these two seems easy to love. I mean, damn, Spirit literally has broken glass shards sticking out of her. But... she has a certain charm to her gloom."
            $ spiritObj.change("emotion", "idle")
            $ wraithObj.change("emotion", "disgusted")
            $ spiritObj.change("pose", "pose04")
            $ wraithObj.change("pose", "pose01")
            mc "Spirit and I were actually having a nice time. Besides, if it's my fate to end up on this island, well, to hell with fate, really."
            mc "And don't take this the wrong way, Wraith, but... the amount of awkwardness you pack into a single day... no wonder you're so skinny! All that second-guessing yourself must burn a lot of calories."
            $ wraithObj.change("emotion", "scared")
            tw "No offense taken. It's... yeah OK it's true. I can be a little awkward. I guess. Sometimes."
            $ wraithObj.change("pose", "pose03")
            $ wraithObj.change("emotion", "disgusted")
            mc "Right. So I'm going to stick with Spirit!"
            $ spiritObj.change("pose", "pose03")
            nrr "Spirit breathes a sigh of relief."
            $ spiritObj.change("emote", "sweat")
            $ wraithObj.change("emotion", "happy")
            ts "I've got enough revenging to do without having to kill you and Wraith, too."
            $ spiritObj.change("emote", "none")
        "gui/button_empty_idle.png¦gui/button_empty_idle.png¦gui/button_empty_idle.png¦Disable":
            $ diamondchoice = False
            jump chosen_killer
        "gui/button_wraith_idle.png¦gui/button_wraith_hover.png¦gui/button_wraith_select.png":
            $ diamondchoice = False
            ##Missing Choice
            jump chosen_killer
        "gui/button_empty_idle.png¦gui/button_empty_idle.png¦gui/button_empty_idle.png¦Disable":
            $ diamondchoice = False
            jump chosen_killer
    stop eventloop fadeout 3.0
    call blackscene
    call lighthouse_day(withDissolve=False)
    call event_darkash
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    show spirit
    with dissolve
    nrr "Spirit walks you around a corner to show you something that she discovered in this place and knew was meant to be connected with her journey: A cherry tree."
    nrr "It is just a small sapling but it has begun to sprout flowers. It doesn't make sense to see a cherry tree here, in this place. It also doesn't make sense to see a ghost in a black bathing suit, so... you just accept it."
    $ spiritObj.change("pose", "pose03")
    show petals behind spirit
    nrr "As Spirit steps up to the tree, a cold breeze pull some petals off and they come cascading through the air around the both of you."
    $ spiritObj.change("emote", "question")
    ts "Do you know the meaning of cherry blossom?"
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "happy")
    ts "They're beautiful... but also quite symbolic. Of course, like all good symbols, their meaning is... pretty complicated."
    mc "What do they mean... to you?"
    $ spiritObj.change("pose", "close01")
    $ spiritObj.change("emotion", "idle")
    ts "For many people, being among cherry blossoms is like being at a celebration of life. People travel great distances just to be near their vibrant beauty."
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("emote", "dread")
    ts "However, as beautiful as they might be... they aren't magical, they're simply flowers. They quickly die and fade away, and for this reason they are also a symbol of the fleeing nature of life, of our fragile mortality."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("pose", "close03")
    ts "In a way, it's the specter of looming death that calls attention to this special moment; to see and appreciate life."
    $ spiritObj.change("emotion", "idle")
    menu:
        ts "The does that duality make you feel, [mc_name]?"
        "Empowered":
            mc "The knowledge that life and death are a cycle has always given me peace."
            mc "Accepting the fleeting nature of life, like the beauty of a flower in bloom, allows me to appreciate the moment without being too hung up on what comes next."
        "Frustrated":
            mc ""
        "Unsure":
            mc ""

    $ spiritObj.change("emotion", "sad")
    nrr "As you explain, Spirit's face begins to look sad to you. You're not sure why... it's not the happiest topic, life and death, but why should that matter?"
    nrr "And then it dawns on you, Spirit has been trapped in this ghastly state of death with no hope to cycle back, no rebirth, her moment of blossoming life long gone. That scary time of death and decay that comes after the good part, that's Spirit's eternity."
    $ spiritObj.change("pose", "close01")
    mc "I feel like an idiot. I wasn't talking about you! I wasn't even thinking about you, I just..."
    $ spiritObj.change("emotion", "disgusted")
    ts "You just answered from the heart. I can't let that bother me. Our priorities are not the same. I have my mission..."
    $ spiritObj.change("emotion", "idle")
    ts "Once, the fallen cherry blossoms represented the souls of samurai warriors. Those with noble characters, those who did not fear death, those who were killed in the greatest sacrifice: to honor their Emperor."
    $ spiritObj.change("pose", "close04")
    ts "Their lives were short, but their purpose gave them beauty. Those warriors saw death coming, but they never despaired. They stood and faced it. They held their swords and struck down their fear."
    $ spiritObj.change("emotion", "disgusted")
    $ spiritObj.change("pose", "close01")
    ts "But, despite the samurai spirit that lives on in me, in my noble bloodline..."
    ts "My life has ended, but my death continues to stretch on. The cycle is frozen."
    $ spiritObj.change("pose", "close02")
    ts "This cherry tree? It's not real. Though its petals fall, they soon replenish. It's as if it were installed here by someone..."
    nrr "You watch as Spirit chooses her words very carefully."
    $ spiritObj.change("emotion", "mad")
    $ spiritObj.change("emote", "dread")
    ts "...by {i}something{/i} with no respect for the balance of life and death."
    $ spiritObj.change("emote", "none")
    $ spiritObj.change("pose", "pose01")
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    play sound "sounds/sfx_signature_clauddwight04.ogg"
    show clauddwight behind spirit at movecenterleft with dissolve
    show spirit at slidetomovecenterright
    dw "We're sorry to interrupt!"
    $ spiritObj.change("pose", "pose03")
    $ spiritObj.change("emotion", "disgusted")
    ts "You know we don't believe you, right?"
    $ clauddwightObj.change("pose", "close01")
    cl "Yep!"
    dw "But this time we've got a really good reason!"
    $ clauddwightObj.change("pose", "pose01")
    $ clauddwightObj.change("emotion", "sad")
    cl "And it has nothing to do with us being manipulated by an unseen force! Because that's definitely not happening!"
    $ spiritObj.change("pose", "pose01")
    $ spiritObj.change("emotion", "idle")
    mc "Nobody accused you of that, but ok..."
    $ clauddwightObj.change("emotion", "happy")
    dw "We're just here to tell you that it's time for dinner, silly!"
    cl "Get it while it's hot!"
    $ clauddwightObj.change("pose", "pose04")
    ts "I guess it's time to go, or whatever. Thanks for spending time with me today. I enjoyed it."
    hide spirit
    mc "Me... too."
    call blackscene
    return

