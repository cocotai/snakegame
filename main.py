from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#  建立 snake 跑出三個正方形
snake = Snake()
screen = Screen()
food = Food()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game, Snake it!")
# distance = 0
# for square in range(3):
#     snake = Turtle(shape="square")
#     snake.color("white")
#     # snake.penup()
#     snake.setposition(x=snake.xcor() - distance, y=snake.ycor())
#     distance += 20

# 更好的方法，是使用tuple
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
screen.tracer(0)  # 停止動畫顯示
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_game_on = True
while is_game_on:
    screen.update()  # 顯示畫面
    time.sleep(0.1)  # 延遲0.1秒鐘
    snake.move()
    #  設定吃食物的距離，若蛇跟食物的距離小於15 (蛇是 20*20；食物是 10* 10) 的話，會重新產生食物
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.gain_score()

    #  設定當蛇的頭碰到邊界的時候，遊戲結束 (也就是當 x axis 超過280或低於-280，同理y也是)
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.score_reset()
        # is_game_on = False
        snake.reset()

    #  偵測是否蛇的頭有撞到任何一結尾巴，因為是任何一節，所以我們用 for loop 來確定
    # for segment in snake.snakes:
        # if segment == snake.head:  #  因為是 loop 所以頭也會被 loop 到，所以當 segment 是頭的話，我們要 pass 跳過
        #     pass
        # elif snake.head.distance(segment) < 10:  #  當頭跟任何一節尾巴的距離小於10的話，表示撞到了，遊戲結束
        #     scoreboard.game_over()
        #     is_game_on = False
    for segment in snake.snakes[1:]:  #  使用 slice 的方法，避開 first head
        if snake.head.distance(segment) < 10:
            scoreboard.score_reset()
            # is_game_on = False
            snake.reset()
screen.exitonclick()