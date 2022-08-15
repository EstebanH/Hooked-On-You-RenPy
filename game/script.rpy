
init:
## warmdark ###########################################################
##
    transform rotatebacknforth:
        around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
        rotate 0
        linear 10 rotate 90
        linear 10 rotate -90       
        repeat

    transform rotateleafa:
        easein 2 rotate 10
        easeout 2 rotate 0
        easein 2 rotate -10  
        easeout 2 rotate 0    
        repeat

    transform rotateleafa_reverse:
        easein 2 rotate -10
        easeout 2 rotate 0
        easein 2 rotate 10  
        easeout 2 rotate 0    
        repeat

    transform rotateleafb:
        #transform_anchor (0.5,1.0) anchor (0.5,1.0) rotate_pad True
        easein 2 rotate -5
        easeout 2 rotate 0
        easein 3 rotate 15  
        easeout 2 rotate 0    
        repeat

    transform rotateleafb_reverse:
        #transform_anchor (0.5,1.0) anchor (0.5,1.0) rotate_pad True
        easein 2 rotate 5
        easeout 2 rotate 0
        easein 3 rotate -15  
        easeout 2 rotate 0    
        repeat

    transform wave:
        #transform_anchor (0.5,1.0) anchor (0.5,1.0) rotate_pad True
        easein 2 yoffset -20
        easeout 2 yoffset 0
        easein 3 yoffset 40  
        easeout 2 yoffset 0    
        repeat
        
    transform slowblink:
        linear 20.0 alpha 0.0
        linear 1.0 alpha 0.7
        repeat

    transform rotateslow:
        around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
        rotate 0
        linear 60 rotate 360  
        repeat

    transform slowerblink:
        alpha 0.1
        linear 5.0 alpha 0.4
        linear 10.0 alpha 0.1
        repeat

    transform twinkle:
        linear 1.0 alpha 0.9
        linear 0.5 alpha 1.0
        repeat

    transform fakeload:
        alpha 0.0
        linear 1.0 alpha 1.0
        linear 0.5 alpha 0.9
        repeat

    transform rotatewarmdark:
        easein 4 rotate -5
        easeout 4 rotate 0
        easein 4 rotate 5  
        easeout 4 rotate 0    
        repeat

    image dots = SnowBlossom(At("images/particle_dot.png", slowblink), border=150, count=20, start=0.00000000001, fast=True,  yspeed=(50, -40),  xspeed=(-25,25), horizontal=True)
    image polygon = SnowBlossom(At("images/polygon.png", rotateslow, slowerblink), border=-500, count=2, start=0.00000000001, fast=True,  yspeed=(10, -10),  xspeed=(-15,15), horizontal=True)
    image leaf1:
        rotate 180
        im.Flip("images/leaf1.png", horizontal="True", vertical="True")
        zoom 1.3
        yalign 2.2
        xalign 1.075
    image leaf2:
        rotate 90
        im.Flip("images/leaf2.png", vertical="True")
        zoom 1.3
        yoffset -200
        xalign 1.15
    image leaf3:
        rotate 0
        im.Flip("images/leaf3.png", horizontal="True", vertical="True")
        zoom 1
        yoffset 225
        xoffset -150
    image leaf4:
        rotate 180
        im.Flip("images/leaf4.png", horizontal="True", vertical="True")
        zoom 1.3
        yoffset 725
        xoffset 275
    image leaf5:
        rotate -30
        im.Flip("images/leaf5.png", horizontal="True")
        zoom 1.55
        yoffset 490
        xoffset -25
    image leaf6:
        rotate 270
        im.Flip("images/leaf1.png", horizontal="False", vertical="False")
        zoom 1.3
        yalign 2.2
    image leaf7:
        rotate 270
        im.Flip("images/leaf2.png", horizontal="True", vertical="True")
        zoom 1.3
        yoffset -200
        xoffset -150
    image leaf8:
        im.Flip("images/leaf3.png", horizontal="True")
        zoom 1.5
        yoffset 325
        xoffset 1475
    image leaf9:
        im.Flip("images/leaf4.png", horizontal="True")
        zoom 1.3
        yoffset 825
        xoffset 1125
    image leaf10:
        rotate 70
        im.Flip("images/leaf5.png", vertical="True")
        zoom 1.55
        yoffset 490
        xoffset 1350

    image bg warmdark:
        "images/bg/bg_warmdark.png"
        zoom 1.1
    image warmdark_effect1:
        xalign 0.5 
        yalign 0.5 
        "images/bg/bg_warmdark_effect1.png"
        zoom 1.1
    image warmdark_effect2:
        xalign 0.5 
        yalign 0.5 
        "images/bg/bg_warmdark_effect2.png"
        zoom 1.1
