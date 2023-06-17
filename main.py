import turtle
from random import randint, random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Where is my Turtle!?")
turtle_screen.setup(800, 600)
score_pen = turtle.Turtle()
timerr = turtle.Turtle()
timerr.hideturtle()

jack = turtle.Turtle()
jack.shapesize(2)


jack.shape("turtle")

################ SCORE SECTİON ###############
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Skor: 0   En Yüksek Skor: 0", align="center", font=("Courier", 24, "normal"))
skor = 0
max_skor=0
# score upper
def up_and_up(x, y):
    global skor, max_skor
    skor += 1
    if skor > max_skor:
        max_skor = skor
    score_pen.clear()
    score_pen.write("Skor: {}   En Yüksek Skor: {}".format(skor, max_skor), align="center", font=("Courier", 24, "normal"))
    jack.penup()
    jack.goto(randint(-350, 350), randint(-200, 200))

##########################
#for run for his life because I am gonna eat him
def turtle_in_shadows():
    jack.penup()
    jack.goto(randint(-350, 350), randint(-200, 200))


FONT = ('Arial', 30, 'normal')

def countdown(time):
    turtle_screen.onclick(None)  # disable click until countdown completes
    timerr.clear()

    if time > 0:
        timerr.write(time, align='center', font=FONT)
        turtle_screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        timerr.write("Click Screen", align='center', font=FONT)
        turtle_screen.onclick(lambda x, y: countdown(30))


timerr.write("Click Screen", align='center', font=FONT)

"""# loop for timer
for i in range(20):
    turtle.ontimer(up_and_up ,t=400 * (i + 1))"""

jack.onclick(up_and_up)
turtle_screen.onclick(lambda x, y: countdown(30))

turtle.mainloop()
