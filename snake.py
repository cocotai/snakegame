from turtle import Turtle
#  建立 const
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]  #  得到第一個 snake 的位置

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):  #  新增節數
        new_snake = Turtle(shape="square")
        # new_snake.shapesize(1, 1)
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def reset(self):
        #  因為碰到牆或是尾巴的蛇，會遺留在螢幕上，所以我們把它放到螢幕看不到的地方
        for seg in self.snakes:
            seg.goto(1000, 1000)
        #  先將snake裡面的片段清空，再重新產生snake
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]


    def extend(self):  #  延伸蛇的節數到最後一節，為什麼是最後一節，因為再移動的時候，最後一節會跑到倒數第二節的位置
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):  # loop 2 to 0, get 2 and 1
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        #  設定第一個走的方向
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # 如果往方向是往上的話，不能在往下轉換方向
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
