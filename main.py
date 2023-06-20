import pandas
from turtle import Turtle, Screen
from PIL import Image

# set up screen + background image
screen = Screen()
screen.bgpic("blank_states_img.gif")
width, height = Image.open("blank_states_img.gif").size
screen.setup(width, height)
screen.title("Name the States Game")

data = pandas.read_csv("50_states.csv")
states_df = data['state']
states = states_df.to_list()


def check_answer(answer, state_dataframe):
    global states
    if answer in states:
        index_val = state_dataframe[state_dataframe == answer].index.item()
        state_dataframe.drop(index=[index_val], inplace=True)
        insert_state(answer)
        return True
    else:
        return False


def insert_state(state_name):
    global data
    row = data[data.state == state_name]
    state = Turtle("blank")
    state.penup()
    state.setx(row.x.item())
    state.sety(row.y.item())
    state.write(f"{state_name}", font=("Arial", 8, "normal"))


def win():
    winner = Turtle("blank")
    winner.penup()
    winner.write("You Win!", font=("Arial", 50, "normal"), align="center")


score = 0
game_is_on = True
user_answer = ""
while game_is_on:
    if score == 50:
        win()
        screen.exitonclick()
    elif score == 0:
        user_answer = screen.textinput(f"{score}/50 States Correct", "What's a state name?:")
    elif 0 < score < 50:
        user_answer = screen.textinput(f"{score}/50 States Correct", "What's another state name?:")
    if user_answer is None and score != 50:
        screen.bye()
    elif user_answer == 'exit':
        states_df.to_csv("states_to_learn.csv")
        screen.bye()
    elif check_answer(user_answer.title(), states_df):
        score += 1
