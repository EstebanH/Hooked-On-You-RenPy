
## Character Positions ###############################################################
init:
    transform moveleft:
        xoffset -700
    transform moveright:
        xoffset 690
    transform movecenterleft:
        xoffset -235
    transform movecenterright:
        xoffset 230

    transform slidetomoveleft:
        linear 0.75 xoffset -700
    transform slidetomoveright:
        linear 0.75 xoffset 690
    transform slidetomovecenterleft:
        linear 0.75 xoffset -235
    transform slidetomovecenterright:
        linear 0.75 xoffset 230

    transform moverightclose:
        xoffset 590
    transform fadeaway:
        linear 0.75 alpha 0.0
    transform fadenear:
        alpha 0.0
        linear 0.75 alpha 1.0
    transform noalpha:
        alpha 0.0
    transform slidetocenter:
        linear 0.75 xoffset 0

## Character Emotes ###############################################################

init:
    ## Heart ###############################################################
    transform heartfade:
        easeout 1.0 alpha 0.0

    image heartboom_pose:
        function play_sfxheart
        zoom 0.15
        (ParticleBurst(At("images/emotes/heart.png", heartfade), explodeTime=0, numParticles=10, particleTime=20.0, particleXSpeed = 20, particleYSpeed = 15, centerZone = 1000).sm) with Dissolve

    image heartboom_close:
        function play_sfxheart
        zoom 0.25
        (ParticleBurst(At("images/emotes/heart.png",heartfade), explodeTime=0, numParticles=10, particleTime=20.0, particleXSpeed = 20, particleYSpeed = 15, centerZone = 1000).sm) with Dissolve

    image heart_pose:
        xalign 0.5
        yalign 0.5
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0
 
    image heart_close:
        xalign 0.5
        yalign 0.5
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    ## Question ###############################################################
    transform question1_rotate:
        rotate -25
        anchor (0.5, 0.5) transform_anchor 1
        easein 3 rotate 25

    transform question2_rotate:
        rotate 10
        anchor (0.5, 0.5) transform_anchor 1
        easein 3 rotate -35
        rotate 10

    transform question_zoom:
        anchor (0.5, 0.5) transform_anchor 1
        easein 3.0 zoom 1.3

    image question_small:
        xalign 0.5
        yalign 0.2
        xoffset 60
        zoom 0.2
        "images/emotes/question.png"
        linear 2.0 yoffset -100
        linear 0 yoffset 0
    
    image question_large:
        xalign 0.5
        yalign 0.25
        xoffset -140
        zoom 0.3
        "images/emotes/question.png"
        linear 5.0 yoffset -300
        linear 0 yoffset 0

    image question1:
        function play_sfxquestion
        alpha 0.00
        At("question_small", question1_rotate,question_zoom)
        easein .5 alpha 1.00
        pause 0.4
        easeout 0.5 alpha 0.0
        
    image question2:
        pause .5
        alpha 0.00
        At("question_large", question2_rotate,question_zoom)
        easein .5 alpha 1.00
        pause .6
        easeout 0.5 alpha 0.0
    
    layeredimage question_layers:
        always:
            "question1"
        always:
            "question2"

    image question_pose:
        "question_layers"
        zoom 0.3

    image question_close:
        "question_layers"
        zoom 0.3
    ## Star ###############################################################
    transform star_zoom:
        zoom 0
        easein 1.0 zoom 1.0
        easeout 1.0 zoom 0.0
    image goldstars:
        function play_sfxstars
        zoom 0.2
        xalign 0.5
        yalign 0.5
        (ParticleBurst(At("images/emotes/GoldStar_01.png",heartfade), explodeTime=0, numParticles=10, particleTime=20.0, particleXSpeed = 0, particleYSpeed = 0, centerZone = 0, xZone = 2000, yZone = 1000).sm) with Dissolve
    image yellowstars:
        function play_sfxstars
        zoom 0.2
        xalign 0.5
        yalign 0.5
        (ParticleBurst(At("images/emotes/YellowStar_01.png",heartfade), explodeTime=0, numParticles=10, particleTime=3.0, particleXSpeed = 0, particleYSpeed = 0, centerZone = 0, xZone = 2000, yZone = 1000).sm) with Dissolve
        
    layeredimage stars_layers:
        always:
            "goldstars"
        always:
            "yellowstars"

    image stars_pose:
        "stars_layers"
        zoom 0.7
        yoffset 160
        xoffset 140

    image stars_close:
        "stars_layers"

    ## Exclamation ###############################################################
    image exclamation:
        function play_sfxexclamation
        "images/emotes/exclamation.png"
        xalign 0.5
        yalign 0.5
        alpha 0.00
        easein .5 alpha 1.00
        linear 2.0 yoffset -100
        pause 0.4
        easeout 0.5 alpha 0.0

    image exclamation_pose:
        "exclamation"
        zoom 0.3
        

    image exclamation_close:
        "exclamation"
        zoom 0.3

    ## Lightbulb ###############################################################
    image lightbulb:
        function play_sfxlightbulb
        "images/emotes/lightbulb1.png"
        xalign 0.5
        yalign 0.5
        alpha 0.00
        easein .5 alpha 1.00
        linear 2.0 yoffset -100
        pause 0.2
        "images/emotes/lightbulb2.png"
        pause 0.2
        easeout 0.5 alpha 0.0
    image lightbulb_flash1:
        "images/emotes/lightbulb2_flash1.png"
        xalign 0.1
        yalign 0.0
    image lightbulb_flash2:
        "images/emotes/lightbulb2_flash2.png"
        xalign 0.0
        yalign 0.0
    image lightbulb_flash3:
        "images/emotes/lightbulb2_flash3.png"
        xalign 0.9
        yalign 0.0

    layeredimage lightbulb_layers:
        always:
            "lightbulb"
        always:
            "lightbulb_flash1"
        always:
            "lightbulb_flash2"
        always:
            "lightbulb_flash3"

    image lightbulb_pose:
        "lightbulb_layers"
        zoom 0.3

    image lightbulb_close:
        "lightbulb_layers"
        zoom 0.3
    ## Sweatdrop ###############################################################
    transform sweat_translate:
        linear 1.0 yoffset 40

    image sweat:
        function play_sfxsweatdrop
        "images/emotes/sweat.png"
        xalign 0.5
        yalign 0.5
        alpha 0.00
        easein .5 alpha 1.00
        pause .5
        easeout 0.5 alpha 0.0

    image sweat_pose:
        At("sweat", sweat_translate)
        zoom 0.1
        xoffset -200
        yoffset 100

    image sweat_close:
        At("sweat", sweat_translate)
        zoom 0.1

    ## Heartbroken ###############################################################
    image heartbroken:
        function play_sfxbrokenheart
        "images/emotes/brokenheart1.png"
        xalign 0.5
        yalign 0.5
        alpha 0.00
        easein .5 alpha 1.00
        pause 0.1
        "images/emotes/brokenheart2.png"
        pause 0.2
        "images/emotes/brokenheart3.png"
        pause 0.2
        easeout 0.5 alpha 0.0

    image heartbroken_pose:
        "heartbroken"
        zoom 0.3

    image heartbroken_close:
        "heartbroken"
        zoom 0.3

    ## Dread ###############################################################
    image dread:
        function play_sfxdread
        "images/emotes/dread.png"
        xalign 0.5
        yalign 0.5
        alpha 0.00
        easein .5 alpha 1.00
        pause 0.4
        easeout 0.5 alpha 0.0

    image dread_pose:
        "dread"
        zoom 0.3

    image dread_close:
        "dread"
        zoom 0.3

    ## Anger ###############################################################
    transform anger_translate:
        linear 2.0 yoffset -1
        linear 0 yoffset 0
        repeat

    image anger_small:
        zoom 0.6
        "images/emotes/anger1.png"
        pause .3
        "images/emotes/anger2.png"
        pause .3
        repeat
    
    image anger_large:
        zoom .7
        "images/emotes/anger2.png"
        pause .3
        "images/emotes/anger1.png"
        pause .3
        repeat

    image anger1:
        function play_sfxanger
        alpha 0.00
        xalign 0.5
        yalign 0.5
        xoffset -400
        yoffset 50
        At("anger_small", anger_translate)
        easein .5 alpha 1.00
        pause 1
        easeout 0.5 alpha 0.0
        
    image anger2:
        alpha 0.00
        xalign 0.5
        yalign 0.5
        xoffset 75
        yoffset -175
        At("anger_large", anger_translate)
        easein .5 alpha 1.00
        pause 1
        easeout 0.5 alpha 0.0

    layeredimage anger_layers:
        always:
            "anger1"
        always:
            "anger2"
    
    image anger_pose:
        "anger_layers"

    image anger_close:
        "anger_layers"

    ## Spark ###############################################################
    transform xoffsetsparks_small:
        linear .2 xoffset -300
        linear .1 xoffset -225
        linear 5 xoffset -300
    transform yoffsetsparks_small:
        linear .2 yoffset 300
        linear .1 yoffset 225
        linear 5 yoffset 300
    transform xoffsetsparks_large:
        linear .2 xoffset 250
        linear .1 xoffset 125
        linear 5 xoffset 250
    transform yoffsetsparks_large:
        linear .2 yoffset -250
        linear .1 yoffset -125
        linear 5 yoffset -250

    image spark_small:
        At("images/emotes/spark1.png",xoffsetsparks_small,yoffsetsparks_small)
        xalign 0.5
        yalign 0.5
        yoffset -200
        zoom .6
    
    image spark_large:
        At("images/emotes/spark2.png",xoffsetsparks_large,yoffsetsparks_large)
        xalign 0.5
        yalign 0.5
        zoom .6

    image spark1:
        function play_sfxshock
        alpha 0.00
        "spark_small"
        easein .5 alpha 1.00
        pause 1
        easeout 0.5 alpha 0.0
        
    image spark2:
        alpha 0.00
        "spark_large"
        easein .5 alpha 1.00
        pause 1
        easeout 0.5 alpha 0.0

    layeredimage spark_layers:
        always:
            "spark1"
        always:
            "spark2"

    image spark_pose:
        "spark_layers"
        xoffset -175

    image spark_close:
        "spark_layers"
        xoffset -175

    ## Thoughts ###############################################################
    image thought_bubble:
        "images/emotes/thought_bubble.png"
        xalign 0.5
        yalign 0.5
    
    image thought_dot1:
        "images/emotes/thought_bubble_dot1.png"
        xalign 1.0
        yalign 1.0

    image thought_dot2:
        "images/emotes/thought_bubble_dot1.png"
        xalign .9
        yalign .9

    image thought_text1:
        "images/emotes/thought_bubble_dot_bl.png"
        xalign 0.6
        yalign 0.5

    image thought_text2:
        "images/emotes/thought_bubble_dot_bl.png"
        xalign 0.5
        yalign 0.5

    image thought_text3:
        "images/emotes/thought_bubble_dot_bl.png"
        xalign 0.4
        yalign 0.5

    image thought_bubble_dot1:
        function play_sfxthought
        alpha 0.00
        "thought_dot1"
        easein .5 alpha 1.00
        pause 1
        easeout 0.5 alpha 0.0
        
    image thought_bubble_dot2:
        pause 0.2
        alpha 0.00
        "thought_dot2"
        easein .5 alpha 1.00
        pause .8
        easeout 0.5 alpha 0.0

    image thought_bubble_base:
        pause 0.4
        alpha 0.00
        "thought_bubble"
        easein .5 alpha 1.00
        pause .6
        easeout 0.5 alpha 0.0

    image thought_bubble_text1:
        pause 0.6
        alpha 0.00
        "thought_text1"
        easein .5 alpha 1.00
        pause .4
        easeout 0.5 alpha 0.0

    image thought_bubble_text1:
        pause .8
        alpha 0.00
        "thought_text2"
        easein .5 alpha 1.00
        pause .2
        easeout 0.5 alpha 0.0

    image thought_bubble_text1:
        pause 1.0
        alpha 0.00
        "thought_text3"
        easein .5 alpha 1.00
        pause .2
        easeout 0.5 alpha 0.0

    layeredimage thoughts_layers:
        always:
            "thought_bubble_base"
        always:
            "thought_bubble_dot1"
        always:
            "thought_bubble_dot2"
        always:
            "thought_bubble_text1"
        always:
            "thought_bubble_text2"
        always:
            "thought_bubble_text3"

    image thoughts_layers:
        "spark_layers"
        zoom 0.3

    image thoughts_layers:
        "spark_layers"
        zoom 0.3


