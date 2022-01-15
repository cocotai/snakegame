from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #  不用給予形狀，因為我們會 hideturtle
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as file:
            h_score = file.read()  #  回傳回來是字串
        self.highest_score = int(float(h_score))
        #  透過update_scoreboard來更新
        # self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 24, 'normal'))
        self.update_scoreboard()

    def update_scoreboard(self):  # 因為上下都有 self.write 我們用 function 來取代
        self.clear()
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def score_reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highest_score}")  #  write一定要傳入字串
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def gain_score(self):
        self.score += 1
        # self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 12, 'normal'))
        self.update_scoreboard()