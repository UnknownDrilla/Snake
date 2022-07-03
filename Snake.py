from tkinter import *
import random

G_WIDTH=720
G_HEIGHT=480
SPEED=50
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOR="#FFFFFF"
FOOD_COLOR="#808080"
BG_COLOUR="#000000"
class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        x=random.randint(0, int((G_WIDTH/SPACE_SIZE))-1)*SPACE_SIZE
        y=random.randint(0, int((G_HEIGHT/SPACE_SIZE))-1)*SPACE_SIZE
        self.coordinates=[x, y]
        canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, outline="#FFFFFF", tag="food")
def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    window.after(SPEED, next_turn, snake, food)
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]
def change_direction(new_direction):
    pass
def check_collisions():
    pass
def game_over():
    pass
window=Tk()
window.title("Snake")
window.resizable(False, False) 
score=0
direction="down"
label=Label(window, text="Score: {}".format(score),bg="#000000", fg="#FFFFFF",pady=10, padx=(G_WIDTH*0.3361), font=("consolas", 40))
label.pack()
canvas=Canvas(window, bg=BG_COLOUR, height=G_HEIGHT, width=G_WIDTH)
canvas.pack()
window.update
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry=window_width*window_height+x+y
snake=Snake()
food=Food()
next_turn(snake, food)
window.mainloop()
    