init python:
    def play_sfxheart(trans, st, at):
        renpy.play("sounds/SFX_Emotes_Hearts_V01.ogg", channel="sound")
    def play_sfxquestion(trans, st, at):
        renpy.play("sounds/SFX_Emotes_Questions_V01.ogg", channel="sound")
    def play_sfxanger(trans, st, at):
        renpy.play("sounds/SFX_Emotes_Anger_V01.ogg", channel="sound")
    def play_sfxbrokenheart(trans, st, at):
        renpy.play("sounds/SFX_Emotes_BrokenHeart_V01.ogg", channel="sound")
    def play_sfxdread(trans, st, at):
        renpy.play("sounds/SFX_Emotes_Dread_V01.ogg", channel="sound")
    def play_sfxexclamation(trans, st, at):
        renpy.play("sounds/SFX_Emotes_Exclamation_V01.ogg", channel="sound")
    def play_sfxlightbulb(trans, st, at):
        renpy.play("sounds/SFX_Emotes_Lightbulb_V01.ogg", channel="sound")
    def play_sfxshock(trans, st, at):
        renpy.play("sounds/SFX_Emotes_ShockSpark_V01.ogg", channel="sound")
    def play_sfxstars(trans, st, at):
        renpy.play("sounds/SFX_Emotes_Stars_V01.ogg", channel="sound")
    def play_sfxsweatdrop(trans, st, at):
        renpy.play("sounds/SFX_Emotes_SweatDrop_V01.ogg", channel="sound")
    def play_sfxthought(trans, st, at):
        renpy.play("sounds/SFX_Emotes_Thought_V01.ogg", channel="sound")


