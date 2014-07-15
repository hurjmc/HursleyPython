#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#


#
# GUI version of hangman
#

# Import tkinter module and use the abbreviation 'tk'
import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox as tkmessage

# Deal with button press
def button_press(letter):
    global badguess
    print ('>>>',letter) 
    if letter in word:
        for (i,L) in enumerate(word):
            if L == letter:
                guess[i] = letter
        current_guess['text'] = ' '.join(guess)+'\n'
        if '_' not in guess:
            tkmessage.showinfo("WELL DONE!","Well done, you guessed the word!")
            root.destroy()
    else:
        canvas.create_line(*drawing[badguess], smooth='true', width=3)
        badguess += 1
        if badguess > 9:
            tkmessage.showinfo("HARD LUCK","Hard luck, you lose!\nThe word was "+word)
            root.destroy()

# Get word for this game
def get_word():
    return 'PYTHON' 


# Some initialisation
word = get_word()
guess = list('_'*len(word))
badguess = 0

qwerty_keys = ['QWERTYUIOP','ASDFGHJKL','ZXCVBNM']
key_map = {}

drawing = [( 50,350,350,350),
           (100,350,100, 75),
           (100, 75,300, 75),
           (200, 75,100,175),
           (300, 75,300,150),
           (300,150,280,170,300,190,320,170,300,150),
           (300,190,300,250),
           (300,250,325,275),
           (300,250,275,275),
           (270,195,330,195)]


# Create a root window
root = tk.Tk()

# Create a 400x400 pixel canvas (to draw the hanged man in) 
canvas = tk.Canvas(root,width=400,height=400)
canvas.grid()

# Set up a large font to display the current guess
largeFont = tkfont.Font(family='Courier', size=24, weight='bold')
current_guess = tk.Label(root)
current_guess['font'] = largeFont
current_guess['text'] = ' '.join(guess)+'\n'
current_guess.grid()

# Set up a frame to hold the keyboard
key_board=tk.Frame(root)
key_board.grid()

for (kb_row, letters) in enumerate(qwerty_keys):
    for (kb_col, letter) in enumerate(letters):
        button = tk.Button(key_board)
        button['text'] = letter
        button['command'] = lambda letter = letter: button_press(letter)
        button.grid(column=kb_col, row=kb_row, ipadx=10, sticky=tk.E+tk.W)
        key_map[letter] = button
        
# Call 'mainloop' to start the program
root.mainloop()
