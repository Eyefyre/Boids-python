import math
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self, vec2):
        self.x += vec2.x
        self.y += vec2.y

    def subtract(self, vec2):
        self.x -= vec2.x
        self.y -= vec2.y

    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def setVector(self,x,y):
        self.x = x
        self.y = y

    def getMagnitude(self):
        ax = self.x * self.x
        bx = self.y * self.y
        d = ax + bx
        return math.sqrt(d)

    def negate(self):
        self.x *= -1
        self.y *= -1

    def normalise(self):
        m = self.getMagnitude()
        if m > 0:
            self.x /= m
            self.y /= m

    def dist(self, vec2):
        d = (self.x - vec2.x) * (self.x - vec2.x)
        e = (self.y - vec2.y) * (self.y - vec2.y)
        f = d + e
        return math.sqrt(f)
    
    def getAngleRadians(self):
        return math.atan(self.y/self.x)

    def getAngleDegrees(self):
        return math.degrees(math.atan(self.y/self.x))

    def div(self, div):
        self.x /= div
        self.y /= div 

    def setMagnitude(self, len):
        self.normalise()
        self.scale(len)

    def limitMag(self, max):
        mSq = self.getMagnitude() * self.getMagnitude()
        if mSq > (max * max):
            self.setMagnitude(max)

    @staticmethod
    def sub(vec1,vec2):
        vec = Vector(vec1.x - vec2.x,vec1.y-vec2.y)
        return vec