## clauddwight ###############################################################
## Pose attritubes: close01, close02, far01, far02
## Emotion attritubes: idle, mad, sad, scared, disgusted, happy
##
init:
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
        if clauddwightObj.emote == "heart" and clauddwightObj.state == "pose":
            "clauddwight_heart_pose"
            
        if clauddwightObj.emote == "heart" and clauddwightObj.state == "close":
            "clauddwight_heart_close"

        if clauddwightObj.emote == "stars" and clauddwightObj.state == "pose":
            "clauddwight_stars_pose"

        if clauddwightObj.emote == "stars" and clauddwightObj.state == "close":
            "clauddwight_stars_close"

        if clauddwightObj.emote == "question" and clauddwightObj.state == "pose":
            "clauddwight_question_pose"

        if clauddwightObj.emote == "question" and clauddwightObj.state == "close":
            "clauddwight_question_close"

        if clauddwightObj.emote == "anger" and clauddwightObj.state == "pose":
            "clauddwight_anger_pose"

        if clauddwightObj.emote == "anger" and clauddwightObj.state == "close":
            "clauddwight_anger_close"
            
        if clauddwightObj.emote == "brokenheart" and clauddwightObj.state == "pose":
            "clauddwight_brokenheart_pose"

        if clauddwightObj.emote == "brokenheart" and clauddwightObj.state == "close":
            "clauddwight_brokenheart_close"

        if clauddwightObj.emote == "dread" and clauddwightObj.state == "pose":
            "clauddwight_dread_pose"

        if clauddwightObj.emote == "dread" and clauddwightObj.state == "close":
            "clauddwight_dread_close"
            
        if clauddwightObj.emote == "exclamation" and clauddwightObj.state == "pose":
            "clauddwight_exclamation_pose"

        if clauddwightObj.emote == "exclamation" and clauddwightObj.state == "close":
            "clauddwight_exclamation_close"

        if clauddwightObj.emote == "lightbulb" and clauddwightObj.state == "pose":
            "clauddwight_lightbulb_pose"

        if clauddwightObj.emote == "lightbulb" and clauddwightObj.state == "close":
            "clauddwight_lightbulb_close"
            
        if clauddwightObj.emote == "spark" and clauddwightObj.state == "pose":
            "clauddwight_spark_pose"

        if clauddwightObj.emote == "spark" and clauddwightObj.state == "close":
            "clauddwight_spark_close"
            
        if clauddwightObj.emote == "sweat" and clauddwightObj.state == "pose":
            "clauddwight_sweat_pose"

        if clauddwightObj.emote == "sweat" and clauddwightObj.state == "close":
            "clauddwight_sweat_close"
            
        if clauddwightObj.emote == "thoughts" and clauddwightObj.state == "pose":
            "clauddwight_thoughts_pose"

        if clauddwightObj.emote == "thoughts" and clauddwightObj.state == "close":
            "clauddwight_thoughts_close"
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

    image heartboom_claud_far:
        xalign 0.45
        yalign 0.15
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_dwight_far01:
        xalign 0.65
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_dwight_far02:
        xalign 0.675
        yalign 0.1
        "heartboom_pose"
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
    image clauddwight_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image clauddwight_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image clauddwight_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image clauddwight_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image clauddwight_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image clauddwight_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image clauddwight_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image clauddwight_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image clauddwight_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image clauddwight_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image clauddwight_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image clauddwight_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image clauddwight_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image clauddwight_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image clauddwight_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image clauddwight_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image clauddwight_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image clauddwight_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image clauddwight_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image clauddwight_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image clauddwight_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image clauddwight_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300

    transform clauddwightfar:
        xalign 0.5
        yalign 0.25

    transform smaller:
        zoom 0.1

init python:
    class ClauddwightClass:
        def __init__(self):
            self.pose = "close01"
            self.emotion = "idle"
            self.emote = "none"
            self.state = "close"
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
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "whoIsDead":
                self.whoIsDead = value
            elif attribute == "emote":
                self.emote = value
            self.resetFilenames()

##
## clauddwight ###############################################################

## grandma ###############################################################
## Pose attritubes: close01, close02, pose01, pose02
## Emotion attritubes: idle, mad, sad, scared, disgusted, happy
##

init:
    layeredimage grandma:
        always:
            "[grandmaObj.poseFilename]"
        always:
            "grandma_blink"
            
        if grandmaObj.emote == "heart" and grandmaObj.state == "pose":
            "grandma_heart_pose"
            
        if grandmaObj.emote == "heart" and grandmaObj.state == "close":
            "grandma_heart_close"

        if grandmaObj.emote == "stars" and grandmaObj.state == "pose":
            "grandma_stars_pose"

        if grandmaObj.emote == "stars" and grandmaObj.state == "close":
            "grandma_stars_close"

        if grandmaObj.emote == "question" and grandmaObj.state == "pose":
            "grandma_question_pose"

        if grandmaObj.emote == "question" and grandmaObj.state == "close":
            "grandma_question_close"

        if grandmaObj.emote == "anger" and grandmaObj.state == "pose":
            "grandma_anger_pose"

        if grandmaObj.emote == "anger" and grandmaObj.state == "close":
            "grandma_anger_close"
            
        if grandmaObj.emote == "brokenheart" and grandmaObj.state == "pose":
            "grandma_brokenheart_pose"

        if grandmaObj.emote == "brokenheart" and grandmaObj.state == "close":
            "grandma_brokenheart_close"

        if grandmaObj.emote == "dread" and grandmaObj.state == "pose":
            "grandma_dread_pose"

        if grandmaObj.emote == "dread" and grandmaObj.state == "close":
            "grandma_dread_close"
            
        if grandmaObj.emote == "exclamation" and grandmaObj.state == "pose":
            "grandma_exclamation_pose"

        if grandmaObj.emote == "exclamation" and grandmaObj.state == "close":
            "grandma_exclamation_close"

        if grandmaObj.emote == "lightbulb" and grandmaObj.state == "pose":
            "grandma_lightbulb_pose"

        if grandmaObj.emote == "lightbulb" and grandmaObj.state == "close":
            "grandma_lightbulb_close"
            
        if grandmaObj.emote == "spark" and grandmaObj.state == "pose":
            "grandma_spark_pose"

        if grandmaObj.emote == "spark" and grandmaObj.state == "close":
            "grandma_spark_close"
            
        if grandmaObj.emote == "sweat" and grandmaObj.state == "pose":
            "grandma_sweat_pose"

        if grandmaObj.emote == "sweat" and grandmaObj.state == "close":
            "grandma_sweat_close"
            
        if grandmaObj.emote == "thoughts" and grandmaObj.state == "pose":
            "grandma_thoughts_pose"

        if grandmaObj.emote == "thoughts" and grandmaObj.state == "close":
            "grandma_thoughts_close"

    image grandma_blink:
        "[grandmaObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[grandmaObj.blinkFilename]"
        pause 0.1
        repeat

    image grandma_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image grandma_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image grandma_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image grandma_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image grandma_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image grandma_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image grandma_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image grandma_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image grandma_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image grandma_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image grandma_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image grandma_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image grandma_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image grandma_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image grandma_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image grandma_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image grandma_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image grandma_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image grandma_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image grandma_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image grandma_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image grandma_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300

    image grandma_blink:
        "[grandmaObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[grandmaObj.blinkFilename]"
        pause 0.1
        repeat

    image heartboom_grandma_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_grandma_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class GrandmaClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.state = "pose"
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/grandma/wraith_grandma_" + self.pose + ".png"
            self.emotionFilename = "images/sprites/grandma/wraith_grandma_" + self.pose + "_" + self.emotion + "_00.png"
            self.blinkFilename = "images/sprites/grandma/wraith_grandma_" + self.pose + "_" + self.emotion + "_01.png"

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "emote":
                self.emote = value
            self.resetFilenames()

##
## grandma ###############################################################

## huntress ##############################################################
## Pose attritubes: close01, close02, close03, close04, pose01, pose02, pose03, pose04
## Emotion attritubes: idle, mad, sad, scared, disgusted, happy, stoic, obsessed
## Swim: True, False
## Notes: Only pose04 has obsessed sprites
## 

