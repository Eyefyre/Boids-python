import pygame
from pygame import *
import numpy
import random
from Vector import Vector

class Boid:
    def __init__(self,x,y,colour,surface,radius):
        self.position = Vector(x,y)
        self.velocity = Vector(random.uniform(-1,1),random.uniform(-1,1))
        self.velocity.setMagnitude(random.choice([2,3,4]))
        self.acceleration = Vector(0,0) 
        self.colour = colour
        self.surface = surface
        self.radius = radius
        self.perception = 100
        self.maxForce = 1
        self.SEPARATION_FORCE = 1
        self.COHESION_FORCE = 1
        self.ALIGNMENT_FORCE = 1
        self.maxSpeed = 4


    def draw(self):
        pygame.draw.circle(self.surface,self.colour,(self.position.x,self.position.y),self.radius)

    def update(self):
        self.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.velocity.limitMag(self.maxSpeed)
        self.acceleration.scale(0)

    def edges(self):
        if self.position.x < 0 - self.radius:
            self.position.x = 800 + self.radius
        elif self.position.x > 800 + self.radius:
            self.position.x = 0 - self.radius
        if self.position.y < 0 - self.radius:
            self.position.y = 800 + self.radius
        elif self.position.y > 800 + self.radius:
            self.position.y = 0 - self.radius

    def align(self,boids):
        average = Vector(0,0)
        total = 0
        for boid in boids:
            if self != boid and self.position.dist(boid.position) < self.perception:
                average.add(boid.velocity)
                total += 1
        if total > 0:
            average.div(total)
            average.setMagnitude(self.maxSpeed)
            average.subtract(self.velocity)
            average.limitMag(self.maxForce)
        return average

    def cohesion(self,boids):
        average = Vector(0,0)
        total = 0
        for boid in boids:
            if self != boid and self.position.dist(boid.position) < self.perception + 50:
                average.add(boid.position)
                total += 1
        if total > 0:
            average.div(total)
            average.subtract(self.position)
            average.setMagnitude(self.maxSpeed)
            average.subtract(self.velocity)
            average.limitMag(self.maxForce)
        return average

    def separation(self, boids):
        average = Vector(0,0)
        total = 0
        for boid in boids:
            dist = self.position.dist(boid.position)
            if self != boid and dist < self.perception:
                difference = Vector.sub(self.position,boid.position)
                if(dist > 0):
                    difference.div(dist * dist)
                average.add(difference)
                total += 1
        if total > 0:
            average.div(total)
            average.setMagnitude(self.maxSpeed)
            average.subtract(self.velocity)
            average.limitMag(self.maxForce)
        return average

    def flock(self,boids):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)
        alignment.scale(self.ALIGNMENT_FORCE)
        cohesion.scale(self.COHESION_FORCE)
        separation.scale(self.SEPARATION_FORCE)
        self.acceleration.add(alignment)
        self.acceleration.add(cohesion)
        self.acceleration.add(separation)