##
## warmdark end #################################################################
## haunting ###############################################################
##
    image bg haunting:
        "images/bg/bg_haunting.png"
    image ocean1:
        "images/sprites/ocean/ocean1.png"
    image ocean2:
        "images/sprites/ocean/ocean2.png"
    image ocean3:
        "images/sprites/ocean/ocean3.png"
    image ocean4:
        "images/sprites/ocean/ocean4.png"

    image cloudy1:
        im.MatrixColor("images/cloudlayer1.png", im.matrix.tint(0.45, 0.45, 0.75))
        yalign 0.5
        xalign 0.5

    image cloudy2:
        im.MatrixColor("images/cloudlayer2.png", im.matrix.tint(0.45, 0.45, 0.75))
        yalign 0.5
        xalign 0.5
        
    transform cloudanimx:
        easein 32 xzoom 1.5
        easeout 8 xzoom 1.3
        repeat
        
    transform cloudanimy:
        easein 16 yzoom 1.1
        easeout 8 yzoom 1.3 
        repeat
        
    transform cloudxoffset:
        easein 16 xoffset -100
        easein 16 xoffset -100
        easeout 32 xoffset 100
        repeat
        
    transform cloudyoffset:
        easein 16 xoffset -50
        easein 16 xoffset -50
        easeout 16 xoffset 50
        repeat
        
    transform cloudxoffset2:
        easein 16 xoffset -50
        easein 16 xoffset -50
        easeout 16 xoffset 50
        repeat
        
    transform cloudyoffset2:
        easeout 8 yoffset 0
        repeat

    transform ocean1place:
        xalign 1.0
        yalign 1.0
        yoffset 1070
        xoffset 700
        zoom 1.75
    transform ocean2place:
        xalign 0.7
        yalign 1.0
        yoffset 950
        xoffset 125
        zoom 1.75
    transform ocean3place:
        xalign .0 
        yalign 1.0
        yoffset 925
        xoffset -450
        zoom 1.5
    transform ocean4place:
        xalign 1.0 
        yalign 1.0
        yoffset 1100
        xoffset 420
        zoom 1.5
    transform ocean1rotate:
        #anchor (0.5, 0.5) transform_anchor 1
        easein 3 rotate -5
        easeout 4 rotate 0
        easein 6 rotate 5  
        easeout 4 rotate 0    
        repeat
    transform ocean2rotate:
        #anchor (0.5, 0.5) transform_anchor 1
        easein 4 rotate 5
        easeout 5 rotate 0
        easein 4 rotate -5  
        easeout 3 rotate 0    
        repeat
    transform ocean3rotate:
        #anchor (0.5, 0.5) transform_anchor 1
        easein 6 rotate -5
        easeout 4 rotate 0
        easein 3 rotate 5  
        easeout 4 rotate 0    
        repeat
    transform ocean4rotate:
        #anchor (1, 1) transform_anchor 1
        easein 4 rotate -5
        easeout 3 rotate 0
        easein 4 rotate 5  
        easeout 3 rotate 0    
        repeat
    transform ocean1offset:
        #anchor (0.5, 0.5) transform_anchor 1
        easein 3 xoffset -50
        easeout 4 xoffset 0
        easein 6 xoffset 50
        easeout 4 xoffset 0    
        repeat
    transform ocean2offset:
        #anchor (0.5, 0.5) transform_anchor 1
        easein 6 xoffset -50
        easeout 5 xoffset 0
        easein 4 xoffset 50  
        easeout 3 xoffset 0    
        repeat
    transform ocean3offset:
        #anchor (0.5, 0.5) transform_anchor 1
        easein 6 xoffset -50
        easeout 4 xoffset 0
        easein 3 xoffset 50  
        easeout 4 xoffset 0    
        repeat
    transform ocean4offset:
        #anchor (1, 1) transform_anchor 1
        easein 4 xoffset -50
        easeout 3 xoffset 0
        easein 4 xoffset 50  
        easeout 3 xoffset 0    
        repeat
