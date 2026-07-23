from tkinter import *
from master_mind import Colors, select_colors, play, Match, GameStatus

root = Tk()
root.title("Master Mind Game")
root.config(bg="lavender")
root.minsize(900,700)

guess_color_amount: int = 6
attempt_rows: int = 20
guess_attempt_total = [1]

user_provided_colors = [0] * guess_color_amount
selected_colors = [select_colors(None)]

guess_label_list = [0] * guess_color_amount
clear_label_list = [0] * guess_color_amount
computer_color_labels = [0] * guess_color_amount

guess_grid = [[0 for i in range(guess_color_amount)] for j in range(attempt_rows)]
result_grid = [[0 for i in range(guess_color_amount)] for j in range(attempt_rows)]

frame_background_color = "lavender"

game_frame = LabelFrame(root, bg = frame_background_color, border=0)
game_frame.grid(row = 0, column = 0, padx = 10)

color_button_frame = LabelFrame(game_frame, bg = frame_background_color, borderwidth = 0, highlightthickness = 0)
color_button_frame.grid(row = 0, column = 0, columnspan = 3, pady = 10)

user_select_frame = LabelFrame(game_frame, bg = frame_background_color, borderwidth = 0, highlightthickness = 0)
user_select_frame.grid(row = 1, column = 0, columnspan = 3, pady = 10)

options_frame = LabelFrame(game_frame, bg = frame_background_color, borderwidth = 0, highlightthickness = 0)
options_frame.grid(row = 2, column = 0, columnspan = 3, pady = 10)

guess_grid_frame = LabelFrame(game_frame, bg = frame_background_color, borderwidth = 0, highlightthickness = 0)
guess_grid_frame.grid(row = 3, column = 0, rowspan = 3)

results_grid_frame = LabelFrame(game_frame, bg = frame_background_color, borderwidth = 0, highlightthickness = 0)
results_grid_frame.grid(row = 3, column = 2, rowspan = 3)

computer_color_frame = LabelFrame(game_frame, bg = frame_background_color, borderwidth = 0, highlightthickness = 0)
computer_color_frame.grid(row = 3, column = 1)      


def assign_color(color):
    index = next((i for i, x in enumerate(user_provided_colors) if x == 0), -1)
    if(index != -1):
        user_provided_colors[index] = color
        color_name = color.name
        guess_label_list[index].config(bg = color_name)


def submit_guess():
    index = next((i for i, x in enumerate(user_provided_colors) if x == 0), -1)
    if((index == -1) and (guess_attempt_total[0] < 21)):
        for index, label in enumerate(user_provided_colors):
            guess_grid[guess_attempt_total[0]-1][index].config(bg = label.name)

        response = play(selected_colors[0], user_provided_colors, guess_attempt_total[0])
        
        assign_result_to_grid(response[0])
        assign_game_result_to_grid(response[1],response[2])
        

def assign_result_to_grid(match_types):
    exact_match_range = match_types[Match.EXACT]
    present_match_range = match_types[Match.PRESENT] + exact_match_range
    no_match_range = match_types[Match.NO_MATCH] + present_match_range

    for match in range(0, exact_match_range):
        result_grid[guess_attempt_total[0]-1][match].config(bg = "black")

    for match in range(exact_match_range, present_match_range):
        result_grid[guess_attempt_total[0]-1][match].config(bg = "silver")

    for match in range(present_match_range, no_match_range):
        result_grid[guess_attempt_total[0]-1][match].config(bg = "gray")


def assign_game_result_to_grid(next_attempt,game_status):
    if(game_status == GameStatus.WON):
        game_status_label.config(text="You win the correct colors are")
        for index, label in enumerate(selected_colors[0]):
            computer_color_labels[index].config(text = " ", bg = label.name)
        guess_attempt_total[0] = 21
    elif(game_status == GameStatus.LOST):
        game_status_label.config(text="You lose the correct colors are")
        for index, label in enumerate(selected_colors[0]):
            computer_color_labels[index].config(text = "  ", bg = label.name)
    else:
        guess_attempt_total[0] = next_attempt   

        
def clear_single_guess(index):
    user_provided_colors[index] = 0
    guess_label_list[index].config(bg = "#F0F0F0")

  
