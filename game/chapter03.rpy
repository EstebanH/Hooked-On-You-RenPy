label chapter3:
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
    nb "But we still gotta get started on storytime so..."
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
            mc ""
        "gui/button_wraith_idle.png¦gui/button_wraith_hover.png¦gui/button_wraith_select.png":
            mc ""
        "gui/button_trapper_idle.png¦gui/button_trapper_hover.png¦gui/button_trapper_select.png":
            mc ""
        "gui/button_huntress_idle.png¦gui/button_huntress_hover.png¦gui/button_huntress_select.png":
            mc ""
    $ diamondchoice = False



    
    call blackscene
    return