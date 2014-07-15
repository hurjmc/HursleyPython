#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

#
# tkinter - grid layout demo
#
import tkinter as tk
import tkinter.font as tkfont


root = tk.Tk()

BIG = tkfont.Font(family='Courier',size=24, weight='bold')

big_button = tk.Button(root,
             text="GREAT BIG\nBUTTON\nIN THE MIDDLE",
             font=BIG)

big_button.grid(row=1,column=1)

TL_button = tk.Button(root,text="Top Left")
TL_button.grid(row=0,column=0)

TM_button = tk.Button(root,text="Top Middle")
TM_button.grid(row=0,column=1,sticky=tk.N+tk.S)

TR_button = tk.Button(root,text="\nTop\nRight\n")
TR_button.grid(row=0,column=2)

ML_button = tk.Button(root,text="Middle Left")
ML_button.grid(row=1,column=0)

MR_button = tk.Button(root,text="Middle Right")
MR_button.grid(row=1,column=2)

BL_button = tk.Button(root,text="Bottom Left")
BL_button.grid(row=2,column=0,columnspan=3,sticky=tk.E+tk.W)

#BM_button = tk.Button(root,text="Bottom Middle")
#BM_button.grid(row=2,column=1)

#BR_button = tk.Button(root,text="Bottom           Right")
#BR_button.grid(row=2,column=2)



root.mainloop()

