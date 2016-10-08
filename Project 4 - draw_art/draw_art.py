"""
This program is abour drawing something 
on the window.

I utilized the turtle module whicj can be installed by running:

$ pip installed turtle


"""


import turtle

def draw_piece_of_art(some_turtle):
	for i in range(1, 4):
		some_turtle.forward(100)  # steps
		some_turtle.right(100)  # degrees

def draw_art():
	window = turtle.Screen()
	window.bgcolor("black")

	# create the turtle myturtle - draws a piece of art
	myturtle = turtle.Turtle()
	myturtle.shape("turtle")
	myturtle.color("white")
	myturtle.speed("fast") # slow, fast, very fast

	# draw that piece of art 36 times, moving 10 degrees to the right each pass
	for i in range(1, 37):
		draw_piece_of_art(myturtle)
		myturtle.right(10)	# degrees

	window.exitonclick()

draw_art()