##
## haunting ###############################################################
## excitement ###############################################################
##
    transform dots:
        #anchor (0.5, 0.5) transform_anchor 1
        easein 16 rotate -90
        easeout 8 rotate 0
        easein 16 rotate 90  
        easeout 8 rotate 0    
        repeat
    transform beam1:
        #anchor (0.5, 0.5) transform_anchor 1
        easein 8 rotate 90
        easeout 4 rotate 0
        easein 8 rotate -90  
        easeout 4 rotate 0    
        repeat
    transform beam2:
        #anchor (0.5, 0.5) transform_anchor 1
        easein 8 rotate 180
        easeout 4 rotate 0
        easein 8 rotate -180 
        easeout 4 rotate 0    
        repeat
    image excite_dots:
        "images/dots1.png"
        zoom 3
        xalign 0.5
        yalign 0.5
    image excite_beam1:
        "images/excitement4.png"
        zoom 1.1
        xalign 0.5
        yalign 0.5
    image excite_beam2:
        "images/excitement5.png"
        zoom 1.1
        xalign 0.5
        yalign 0.5
    image dots2 = SnowBlossom(At("images/particle_dot.png", slowblink), border=150, count=40, start=0.00000000001, fast=True,  yspeed=(50, -40),  xspeed=(-25,25), horizontal=True)
    image glow:
        zoom 1.5
        "images/glow.png"
        xalign 0.5 
        yalign 0.5
##
## excitement ###############################################################
## inner monologue ###############################################################
##
    transform dissolvecenter:
        yalign 1.0
        xalign 0.5
        easein 2 yalign 0.25
    transform nodissolvecenter:
        yalign 0.25
        xalign 0.5
    image head_coin:
        "images/head_coin.png" 
        xalign 0.5 
        yalign 0.25
    image dreadnoise:
        contains:
            parallel:
                "images/sprites/effects/dreadfear_noise.png"
                xpan 5400
                ypan 5400
                linear 8 xpan 1 ypan 1
                repeat
##
## inner monologue ###############################################################
## speedlines ###############################################################
##
    image speedlines = Movie(play="images/sprites/video/speedlines.webm", mask="images/sprites/video/speedlines_mask.webm")

    transform coin_yoffset:
        yoffset 50

## speedlines ###############################################################
    transform volleycenter:
        yalign 0.5
        xalign 0.5
        easein 3 yalign 0.25
## other ###############################################################
##
    image flower:
        "gui/window_icon.png"
        yalign 0.925
        xalign 0.9575

    image bg loading:
        "images/bg/bg_loading.png"
    image bg beach0:
        "images/bg/bg_beach_0.png"
    image bg volley0:
        "images/bg/bg_volley_0.png"

    image bg inner_monologue:
        "images/bg/bg_inner_monologue.png"

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
    transform clauddwightfar:
        xalign 0.5
        yalign 0.25
    transform smaller:
        zoom 0.1
    
## clauddwight ###############################################################
##

init python:
    class ClauddwightClass:
        def __init__(self):
            self.pose = "close01"
            self.emotion = "idle"
            self.emote = "none"
            self.whoIsDead = ""
            self.resetFilenames()
            ##self.clothingFilename = "images/sprites/clauddwight/clauddwight_" + self.pose + ".png"
        def resetFilenames(self):
            self.poseFilename = "images/sprites/clauddwight/clauddwight_" + self.pose + self.whoIsDead + ".png"
            if self.whoIsDead != "":
                self.emotionFilename = "images/sprites/clauddwight/clauddwight_" + self.pose + "_" + self.emotion + "_00_" + self.whoIsDead + ".png"
                self.blinkFilename = "images/sprites/clauddwight/clauddwight_" + self.pose + "_" + self.emotion + "_01_" + self.whoIsDead + ".png"
            else:
                self.emotionFilename = "images/sprites/clauddwight/clauddwight_" + self.pose + "_" + self.emotion + "_00.png"
                self.blinkFilename = "images/sprites/clauddwight/clauddwight_" + self.pose + "_" + self.emotion + "_01.png"
            if self.emotion == "dead":
                self.emotionFilename = "images/sprites/clauddwight/clauddwight_" + self.pose + "_dead_00" + self.whoIsDead + ".png"
                self.blinkFilename = "images/sprites/clauddwight/clauddwight_" + self.pose + "_dead_00" + self.whoIsDead + ".png"



        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "whoIsDead":
                self.whoIsDead = value
            elif attribute == "emote":
                self.emote = value
            self.resetFilenames()

    def play_effect(trans, st, at):
            renpy.play("sounds/sfx_emotes_hearts_v01.ogg", channel="sound")