init:
    layeredimage huntress:
        always:
            "[huntressObj.poseFilename]"
        always:
            "huntress_blink"
            
        if huntressObj.emote == "heart" and huntressObj.state == "pose":
            "huntress_heart_pose"
            
        if huntressObj.emote == "heart" and huntressObj.state == "close":
            "huntress_heart_close"

        if huntressObj.emote == "stars" and huntressObj.state == "pose":
            "huntress_stars_pose"

        if huntressObj.emote == "stars" and huntressObj.state == "close":
            "huntress_stars_close"

        if huntressObj.emote == "question" and huntressObj.state == "pose":
            "huntress_question_pose"

        if huntressObj.emote == "question" and huntressObj.state == "close":
            "huntress_question_close"

        if huntressObj.emote == "anger" and huntressObj.state == "pose":
            "huntress_anger_pose"

        if huntressObj.emote == "anger" and huntressObj.state == "close":
            "huntress_anger_close"
            
        if huntressObj.emote == "brokenheart" and huntressObj.state == "pose":
            "huntress_brokenheart_pose"

        if huntressObj.emote == "brokenheart" and huntressObj.state == "close":
            "huntress_brokenheart_close"

        if huntressObj.emote == "dread" and huntressObj.state == "pose":
            "huntress_dread_pose"

        if huntressObj.emote == "dread" and huntressObj.state == "close":
            "huntress_dread_close"
            
        if huntressObj.emote == "exclamation" and huntressObj.state == "pose":
            "huntress_exclamation_pose"

        if huntressObj.emote == "exclamation" and huntressObj.state == "close":
            "huntress_exclamation_close"

        if huntressObj.emote == "lightbulb" and huntressObj.state == "pose":
            "huntress_lightbulb_pose"

        if huntressObj.emote == "lightbulb" and huntressObj.state == "close":
            "huntress_lightbulb_close"
            
        if huntressObj.emote == "spark" and huntressObj.state == "pose":
            "huntress_spark_pose"

        if huntressObj.emote == "spark" and huntressObj.state == "close":
            "huntress_spark_close"
            
        if huntressObj.emote == "sweat" and huntressObj.state == "pose":
            "huntress_sweat_pose"

        if huntressObj.emote == "sweat" and huntressObj.state == "close":
            "huntress_sweat_close"
            
        if huntressObj.emote == "thoughts" and huntressObj.state == "pose":
            "huntress_thoughts_pose"

        if huntressObj.emote == "thoughts" and huntressObj.state == "close":
            "huntress_thoughts_close"

    image huntress_blink:
        "[huntressObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[huntressObj.blinkFilename]"
        pause 0.1
        repeat

    image huntress_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image huntress_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image huntress_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image huntress_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image huntress_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image huntress_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image huntress_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image huntress_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image huntress_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image huntress_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image huntress_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image huntress_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image huntress_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image huntress_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image huntress_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image huntress_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image huntress_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image huntress_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image huntress_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image huntress_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image huntress_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image huntress_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300

    image heartboom_huntress_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class HuntressClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.state = "pose"
            self.swim = False
            self.resetFilenames()
            
        def resetFilenames(self):
            if self.swim != True:
                self.poseFilename = "images/sprites/huntress/huntress_" + self.pose + ".png"
            else:
                self.poseFilename = "images/sprites/huntress/huntress_" + self.pose + "_swim.png"
            if self.emotion != "obsessed":
                self.emotionFilename = "images/sprites/huntress/huntress_" + self.pose + "_" + self.emotion + "_00.png"
                self.blinkFilename = "images/sprites/huntress/huntress_" + self.pose + "_" + self.emotion + "_01.png"
            else:
                self.emotionFilename = "images/sprites/huntress/huntress_pose04_" + self.emotion + "_00.png"
                self.blinkFilename = "images/sprites/huntress/huntress_pose04_" + self.emotion + "_01.png"

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "emote":
                self.emote = value
            elif attribute == "swim":
                self.emote = value
            self.resetFilenames()
##
## huntress ###############################################################

## huntress mom ###########################################################
## Pose attritubes: close01, close02, pose01, pose02
## Emotion attritubes: idle, mad, sad, scared, disgusted, happy
##

init:
    layeredimage mom:
        always:
            "[momObj.poseFilename]"
        always:
            "mom_blink"
            
        if momObj.emote == "heart" and momObj.state == "pose":
            "mom_heart_pose"
            
        if momObj.emote == "heart" and momObj.state == "close":
            "mom_heart_close"

        if momObj.emote == "stars" and momObj.state == "pose":
            "mom_stars_pose"

        if momObj.emote == "stars" and momObj.state == "close":
            "mom_stars_close"

        if momObj.emote == "question" and momObj.state == "pose":
            "mom_question_pose"

        if momObj.emote == "question" and momObj.state == "close":
            "mom_question_close"

        if momObj.emote == "anger" and momObj.state == "pose":
            "mom_anger_pose"

        if momObj.emote == "anger" and momObj.state == "close":
            "mom_anger_close"
            
        if momObj.emote == "brokenheart" and momObj.state == "pose":
            "mom_brokenheart_pose"

        if momObj.emote == "brokenheart" and momObj.state == "close":
            "mom_brokenheart_close"

        if momObj.emote == "dread" and momObj.state == "pose":
            "mom_dread_pose"

        if momObj.emote == "dread" and momObj.state == "close":
            "mom_dread_close"
            
        if momObj.emote == "exclamation" and momObj.state == "pose":
            "mom_exclamation_pose"

        if momObj.emote == "exclamation" and momObj.state == "close":
            "mom_exclamation_close"

        if momObj.emote == "lightbulb" and momObj.state == "pose":
            "mom_lightbulb_pose"

        if momObj.emote == "lightbulb" and momObj.state == "close":
            "mom_lightbulb_close"
            
        if momObj.emote == "spark" and momObj.state == "pose":
            "mom_spark_pose"

        if momObj.emote == "spark" and momObj.state == "close":
            "mom_spark_close"
            
        if momObj.emote == "sweat" and momObj.state == "pose":
            "mom_sweat_pose"

        if momObj.emote == "sweat" and momObj.state == "close":
            "mom_sweat_close"
            
        if momObj.emote == "thoughts" and momObj.state == "pose":
            "mom_thoughts_pose"

        if momObj.emote == "thoughts" and momObj.state == "close":
            "mom_thoughts_close"

    image mom_blink:
        "[momObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[momObj.blinkFilename]"
        pause 0.1
        repeat

    image mom_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image mom_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image mom_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image mom_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image mom_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image mom_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image mom_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image mom_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image mom_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image mom_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image mom_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image mom_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image mom_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image mom_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image mom_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image mom_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image mom_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image mom_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image mom_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image mom_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image mom_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image mom_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300
    image mom_blink:
        "[momObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[momObj.blinkFilename]"
        pause 0.1
        repeat

    image heartboom_mom_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_mom_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class MomClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.state = "pose"
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/huntress_mom/huntress_mom_" + self.pose + ".png"
            self.emotionFilename = "images/sprites/huntress_mom/huntress_mom_" + self.pose + "_" + self.emotion + "_00.png"
            self.blinkFilename = "images/sprites/huntress_mom/huntress_mom_" + self.pose + "_" + self.emotion + "_01.png"

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "emote":
                self.emote = value
            self.resetFilenames()
##
## huntress mom ############################################################

## spirit ##################################################################
## Pose attritubes: close01, close02, close03, close04, pose01, pose02, pose03, pose04
## Emotion attritubes: idle, mad, sad, scared, disgusted, happy, obsessed
## Swim: True, False
## Notes: Only pose04 and close04 has obsessed sprites
##

