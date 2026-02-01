from turtle import *
import random
forward(-100)

for k in range(4):
        
        for j in range(5):
                forward(120)
                
                for x in range(25):
                        forward(10+random.randint(2,5))
                        left(10)

        for j in range(5):
                forward(300+random.randint(100,200))
                left(72)
                