def clear_board():
    for column in range(0, guess_color_amount):
        for row in range(0,attempt_rows):
            guess_grid[row][column].config(bg = "#F0F0F0")
            result_grid[row][column].config(bg = "#F0F0F0")
        user_provided_colors[column] = 0
        guess_label_list[column].config(bg = "#F0F0F0")
        computer_color_labels[column].config(text = "?", bg = "#F0F0F0")
        game_status_label.config(text="Unknown Colors!")  
    guess_attempt_total[0] = 1 
    selected_colors[0] = select_colors(None)  


def give_up():
    if(guess_attempt_total[0] != 21):
        game_status_label.config(text="You lose the correct colors are")
        for index, label in enumerate(selected_colors[0]):
            computer_color_labels[index].config(text = " ", bg = label.name)
        guess_attempt_total[0] = 21

     
redButton = Button(color_button_frame, padx = 80, pady = 10, command = lambda: assign_color(Colors.RED), bg = "red")
orangeButton = Button(color_button_frame, padx = 80, pady=10, command = lambda: assign_color(Colors.ORANGE), bg = "orange")
yellowButton = Button(color_button_frame, padx = 80, pady = 10, command = lambda: assign_color(Colors.YELLOW), bg = "yellow")
greenButton = Button(color_button_frame, padx = 80, pady = 10, command = lambda: assign_color(Colors.GREEN), bg = "green")
blueButton = Button(color_button_frame, padx = 80, pady = 10, command = lambda: assign_color(Colors.BLUE), bg = "blue")
purpleButton = Button(color_button_frame, padx = 80, pady = 10, command = lambda: assign_color(Colors.PURPLE), bg = "purple")
brownButton = Button(color_button_frame, padx = 80, pady = 10, command = lambda: assign_color(Colors.BROWN), bg = "brown")
pinkButton = Button(color_button_frame, padx = 80, pady = 10, command = lambda: assign_color(Colors.PINK), bg = "pink")
darkGreenButton = Button(color_button_frame, padx = 80, pady = 10, command = lambda: assign_color(Colors.DARKGREEN), bg = "darkgreen")
darkBlueButton = Button(color_button_frame, padx = 80, pady = 10, command = lambda: assign_color(Colors.DARKBLUE), bg = "darkblue")


redButton.grid(row = 0, column = 0)
orangeButton.grid(row = 0, column = 1)
yellowButton.grid(row = 0, column = 2)
greenButton.grid(row = 0, column = 3)
blueButton.grid(row = 0, column = 4)
purpleButton.grid(row = 1, column = 3)
brownButton.grid(row = 1, column = 1)
pinkButton.grid(row = 1, column = 2)
darkGreenButton.grid(row = 1, column = 0)
darkBlueButton.grid(row = 1, column = 4)


play_button = Button(options_frame, text = "Play", padx = 30, pady = 10, command = submit_guess).grid(row = 5, column = 2)
give_up_button = Button(options_frame, text = "Give Up", padx = 30, pady = 10, command = give_up).grid(row = 5, column = 3)
clear_button = Button(options_frame, text = "Restart Game", padx = 30, pady = 10, command = clear_board).grid(row = 5, column = 4)


for column in range(0, guess_color_amount):
    clear_Label = Button(user_select_frame, text = "X", command = lambda index = column: clear_single_guess(index), relief = "solid", borderwidth = 2, padx = 20, pady = 10)
    clear_Label.grid(row = 4, column = column)
    clear_label_list[column] = clear_Label

    guess_Label = Label(user_select_frame, relief = "solid", borderwidth = 2, padx = 40, pady = 15)
    guess_Label.grid(row = 3, column = column)
    guess_label_list[column] = guess_Label

    labels = Label(computer_color_frame, text = "?", relief = "solid", borderwidth = 1, width=5, height=2)
    labels.grid(row = 1, column = column)
    computer_color_labels[column] = labels

    
for row in range(0, attempt_rows):
    for column in range(0,guess_color_amount):
        guess_grid_label = Label(guess_grid_frame, text = "", relief = "solid", borderwidth = 1, padx=10, pady=1)
        guess_grid_label.grid(row = row, column = column)
        guess_grid[row][column] = guess_grid_label

        result_grid_label = Label(results_grid_frame, text = "", relief = "solid", borderwidth = 1, padx=10)
        result_grid_label.grid(row=row, column=column)
        result_grid[row][column] = result_grid_label


game_status_label = Label(computer_color_frame, text = "Unknown Colors!", bg = frame_background_color, width=30, height=2)
game_status_label.grid(row = 0, column = 0, columnspan = 6)


root.mainloop()
