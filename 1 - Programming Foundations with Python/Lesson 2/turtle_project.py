import turtle

def draw_triangle(some_turtle):
	some_turtle.forward(50)
	for i in range(2):
		some_turtle.right(120)
		some_turtle.forward(100)		
	some_turtle.right(120)
	some_turtle.forward(50)

def draw_art():
	window = turtle.Screen()

	# Create the turtle Brad - Draw a square
	wewe = turtle.Turtle()
	wewe.shape("turtle")
	wewe.color("indigo")
	wewe.speed(4)
	for i in range(36):
		draw_triangle(wewe)
		wewe.right(10)

	window.exitonclick()

draw_art()