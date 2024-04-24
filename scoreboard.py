from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("DeepPink4")
        self.penup()
        self.goto(0,250)
        self.update_scbd()
        self.hideturtle()
    def update_scbd(self):
        self.write(f"Ilość spożytego jedzonka: {self.score}", align="center", font=("Cambria", 24, "bold"))
    def score_up(self):
        self.score += 1
        self.clear()
        self.update_scbd()
    def gameover1(self):
        self.clear()
        self.goto(0,0)
        self.write("Wonsz uderzył się w główkę!\n",align="center", font=("Cambria", 24, "bold"))
        self.write(f"Tyle jedzonka spożył: {self.score}",align="center", font=("Cambria", 24, "bold"))
    def gameover2(self):
        self.clear()
        self.goto(0,0)
        self.write("Wonsz się zaplątał!\n",align="center", font=("Cambria", 24, "bold"))
        self.write(f"Tyle jedzonka spożył: {self.score}",align="center", font=("Cambria", 24, "bold"))    
        