layeredimage clauddwight:
    always:
        "[clauddwightObj.poseFilename]"
    always:
        "clauddwight_blink"
        
    if clauddwightObj.emote == "heart" and clauddwightObj.pose == "far01":
        "heartboom_dwight_far01"
    if clauddwightObj.emote == "heart" and clauddwightObj.pose == "far02":
        "heartboom_dwight_far02"
    if clauddwightObj.emote == "heart" and (clauddwightObj.pose == "far01" or clauddwightObj.pose == "far02"):
        "heartboom_claud_far"

        
    if clauddwightObj.emote == "heart" and clauddwightObj.pose == "close01":
        "heartboom_dwight_close01"
    if clauddwightObj.emote == "heart" and clauddwightObj.pose == "close02":
        "heartboom_dwight_close02"
    if clauddwightObj.emote == "heart" and (clauddwightObj.pose == "close01" or clauddwightObj.pose == "close02"):
        "heartboom_claud_close"

image clauddwight_blink:
    "[clauddwightObj.emotionFilename]"
    choice:
        pause 3
    choice:
        pause 4
    choice:
        pause 5
    "[clauddwightObj.blinkFilename]"
    pause 0.1
    repeat

image heartboom_far:
    function play_effect
    zoom 0.15
    (ParticleBurst("images/sprites/effects/heart.png", explodeTime=0, numParticles=10, particleTime=20.0, particleXSpeed = 20, particleYSpeed = 15, centerZone = 1000, fadeWithParticleTime = True).sm) with Dissolve

image heartboom_close:
    function play_effect
    zoom 0.25
    (ParticleBurst("images/sprites/effects/heart.png", explodeTime=0, numParticles=10, particleTime=20.0, particleXSpeed = 20, particleYSpeed = 15, centerZone = 1000, fadeWithParticleTime = True).sm) with Dissolve

image heartboom_claud_far:
    xalign 0.45
    yalign 0.15
    "heartboom_far"
    pause 1
    easeout 0.5 alpha 0.0

image heartboom_dwight_far01:
    xalign 0.65
    yalign 0.05
    "heartboom_far"
    pause 1
    easeout 0.5 alpha 0.0

image heartboom_dwight_far02:
    xalign 0.675
    yalign 0.1
    "heartboom_far"
    pause 1
    easeout 0.5 alpha 0.0

image heartboom_claud_close:
    xalign 0.4
    yalign 0.25
    "heartboom_close"
    pause 1
    easeout 0.5 alpha 0.0

image heartboom_dwight_close01:
    xalign 0.75
    yalign 0.1
    "heartboom_close"
    pause 1
    easeout 0.5 alpha 0.0


image heartboom_dwight_close02:
    xalign 0.85
    yalign 0.1
    "heartboom_close"
    pause 1
    easeout 0.5 alpha 0.0
##
## clauddwight ###############################################################
##image heartboom = ParticleBurst([Solid("#%06x"%renpy.random.randint(0, 0xFFFFFF), xysize=(5, 5)) for i in xrange(50)], mouse_sparkle_mode=True)
#image heartboom = (ParticleBurst("images/sprites/effects/heart.png", explodeTime=0, numParticles=10, particleTime=4.0, particleXSpeed = 10, particleYSpeed = 10).sm)


