#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

#
# tkinter - canvas demo
#

import tkinter as tk

root = tk.Tk()

drawing = tk.Canvas(root,width=450,height=300)
drawing.pack()

drawing.create_oval(20,20,120,120,fill='red',width=0)
drawing.create_rectangle(80,80,320,220,width=5,fill='white')
drawing.create_oval(200,200,380,280,width=5,outline='blue')
drawing.create_text(400,30,text='Some text')

root.mainloop()

