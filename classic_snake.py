# A throw back classic Snake game
# Rules everytime your snake eats something it gets bigger
# Game ends if the snake touches the sides of the screen
# or if it touches its own tail.
# Have Fun!

import turtle
import time 

delay = 0.1 

# Set up the screen

wn = turtle.Screen()
wn.title("Snake Game by jramuldrow")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) # this turns off screen updates 


# Snake head
head = turtle.Turtle() #this creates the turtle object
head.speed(0)
head.shape("square")
head.color("black")
head.penup()    #we are not drwaing so we dont need the pen
head.goto(0,0)   #start in the middle of the screen
head.direction = "stop"


# Snake Food
food = turtle.Turtle() #this creates the turtle object
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()    
food.goto(0,100)  


# Functions
def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"
    
def go_left():
    head.direction = "left"
    
def go_right():
    head.direction = "right"




def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20) 
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20) 
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    
     
# Keyboard bindings 

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
        


# Main game loop
while True:
    wn.update()
    
    move()
    
    time.sleep(delay)









wn.mainloop()
