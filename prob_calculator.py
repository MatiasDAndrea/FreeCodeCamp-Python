#####################################################################
#
#   Class : Hat
#       methods: draw(number of drawn balls)
#           This method should remove balls at random from contents
#  
#   function: experiment (
#       hat: Object
#       expected_balls: Dictionary
#       num_balls_drawn: Number of balls to draw
#       num_experiments: Number of experimets to realize
#   )
#   Calculates the probability of drawing an expected set of balls
#   from the hat in N iterations (experimets)
#
######################################################################

from random import *

class Hat:

    def __init__(self,**kwargs):
        
        self.balls   = kwargs
        self.content = [key for key in kwargs]

    def __str__(self):
        
        return "Hat Probability Experiment"

    def draw(self,ball_num):

        balls_drawn  = {}
        balls_copy   = self.balls.copy()
        content_copy = self.content[:]

        max_ball = sum([balls_copy[key] for key in balls_copy])
        
        if ball_num > max_ball:
            return {}

        for x in range(ball_num):
            
            ball_colour = content_copy[randint(0,len(content_copy)-1)]
            balls_copy[ball_colour] -= 1
            
            if self.balls[ball_colour] == 0:

                content_copy.remove(ball_colour)

            
            number = balls_drawn.get(ball_colour,0)
            number += 1

            balls_drawn[ball_colour] = number

        return balls_drawn

def experiment(**kwargs):

    hat             = kwargs.get("hat",False)
    expected_balls  = kwargs.get("expected_balls",False)
    num_balls_drawn = kwargs.get("num_balls_drawn",False)
    num_experiments = kwargs.get("num_experiments",False)

    experiment_result = 0

    if all([hat,expected_balls,num_balls_drawn,num_experiments]):

        for x in range(num_experiments):
            bool_list = []
            for key in expected_balls:

                expected_ball = expected_balls.get(key,0)
                actual_ball   = hat.draw(num_balls_drawn).get(key,0)

                bool_list.append(True) if expected_ball<=actual_ball else bool_list.append(False)

            experiment_result +=1 if all(bool_list) else False
        
        return experiment_result/num_experiments
    
    else:
        return False


########
# Tests.
hat = Hat(yellow=3, blue=2, green=6)
print(experiment(hat=hat,expected_balls={"yellow":1,"green":1},num_balls_drawn=5,num_experiments=2000))