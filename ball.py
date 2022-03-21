from turtle import Turtle, width

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.5
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x_l_paddle(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 1.3
 
    def bounce_x_r_paddle(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 1.3
    
    def reset_position_rloses(self):
        self.goto(0,0) 
        self.move_speed = 0.1
        self.bounce_x_r_paddle()

    def reset_position_lloses(self):
        self.goto(0,0) 
        self.move_speed = 0.1
        self.bounce_x_l_paddle()