init python:
    import math
    import random
    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.sound.play("sounds/sfx_tap.ogg",channel="sound")
    def callbackchoice(ctc, **kwargs):
        if ctc == "end":
            renpy.sound.play("sounds/sfx_ui_choice_appear.ogg",channel="sound")
    renpy.music.register_channel("hauntloop", "music", loop=True)
    renpy.music.register_channel("choiceloop", "music", loop=True)
    renpy.music.register_channel("moodloop", "music", loop=True)
    renpy.music.register_channel("eventloop", "music", loop=True)
    class ParticleBurst(object):
        def __init__(self, theDisplayable, explodeTime=0, numParticles=20, particleTime = 0.500, particleXSpeed = 5, particleYSpeed = 5, centerZone = 10, fadeWithParticleTime = False):
            self.sm = SpriteManager(update=self.update)
            # A list of (sprite, starting-x, speed).
            self.stars = [ ]
            self.displayable = theDisplayable
            self.centerZone = centerZone
            self.explodeTime = explodeTime
            self.particleMax = numParticles
            self.particleTime = particleTime
            self.particleXSpeed = particleXSpeed
            self.particleYSpeed = particleYSpeed
            self.fadeWithParticleTime = fadeWithParticleTime ##Unused
            self.timePassed = 0
           
        def add(self, d, speed, st):
            s = self.sm.create(d)
            s.x = self.sm.width/2 - (random.random()*self.centerZone)
            s.y = self.sm.height/2 - (random.random()*self.centerZone)
            ySpeed = ((random.random() - 0.5) * self.particleYSpeed)
            xSpeed = ((random.random() - 0.5) * self.particleXSpeed)
            pTime = (random.random() * self.particleTime ) + st
            self.stars.append((s, ySpeed, xSpeed, pTime))
            
        def update(self, st):
            sindex=0
            for s, ySpeed, xSpeed, particleTime in self.stars:
                if (st < particleTime):
                    s.x += xSpeed
                    s.y += ySpeed
                    #if (self.fadeWithParticleTime):
                        #trans.alpha = abs(st/self.particleTime)
                else:
                    s.destroy()
                    self.stars.pop(sindex)
                sindex += 1
            if len(self.stars) < self.particleMax:
                if st < self.explodeTime or self.explodeTime == 0:
                    self.add(self.displayable, 2, st)
            return 0    

##https://youtu.be/DPFXHoIBmAo
# Declare the characters.
define nrr = Character(None, window_style="window_narrator", color="#3a2e55",callback=callbackcontinue)
define cho = Character(None, window_style="window_narrator", color="#3a2e55",  callback=callbackchoice)
define look = Character(None, window_style="window_look", color="#3a2e55",  callback=callbackchoice)

define oc = Character("", window_style="window_ocean", namebox_style="namebox_ocean", color="#3a2e55", callback=callbackcontinue)
define mc = DynamicCharacter('mc_name', color="#3a2e55", callback=callbackcontinue)

define dw = Character("DWIGHT", color="#bb7d31", callback=callbackcontinue)

define cl = Character("CLAUDETTE", color="#b4992e",  callback=callbackcontinue)
define th = Character("THE HUNTRESS", window_style="window_killer", color="#c64631", callback=callbackcontinue)
define ts = Character("THE SPIRIT", window_style="window_killer", color="#d94464", callback=callbackcontinue)
define tt = Character("THE TRAPPER", window_style="window_killer", color="#335480", callback=callbackcontinue)
define tw = Character("THE WRAITH", window_style="window_killer", color="#58902c", callback=callbackcontinue)
## Character Example
#p = Character('Protagonist', what_prefix="\"", what_suffix="\"", what_size=26, who_outlines=[(4, "#004035", -5, 3),(2, "#0a9e9a", -5, 3), (3, "#252118", absolute(-2), absolute(0)), (absolute(1), "#FFF", absolute(0), absolute(0))],what_outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ], show_two_window=True, color="#000000", ctc = anim.Blink("ctc.png", xpos=600, ypos=450), ctc_position= "fixed", callback=callbackcontinue)

