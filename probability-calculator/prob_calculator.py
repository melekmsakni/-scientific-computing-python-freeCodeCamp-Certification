import random
import copy 
class Hat:
    def __init__(self,**ty):
        self.contents=[]
        #from dic to list(conversion)
        for k,v in ty.items():
            c=[k]*v
            self.contents=self.contents+c
            
    def draw(self,numberBalls):
        #if number of balls drawn are more than the existing          ball so we take all the ball's hat
        
        if (numberBalls>=len(self.contents)):
          numberBalls=len(self.contents)
        else:
          numberBalls=numberBalls
          
        ballsDraw=[]
        #get random balls , delete them and return the balls 
        #drawn
        for i in range(numberBalls):
            
            randBall=random.randint(0, len(self.contents)-1)
            
            x=self.contents.pop(randBall)
            ballsDraw.append(x)
            
        return ballsDraw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    success=0
    for i in range(num_experiments):
        #using the draw function we will get some random balls
        hatCopy=copy.deepcopy(hat)
        ballDraw=hatCopy.draw(num_balls_drawn)
        count=0
        #checking if the draw-balls are the same as  expected              balls in an experiment
        for color in expected_balls.keys():
            if ballDraw.count(color)>= expected_balls[color]:
                count=count+1
        #if all the drawn balls are like the expected then we         add one  succed
        if count== len(expected_balls):
            success= success+1
    
    return success/ num_experiments
            

                