from turtle import *
import random
import winsound

#Aluna: Luana Santiago
#Curso: CC

# Configuration Window
def configuration_window():
    global window
    window.setup(width=1.0, height=1.0)  # dimenção da tela
    window.title('Jogo do Tom e Jerry')  # titulo
    window.bgpic('fundo.png') # plano de fundo
    window.addshape('jerry.gif')
    window.addshape('tom.gif')
    window.addshape('queijo.gif')
    window.addshape('obstaculo.gif')
    window.addshape('gatorua.gif')
    window.addshape('obstaculos2.gif')
    window.addshape('fundo.gif')
    window.addshape('fundo2.gif')
    window.addshape('inicio.gif')
    window.addshape('fim.gif')


# created game edge
def game_edge():
    global gameEdge
    gameEdge.penup()
    gameEdge.setposition(-800, -350)
    gameEdge.pensize(2)
    gameEdge.ht()
    gameEdge.color('black')
    gameEdge.down()
    gameEdge.speed(0)
    for c in range(2):
        gameEdge.forward(2000)
        gameEdge.left(90)
        gameEdge.forward(350)
        gameEdge.left(90)

# Configuration do start
def star_i():
    global star
    star = Turtle()
    star.up()
    star.shape(('inicio.gif'))
    star.goto(-10, -70)


def start_text_play():
        global start_text
        start_text.hideturtle()
        start_text.penup()
        start_text.color('white')
        start_text.sety(10)
        start_text.write("Pressione ESPAÇO para iniciar", align="center", font=("Times New Roman", 20, "bold"))


def game_star():
    global start, star, game_over1
    start_text.clear()
    start = True
    star.ht()
    game_over1.ht()
    jerry.showturtle()
    play()


def score_game():
    global score
    score.speed(0)
    score.shape('square')
    score.color('black')
    score.penup()
    score.hideturtle()
    score.goto(-750, 390)
    score.write(f'Score: {score_P}', font=('Times New Roman', 20, "bold"))

# Function Up
def up_character():
    y = jerry.ycor()
    y += 10
    jerry.sety(y)


# Function Down
def down_character():
    y = jerry.ycor()
    y -= 10
    jerry.sety(y)


def road_p():
    global road
    road = Turtle("fundo.gif")
    road.up()
    road.goto(0,0)
    road.speed(0)


def road_move():
    global road2
    road2 = Turtle("fundo2.gif")
    road2.up()
    road2.hideturtle()
    road2.goto(1800,0)
    road2.speed(0)
    road2.showturtle()


#  Function Character
def jerry_character():
    global jerry
    jerry.ht()
    jerry.up()
    jerry.shape('jerry.gif')
    jerry.setpos(-500, -170)
    jerry.speed('fastest')
    jerry.pensize(100)


#  Function life
def cheese():
    global queijo
    queijo.up()
    queijo.ht()
    queijo.shape('queijo.gif')
    x = 500
    y = [-50, -170, -300]
    teste = random.choice(y)
    queijo.goto(900, teste)
    queijo.speed(0)
    queijo.st()


def cheese1():
    global queijo1
    queijo1.up()
    queijo1.ht()
    queijo1.shape('queijo.gif')
    x = 500
    y = [-50, -170, -300]
    teste = random.choice(y)
    queijo1.goto(900, teste)
    queijo1.speed(0)
    queijo1.st()

# Function enemy
def cat_enemy():
    global tom
    tom = Turtle("tom.gif", visible=False)
    tom.pensize(1000)
    tom.shapesize(2, 1)
    tom.speed('fast')
    tom.penup()
    tom.setheading(180)
    y = [-50, -100, -170, -230, -300]
    teste = random.choice(y)
    tom.setposition(900, teste)
    tom.showturtle()


def obstacle_enemy1():
    global obstacle1
    obstacle1 = Turtle("obstaculo.gif", visible=False)
    obstacle1.pensize(1000)
    obstacle1.shapesize(2, 1)
    obstacle1.speed('fastest')
    obstacle1.penup()
    obstacle1.setheading(180)
    y = [-50, -100, -170, -230, -300]
    teste = random.choice(y)
    obstacle1.setposition(900, teste)
    obstacle1.showturtle()


