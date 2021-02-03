  #   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:

i = 0
while (i < 1): 
  move()
  turn_left()
  turn_left()
  turn_left()
  move()
  i += 1 
  while (i < 6):
    turn_left()
    i += 1
  while (i < 7):
    move()
    i += 1

while (i < 10):
  turn_left()
  i += 1

while (i < 11):
  move()
  i += 1

while (i < 12):
  robot.color("#2eae5b")
  robot.pencolor("#2eae5b")
  turn_left()
  i += 1
while (i < 13):
  move()    
  i += 1

while (i < 16):
  turn_left()    
  i += 1

while ( i < 17):
  move()
  i += 1

while (i < 18):
  turn_left()    
  i += 1

while (i < 19):
  move()    
  i += 1

while (i < 22):
  turn_left()    
  i += 1

while (i < 23):
  move()    
  i += 1

#---- end robot movement 

wn.mainloop()
