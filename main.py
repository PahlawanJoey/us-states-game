import turtle
import pandas
from state_placer import State_placer

screen = turtle.Screen()
screen.title("PahlawanJoey's U.S. States Game for GOATS")
screen.bgpic("blank_states_img.gif")


def user_guess_state():
    if State_placer.counter > 0:
        answer_state = screen.textinput(title=f"{State_placer.counter}/50 States Correct",
                                        prompt="What's another state's name?").title()
        return answer_state
    else:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
        return answer_state


state_data = pandas.read_csv("50_states.csv")
column_names = ["a", "b", "c"]
state_guess = pandas.DataFrame(columns=column_names)
states_left = state_data["state"].tolist()

while State_placer.counter < 50:
    answer_state = user_guess_state()
    if answer_state == "Exit":
        break
    state_guess = state_data[state_data["state"] == answer_state]
    if not state_guess.empty:
        states_left.remove(answer_state)
        x_cor = state_guess["x"].item()
        y_cor = state_guess["y"].item()
        nation_state = State_placer(x=x_cor, y=y_cor, statename=answer_state)
        state_counter = State_placer.counter

df_states_left = pandas.DataFrame(states_left, columns=["states:"])
df_states_left.to_csv('states_to_learn.csv', index=False)