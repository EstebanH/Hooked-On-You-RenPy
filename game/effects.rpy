
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
        def __init__(self, theDisplayable, explodeTime=0, numParticles=20, particleTime = 0.500, particleXSpeed = 5, particleYSpeed = 5, centerZone = 0, xZone = 10, yZone = 10):
            self.sm = SpriteManager(update=self.update)
            # A list of (sprite, starting-x, speed).
            self.stars = [ ]
            self.displayable = theDisplayable
            self.centerZone = centerZone
            self.xZone = xZone
            self.yZone = yZone
            self.explodeTime = explodeTime
            self.particleMax = numParticles
            self.particleTime = particleTime
            self.particleXSpeed = particleXSpeed
            self.particleYSpeed = particleYSpeed
            self.timePassed = 0
           
        def add(self, d, speed, st):
            s = self.sm.create(d)
            if (self.centerZone == 0):
                s.x = self.sm.width/2 - (random.random()*self.xZone)
                s.y = self.sm.height/2 - (random.random()*self.yZone)
            else:
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