label warmdarkscene:
    window hide
    scene bg warmdark
    show dots
    show polygon
    show leaf1 at rotateleafa
    show leaf2 at rotateleafa
    show leaf3 at rotateleafb, wave
    show leaf4 at rotateleafa
    show leaf5 at rotateleafa
    show leaf6 at rotateleafa_reverse
    show leaf7 at rotateleafa_reverse
    show leaf8 at rotateleafb_reverse, wave
    show leaf9 at rotateleafa_reverse
    show leaf10 at rotateleafa_reverse
    show warmdark_effect1 at rotatewarmdark
    show warmdark_effect2 at twinkle
    with dissolve
    return

label loadingscene:
    window hide
    scene bg loading with dissolve
    show flower at fakeload
    pause 1
    return

label beach0scene(keep_images=False):
    window hide
    $ renpy.music.set_volume(1,3.0,"music")
    play music "audio/sfx_ambience_beach.ogg"
    if keep_images:
        call hideeffects
        show bg beach0 with dissolve
    else:
        scene bg beach0 with dissolve
    return
label hideeffects:
    hide cloudy1
    hide cloudy2
    hide ocean1
    hide ocean2
    hide ocean3
    hide ocean4
    hide dreadnoise
    return

label oceanhaunting(image_name=Null, ismoveinbottom = False):
    window hide
    call hideeffects
    $ renpy.music.set_volume(0.25,3.0,"music")
    show bg haunting
    play hauntloop("audio/m_Mood_Haunting_Loop_V1.ogg") fadein 3.0 loop
    show cloudy1 at cloudanimx, cloudanimy,cloudxoffset,cloudyoffset
    show cloudy2 at cloudanimx, cloudanimy,cloudxoffset2,cloudyoffset2
    show ocean1 at ocean1place, ocean1rotate, ocean1offset
    show ocean2 at ocean2place, ocean2rotate, ocean2offset
    show ocean3 at ocean3place, ocean3rotate, ocean3offset
    show ocean4 at ocean4place, ocean4rotate, ocean4offset 
    if image_name is not Null:
        if ismoveinbottom:
            show expression image_name at dissolvecenter,coin_yoffset
        else:
            show expression image_name at nodissolvecenter

    with dissolve
    return

