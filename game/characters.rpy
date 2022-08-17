## Character Emotes ###############################################################

init:
    image heartboom_far:
        function play_effect
        zoom 0.15
        (ParticleBurst("images/emotes/heart.png", explodeTime=0, numParticles=10, particleTime=20.0, particleXSpeed = 20, particleYSpeed = 15, centerZone = 1000, fadeWithParticleTime = True).sm) with Dissolve

    image heartboom_close:
        function play_effect
        zoom 0.25
        (ParticleBurst("images/emotes/heart.png", explodeTime=0, numParticles=10, particleTime=20.0, particleXSpeed = 20, particleYSpeed = 15, centerZone = 1000, fadeWithParticleTime = True).sm) with Dissolve

init python:
    def play_effect(trans, st, at):
        renpy.play("sounds/SFX_Emotes_Hearts_V01.ogg", channel="sound")

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
            
        if grandmaObj.emote == "heart" and grandmaObj.pose == "pose01":
            "heartboom_grandma_pose01"
            
        if grandmaObj.emote == "heart" and grandmaObj.pose == "close01":
            "heartboom_grandma_close01"
        
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
        "heartboom_far"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class GrandmaClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/grandma/wraith_grandma_" + self.pose + ".png"
            self.emotionFilename = "images/sprites/grandma/wraith_grandma_" + self.pose + "_" + self.emotion + "_00.png"
            self.blinkFilename = "images/sprites/grandma/wraith_grandma_" + self.pose + "_" + self.emotion + "_01.png"

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
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
            
        if huntressObj.emote == "heart" and huntressObj.pose == "pose01":
            "heartboom_huntress_pose01"
            
        if huntressObj.emote == "heart" and huntressObj.pose == "close01":
            "heartboom_huntress_close01"
        
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

    image heartboom_huntress_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_huntress_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_far"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class HuntressClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
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
            
        if momObj.emote == "heart" and momObj.pose == "pose01":
            "heartboom_mom_pose01"
            
        if momObj.emote == "heart" and momObj.pose == "close01":
            "heartboom_mom_close01"
        
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
        "heartboom_far"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class MomClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/huntress_mom/huntress_mom_" + self.pose + ".png"
            self.emotionFilename = "images/sprites/huntress_mom/huntress_mom_" + self.pose + "_" + self.emotion + "_00.png"
            self.blinkFilename = "images/sprites/huntress_mom/huntress_mom_" + self.pose + "_" + self.emotion + "_01.png"

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
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
            
        if spiritObj.emote == "heart" and spiritObj.pose == "pose01":
            "heartboom_spirit_pose01"
            
        if spiritObj.emote == "heart" and spiritObj.pose == "close01":
            "heartboom_spirit_close01"
        
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
        "heartboom_far"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class SpiritClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
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
            
        if trapperObj.emote == "heart" and trapperObj.pose == "pose01":
            "heartboom_trapper_pose01"
            
        if trapperObj.emote == "heart" and trapperObj.pose == "close01":
            "heartboom_trapper_close01"
        
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
        "heartboom_far"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class TrapperClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
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
            
        if dadObj.emote == "heart" and dadObj.pose == "pose01":
            "heartboom_dad_pose01"
            
        if dadObj.emote == "heart" and dadObj.pose == "close01":
            "heartboom_dad_close01"
        
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
        "heartboom_far"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class DadClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
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
            
        if oniObj.emote == "heart" and oniObj.pose == "pose01":
            "heartboom_oni_pose01"
            
        if oniObj.emote == "heart" and oniObj.pose == "close01":
            "heartboom_oni_close01"
        
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
        "heartboom_far"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class OniClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
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
            
        if tricksterObj.emote == "heart" and tricksterObj.pose == "pose01":
            "heartboom_trickster_pose01"
            
        if tricksterObj.emote == "heart" and tricksterObj.pose == "close01":
            "heartboom_trickster_close01"
        
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
        "heartboom_far"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class TricksterClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
            self.resetFilenames()
            
        def resetFilenames(self):
            self.poseFilename = "images/sprites/trickster/trickster_" + self.pose + ".png"
            self.emotionFilename = "images/sprites/trickster/trickster_" + self.pose + "_" + self.emotion + "_00.png"
            self.blinkFilename = "images/sprites/trickster/trickster_" + self.pose + "_" + self.emotion + "_01.png"

        def change(self, attribute, value):
            if attribute == "pose":
                self.pose = value
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
            
        if wraithObj.emote == "heart" and wraithObj.pose == "pose01":
            "heartboom_wraith_pose01"
            
        if wraithObj.emote == "heart" and wraithObj.pose == "close01":
            "heartboom_wraith_close01"
        
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
        "heartboom_far"
        pause 1
        easeout 0.5 alpha 0.0

init python:
    class WraithClass:
        def __init__(self):
            self.pose = "pose01"
            self.emotion = "idle"
            self.emote = "none"
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
            
        if entityObj.emote == "heart" and entityObj.pose == "pose01":
            "heartboom_entity_pose01"
            
        if entityObj.emote == "heart" and entityObj.pose == "close01":
            "heartboom_entity_close01"

    image heartboom_entity_close01:
        xalign 0.5
        yalign 0.1
        "heartboom_close"
        pause 1
        easeout 0.5 alpha 0.0

    image heartboom_entity_pose01:
        xalign 0.5
        yalign 0.05
        "heartboom_far"
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
            elif attribute == "emote":
                self.emote = value
            self.resetFilenames()
##
## Entity ##################################################################