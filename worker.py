import turtle

# إعداد النافذة
wind = turtle.Screen()
wind.title("Ping Pong Game")
wind.bgcolor("black")
wind.setup(width=600, height=600)
wind.tracer(0)

# المضرب الأول
madrab1 = turtle.Turtle()
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-260, 0)

# المضرب الثاني
madrab2 = turtle.Turtle()
madrab2.shape("square")
madrab2.color("white")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(260, 0)

# الكرة
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# النقاط
score1 = 0
score2 = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Player 1: 0   Player 2: 0", align="center",
                font=("Courier", 16, "normal"))

# حركة المضارب
def madrab1_up():
    if madrab1.ycor() < 250:
        madrab1.sety(madrab1.ycor() + 20)

def madrab1_down():
    if madrab1.ycor() > -250:
        madrab1.sety(madrab1.ycor() - 20)

def madrab2_up():
    if madrab2.ycor() < 250:
        madrab2.sety(madrab2.ycor() + 20)

def madrab2_down():
    if madrab2.ycor() > -250:
        madrab2.sety(madrab2.ycor() - 20)

# التحكم
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

# حركة الكرة
def move_ball():
    global score1, score2

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ارتداد من الأعلى والأسفل
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # تصادم مع المضرب الثاني
    if (250 < ball.xcor() < 270) and \
       (madrab2.ycor() - 50 < ball.ycor() < madrab2.ycor() + 50):
        ball.setx(250)
        ball.dx *= -1

    # تصادم مع المضرب الأول
    if (-270 < ball.xcor() < -250) and \
       (madrab1.ycor() - 50 < ball.ycor() < madrab1.ycor() + 50):
        ball.setx(-250)
        ball.dx *= -1

    # تسجيل هدف
    if ball.xcor() > 300:
        score1 += 1
        ball.goto(0, 0)
        ball.dx *= -1
        update_score()

    if ball.xcor() < -300:
        score2 += 1
        ball.goto(0, 0)
        ball.dx *= -1
        update_score()

    wind.update()
    wind.ontimer(move_ball,10)

def update_score():
    score_pen.clear()
    score_pen.write(f"Player 1: {score1}   Player 2: {score2}",
                    align="center", font=("Courier", 16, "normal"))

# تشغيل اللعبة
move_ball()
wind.mainloop()