init:
    layeredimage spirit:
        always:
            "[spiritObj.poseFilename]"
        always:
            "spirit_blink"
            
        if spiritObj.emote == "heart" and spiritObj.state == "pose":
            "spirit_heart_pose"
            
        if spiritObj.emote == "heart" and spiritObj.state == "close":
            "spirit_heart_close"

        if spiritObj.emote == "stars" and spiritObj.state == "pose":
            "spirit_stars_pose"

        if spiritObj.emote == "stars" and spiritObj.state == "close":
            "spirit_stars_close"

        if spiritObj.emote == "question" and spiritObj.state == "pose":
            "spirit_question_pose"

        if spiritObj.emote == "question" and spiritObj.state == "close":
            "spirit_question_close"

        if spiritObj.emote == "anger" and spiritObj.state == "pose":
            "spirit_anger_pose"

        if spiritObj.emote == "anger" and spiritObj.state == "close":
            "spirit_anger_close"
            
        if spiritObj.emote == "brokenheart" and spiritObj.state == "pose":
            "spirit_brokenheart_pose"

        if spiritObj.emote == "brokenheart" and spiritObj.state == "close":
            "spirit_brokenheart_close"

        if spiritObj.emote == "dread" and spiritObj.state == "pose":
            "spirit_dread_pose"

        if spiritObj.emote == "dread" and spiritObj.state == "close":
            "spirit_dread_close"
            
        if spiritObj.emote == "exclamation" and spiritObj.state == "pose":
            "spirit_exclamation_pose"

        if spiritObj.emote == "exclamation" and spiritObj.state == "close":
            "spirit_exclamation_close"

        if spiritObj.emote == "lightbulb" and spiritObj.state == "pose":
            "spirit_lightbulb_pose"

        if spiritObj.emote == "lightbulb" and spiritObj.state == "close":
            "spirit_lightbulb_close"
            
        if spiritObj.emote == "spark" and spiritObj.state == "pose":
            "spirit_spark_pose"

        if spiritObj.emote == "spark" and spiritObj.state == "close":
            "spirit_spark_close"
            
        if spiritObj.emote == "sweat" and spiritObj.state == "pose":
            "spirit_sweat_pose"

        if spiritObj.emote == "sweat" and spiritObj.state == "close":
            "spirit_sweat_close"
            
        if spiritObj.emote == "thoughts" and spiritObj.state == "pose":
            "spirit_thoughts_pose"

        if spiritObj.emote == "thoughts" and spiritObj.state == "close":
            "spirit_thoughts_close"

    image spirit_blink:
        "[spiritObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[spiritObj.blinkFilename]"
        pause 0.1
        repeat

    image spirit_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image spirit_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image spirit_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image spirit_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image spirit_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image spirit_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image spirit_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image spirit_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image spirit_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image spirit_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image spirit_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image spirit_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image spirit_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image spirit_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image spirit_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image spirit_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image spirit_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image spirit_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image spirit_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image spirit_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image spirit_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image spirit_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300

    image spirit_blink:
        "[spiritObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[spiritObj.blinkFilename]"
        pause 0.1
        repeat

    image heartboom_spirit_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_spirit_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class SpiritClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.state = "pose"
            self.swim = False
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/spirit/spirit_" + self.pose + ".png"
            if self.emotion != "obsessed":
                self.emotionFilename = "images/sprites/spirit/spirit_" + self.pose + "_" + self.emotion + "_00.png"
                if self.emotion != "mad":
                    ## If NOT mad or obsessed
                    self.blinkFilename = "images/sprites/spirit/spirit_" + self.pose + "_" + self.emotion + "_01.png"
                else:
                    ## If mad, don't blink
                    self.blinkFilename = self.emotionFilename
            else:
                if self.pose == "close04" or self.pose == "pose04":
                    ## If obsessed and using close04/pose04
                    self.emotionFilename = "images/sprites/spirit/spirit_" + self.pose + "_" + self.emotion + "_00.png"
                    self.blinkFilename = "images/sprites/spirit/spirit_" + self.pose + "_" + self.emotion + "_01.png"
                else:
                    ## If NOT obsessed and using any pose
                    self.emotionFilename = "images/sprites/spirit/spirit_" + self.pose + "_happy_00.png"
                    self.blinkFilename = "images/sprites/spirit/spirit_" + self.pose + "_happy_01.png"

            if self.swim == True and self.pose == "pose04":
                    ## If swimming and using pose04
                    self.emotionFilename = "images/sprites/spirit/spirit_swim_" + self.pose + "_" + self.emotion + "_00.png"
                    self.blinkFilename = "images/sprites/spirit/spirit_swim_" + self.pose + "_" + self.emotion + "_01.png"


        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "emote":
                self.emote = value
            elif attribute == "swim":
                self.emote = value
            self.resetFilenames()

##
## spirit ##################################################################

## trapper #################################################################
## Pose attritubes: close01, close02, close03, close04, pose01, pose02, pose03, pose04
## Emotion attritubes: idle, mad, sad, scared, disgusted, happy, obsessed
## Notes: Only pose04 and close04 has obsessed sprites
##


init:
    layeredimage trapper:
        always:
            "[trapperObj.poseFilename]"
        always:
            "trapper_blink"
            
        if trapperObj.emote == "heart" and trapperObj.state == "pose":
            "trapper_heart_pose"
            
        if trapperObj.emote == "heart" and trapperObj.state == "close":
            "trapper_heart_close"

        if trapperObj.emote == "stars" and trapperObj.state == "pose":
            "trapper_stars_pose"

        if trapperObj.emote == "stars" and trapperObj.state == "close":
            "trapper_stars_close"

        if trapperObj.emote == "question" and trapperObj.state == "pose":
            "trapper_question_pose"

        if trapperObj.emote == "question" and trapperObj.state == "close":
            "trapper_question_close"

        if trapperObj.emote == "anger" and trapperObj.state == "pose":
            "trapper_anger_pose"

        if trapperObj.emote == "anger" and trapperObj.state == "close":
            "trapper_anger_close"
            
        if trapperObj.emote == "brokenheart" and trapperObj.state == "pose":
            "trapper_brokenheart_pose"

        if trapperObj.emote == "brokenheart" and trapperObj.state == "close":
            "trapper_brokenheart_close"

        if trapperObj.emote == "dread" and trapperObj.state == "pose":
            "trapper_dread_pose"

        if trapperObj.emote == "dread" and trapperObj.state == "close":
            "trapper_dread_close"
            
        if trapperObj.emote == "exclamation" and trapperObj.state == "pose":
            "trapper_exclamation_pose"

        if trapperObj.emote == "exclamation" and trapperObj.state == "close":
            "trapper_exclamation_close"

        if trapperObj.emote == "lightbulb" and trapperObj.state == "pose":
            "trapper_lightbulb_pose"

        if trapperObj.emote == "lightbulb" and trapperObj.state == "close":
            "trapper_lightbulb_close"
            
        if trapperObj.emote == "spark" and trapperObj.state == "pose":
            "trapper_spark_pose"

        if trapperObj.emote == "spark" and trapperObj.state == "close":
            "trapper_spark_close"
            
        if trapperObj.emote == "sweat" and trapperObj.state == "pose":
            "trapper_sweat_pose"

        if trapperObj.emote == "sweat" and trapperObj.state == "close":
            "trapper_sweat_close"
            
        if trapperObj.emote == "thoughts" and trapperObj.state == "pose":
            "trapper_thoughts_pose"

        if trapperObj.emote == "thoughts" and trapperObj.state == "close":
            "trapper_thoughts_close"

    image trapper_blink:
        "[trapperObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[trapperObj.blinkFilename]"
        pause 0.1
        repeat

    image trapper_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image trapper_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image trapper_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image trapper_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image trapper_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image trapper_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image trapper_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image trapper_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image trapper_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image trapper_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image trapper_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image trapper_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image trapper_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image trapper_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image trapper_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image trapper_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image trapper_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image trapper_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image trapper_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image trapper_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image trapper_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image trapper_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300

    image trapper_blink:
        "[trapperObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[trapperObj.blinkFilename]"
        pause 0.1
        repeat

    image heartboom_trapper_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_trapper_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class TrapperClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.state = "pose"
            self.thong = False
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/trapper/trapper_" + self.pose + ".png"
            if self.emotion != "obsessed":
                self.emotionFilename = "images/sprites/trapper/trapper_" + self.pose + "_" + self.emotion + "_00.png"
                if self.emotion != "mad":
                    ## If NOT mad or obsessed
                    self.blinkFilename = "images/sprites/trapper/trapper_" + self.pose + "_" + self.emotion + "_01.png"
                else:
                    ## If mad, don't blink
                    self.blinkFilename = self.emotionFilename
            else:
                if self.pose == "close04" or self.pose == "pose04":
                    ## If obsessed and using close04/pose04
                    self.emotionFilename = "images/sprites/trapper/trapper_" + self.pose + "_" + self.emotion + "_00.png"
                    self.blinkFilename = "images/sprites/trapper/trapper_" + self.pose + "_" + self.emotion + "_01.png"
                else:
                    ## If NOT obsessed and using any pose
                    self.emotionFilename = "images/sprites/trapper/trapper_" + self.pose + "_happy_00.png"
                    self.blinkFilename = "images/sprites/trapper/trapper_" + self.pose + "_happy_01.png"
            if self.thong == True and self.pose == "pose04":
                ## If thong and using pose04
                self.emotionFilename = "images/sprites/trapper/trapper_thong_" + self.pose + "_" + self.emotion + "_00.png"
                self.blinkFilename = "images/sprites/trapper/trapper_thong_" + self.pose + "_" + self.emotion + "_01.png"

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "emote":
                self.emote = value
            elif attribute == "thong":
                self.emote = value
            self.resetFilenames()

