import turtle

screen = turtle.Screen()
screen.bgcolor("white")

smile = turtle.Turtle()
smile.speed(3)

smile.penup()
smile.goto(0, -100)  
smile.pendown()
smile.begin_fill()
smile.color("yellow")
smile.circle(100)  
smile.end_fill()

smile.penup()
smile.goto(-35, 35)
smile.pendown()
smile.begin_fill()
smile.color("black")
smile.circle(15) 
smile.end_fill()

smile.penup()
smile.goto(35, 35)
smile.pendown()
smile.begin_fill()
smile.color("black")
smile.circle(15)
smile.end_fill()

smile.penup()
smile.goto(-60, -10)
smile.pendown()
smile.setheading(-60)  
smile.circle(60, 120)  

smile.hideturtle()
turtle.done()