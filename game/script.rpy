
# Declare the characters.

# define e = Character(_('Eileen'), color="#c8ffc8")
define nrr = Character(None, window_style="window_narrator", color="#3a2e55", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define oc = Character("", window_style="window_ocean", namebox_style="namebox_ocean", color="#3a2e55", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define mc = DynamicCharacter('mc_name', color="#3a2e55", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])

define dw = Character("DWIGHT", color="#bb7d31", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define cl = Character("CLAUDETTE", color="#b4992e", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define th = Character("THE HUNTRESS", window_style="window_killer", color="#c64631", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define ts = Character("THE SPIRIT", window_style="window_killer", color="#d94464", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define tt = Character("THE TRAPPER", window_style="window_killer", color="#335480", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])
define tw = Character("THE WRAITH", window_style="window_killer", color="#58902c", what_size=26, who_outlines=[ (absolute(1), "#FFF", absolute(0), absolute(0)) ], what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])

default name = ""

transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 10 rotate 360    
    repeat

init:
    image bg loading:
        "images/bg/bg_loading.png"
    image bg beach0:
        "images/bg/bg_beach_0.png"
    image bg volley0:
        "images/bg/bg_volley_0.png"
    image bg warmdark:
        "images/bg/bg_warmdark.png"
        zoom 1.1
    image bg inner_monologue:
        "images/bg/bg_inner_monologue.png"
    image bg haunting:
        "images/bg/bg_haunting.png"
    image bg excitement:
        "images/bg/bg_excitement.png"
        zoom 1.11
    image bg warmlight:
        "images/bg/bg_warmlight.png"
    image bg happy:
        "images/bg/bg_happy.png"
    image bg speedlinebg_red:
        xoffset -3920
        yoffset -1250
        zoom 2
        rotate -45
        anchor (0, 0) transform_anchor 1
        contains:
            parallel:
                Tile("images/bg/bg_speedlinebg_red.png")
                ytile 3
                xtile 3
                xpan -5400
                linear 8 xpan 180
                xalign 1
                yalign 1
                repeat

    define loadIn = ImageDissolve("images/bg/bg_loading.png", 5.0)
    define loadOut = ImageDissolve("images/bg/bg_loading.png", 5.0, reverse=True)

init python:
    import random
    config.character_id_prefixes.append('namebox')
    config.character_id_prefixes.append('window')
    def change_name(newstring):                                              
     #Functions that allow us to store the input
        store.name = newstring





image namebox_caret:                                                                
 #This is for that flashing line thingy next to your input :>
    Text("|", color="#323232",size=20)
    ypos -2
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat
style namebox_button:                                                               
 #Some styles..
    background Frame("gui/gui_input_name_textbox.png")
    xsize 430
    xpadding 10

style namebox_text:
    size 20
    hover_color "#323232"
    idle_color "#b6a699"
    selected_color "#323232"

style namebox_input:
    size 20
    caret "namebox_caret"
    
screen button_input():
    #Screen variable for input
    default input_on = False
    # add "images/overlay.png"    
    #Prevents user from accidentally clicking out of the screen                                                
    modal True              
    zorder 100                                                    
    key "a" action NullAction()
    key "b" action NullAction()
    key "c" action NullAction()
    key "d" action NullAction()
    key "e" action NullAction()
    key "f" action NullAction()
    key "g" action NullAction()
    key "h" action NullAction()
    key "i" action NullAction()
    key "j" action NullAction()
    key "k" action NullAction()
    key "m" action NullAction()
    key "n" action NullAction()
    key "o" action NullAction()
    key "p" action NullAction()
    key "q" action NullAction()
    key "r" action NullAction()
    key "s" action NullAction()
    key "t" action NullAction()
    key "u" action NullAction()
    key "v" action NullAction()
    key "w" action NullAction()
    key "x" action NullAction()
    key "y" action NullAction()
    key "z" action NullAction()
    frame:
        background Frame("gui/gui_input_name_frame.png")
        xpadding 256
        top_padding 90
        bottom_padding 40
        xalign 0.5
        yalign 0.5
        has vbox:
            text "Welcome to your dream vacation!" xalign 0.5 bold True size 25 color "#2c948e" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
            text "" size 25
            text "Before we get started, what shall we" xalign 0.5 bold True size 25 color "#2e1d15" 
            text "call you?" xalign 0.5 bold True size 25 color "#2e1d15"
            text ""  size 25
            xalign 0.5
        button style_prefix "namebox":
            #Only activate input after the user has clicked the button
            if input_on:                                                
                input default name length 8 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" changed change_name color "#323232" bold True xalign 0.5
                action SetScreenVariable("input_on", False)             
                #Pressing enter turns input back off
            else:
                if name == "":
                    text "ENTER YOUR NAME..." bold True xalign 0.5
                else:
                    text name color "#323232" bold True xalign 0.5        
                #Activate input
                action SetScreenVariable("input_on", True)     
            xalign 0.5 
        text "" size 25
        if name == "":
            imagebutton:
                idle "gui/ui_button_hover.png"
                xalign 0.5
                action SetScreenVariable("input_on", False)
            text _("CONFIRM") size 25 xalign 0.5 yoffset -50 outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        else:
            imagebutton:
                idle "gui/ui_button_hover.png"
                selected "gui/ui_button_idle.png"
                selected_idle "gui/ui_button_idle.png"
                selected_hover "gui/ui_button_selected.png"
                hover "gui/ui_button_selected.png"
                xalign 0.5
                action [Hide("button_input"), Return()]
            text _("CONFIRM") size 25 xalign 0.5 yoffset -50 outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
label naming:
    show screen button_input

# The game starts here.
label start:
    $ mc_name = "Bill"
    scene bg warmdark
    show screen button_input
    pause
    python:
        while name == "":
            renpy.jump("naming")
        name = name.strip() or "Bill"
    hide screen button_input
    scene bg loading with dissolve
    pause 2
    scene bg beach0 with Dissolve(1.0)
    $ mc_name = name
    mc "*cough* *cough* *cough*"
    nrr "You wake up on the beach, soaking wet, saltwater stinging the inside of your throat, as if you'd nearly drowned."
    nrr "Water falls from your mouth as you open it to gasp for air."
    nrr "You have no memory of how you got here. In fact, you can only remember your own name, but not where you came from, or a single fact about your life."
    nrr "What you do know is that, despite the outrageous beauty of the landscape around you, you feel incredibly sick to your stomach--"
    nrr "Wow, really went down the wrong pipe, huh? You need a minute, or can I go on?"
    mc "..."
    nrr "Because I can give you a minute. We've got plenty of time. Endles time, really."
    window hide
    scene bg haunting with dissolve
    oc "An eternity, if you catch my drift."
    window hide
    scene bg beach0 with dissolve
    nrr "Woah, not now, Ocean! Sorry, [mc_name]. May I continue?"
    nrr "OK then. As I was--"
    mc "*cough* *cough*"
    nrr "AS I WAS SAYING."
    nrr "You look down at your feet, ankle-deep in the crystal blue water of a newly arrived wave."
    nrr "As the water recedes back into the ocean, it reveals a grotesque discovery!"
    window hide
    scene bg inner_monologue with dissolve
    nrr "A decomposing face stares up at you from beneath the sand. All you can do is vomit--a stream of dark bile, bugs, worms, and other... ick."
    nrr "Questions race through your mind. Where are you? How did you get here? {i}Who is behind this incredibly charming and well-spoken voice in your head?{/i} However, answers don't come easy. Your mind... is completely blank."
    window hide
    scene bg beach0 with dissolve
    menu:
        nrr "What will you do?"
        "Run":
            ""

        "Close your eyes":
            ""

        "Dig up that face!":
            window hide
            scene bg inner_monologue with dissolve
            pause 1
            nrr "You brush the sand away from the half-buried human head-embedded in the ground before you."
            window hide
            pause 1
            nrr "There is no body, just this head. As you pick it up, flakes of skin fall to the ground. The jaw falls open, revealing a gold coin sitting on the rotting tongue of this poor dead soul."
            scene bg haunting with dissolve
            oc "Getting your hands dirty, I see. I like that... You're a take charge type."
            window hide
            pause 1
    window hide
    scene bg beach0 with dissolve
    nrr "You examine the gold coin briefly, happily distracted from what has otherwise been an extremely.... confusing morning."
    nrr "The sun beats down on you, drying your clothes. You check your pockets, but they're empty. Plenty of room for a gold coin, you suppose, and so you deposit it."
    menu:
        nrr "Why that's a nice coin you've got there! What if you were to spend it right now?"
        "\"No, thanks\"":
            ""

        "\"Why not?\"":
            mc "Why not?"
    dw "Well hello, there! I'm Dwight!"
    cl "And I'm Claudette!"
    cl "We'll take that!"
    nrr "Claudette quickly relieves you of your gold coin and tosses it to Dwight, who bites down on it like an old-timey prospector before handing it back to her."
    cl "And this..."
    dw  "...is for you!"
    window hide
    scene bg excitement with dissolve
    nrr "Claudette presents you with a tropical drink."
    nrr "When you take a sip, you find that it's incredible. Money well spent, in your estimation."
    menu:
        nrr "But I gotta ask: Could somebody maybe design the next one of these dating sims to be all-inclusive? It really takes some of the fun out of a fantasy vacation to be watching your wallet the entire time."
        "Thank them for the delicious drink":
            mc "Thanks for the drink. It's quite delicious!"

        "This is suspicious, spit that out!":
            ""
    cl "You're... welcome!"
    dw "Did someone just thank us?"
    cl "Go with it, Dwight. It's normal to be thanked for doing a good job. Trust me on this one."
    nrr "Your mind doesn't have a chance to linger any longer on your current situation, as you feel something soft bump into your foot."
    window hide
    scene bg speedlinebg_red with dissolve
    nrr "When you look down, you find a volleyball sitting in the sand there next to you."
    nrr "You stare down, frozen. A voice calls out from behind you."
    th "Little help, please?"
    window hide
    scene bg beach0 with dissolve
    nrr "You turn around, and when you see what's waiting for you, your jaw just about hits the ground."
    window hide
    scene bg happy with dissolve
    pause 1
    scene bg excitement with dissolve
    pause 1
    scene bg warmlight with dissolve
    pause 1
    scene bg warmdark with dissolve
    pause 1
    scene bg beach0 with dissolve
    pause 1
    window hide
    nrr "Four gorgeous monsters stand halfway between you and a well-tended volleyball court."
    nrr "Each of them oozes with undead energy, a magical aura reaching out and penetrating you. Via your eyes."
    nrr "Your heart begins to race. Curiousity. Fear. Desire. You can't help but stare at these casually dressed... let's call them Killers--I dunno, not to be judgemental but that's just the energy they put out there."
    nrr "So many competing feelings rush through your mind at once you are completely paralyzed."
    th "Hello?"
    nrr "There are weird days, and then there's this. All you can do is look down at the ball and back up at this monstrous line-up of, wll, literal monsters. Sexy ass monsters, though."
    menu:
        nrr "What do you do?"
        "Toss it back":
            nrr "You bend down and grab the ball. It's warm from sitting in the sand on this beautiful day."
            nrr "When you give the ball a toss, it arcs beautifully through the air and lands right in Huntress's hands."
            th "Not bad, stranger."
            nrr "Huntress's muscles ripple as she grips it in her hand. You look her up and down and consider what it might be like to be held tightly in those strong arms. Warm, perhaps. Maybe a little sweaty, but that's OK--it's natural."
            ts "Try hard much? Blech."
        "Kick it back":
            ""
        "Say \"No, thanks!\"":
            ""
        "Say nothing. Do nothing.":
            ""
    nrr "They're speaking directly to you, but you still can't bring yourself to reply. You're entranced."
    nrr "When you snap out of it, you realize that everyone has gone back to the volleyball court."
    nrr "Alone again, you look across the beach at these strange residents who casually bat a volleyball back and forth, happily ignoring your intrusion onto their private beach."
    nrr "Should you be frightened? Worried? Excited? I did refer to them as Killers, not to give too much away."
    nrr "But at the same time, damn, they are looking very appealing in their own way, and nobody so much as lifted a blood-soaked finger in your direction."
    window hide
    scene bg haunting with dissolve
    oc "Don't be scared, [mc_name]. You were made for this."
    nrr "Well jeez. If the spooky Ocean-voice says not to be scared, I'm sure it's all going to work out."
    window hide
    scene bg beach0 with dissolve
    nrr "With no good reason not to, you decide to head over and see what happens next."
    window hide
    scene bg volley0 with dissolve
    nrr "It seems like you've derailed the volleyball game just by showing up."
    tt "You derailed the game just by showing up, nitwit."
    nrr "And I guess you're also a nitwit."
    nrr "Look, it's best to just go with what Trapper says when he says it. That's a policy I hold for pretty much anyone who always seems to have fresh blood on their hands."
    ts "Hey, don't worry about it. It's all just a game. Existence, that is."
    th "Besides, you seem a lot more interesting than a silly game."
    th "What's your deal? What brings you here?"
    tt "You mean they're here to do more than distract from my total domination?"
    tw "*deep sigh*"
    nrr "That was Wraith. That sign means he was done with the game too."
    nrr "Either that or he saw a butterfly or something."
    tt "Look, I don't care why this slack-jawed moron is here."
    tt "I just want to know: can I kill them or not?"
    th "You know you can't."
    th "At least not yet."
    tt "Oh yeah. Not yet."
    nrr "Hey, [mc_name], you might want to, you know, say something."
    nrr "Actually, never mind. There'll be plenty of time for that soon enough."
    nrr "Right now this group has some questions for you."
    nrr "But be warned: answer quickly and answer well."
    nrr "This is a timed quiz. And it will be very important later."
    nrr "Very important."
    nrr "Orrrrrrr not important in any way whatsoever. Probably that one. I can't remember."

    menu:
        tt "How attractive would you say you are?"
        "Very":
            ""
        "Not at all":
            ""
        "Average":
            mc "I'm pretty average, I think."
            ts "Just another face in the crowd, another normal, meaningless life in an endless cycle..."
            th "I think you're quite cute, myself. Like a chipmunk! Or a grizzly bear!"

    menu:
        tw "If you could have any superpower what would it be?"
        "Invisibility":
            mc "Umm... invisibility?"
            tw "Same. Although sometimes I think I already am..."
        "Flight":
            ""
        "Super strength":
            ""

    menu:
        ts "What was your best subject in school?"
        "Math":
            mc "Probably math."
            tw "It's the only thing that makes sense, when you think about it."
        "History":
            ""
        "Skipping Class":
            ""

    menu:
        th "What's your favorite animal?"
        "Dog":
            mc "Dog?"
            th "You'd look absolutely adorable in a little puppy mask!"
        "Cat":
            ""
        "Mustelid":
            ""

    menu:
        tw "What's your favorite color?"
        "Blue":
            ""
        "Blood red":
            ""
        "There-day-old corpse":
            mc "Nobody would expect me to pick this, so I'm gonna say three-day-old corpse. That's a pretty edgy answer, right? I'm pretty dangerous. I talk about corpses. No biggie."
            th "Those are no good to me unless they've been frozen. You'd be surprised by how quick;y good meat can spoil. Or maybe you wouldn't be surprised? I'm still getting to know you."

    menu:
        ts "What's your dream job?"
        "Astronaut":
            ""
        "Nightclub promoter":
            ""
        "Not working at all":
            mc "If we get to do what we really want, why work at all?"
            ts "It takes a lot of courage to break free from society's expectations to climb the ladder."
            tt "Only she could spin laziness into some kind of grand crusade. These damned millenials..."

    menu:
        tt "Best flavor of ice cream?"
        "Vanilla":
            ""
        "Chocolate":
            mc "Chocolate."
            tt "My favorite flavor is Pain."
            th "Same."
            ts "Same here."
            tw "..."
            tw "...Mine is vanilla. Swiriled with Pain."
        "Horseflesh":
            ""
    nrr "I think mint chip is the greatest flavor ever conceived, myself. But enough about ice cream, am I right?"
    nrr "Hold on a second, this reminds me... I am right. Always. It's a lesson you should learn before we go too much further. Do what I say if you want to survive. Pick mint chip."
    window hide
    scene bg haunting with dissolve
    oc "We're teaching lessons now, Narrator? You rascal... Kill or be killed is the rule on this island, even for faceless voices."

    menu:
        nrr "Tell me, what's the best flavor of ice cream?"
        "Vanilla":
            ""
        "Chocolate":
            ""
        "Horseflesh":
            ""
        "Mint Chip":
            mc "The best flavor is... mint chip!"
            oc "So obedient..."
            nrr "I think you're gonna do juuuuust fine."
    window hide
    scene bg beach0 with dissolve
    nrr "Anyhoo, now that they know so much about you, I'm sure the group wants you to start getting to know them."
    tt "I'm Trapper. I pretty much run things around here. I'm the smartest, richest, strongest person on this whole island."
    tt "I don't like losers. If you want to know what a loser is say hello to Wraith."
    tw "Hi, I'm Wraith. I'm nothing like everyone else."
    tw "I like nice people and loathe big dumb idiots."
    ts "Hey what's up? I'm Spirit. I don't like... most things."
    ts "I don't really hate most things either. It's not worth my time. But the things I do hate I really hate, you know?"
    ts "Based on my personal observations, life is nothing but suffering, and society is a carefully calculated lie to keep everyone subserviant to those in power. It's better to choose to just not take part."
    nrr "Jeez, it's like she was downright murdered by society, she hates it so much."
    nrr "Oh, no, wait--I'm remembering Spirit's story now, and that's almost exactly what happened."
    th "Hey! I'm Huntress. Don't let these bummers get you down."
    th "There's lots of fun to be had on this island. Along with lots of love."
    tt "Yeah there is! If you know what I mean!"
    ts "Grow up."
    tt "Grow a body."
    ts "I've explained this a thousand times: I'm dead but I'm not a literal ghost. I just create a trail of fog, I'm not made for it."
    tt "Whatever, fogbody."
    tw "That's not nice."
    th "He's not nice."
    tt "You love it."
    th "Only sometimes."
    tw "Eww, really? That's disgusting."
    tt "That's why she likes it!"
    th "Don't speak for me. I also hate it."
    ts "Stop speaking entirely actually."
    nrr "For the first time ever I agree with Wraith. Let's move on, otherwise they'll do this all day."
    nrr "Besides, if I know this crew--and I do--they'll want to show off soon enough."
    tt "If we're done playing, let's do something else instead."
    ts "Wow, for once I actually agree with this meathead."
    tt "I say we go to my yacht. It's the massive boat docked nearby."
    tt "I'll give everyone a taste of true luxury and power."
    nrr "Wraith rolls his eyes."
    tt "Don't mind him, he just hates fun and happiness."
    tw "No, I hate the endless, desperate, soul-crushing pursuit of wealth, the way it's flaunted needlessly, and the cruelty it engenders."
    tw "What about hanging out by the pool?"
    tw "I find the water calming. Simple. Beautiful."
    th "Hey! What about our volleyball game?"
    th "We can exercise and have some fun as a group!"
    ts "Are you all serious? There's a perfectly good lounge to chill out at right here."
    ts "I'm tired. And besides, I hate being in the sun."
    menu:
        nrr "Where do you want to go?"
        "Vanilla":
            ""
        "Chocolate":
            ""
        "Horseflesh":
            ""
        "Mint Chip":
            ""

            
    nrr "<<<<<<<Ends here>>>>>>>>"
    # This ends the game.
    return
