init: 
    transform defaultrotate:
        linear 4.0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        repeat
    transform zrotate:
        linear 4.0 matrixtransform RotateMatrix(0.0, 0.0, 360.0)
        repeat

    transform yrotate:
        linear 4.0 matrixtransform RotateMatrix(0.0, 360.0, 0.0)
        repeat

    transform yzrotate:
        linear 4.0 matrixtransform RotateMatrix(0.0, 360.0, 360.0)
        repeat

    transform xrotate:
        linear 4.0 matrixtransform RotateMatrix(360.0, 0.0, 0.0)
        repeat

    transform zxrotate:
        linear 4.0 matrixtransform RotateMatrix(360.0, 0.0, 360.0)
        repeat

    transform xyrotate:
        linear 4.0 matrixtransform RotateMatrix(360.0, 360.0, 0.0)
        repeat

    transform xyzrotate:
        linear 4.0 matrixtransform RotateMatrix(360.0, 360.0, 360.0)
        repeat


    image petal:
        choice:
            pause 1
        choice:
            At("images/petal.png", defaultrotate)
        choice:
            At("images/petal.png", zrotate)
        choice:
            At("images/petal.png", yrotate)
        choice:
            At("images/petal.png", yzrotate)
        choice:
            At("images/petal.png", xrotate)
        choice:
            At("images/petal.png", zxrotate)
        choice:
            At("images/petal.png", xyrotate)
        choice:
            At("images/petal.png", xyzrotate)
        pause 1
        repeat

    image petals = SnowBlossom("petal", count=200, border=60, xspeed=(-40, -20), yspeed=(20, 40), start=1.5, fast=False, horizontal=True)



init python:
    import math
    import random
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
    class Shaker(object):
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
        
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                    time,
                    child,
                    add_sizes=True,
                    **properties)

    Shake = renpy.curry(_Shake)
