import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title('hanie tic-tac-toe')

#bools
clicker =True
winner = False

#counters
counter=0

def buttonclick(b):
    global clicker, counter
    if b["text"] == " " and clicker == True:
        b["text"] ="X"
        clicker = False
        counter += 1
        ifwin()
    elif b["text"] == " " and clicker == False:
        b["text"] = "O"
        clicker = True
        ifwin()
        counter += 1
    elif (b["text"] == "X" or b["text"] == "O" ):
        	messagebox.showerror("tic-tac-no","i bet that you know how to play ti-tac-toe\n don\'t be stupid and go to anotherbox")

#disabling buttons
def disablebuttons():
	b2.config(state = DISABLED)
	b3.config(state = DISABLED)
	b4.config(state = DISABLED)
	b5.config(state = DISABLED)
	b6.config(state = DISABLED)
	b7.config(state = DISABLED)
	b8.config(state = DISABLED)
	b9.config(state = DISABLED)
	b10.config(state = DISABLED)
#to check for the winner
def ifwin():
	global winner, counter, clicker

	if (b2["text"] == "X" and b3["text"] == "X" and b4["text"] == "X") or (b2["text"] == "O" and b3["text"] == "O" and b4["text"] == "O"):
			b2.config(bg="green")
			b3.config(bg="green")
			b4.config(bg="green")
			winner= True 
			messagebox.showinfo("tic-tac-bow", "GGWP")
			disablebuttons()
	elif (b5["text"] == "X" and b6["text"] == "X" and b7["text"] == "X") or (b5["text"] == "O" and b6["text"] == "O" and b7["text"] == "O"):
			b5.config(bg="green")
			b6.config(bg="green")
			b7.config(bg="green")
			winner= True 
			messagebox.showinfo("tic-tac-bow", "GGWP")
			disablebuttons()
	elif (b8["text"] == "X" and b9["text"] == "X" and b10["text"] == "X") or (b8["text"] == "O" and b9["text"] == "O" and b10["text"] == "O"):
			b8.config(bg="green")
			b9.config(bg="green")
			b10.config(bg="green")
			winner= True 
			messagebox.showinfo("tic-tac-bow", "GGWP")
			disablebuttons()
	elif (b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X") or (b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O"):
			b2.config(bg="green")
			b5.config(bg="green")
			b8.config(bg="green")
			winner= True 
			messagebox.showinfo("tic-tac-bow", "GGWP")
			disablebuttons()	
	elif (b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X") or (b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O"):
			b3.config(bg="green")
			b6.config(bg="green")
			b9.config(bg="green")
			winner= True 
			messagebox.showinfo("tic-tac-bow", "GGWP")
			disablebuttons()
	elif (b4["text"] == "X" and b7["text"] == "X" and b10["text"] == "X") or (b4["text"] == "O" and b7["text"] == "O" and b10["text"] == "O"):
			b4.config(bg="green")
			b7.config(bg="green")
			b10.config(bg="green")
			winner= True 
			messagebox.showinfo("tic-tac-bow", "GGWP")
			disablebuttons()	
	elif (b2["text"] == "X" and b6["text"] == "X" and b10["text"] == "X") or (b2["text"] == "O" and b6["text"] == "O" and b10["text"] == "O"):
			b2.config(bg="green")
			b6.config(bg="green")
			b10.config(bg="green")
			winner= True 
			messagebox.showinfo("tic-tac-bow", "GGWP")
			disablebuttons()
	elif (b4["text"] == "X" and b6["text"] == "X" and b8["text"] == "X") or (b4["text"] == "O" and b6["text"] == "O" and b8["text"] == "O"):
			b4.config(bg="green")
			b6.config(bg="green")
			b8.config(bg="green")
			winner= True 
			messagebox.showinfo("tic-tac-bow", "GGWP")
			disablebuttons()
	elif counter ==9 and winner== False:
        	b2.config(bg="blue"),b3.config(bg="blue"),b4.config(bg="blue"),b5.config(bg="blue"),b6.config(bg="blue"),b7.config(bg="blue"),b8.config(bg="blue"),b9.config(bg="blue"),b10.config(bg="blue"),messagebox.showinfo("tic-tac-tie", "GGWP, but sorry it\'s a tie\ntry again"),disablebuttons(),

#buttons

b2 = Button(root, text= " ", font=("helvetica", 20), width= 6, height=3, bg="whitesmoke", command=lambda: buttonclick(b2))
b3 = Button(root, text= " ", font=("helvetica", 20), width= 6, height=3, bg="whitesmoke", command=lambda: buttonclick(b3))
b4 = Button(root, text= " ", font=("helvetica", 20), width= 6, height=3, bg="whitesmoke", command=lambda: buttonclick(b4))

b5 = Button(root, text= " ", font=("helvetica", 20), width= 6, height=3, bg="whitesmoke", command=lambda: buttonclick(b5))
b6 = Button(root, text= " ", font=("helvetica", 20), width= 6, height=3, bg="whitesmoke", command=lambda: buttonclick(b6))
b7 = Button(root, text= " ", font=("helvetica", 20), width= 6, height=3, bg="whitesmoke", command=lambda: buttonclick(b7))

b8 = Button(root, text= " ", font=("helvetica", 20), width= 6, height=3, bg="whitesmoke", command=lambda: buttonclick(b8))
b9 = Button(root, text= " ", font=("helvetica", 20), width= 6, height=3, bg="whitesmoke", command=lambda: buttonclick(b9))
b10 = Button(root, text= " ", font=("helvetica", 20), width= 6, height=3, bg="whitesmoke", command=lambda: buttonclick(b10))

#3x3 grid

b2.grid(row= 1, column=0)
b3.grid(row= 1, column=1)
b4.grid(row= 1, column=2)

b5.grid(row= 2, column=0)
b6.grid(row= 2, column=1)
b7.grid(row= 2, column=2)

b8.grid(row= 3, column=0)
b9.grid(row= 3, column=1)
b10.grid(row= 3, column=2)

root.mainloop()         