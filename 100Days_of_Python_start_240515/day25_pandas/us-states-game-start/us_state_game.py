import turtle as t
import pandas as pd

# data load
def get_state_data(csv_path = '50_states.csv'):
    data = pd.read_csv(csv_path)
    return data
# check the state is in 50 states
def is_in_US_states(state, pd_data):
    if state in pd_data.state.values:
        return True
    return False

if __name__ == '__main__':
    screen = t.Screen()
    screen.title("U.S. States Game")

    image = 'blank_states_img.gif'
    screen.bgpic(image)

    # input user answer
    text_input_title = 'Guess the State'
    text_input_prompt = "what's another state's name? "
    data = get_state_data()
    answer_state = screen.textinput(title=text_input_title, prompt=text_input_prompt)
    if is_in_US_states(answer_state,data) :
        pass
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