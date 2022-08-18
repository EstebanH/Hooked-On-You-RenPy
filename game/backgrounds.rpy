
init:    
    transform dissolvecenter:
        yalign 1.0
        xalign 0.5
        easein 2 yalign 0.25
    transform nodissolvecenter:
        yalign 0.25
        xalign 0.5

## haunting ###############################################################
##
init:
    image bg haunting:
        "images/bg/moods/bg_haunting.png"
    image ocean1:
        "images/sprites/ocean/ocean1.png"
    image ocean2:
        "images/sprites/ocean/ocean2.png"
    image ocean3:
        "images/sprites/ocean/ocean3.png"
    image ocean4:
        "images/sprites/ocean/ocean4.png"

    image cloudy1:
        im.MatrixColor("images/moods/cloudlayer1.png", im.matrix.tint(0.45, 0.45, 0.75))
        yalign 0.5
        xalign 0.5

    image cloudy2:
        im.MatrixColor("images/moods/cloudlayer2.png", im.matrix.tint(0.45, 0.45, 0.75))
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



label oceanhaunting(image_name=Null, ismovefrombottom = False):
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
        if ismovefrombottom:
            show expression image_name at dissolvecenter,coin_yoffset
        else:
            show expression image_name at nodissolvecenter
    
    with dissolve
    return

##
## haunting ###############################################################

## inner monologue ###############################################################
##
init:
    image head_coin:
        "images/head_coin.png" 
        xalign 0.5 
        yalign 0.25
    image dreadnoise:
        alpha 0.5
        contains:
            parallel:
                "images/moods/dreadfear_noise.png"
                xpan 3400
                ypan 3400
                linear 8 xpan 1 ypan 1
                repeat
##
## inner monologue ###############################################################
## speedlines ###############################################################
##
init:
    image speedlines = Movie(play="images/sprites/moods/speedlines.webm", mask="images/sprites/moods/speedlines_mask.webm")

    transform coin_yoffset:
        yoffset 50
    
    transform volleycenter:
        yalign 0.5
        xalign 0.5
        easein 3 yalign 0.25
##
## speedlines ###############################################################

## warmdark ###########################################################
##
init:
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

    image dots = SnowBlossom(At("images/moods/particle_dot.png", slowblink), border=150, count=20, start=0.00000000001, fast=True,  yspeed=(50, -40),  xspeed=(-25,25), horizontal=True)
    image polygon = SnowBlossom(At("images/moods/polygon.png", rotateslow, slowerblink), border=-500, count=2, start=0.00000000001, fast=True,  yspeed=(10, -10),  xspeed=(-15,15), horizontal=True)
    image leaf1:
        rotate 180
        im.Flip("images/moods/leaf1.png", horizontal="True", vertical="True")
        zoom 1.3
        yalign 2.2
        xalign 1.075
    image leaf2:
        rotate 90
        im.Flip("images/moods/leaf2.png", vertical="True")
        zoom 1.3
        yoffset -200
        xalign 1.15
    image leaf3:
        rotate 180
        im.Flip("images/moods/leaf3.png", horizontal="True", vertical="True")
        zoom 1.5
        yoffset 225
        xoffset -150
    image leaf4:
        rotate 180
        im.Flip("images/moods/leaf4.png", horizontal="True", vertical="True")
        zoom 1.3
        yoffset 725
        xoffset 275
    image leaf5:
        rotate -30
        im.Flip("images/moods/leaf5.png", horizontal="True")
        zoom 1.55
        yoffset 490
        xoffset -25
    image leaf6:
        rotate 270
        im.Flip("images/moods/leaf1.png", horizontal="False", vertical="False")
        zoom 1.3
        yalign 2.2
    image leaf7:
        rotate 270
        im.Flip("images/moods/leaf2.png", horizontal="True", vertical="True")
        zoom 1.3
        yoffset -200
        xoffset -150
    image leaf8:
        im.Flip("images/moods/leaf3.png", horizontal="True")
        zoom 1.5
        yoffset 325
        xoffset 1475
    image leaf9:
        im.Flip("images/moods/leaf4.png", horizontal="True")
        zoom 1.3
        yoffset 825
        xoffset 1125
    image leaf10:
        rotate 70
        im.Flip("images/moods/leaf5.png", vertical="True")
        zoom 1.55
        yoffset 490
        xoffset 1350

    image bg warmdark:
        "images/bg/moods/bg_warmdark.png"
        zoom 1.1
    image warmdark_effect1:
        xalign 0.5 
        yalign 0.5 
        "images/moods/bg_warmdark_effect1.png"
        zoom 1.1
    image warmdark_effect2:
        xalign 0.5 
        yalign 0.5 
        "images/moods/bg_warmdark_effect2.png"
        zoom 1.1

