import turtle as t
import pandas as pd
title_name = "U.S. States Game"
text_input_title = 'Guess the State'
text_input_prompt = "what's another state's name? "
image_path = 'blank_states_img.gif'

search_col = 'state'

answers = []
# data load
def get_state_data(csv_path = '50_states.csv'):
    data = pd.read_csv(csv_path)
    print(data[data[search_col] == 'Texas'].values[0])
    return data
# check the state is in 50 states
def is_in_US_states(state, pd_data):
    if state in pd_data.state.values:
        return True
    return False

def answering(state,pd_data):
    if is_in_US_states(state,pd_data):
        if state not in answers:
            row = pd_data[pd_data[search_col] == state].values[0]
            t.goto(row[1],row[2])
            t.write(state)

if __name__ == '__main__':
    # set screen
    screen = t.Screen()
    screen.title(title_name)
    screen.bgpic(image_path)

    # set turtle library
    t.hideturtle()
    t.penup()

    # get pd_data
    data = get_state_data()

    # main loop
    # input user answer
    answer_state = screen.textinput(title=text_input_title, prompt=text_input_prompt)
    answering(answer_state,data)

    # wait screen
    screen.mainloop()




### reference code

## add mouse click event
# def mouse_click_pos(x,y):
#     print(x,y)
# screen.onclick(mouse_click_pos)
# screen.mainloop()

## add picture to shape
# screen.addshape(image)
# t.shape(image)