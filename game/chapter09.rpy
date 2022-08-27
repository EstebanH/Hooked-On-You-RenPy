label chapter09:
    call barnightscene
    call event_bloodconfident
    $ clauddwightObj.change("pose", "pose02")
    $ clauddwightObj.change("emotion", "happy")
    show clauddwight at movecenterleft
    nrr "You arrive at the bar to find Dwight and Claudette both holding cocktail shakers, surrounded by a bevy of bottles for assorted boozes."
    return