def obstacle_enemy2():
    global obstacle2
    obstacle2 = Turtle("obstaculos2.gif", visible=False)
    obstacle2.pensize(1000)
    obstacle2.shapesize(2, 1)
    obstacle2.speed('fastest')
    obstacle2.penup()
    obstacle2.setheading(180)
    y = [-50, -100, -170, -230, -300]
    teste = random.choice(y)
    obstacle2.setposition(900, teste)
    obstacle2.showturtle()


def cat_enemy2():
    global tom2
    tom2 = Turtle("tom.gif", visible=False)
    tom2.pensize(1000)
    tom2.shapesize(2, 1)
    tom2.speed('fast')
    tom2.penup()
    tom2.setheading(180)
    y = [-50, -100, -170, -230, -300]
    teste = random.choice(y)
    tom2.setposition(900, teste)
    tom2.showturtle()


def cat_enemy3():
    global tom3
    tom3 = Turtle("gatorua.gif", visible=False)
    tom3.pensize(100)
    tom3.shapesize(2, 1)
    tom3.speed('fast')
    tom3.penup()
    tom3.setheading(180)
    y = [-50, -100, -170, -230, -300]
    teste = random.choice(y)
    tom3.setposition(900, teste)
    tom3.showturtle()


def cheers():
    global cheersP, valor
    cheersP.speed(0)
    cheersP.shape('square')
    cheersP.color('red')
    cheersP.penup()
    cheersP.hideturtle()
    cheersP.goto(-750, 350)
    cheersP.write(f'Energia: {novaP}', font=('Times New Roman', 25, "bold"))


def game_over():
    global game_over1
    game_over1 = Turtle()
    game_over1.ht()
    game_over1.shape('fim.gif')
    game_over1.up()
    game_over1.goto(-10, -70)


