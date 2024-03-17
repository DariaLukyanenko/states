import pandas
from turtle import *


data = pandas.read_csv('50_states.csv')

screen = Screen()
turtle = Turtle()
screen.bgpic("blank_states_img.gif")

list=[]
end=5
while end!=0:
    state= screen.textinput('input','Input a state')
    
    for i, row in data.iterrows():
        if state == row['state']:
            x_coordinate = row['x']
            y_coordinate = row['y']
            turtle.penup()
            turtle.goto(x_coordinate, y_coordinate)
            turtle.write(state, True, align="center")
            list.append(state)
            

    end-=1

exitonclick()

# NOTE Alternative
# not_learned = [for all_states if states not in list ] 
# list to csv + save
remaining_states = data[~data['state'].isin(list)]
remaining_states.to_csv('remaining_states.csv', index=False)
