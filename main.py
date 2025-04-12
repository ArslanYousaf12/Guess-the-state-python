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

TOTAL_STATES = 50

correct_answer= 0
while correct_answer < TOTAL_STATES:
    screen.title(f"{correct_answer}/50 US-State-Game")
    turtle.home()
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name? ").title()

    print(answer_state)
    
    state = data[data.state == answer_state]
    state_name = state.state
    print(state_name)
    if(state_name.empty):
        continue
    else:
        correct_answer += 1 
        state_xcor = float(state.x)
        state_ycor = float(state.y)
        turtle.penup()
        turtle.setposition(x=state_xcor, y=state_ycor)
        turtle.write(answer_state)
    
   



turtle.mainloop()