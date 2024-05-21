import turtle as t



if __name__ == '__main__':
    screen = t.Screen()
    screen.title("U.S. States Game")

    image = 'blank_states_img.gif'
    screen.bgpic(image)


# reference code

## add mouse click event
# def mouse_click_pos(x,y):
#     print(x,y)
# screen.onclick(mouse_click_pos)
# screen.mainloop()

## add picture to shape
# screen.addshape(image)
# t.shape(image)