label speedlinesredscene(image_name=Null, ismoveinbottom = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_SpeedLine_Loop-003.ogg") fadein 3.0 loop
    scene bg speedlinebg_red with dissolve
    if image_name is not Null:
        if ismoveinbottom:
            show expression image_name at volleycenter,coin_yoffset zorder 1
        else:
            show expression image_name at nodissolvecenter,coin_yoffset zorder 1
    with dissolve
    return

label mood_speedlines(image_name=Null, ismoveinbottom = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_SpeedLine_Loop-001.ogg") fadein 3.0 loop
    show speedlines
    if image_name is not Null:
        if ismoveinbottom:
            show expression image_name at dissolvecenter,coin_yoffset zorder 1
        else:
            show expression image_name at nodissolvecenter,coin_yoffset zorder 1
    with dissolve
    return

label mood_inner_monologuescene(image_name=Null, ismoveinbottom = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_InnerMonologue_Loop_V1.ogg") fadein 3.0 loop
    scene bg inner_monologue
    show dreadnoise
    if image_name is not Null:
        if ismoveinbottom:
            show expression image_name at dissolvecenter zorder 1
        else:
            show expression image_name at nodissolvecenter zorder 1
    with dissolve
    return


label mood_excitement(image_name=Null, ismoveinbottom = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_Excitement_Loop_V1.ogg") fadein 3.0 loop
    scene bg excitement
    show dots2
    show excite_beam2 at beam2
    show excite_beam1 at beam1
    show excite_dots at dots
    show glow
    if image_name is not Null:
        if ismoveinbottom:
            show expression image_name at dissolvecenter zorder 1
        else:
            show expression image_name at nodissolvecenter zorder 1
    with dissolve
    return

label mood_warmdark(image_name=Null, ismoveinbottom = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_WarmDark_Loop_V1.ogg") fadein 3.0 loop
    scene bg warmdark
    show dots
    show polygon
    show leaf1 at rotateleafa
    show leaf2 at rotateleafa
    show leaf3 at rotateleafb, wave
    show leaf4 at rotateleafa
    show leaf5 at rotateleafa
    show leaf6 at rotateleafa_reverse
    show leaf7 at rotateleafa_reverse
    show leaf8 at rotateleafb_reverse, wave
    show leaf9 at rotateleafa_reverse
    show leaf10 at rotateleafa_reverse
    show warmdark_effect1 at rotatewarmdark
    show warmdark_effect2 at twinkle
    if image_name is not Null:
        if ismoveinbottom:
            show expression image_name at dissolvecenter zorder 1
        else:
            show expression image_name at nodissolvecenter zorder 1
    with dissolve
    return

label mood_warmlight(image_name=Null, ismoveinbottom = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_WarmLight_Loop_V1.ogg") fadein 3.0 loop
    scene bg warmlight
    show dots2
    show excite_dots at dots
    if image_name is not Null:
        if ismoveinbottom:
            show expression image_name at dissolvecenter zorder 1
        else:
            show expression image_name at nodissolvecenter zorder 1
    with dissolve
    return

label mood_happy(image_name=Null, ismoveinbottom = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_Happy_Loop_V1.ogg") fadein 3.0 loop
    scene bg happy
    show dots2
    show excite_dots at dots
    if image_name is not Null:
        if ismoveinbottom:
            show expression image_name at dissolvecenter zorder 1
        else:
            show expression image_name at nodissolvecenter zorder 1
    with dissolve
    return


label event_choices:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play choiceloop("audio/sfx_time_to_kill.ogg") fadein 3.0 loop
    return

label event_clauddwight:
    $ renpy.music.set_volume(0.25,3.0,"music")
    play eventloop("audio/sfx_banana_hammak.ogg") fadein 3.0 loop
    return

# The game starts here.
label start:
    #image snow = SnowBlossom("particle_dot.png", count=100)
    $ mc_name = "PlayerName"
    $ save_name = mc_name
    $ quick_menu = False
    $ clauddwightObj = ClauddwightClass()

    call warmdarkscene

    while user_input == "":
        call screen name_input
    python:
        user_input = user_input.strip() or "Bill"
        mc_name = user_input
        save_name = user_input

    call loadingscene
    pause 1
    call beach0scene

    $ quick_menu = True

    mc "*cough* *cough* *cough*"
    nrr "You wake up on the beach, soaking wet, saltwater stinging the inside of your throat, as if you'd nearly drowned."
    nrr "Water falls from your mouth as you open it to gasp for air."
    nrr "You have no memory of how you got here. In fact, you can only remember your own name, but not where you came from, or a single fact about your life."
    nrr "What you do know is that, despite the outrageous beauty of the landscape around you, you feel incredibly sick to your stomach--"
    nrr "Wow, really went down the wrong pipe, huh? You need a minute, or can I go on?"
    mc "..."
    nrr "Because I can give you a minute. We've got plenty of time. Endless time, really."
    call oceanhaunting
    oc "An eternity, if you catch my drift."
    stop hauntloop fadeout 3.0
    nrr "Woah, not now, Ocean! Sorry, [mc_name]. May I continue?"
    call beach0scene

    nrr "OK then. As I was--"
    mc "*cough* *cough*"
    nrr "AS I WAS SAYING."
    nrr "You look down at your feet, ankle-deep in the crystal blue water of a newly arrived wave."
    nrr "As the water recedes back into the ocean, it reveals a grotesque discovery!"

    call mood_inner_monologuescene("images/head_idle.png", True)

    nrr "A decomposing face stares up at you from beneath the sand. All you can do is vomit--a stream of dark bile, bugs, worms, and other... ick."
    nrr "Questions race through your mind. Where are you? How did you get here? {i}Who is behind this incredibly charming and well-spoken voice in your head?{/i} However, answers don't come easy. Your mind... is completely blank."
    stop moodloop fadeout 3.0
    window hide
    scene bg beach0 with dissolve

    call event_choices
    menu:
        cho "What will you do?"
        "Run":
            ""

        "Close your eyes":
            ""

        "Dig up that face!":
            window hide
            call mood_inner_monologuescene("images/head_idle.png")
            pause 1
            nrr "You brush the sand away from the half-buried human head-embedded in the ground before you."
            window hide
            call mood_inner_monologuescene("images/head_coin.png")
            pause 1
            nrr "There is no body, just this head. As you pick it up, flakes of skin fall to the ground. The jaw falls open, revealing a gold coin sitting on the rotting tongue of this poor dead soul."
            stop choiceloop fadeout 3.0
    stop choiceloop fadeout 3.0
    
    call oceanhaunting
    oc "Getting your hands dirty, I see. I like that... You're a take charge type."
    stop hauntloop fadeout 3.0
    window hide
    call oceanhaunting("images/coin.png", True)
    pause 1
    stop hauntloop fadeout 3.0

    call beach0scene(True)
    call mood_speedlines("images/coin.png")

    nrr "You examine the gold coin briefly, happily distracted from what has otherwise been an extremely.... confusing morning."
    nrr "The sun beats down on you, drying your clothes. You check your pockets, but they're empty. Plenty of room for a gold coin, you suppose, and so you deposit it."
    hide speedlines
    stop moodloop fadeout 3.0
    call beach0scene

    call event_choices
    menu:
        cho "Why that's a nice coin you've got there! What if you were to spend it right now?"
        "\"No, thanks\"":
            ""

        "\"Why not?\"":
            mc "Why not?"
    stop choiceloop fadeout 3.0

    call event_clauddwight
    show clauddwight
    $ clauddwightObj.change("pose", "close02")
    $ clauddwightObj.change("emotion", "happy")
    dw "Well hello, there! I'm Dwight!"
    cl "And I'm Claudette!"
    $ clauddwightObj.change("pose", "close01")
    play sound "sounds/sfx_signature_clauddwight01.ogg"
    cl "We'll take that!"
    $ clauddwightObj.change("emotion", "idle")
    nrr "Claudette quickly relieves you of your gold coin and tosses it to Dwight, who bites down on it like an old-timey prospector before handing it back to her."
    cl "And this..."
    dw  "...is for you!"
    window hide
    #scene bg excitement with dissolve
    stop eventloop fadeout 3.0

    call mood_excitement("images/skull.png", True)
    pause 1
    nrr "Claudette presents you with a tropical drink."
    nrr "When you take a sip, you find that it's incredible. Money well spent, in your estimation."
    stop moodloop fadeout 3.0
    call beach0scene
    call event_clauddwight
    menu:
        cho "But I gotta ask: Could somebody maybe design the next one of these dating sims to be all-inclusive? It really takes some of the fun out of a fantasy vacation to be watching your wallet the entire time."
        "Thank them for the delicious drink":
            mc "Thanks for the drink. It's quite delicious!"

        "This is suspicious, spit that out!":
            ""
    $ clauddwightObj.change("emotion", "happy")
    $ clauddwightObj.change("emote", "heart")
    $ clauddwightObj.change("pose", "far01")
    show clauddwight with Dissolve(0.2)
    pause 1
    cl "You're... welcome!"
    $ clauddwightObj.change("emote", "none")
    $ clauddwightObj.change("emotion", "sad")
    dw "Did someone just thank us?"
    cl "Go with it, Dwight. It's normal to be thanked for doing a good job. Trust me on this one."
    hide clauddwight with dissolve
    stop eventloop fadeout 3.0
    $ renpy.music.set_volume(1,3.0,"music")

    nrr "Your mind doesn't have a chance to linger any longer on your current situation, as you feel something soft bump into your foot."
    window hide
    call speedlinesredscene("images/volleyball.png", True)
    pause 3
    nrr "When you look down, you find a volleyball sitting in the sand there next to you."
    nrr "You stare down, frozen. A voice calls out from behind you."
    th "Little help, please?"
    window hide
    stop moodloop fadeout 3.0
    call beach0scene
    nrr "You turn around, and when you see what's waiting for you, your jaw just about hits the ground."
    window hide
    call mood_happy
    show huntress
    look "{w=5.0}"
    call mood_excitement
    show wraith
    look "{w=5.0}"
    call mood_warmlight
    show spirit
    look "{w=5.0}" 
    call mood_warmdark
    show trapper
    look "{w=5.0}"
    stop moodloop fadeout 3.0
    scene bg beach0 with dissolve
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