##
## trapper #################################################################

## trapper dad #############################################################
## Pose attritubes: close01, close02, pose01, pose02
## Emotion attritubes: idle, mad, sad, scared, disgusted, happy
## Note: Only scared emotion doesn't blink
##

init:
    layeredimage dad:
        always:
            "[dadObj.poseFilename]"
        always:
            "dad_blink"
            
        if dadObj.emote == "heart" and dadObj.state == "pose":
            "dad_heart_pose"
            
        if dadObj.emote == "heart" and dadObj.state == "close":
            "dad_heart_close"

        if dadObj.emote == "stars" and dadObj.state == "pose":
            "dad_stars_pose"

        if dadObj.emote == "stars" and dadObj.state == "close":
            "dad_stars_close"

        if dadObj.emote == "question" and dadObj.state == "pose":
            "dad_question_pose"

        if dadObj.emote == "question" and dadObj.state == "close":
            "dad_question_close"

        if dadObj.emote == "anger" and dadObj.state == "pose":
            "dad_anger_pose"

        if dadObj.emote == "anger" and dadObj.state == "close":
            "dad_anger_close"
            
        if dadObj.emote == "brokenheart" and dadObj.state == "pose":
            "dad_brokenheart_pose"

        if dadObj.emote == "brokenheart" and dadObj.state == "close":
            "dad_brokenheart_close"

        if dadObj.emote == "dread" and dadObj.state == "pose":
            "dad_dread_pose"

        if dadObj.emote == "dread" and dadObj.state == "close":
            "dad_dread_close"
            
        if dadObj.emote == "exclamation" and dadObj.state == "pose":
            "dad_exclamation_pose"

        if dadObj.emote == "exclamation" and dadObj.state == "close":
            "dad_exclamation_close"

        if dadObj.emote == "lightbulb" and dadObj.state == "pose":
            "dad_lightbulb_pose"

        if dadObj.emote == "lightbulb" and dadObj.state == "close":
            "dad_lightbulb_close"
            
        if dadObj.emote == "spark" and dadObj.state == "pose":
            "dad_spark_pose"

        if dadObj.emote == "spark" and dadObj.state == "close":
            "dad_spark_close"
            
        if dadObj.emote == "sweat" and dadObj.state == "pose":
            "dad_sweat_pose"

        if dadObj.emote == "sweat" and dadObj.state == "close":
            "dad_sweat_close"
            
        if dadObj.emote == "thoughts" and dadObj.state == "pose":
            "dad_thoughts_pose"

        if dadObj.emote == "thoughts" and dadObj.state == "close":
            "dad_thoughts_close"

    image dad_blink:
        "[dadObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[dadObj.blinkFilename]"
        pause 0.1
        repeat

    image dad_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image dad_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image dad_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image dad_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image dad_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image dad_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image dad_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image dad_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image dad_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image dad_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image dad_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image dad_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image dad_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image dad_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image dad_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image dad_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image dad_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image dad_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image dad_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image dad_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image dad_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image dad_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300
    image dad_blink:
        "[dadObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[dadObj.blinkFilename]"
        pause 0.1
        repeat

    image heartboom_dad_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_dad_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class DadClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.state = "pose"
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/trapper_dad/trapper_dad_" + self.pose + ".png"
            self.emotionFilename = "images/sprites/trapper_dad/trapper_dad_" + self.pose + "_" + self.emotion + "_00.png"
            if self.emotion != "scared":
                self.blinkFilename = "images/sprites/trapper_dad/trapper_dad_" + self.pose + "_" + self.emotion + "_01.png"
            else:
                self.blinkFilename = self.emotionFilename

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "emote":
                self.emote = value
            self.resetFilenames()
##
## trapper dad #############################################################

## oni #####################################################################
## Pose attritubes: close01, close02, pose01, pose02
## Emotion attritubes: idle, mad, sad, disgusted, happy
## Note: Only idle emotion blinks
##

init:
    layeredimage oni:
        always:
            "[oniObj.poseFilename]"

        if oniObj.emotion == "idle":
            "oni_blink"
            
        if oniObj.emote == "heart" and oniObj.state == "pose":
            "oni_heart_pose"
            
        if oniObj.emote == "heart" and oniObj.state == "close":
            "oni_heart_close"

        if oniObj.emote == "stars" and oniObj.state == "pose":
            "oni_stars_pose"

        if oniObj.emote == "stars" and oniObj.state == "close":
            "oni_stars_close"

        if oniObj.emote == "question" and oniObj.state == "pose":
            "oni_question_pose"

        if oniObj.emote == "question" and oniObj.state == "close":
            "oni_question_close"

        if oniObj.emote == "anger" and oniObj.state == "pose":
            "oni_anger_pose"

        if oniObj.emote == "anger" and oniObj.state == "close":
            "oni_anger_close"
            
        if oniObj.emote == "brokenheart" and oniObj.state == "pose":
            "oni_brokenheart_pose"

        if oniObj.emote == "brokenheart" and oniObj.state == "close":
            "oni_brokenheart_close"

        if oniObj.emote == "dread" and oniObj.state == "pose":
            "oni_dread_pose"

        if oniObj.emote == "dread" and oniObj.state == "close":
            "oni_dread_close"
            
        if oniObj.emote == "exclamation" and oniObj.state == "pose":
            "oni_exclamation_pose"

        if oniObj.emote == "exclamation" and oniObj.state == "close":
            "oni_exclamation_close"

        if oniObj.emote == "lightbulb" and oniObj.state == "pose":
            "oni_lightbulb_pose"

        if oniObj.emote == "lightbulb" and oniObj.state == "close":
            "oni_lightbulb_close"
            
        if oniObj.emote == "spark" and oniObj.state == "pose":
            "oni_spark_pose"

        if oniObj.emote == "spark" and oniObj.state == "close":
            "oni_spark_close"
            
        if oniObj.emote == "sweat" and oniObj.state == "pose":
            "oni_sweat_pose"

        if oniObj.emote == "sweat" and oniObj.state == "close":
            "oni_sweat_close"
            
        if oniObj.emote == "thoughts" and oniObj.state == "pose":
            "oni_thoughts_pose"

        if oniObj.emote == "thoughts" and oniObj.state == "close":
            "oni_thoughts_close"

    image oni_blink:
        "[oniObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[oniObj.blinkFilename]"
        pause 0.1
        repeat

    image oni_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image oni_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image oni_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image oni_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image oni_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image oni_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image oni_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image oni_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image oni_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image oni_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image oni_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image oni_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image oni_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image oni_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image oni_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image oni_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image oni_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image oni_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image oni_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image oni_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image oni_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image oni_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300
    image oni_blink:
        "[oniObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[oniObj.blinkFilename]"
        pause 0.1
        repeat

    image heartboom_oni_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_oni_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class OniClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.state = "pose"
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/oni/oni_" + self.pose + ".png"
            self.emotionFilename = "images/sprites/oni/oni_" + self.pose + "_" + self.emotion + "_00.png"
            if self.emotion == "idle":
                self.blinkFilename = "images/sprites/oni/oni_" + self.pose + "_" + self.emotion + "_01.png"
            else:
                self.blinkFilename = self.emotionFilename

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "emote":
                self.emote = value
            self.resetFilenames()
