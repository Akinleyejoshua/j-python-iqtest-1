import random
number  = random.randint(1,10)
from tkinter import *
from tkinter import ttk 
app = Tk()
app.title("guessing game")
ttk.Label(text = 'IQ test').grid(row = 0,column = 0)
ttk.Label(text = 'If you are smart guess a number am thinking of').grid(row = 1,column = 0)
entryI = IntVar()
print(number)
entry = ttk.Entry(textvariable = entryI.get)
def guess():
	try:
		count = 0
		#count += 1
		reply = ttk.Label()
		reply.grid(row = 4)
		inp = int(entry.get())
	except:
		pass
	try:
		count = 0
		for count in range(1,10):
			pass
		if inp != number:
			print(count)
			print(inp)
			reply.configure(text = 'wrong!, you are not even smart!')
		elif inp == number:
			reply.configure(text = 'Correct!, you are very intelligent')
	except:
		reply.configure(text = 'Dummy, input only numeric values')
check = ttk.Button(text = 'Guess',command = guess)
check.grid(row = 3,column = 0)
entry.grid(row = 2,column = 0)
entry.focus()
app.mainloop()