def play():
    global novaP, score_P, star, game_over1
    delay(0.1)
    yy = [-50, -100, -170, -230, -300]
    cheers()
    score_game()
    teste = random.choice(yy)
    queijo.forward(-10)
    queijo1.forward(-5)
    tom.forward(10)
    obstacle1.forward(17)
    obstacle2.forward(25)
    tom3.forward(30)
    tom2.forward(40)
    road.forward(-20)
    road2.forward(-20)
    if tom.xcor() < -700: #score
        tom.hideturtle()
        tom.goto(900, teste)
        tom.showturtle()
        novaP = novaP - 1
        cheersP.clear()
    elif road.xcor() < -1800:
        road.hideturtle()
        road.goto(1800, 0)
        road.showturtle()
    elif road2.xcor() < -1800:
        road2.hideturtle()
        road2.goto(1800, 0)
        road2.showturtle()
    elif obstacle1.xcor() < -700:
        obstacle1.hideturtle()
        obstacle1.goto(900, teste)
        obstacle1.showturtle()
        novaP = novaP - 1
        cheersP.clear()
        score_P += 30
        score.clear()
    elif obstacle2.xcor() < -700:
        obstacle2.hideturtle()
        obstacle2.goto(900, teste)
        obstacle2.showturtle()
        novaP = novaP - 1
        cheersP.clear()
        score_P += 30
        score.clear()
    elif tom3.xcor() < -700:
        tom3.hideturtle()
        tom3.goto(900, teste)
        tom3.showturtle()
        novaP = novaP - 1
        cheersP.clear()
    elif tom2.xcor() < -700:
        tom2.hideturtle()
        tom2.goto(900, teste)
        tom2.showturtle()
        novaP = novaP - 1
        cheersP.clear()
    elif queijo.xcor() < -700:
        queijo.hideturtle()
        teste = random.choice(yy)
        queijo.goto(900, teste)
        queijo.showturtle()
    elif queijo1.xcor() < -700:
        queijo1.hideturtle()
        teste = random.choice(yy)
        queijo1.goto(900, teste)
        queijo1.showturtle()
    elif jerry.distance(queijo) < 20 or jerry.distance(queijo1) < 40:
        print("Collision1")
        queijo.hideturtle()
        queijo1.hideturtle()
        if novaP == 50:
            teste = random.choice(yy)
            queijo.goto(900, teste)
            queijo1.goto(900, teste)
            queijo.showturtle()
            queijo1.showturtle()
        elif novaP > 0 and novaP <= 49: #ganhandopontuação
            teste = random.choice(yy)
            queijo.goto(900, teste)
            queijo1.goto(900, teste)
            queijo.showturtle()
            queijo1.showturtle()
            novaP = novaP + 2
            cheersP.clear()
    elif jerry.ycor() > -50 or jerry.ycor() < -300:
        tom.goto(900, teste)
        obstacle1.goto(900, teste)
        obstacle2.goto(900, teste)
        tom3.goto(900, teste)
        tom2.goto(900, teste)
        tom.showturtle()
        obstacle1.showturtle()
        obstacle2.showturtle()
        tom3.showturtle()
        tom2.showturtle()
        jerry.setpos(-500, -170)
        start_text_play()
        start_text()
    elif jerry.distance(tom) < 20 or jerry.distance(obstacle1) < 20 or jerry.distance(obstacle2) < 20 \
            or jerry.distance(tom3) < 20 or jerry.distance(tom2) < 20:
        print("Collision")
        teste = random.choice(yy)
        tom.goto(900, teste)
        teste = random.choice(yy)
        obstacle1.goto(900, teste)
        teste = random.choice(yy)
        obstacle2.goto(900, teste)
        teste = random.choice(yy)
        tom3.goto(900, teste)
        teste = random.choice(yy)
        tom2.goto(900, teste)
        tom.showturtle()
        obstacle1.showturtle()
        obstacle2.showturtle()
        tom3.showturtle()
        tom2.showturtle()
        jerry.setpos(-500, -170)
        teste = random.choice(yy)
        queijo.goto(900, teste)
        teste = random.choice(yy)
        queijo1.goto(900, teste)
        start_text_play()
        start_text()
    elif novaP == 0:
        teste = random.choice(yy)
        tom.goto(900, teste)
        teste = random.choice(yy)
        obstacle1.goto(900, teste)
        teste = random.choice(yy)
        obstacle2.goto(900, teste)
        teste = random.choice(yy)
        tom3.goto(900, teste)
        teste = random.choice(yy)
        tom2.goto(900, teste)
        tom.showturtle()
        obstacle1.showturtle()
        obstacle2.showturtle()
        tom3.showturtle()
        tom2.showturtle()
        jerry.setpos(-500, -170)
        teste = random.choice(yy)
        queijo.goto(900, teste)
        teste = random.choice(yy)
        queijo1.goto(900, teste)
        cheersP.goto(-150, 0)
        cheersP.write('Gamer Over', font=('Times New Roman', 40, "bold"))
        game_over1.st()
        jerry.ht()
        start_text()

    window.ontimer(play, 75)

window = Screen()
window2 = Turtle()
configuration_window()
winsound.PlaySound('musica', winsound.SND_ASYNC + winsound.SND_LOOP)
road_p()
road_move()
start = False
start_text = Turtle()
start_text_play()
star_i()
gameEdge = Turtle()
game_edge()
jerry = Turtle()
jerry_character()
score_P = 0
score = Turtle()
score_game()
xxx = 700

queijo = Turtle()
cheese()

queijo1 = Turtle()
cheese1()

novaP = 50
cheersP = Turtle()
cheers()

cat_enemy()
obstacle_enemy1()
obstacle_enemy2()
cat_enemy2()
cat_enemy3()
game_over()

window.onkeypress(up_character, "Up")
window.onkeypress(down_character, "Down")
window.onkey(game_star, 'space')
window.listen()
mainloop()