##
## oni #####################################################################

## trickster ###############################################################
## Pose attritubes: close01, close02, pose01, pose02
## Emotion attritubes: idle, mad, sad, scared, disgusted, happy
##

init:
    layeredimage trickster:
        always:
            "[tricksterObj.poseFilename]"
        always:
            "trickster_blink"
            
        if tricksterObj.emote == "heart" and tricksterObj.state == "pose":
            "trickster_heart_pose"
            
        if tricksterObj.emote == "heart" and tricksterObj.state == "close":
            "trickster_heart_close"

        if tricksterObj.emote == "stars" and tricksterObj.state == "pose":
            "trickster_stars_pose"

        if tricksterObj.emote == "stars" and tricksterObj.state == "close":
            "trickster_stars_close"

        if tricksterObj.emote == "question" and tricksterObj.state == "pose":
            "trickster_question_pose"

        if tricksterObj.emote == "question" and tricksterObj.state == "close":
            "trickster_question_close"

        if tricksterObj.emote == "anger" and tricksterObj.state == "pose":
            "trickster_anger_pose"

        if tricksterObj.emote == "anger" and tricksterObj.state == "close":
            "trickster_anger_close"
            
        if tricksterObj.emote == "brokenheart" and tricksterObj.state == "pose":
            "trickster_brokenheart_pose"

        if tricksterObj.emote == "brokenheart" and tricksterObj.state == "close":
            "trickster_brokenheart_close"

        if tricksterObj.emote == "dread" and tricksterObj.state == "pose":
            "trickster_dread_pose"

        if tricksterObj.emote == "dread" and tricksterObj.state == "close":
            "trickster_dread_close"
            
        if tricksterObj.emote == "exclamation" and tricksterObj.state == "pose":
            "trickster_exclamation_pose"

        if tricksterObj.emote == "exclamation" and tricksterObj.state == "close":
            "trickster_exclamation_close"

        if tricksterObj.emote == "lightbulb" and tricksterObj.state == "pose":
            "trickster_lightbulb_pose"

        if tricksterObj.emote == "lightbulb" and tricksterObj.state == "close":
            "trickster_lightbulb_close"
            
        if tricksterObj.emote == "spark" and tricksterObj.state == "pose":
            "trickster_spark_pose"

        if tricksterObj.emote == "spark" and tricksterObj.state == "close":
            "trickster_spark_close"
            
        if tricksterObj.emote == "sweat" and tricksterObj.state == "pose":
            "trickster_sweat_pose"

        if tricksterObj.emote == "sweat" and tricksterObj.state == "close":
            "trickster_sweat_close"
            
        if tricksterObj.emote == "thoughts" and tricksterObj.state == "pose":
            "trickster_thoughts_pose"

        if tricksterObj.emote == "thoughts" and tricksterObj.state == "close":
            "trickster_thoughts_close"

    image trickster_blink:
        "[tricksterObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[tricksterObj.blinkFilename]"
        pause 0.1
        repeat

    image trickster_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image trickster_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image trickster_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image trickster_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image trickster_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image trickster_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image trickster_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image trickster_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image trickster_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image trickster_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image trickster_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image trickster_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image trickster_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image trickster_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image trickster_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image trickster_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image trickster_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image trickster_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image trickster_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image trickster_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image trickster_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image trickster_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300
    image trickster_blink:
        "[tricksterObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[tricksterObj.blinkFilename]"
        pause 0.1
        repeat

    image heartboom_trickster_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_trickster_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class TricksterClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.state = "pose"
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/trickster/trickster_" + self.pose + ".png"
            self.emotionFilename = "images/sprites/trickster/trickster_" + self.pose + "_" + self.emotion + "_00.png"
            self.blinkFilename = "images/sprites/trickster/trickster_" + self.pose + "_" + self.emotion + "_01.png"

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "emote":
                self.emote = value
            self.resetFilenames()
##
## trickster ###############################################################

## wraith ##################################################################
## Pose attritubes: close01, close02, close03, close04, pose01, pose02, pose03, pose04
## Emotion attritubes: idle, mad, sad, scared, disgusted, happy, obsessed
## Shirtless: True, False
## Notes: Only pose04 and close04 has obsessed sprites
##

init:
    layeredimage wraith:
        always:
            "[wraithObj.poseFilename]"
        always:
            "wraith_blink"
            
        if wraithObj.emote == "heart" and wraithObj.state == "pose":
            "wraith_heart_pose"
            
        if wraithObj.emote == "heart" and wraithObj.state == "close":
            "wraith_heart_close"

        if wraithObj.emote == "stars" and wraithObj.state == "pose":
            "wraith_stars_pose"

        if wraithObj.emote == "stars" and wraithObj.state == "close":
            "wraith_stars_close"

        if wraithObj.emote == "question" and wraithObj.state == "pose":
            "wraith_question_pose"

        if wraithObj.emote == "question" and wraithObj.state == "close":
            "wraith_question_close"

        if wraithObj.emote == "anger" and wraithObj.state == "pose":
            "wraith_anger_pose"

        if wraithObj.emote == "anger" and wraithObj.state == "close":
            "wraith_anger_close"
            
        if wraithObj.emote == "brokenheart" and wraithObj.state == "pose":
            "wraith_brokenheart_pose"

        if wraithObj.emote == "brokenheart" and wraithObj.state == "close":
            "wraith_brokenheart_close"

        if wraithObj.emote == "dread" and wraithObj.state == "pose":
            "wraith_dread_pose"

        if wraithObj.emote == "dread" and wraithObj.state == "close":
            "wraith_dread_close"
            
        if wraithObj.emote == "exclamation" and wraithObj.state == "pose":
            "wraith_exclamation_pose"

        if wraithObj.emote == "exclamation" and wraithObj.state == "close":
            "wraith_exclamation_close"

        if wraithObj.emote == "lightbulb" and wraithObj.state == "pose":
            "wraith_lightbulb_pose"

        if wraithObj.emote == "lightbulb" and wraithObj.state == "close":
            "wraith_lightbulb_close"
            
        if wraithObj.emote == "spark" and wraithObj.state == "pose":
            "wraith_spark_pose"

        if wraithObj.emote == "spark" and wraithObj.state == "close":
            "wraith_spark_close"
            
        if wraithObj.emote == "sweat" and wraithObj.state == "pose":
            "wraith_sweat_pose"

        if wraithObj.emote == "sweat" and wraithObj.state == "close":
            "wraith_sweat_close"
            
        if wraithObj.emote == "thoughts" and wraithObj.state == "pose":
            "wraith_thoughts_pose"

        if wraithObj.emote == "thoughts" and wraithObj.state == "close":
            "wraith_thoughts_close"

    image wraith_blink:
        "[wraithObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[wraithObj.blinkFilename]"
        pause 0.1
        repeat

    image wraith_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image wraith_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image wraith_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image wraith_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image wraith_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image wraith_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image wraith_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image wraith_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image wraith_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image wraith_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image wraith_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image wraith_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image wraith_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image wraith_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image wraith_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image wraith_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image wraith_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image wraith_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image wraith_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image wraith_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image wraith_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image wraith_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300
    image wraith_blink:
        "[wraithObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[wraithObj.blinkFilename]"
        pause 0.1
        repeat

    image heartboom_wraith_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_wraith_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class WraithClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.state = "pose"
            self.shirtless = False
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/wraith/wraith_" + self.pose + ".png"
            if self.emotion != "obsessed":
                self.emotionFilename = "images/sprites/wraith/wraith_" + self.pose + "_" + self.emotion + "_00.png"
                self.blinkFilename = "images/sprites/wraith/wraith_" + self.pose + "_" + self.emotion + "_01.png"
            else:
                if self.pose == "close04" or self.pose == "pose04":
                    ## If obsessed and using close04/pose04
                    self.emotionFilename = "images/sprites/wraith/wraith_" + self.pose + "_" + self.emotion + "_00.png"
                    self.blinkFilename = "images/sprites/wraith/wraith_" + self.pose + "_" + self.emotion + "_01.png"
                else:
                    ## If NOT obsessed and using any pose
                    self.emotionFilename = "images/sprites/wraith/wraith_" + self.pose + "_happy_00.png"
                    self.blinkFilename = "images/sprites/wraith/wraith_" + self.pose + "_happy_01.png"
            if self.shirtless == True and self.pose == "pose04":
                ## If shirtless and using pose04
                self.emotionFilename = "images/sprites/wraith/wraith_shirtless_" + self.pose + "_" + self.emotion + "_00.png"
                self.blinkFilename = "images/sprites/wraith/wraith_shirtless_" + self.pose + "_" + self.emotion + "_01.png"

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emotion":
                self.emotion = value
            elif attribute == "emote":
                self.emote = value
            elif attribute == "shirtless":
                self.emote = value
            self.resetFilenames()

