import turtle


screen = turtle.Screen()
# screen.title("US-State-Game")

image = "blank_states_img.gif"

screen.addshape(image)


turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x,y)



# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
import pandas

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guess_states = []

while len(guess_states) <= 50: 
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 correct", prompt="What's another state's name? ").title()
    
    if answer_state == "Exit":
        break

    print(answer_state)
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        print(state_data)
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        
        
missed_states = []
for state in all_states:
    if state not in guess_states:
        missed_states.append(state)

missed_states_dic = {
    "state": missed_states
}


print(missed_states)

data_frame = pandas.DataFrame(missed_states_dic)
data_frame.to_csv("state_to_learn.csv")