label mood_warmdark(image_name=Null, ismovefrombottom = False, scenedissolve = True):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_WarmDark_Loop_V1.ogg") fadein 3.0 loop
    scene bg warmdark
    show excite_dots
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
        if ismovefrombottom:
            show expression image_name at dissolvecenter zorder 1
        else:
            show expression image_name at nodissolvecenter zorder 1
    if scenedissolve:
        with dissolve
    return

##
## warmdark end #################################################################

## warmlight ###############################################################
##
init:
    image bg warmlight:
        "images/bg/moods/bg_warmlight.png"

    image wlflower1:
        "images/moods/wl_flower_1.png"
        xalign 0.15
        yalign 0.925
        zoom .7
    image wlflower2:
        "images/moods/wl_flower_2.png"
        xalign 0.175
        yalign 0.525
        zoom .7
    image wlflower3:
        "images/moods/wl_flower_3.png"
        xalign 0.15
        yalign 0.35
        zoom .7
    image wlflower4:
        "images/moods/wl_flower_4.png"
        xalign 0.1125
        yalign 0.675
        zoom .7

    image wlflower5:
        "images/moods/wl_flower_1.png"
        xalign 1.035-0.15
        yalign 0.925
        yzoom .7
        xzoom -.7
    image wlflower6:
        "images/moods/wl_flower_2.png"
        xalign 1.035-0.175
        yalign 0.525
        yzoom .7
        xzoom -.7
    image wlflower7:
        "images/moods/wl_flower_3.png"
        xalign 1.035-0.15
        yalign 0.35
        yzoom .7
        xzoom -.7
    image wlflower8:
        "images/moods/wl_flower_4.png"
        xalign 1.035-0.1125
        yalign 0.675
        yzoom .7
        xzoom -.7

    transform rotateflowera:
        anchor (0.5, 0.5) transform_anchor 1
        easein 4 rotate 10
        easeout 4 rotate 0
        easein 4 rotate -10  
        easeout 2 rotate 0    
        repeat

    transform rotateflowera_reverse:
        anchor (0.5, 0.5) transform_anchor 1
        easein 2 rotate -10
        easeout 2 rotate 0
        easein 2 rotate 10  
        easeout 2 rotate 0    
        repeat

    transform circlesize:
        zoom .125

    image wl_circle2topright:
        SnowBlossom(At("images/moods/WL_Circle_2.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(40, 80),  xspeed=(-80,-40), horizontal=True)

    image wl_circle1topright:
        SnowBlossom(At("images/moods/WL_Circle_1.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(40, 80),  xspeed=(-80,0), horizontal=True)

    image wl_circle2topleft:
        SnowBlossom(At("images/moods/WL_Circle_2.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(40, 80),  xspeed=(40,80), horizontal=True)

    image wl_circle1topleft:
        SnowBlossom(At("images/moods/WL_Circle_1.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(40, 80),  xspeed=(40,80), horizontal=True)

    image wl_circle2left:
        SnowBlossom(At("images/moods/WL_Circle_2.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(-40, -80),  xspeed=(40,80), horizontal=True)

    image wl_circle1left:
        SnowBlossom(At("images/moods/WL_Circle_1.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(-40, -80),  xspeed=(40,80), horizontal=True)
        
    image wl_circle2right:
        SnowBlossom(At("images/moods/WL_Circle_2.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(-80, -40),  xspeed=(-80,-40), horizontal=True)

    image wl_circle1right:
        SnowBlossom(At("images/moods/WL_Circle_1.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(-80, -40),  xspeed=(-80,-40), horizontal=True)

    image wl_circle1:
        (ParticleBurst(At("images/moods/WL_Circle_1.png", starsizefade), explodeTime=0, numParticles=3, particleTime=60.0, particleXSpeed = 15, particleYSpeed = 1, centerZone = 1000).sm) with Dissolve
        xzoom .5
        yzoom 0.1
    image wl_circle2:
        (ParticleBurst(At("images/moods/WL_Circle_2.png", starsizefade), explodeTime=0, numParticles=3, particleTime=60.0, particleXSpeed = 1, particleYSpeed = 10, centerZone = 1000).sm) with Dissolve
        zoom .125

label mood_warmlight(image_name=Null, ismovefrombottom = False, scenedissolve = True):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_WarmLight_Loop_V1.ogg") fadein 3.0 loop
    scene bg warmlight
    show wlflower3 at rotateflowera_reverse 
    show wlflower4 at rotateflowera_reverse 
    show wlflower2 at rotateflowera 
    show wlflower1 at rotateflowera 

    show wlflower7 at rotateflowera_reverse 
    show wlflower8 at rotateflowera_reverse 
    show wlflower6 at rotateflowera 
    show wlflower5 at rotateflowera 

    show wl_circle1 at truecenter
    show wl_circle2 at truecenter
    show wl_circle1topright at topright, bubblesize
    show wl_circle2topright at topright, circlesize
    show wl_circle1topleft at topleft, bubblesize
    show wl_circle2topleft at topleft, circlesize
    show wl_circle1right at right, bubblesize
    show wl_circle2right at right, circlesize
    show wl_circle1left at left, bubblesize
    show wl_circle2left at left, circlesize
    if image_name is not Null:
        if ismovefrombottom:
            show expression image_name at dissolvecenter zorder 1
        else:
            show expression image_name at nodissolvecenter zorder 1
    if scenedissolve:
        with dissolve
    return
##
## warmlight ###############################################################

## excitement ###############################################################
##
init:
    transform dotsrotate:
        rotate 0
        #anchor (0.5, 0.5) transform_anchor 1
        easein 64 rotate 360
        repeat
    transform dotsfade:
        alpha 0.7
        easein 2.0 alpha 1.0
        easeout 1.0 alpha 0.7
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
    transform beamfade:
        alpha 0.25
        easein 5.0 alpha 0.5
        easeout 5.0 alpha 0.25
        repeat
    transform starsizefade:
        zoom .5
        easein 1.0 alpha 1.0
        easeout 1.0 alpha 0.0
        repeat

    image bg excitement:
        "images/bg/moods/bg_excitement.png"
        zoom 1.11
    image excite_dots:
        "images/moods/dots1.png"
        zoom 3
    image excite_beam1:
        "images/moods/excitement4.png"
        zoom 1.1
    image excite_beam2:
        "images/moods/excitement5.png"
        zoom 1.1
    image excite_small_dots:
        SnowBlossom(At("images/moods/particle_dot.png", slowblink), border=150, count=80, start=0.00000000001, fast=True,  yspeed=(50, -40),  xspeed=(-25,25), horizontal=True)
    image glow:
        zoom 1.5
        "images/moods/glow.png"

    image excite_stars:
        (ParticleBurst(At("images/moods/EX_Stars.png", starsizefade), explodeTime=0, numParticles=10, particleTime=20.0, particleXSpeed = 20, particleYSpeed = 15, centerZone = 1000 ).sm) with Dissolve
        zoom 0.15

    layeredimage excite_flower_layers:
        always:
            "images/moods/EX_blurflower.png"
        always:
            "images/moods/EX_flower.png"
    transform flowerfade:
        alpha 0
        easein 2.0 alpha 1.0
        easeout 2.0 alpha 0.1
        linear 5.0 alpha 0.1
        repeat

    image excite_flower:
        (ParticleBurst(At("excite_flower_layers", flowerfade), explodeTime=0, numParticles=2, particleTime=60.0, particleXSpeed = 30, particleYSpeed = 15, centerZone = 1000 ).sm) with Dissolve
        zoom 0.1

label mood_excitement(image_name=Null, ismovefrombottom = False, scenedissolve = True):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_Excitement_Loop_V1.ogg") fadein 3.0 loop
    scene bg excitement
    show excite_small_dots
    show excite_stars at truecenter,dotsrotate
    show excite_flower at truecenter
    show excite_beam2 at beam2, truecenter, beamfade
    show excite_beam1 at beam1, truecenter, beamfade
    show excite_dots at dotsrotate, truecenter, dotsfade
    show glow at truecenter
    if image_name is not Null:
        if ismovefrombottom:
            show expression image_name at dissolvecenter zorder 1
        else:
            show expression image_name at nodissolvecenter zorder 1
    if scenedissolve:
        with dissolve
    return

##
## excitement ###############################################################

## happy ###############################################################
##
init:
    transform starfade:
        alpha 0.0
        linear 5.0 alpha 1.0
        easeout 2.0 alpha 0.0
        repeat
    transform bubblefade:
        alpha 0.0
        easein 10.0 alpha 0.9
        easeout 10.0 alpha 0.0
        repeat

    transform bubblesize:
        xzoom .25
        yzoom 0.07

    image bg happy:
        "images/bg/moods/bg_happy.png"
        
    image happy_bubble3topright:
        SnowBlossom(At("images/moods/Happy_bubble3.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(40, 80),  xspeed=(-80,-40), horizontal=True)

    image happy_bubble4topright:
        SnowBlossom(At("images/moods/Happy_bubble4.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(40, 80),  xspeed=(-80,0), horizontal=True)

    image happy_bubble3topleft:
        SnowBlossom(At("images/moods/Happy_bubble3.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(40, 80),  xspeed=(40,80), horizontal=True)

    image happy_bubble4topleft:
        SnowBlossom(At("images/moods/Happy_bubble4.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(40, 80),  xspeed=(40,80), horizontal=True)

    image happy_bubble3left:
        SnowBlossom(At("images/moods/Happy_bubble3.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(-40, -80),  xspeed=(40,80), horizontal=True)

    image happy_bubble4left:
        SnowBlossom(At("images/moods/Happy_bubble4.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(-40, -80),  xspeed=(40,80), horizontal=True)
        
    image happy_bubble3right:
        SnowBlossom(At("images/moods/Happy_bubble3.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(-80, -40),  xspeed=(-80,-40), horizontal=True)

    image happy_bubble4right:
        SnowBlossom(At("images/moods/Happy_bubble4.png", bubblefade), border=400, count=1, start=0.00000000001, fast=True,  yspeed=(-80, -40),  xspeed=(-80,-40), horizontal=True)

    image happy_starwhite:
        (ParticleBurst(At("images/moods/Happy_StarWhite.png", starfade), explodeTime=0, numParticles=3, particleTime=20.0, particleXSpeed = 20, particleYSpeed = 15, centerZone = 1000 ).sm) with Dissolve
        zoom 0.15

    image happy_stargreen:
        (ParticleBurst(At("images/moods/Happy_Stargreen.png", starfade), explodeTime=0, numParticles=3, particleTime=20.0, particleXSpeed = 15, particleYSpeed = 10, centerZone = 1000 ).sm) with Dissolve
        zoom 0.25
        
    image happy_starblur:
        (ParticleBurst(At("images/moods/Happy_Starblur.png", starfade), explodeTime=0, numParticles=3, particleTime=20.0, particleXSpeed = 10, particleYSpeed = 5, centerZone = 1000 ).sm) with Dissolve
        zoom 0.1

label mood_happy(image_name=Null, ismovefrombottom = False, scenedissolve = True):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_Happy_Loop_V1.ogg") fadein 3.0 loop
    scene bg happy
    show happy_stargreen at truecenter
    show happy_starwhite at truecenter
    show happy_starblur at truecenter
    show happy_bubble3topright at topright, bubblesize
    show happy_bubble4topleft at topright, bubblesize
    show happy_bubble3topleft at topleft, bubblesize
    show happy_bubble4topleft at topleft, bubblesize
    show happy_bubble3right at right, bubblesize
    show happy_bubble4right at right, bubblesize
    show happy_bubble3left at left, bubblesize
    show happy_bubble4left at left, bubblesize
    #show excite_dots at dots
    if image_name is not Null:
        if ismovefrombottom:
            show expression image_name at dissolvecenter zorder 1
        else:
            show expression image_name at nodissolvecenter zorder 1
    if scenedissolve:
        with dissolve
    return


##
## happy ###############################################################

## other ###############################################################
##
define mymatrix_normal = Matrix([1.0, 0.0, 0.0, 0.0,
                                0.0, 1.0, 0.0, 0.0,
                                0.0, 0.0, 1.0, 0.0,
                                0.0, 0.0, 0.0, 1.0,])
init:
    image flower:
        "gui/window_icon.png"
        yalign 0.925
        xalign 0.9575

    image bg loading:
        "images/bg_loading.png"
    image bg beach_day:
        "images/bg/bg_beach_day.png"
        matrixcolor mymatrix_normal
    image bg volleyball_day:
        "images/bg/bg_volleyball_day.png"
        matrixcolor mymatrix_normal

    image bg inner_monologue:
        "images/bg/moods/bg_inner_monologue.png"


    image bg speedlinebg_red:
        xoffset -3920
        yoffset -1250
        zoom 2
        rotate -45
        anchor (0, 0) transform_anchor 1
        contains:
            parallel:
                Tile("images/bg/moods/bg_speedlinebg_red.png")
                ytile 3
                xtile 3
                xpan -5400
                linear 8 xpan 180
                xalign 1
                yalign 1
                repeat

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
    pause 2
    return

label beachdayscene(keep_images=False):
    window hide
    $ renpy.music.set_volume(1,3.0,"music")
    play music "audio/sfx_ambience_beach.ogg"
    if keep_images:
        call hideeffects
        show bg beach_day with dissolve
    else:
        scene bg beach_day with dissolve
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

label speedlinesredscene(image_name=Null, ismovefrombottom = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_SpeedLine_Loop-003.ogg") fadein 3.0 loop
    scene bg speedlinebg_red with dissolve
    if image_name is not Null:
        if ismovefrombottom:
            show expression image_name at volleycenter,coin_yoffset zorder 1
        else:
            show expression image_name at nodissolvecenter,coin_yoffset zorder 1
    with dissolve
    return

label mood_speedlines(image_name=Null, ismovefrombottom = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_SpeedLine_Loop-001.ogg") fadein 3.0 loop
    show speedlines
    if image_name is not Null:
        if ismovefrombottom:
            show expression image_name at dissolvecenter,coin_yoffset zorder 1
        else:
            show expression image_name at nodissolvecenter,coin_yoffset zorder 1
    with dissolve
    return

label mood_inner_monologuescene(image_name=Null, ismovefrombottom = False, nobg = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_InnerMonologue_Loop_V1.ogg") fadein 3.0 loop
    if not nobg:
        scene bg inner_monologue
    show dreadnoise
    if image_name is not Null:
        if ismovefrombottom:
            show expression image_name at dissolvecenter zorder 1
        else:
            show expression image_name at nodissolvecenter zorder 1
    with dissolve
    return

label show_item(image_name=Null, ismovefrombottom = False):
    window hide
    $ renpy.music.set_volume(0.25,3.0,"music")
    play moodloop("audio/m_Mood_InnerMonologue_Loop_V1.ogg") fadein 3.0 loop
    show dreadnoise
    if image_name is not Null:
        if ismovefrombottom:
            show expression image_name at dissolvecenter,coin_yoffset zorder 1
        else:
            show expression image_name at nodissolvecenter,coin_yoffset zorder 1
    with dissolve
    return
    