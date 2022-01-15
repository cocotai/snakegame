from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()  #  從 Turtle 繼承 method and attritube
        self.shape("circle")  #  可以直接呼叫 Turtle 的 method, attritube
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  #  設定食物會出現的地點，因為螢幕的界線是-300~300，而snake的長寬是20 pixels
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)