##
## wraith ##################################################################

## Entity ##################################################################
## Pose attritubes: close01, pose01, mad
##

init:
    layeredimage entity:
        always:
            "[entityObj.poseFilename]"
            
        if entityObj.emote == "heart" and entityObj.state == "pose":
            "entity_heart_pose"
            
        if entityObj.emote == "heart" and entityObj.state == "close":
            "entity_heart_close"

        if entityObj.emote == "stars" and entityObj.state == "pose":
            "entity_stars_pose"

        if entityObj.emote == "stars" and entityObj.state == "close":
            "entity_stars_close"

        if entityObj.emote == "question" and entityObj.state == "pose":
            "entity_question_pose"

        if entityObj.emote == "question" and entityObj.state == "close":
            "entity_question_close"

        if entityObj.emote == "anger" and entityObj.state == "pose":
            "entity_anger_pose"

        if entityObj.emote == "anger" and entityObj.state == "close":
            "entity_anger_close"
            
        if entityObj.emote == "brokenheart" and entityObj.state == "pose":
            "entity_brokenheart_pose"

        if entityObj.emote == "brokenheart" and entityObj.state == "close":
            "entity_brokenheart_close"

        if entityObj.emote == "dread" and entityObj.state == "pose":
            "entity_dread_pose"

        if entityObj.emote == "dread" and entityObj.state == "close":
            "entity_dread_close"
            
        if entityObj.emote == "exclamation" and entityObj.state == "pose":
            "entity_exclamation_pose"

        if entityObj.emote == "exclamation" and entityObj.state == "close":
            "entity_exclamation_close"

        if entityObj.emote == "lightbulb" and entityObj.state == "pose":
            "entity_lightbulb_pose"

        if entityObj.emote == "lightbulb" and entityObj.state == "close":
            "entity_lightbulb_close"
            
        if entityObj.emote == "spark" and entityObj.state == "pose":
            "entity_spark_pose"

        if entityObj.emote == "spark" and entityObj.state == "close":
            "entity_spark_close"
            
        if entityObj.emote == "sweat" and entityObj.state == "pose":
            "entity_sweat_pose"

        if entityObj.emote == "sweat" and entityObj.state == "close":
            "entity_sweat_close"
            
        if entityObj.emote == "thoughts" and entityObj.state == "pose":
            "entity_thoughts_pose"

        if entityObj.emote == "thoughts" and entityObj.state == "close":
            "entity_thoughts_close"

    image entity_blink:
        "[entityObj.emotionFilename]"
        choice:
            pause 3
        choice:
            pause 4
        choice:
            pause 5
        "[entityObj.blinkFilename]"
        pause 0.1
        repeat

    image entity_heart_close:
        "heart_close"
        xoffset 250
        yoffset -300

    image entity_heart_pose:
        "heart_pose"
        xoffset 250
        yoffset -300

    image entity_stars_close:
        "stars_close"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image entity_stars_pose:
        "stars_pose"
        xoffset 250
        yoffset -300
        pause 3
        easeout 1.0 alpha 0.0

    image entity_question_close:
        "question_close"
        xoffset 250
        yoffset -300

    image entity_question_pose:
        "question_pose"
        xoffset 250
        yoffset -300

    image entity_anger_close:
        "anger_close"
        xoffset 250
        yoffset -300

    image entity_anger_pose:
        "anger_pose"
        xoffset 250
        yoffset -300

    image entity_heartbroken_close:
        "heartbroken_close"
        xoffset 250
        yoffset -300

    image entity_heartbroken_pose:
        "heartbroken_pose"
        xoffset 250
        yoffset -300

    image entity_spark_close:
        "spark_close"
        xoffset 250
        yoffset -300

    image entity_spark_pose:
        "spark_pose"
        xoffset 250
        yoffset -300

    image entity_dread_close:
        "dread_close"
        xoffset 250
        yoffset -300

    image entity_dread_pose:
        "dread_pose"
        xoffset 250
        yoffset -300

    image entity_exclamation_close:
        "exclamation_close"
        xoffset 250
        yoffset -300

    image entity_exclamation_pose:
        "exclamation_pose"
        xoffset 250
        yoffset -300

    image entity_lightbulb_close:
        "lightbulb_close"
        xoffset 250
        yoffset -300

    image entity_lightbulb_pose:
        "lightbulb_pose"
        xoffset 250
        yoffset -300

    image entity_sweat_close:
        "sweat_close"
        xoffset 250
        yoffset -300

    image entity_sweat_pose:
        "sweat_pose"
        xoffset 250
        yoffset -300

    image entity_thoughts_close:
        "thoughts_close"
        xoffset 250
        yoffset -300

    image entity_thoughts_pose:
        "thoughts_pose"
        xoffset 250
        yoffset -300
    image heartboom_entity_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_entity_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_pose"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class EntityClass:
        def __init__(self):
            self.pose = "pose01"
            self.emote = "none"
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/entity/entity_" + self.pose + ".png"

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
                States = {
                    "close01": "close",
                    "close02": "close",
                    "close03": "close",
                    "close04": "close",
                    "pose01": "pose",
                    "pose02": "pose",
                    "pose03": "pose",
                    "pose04": "pose",
                    "far01": "pose",
                    "far02": "pose",
                    "mad": "pose"
                    }
                self.state = States.get(value)
            elif attribute == "emote":
                self.emote = value
            self.resetFilenames()
##
## Entity ##################################################################