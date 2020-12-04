from tkinter import *
import random

class App:
	def __init__(self, root):
		self.root = root
		self.root.geometry('500x500')
		self.root.title("Dice Simulation by Muhammad Hanan Asghar")
		self.root.maxsize(500,500)
		self.root.minsize(500,500)
		self.gui_board()


	def frame(self,width, height, x, y):
		frame = Frame(self.root, width=f'{width}', height=f'{width}')
		frame.place(x=x, y=y)
		return frame

		# first is x 
		# second is y
		# third is radius+x
		# fourth is radius+y
	def dice(self, master, dot):	
		if dot == 6:
			rectangle = Canvas(master, width=500, height=430)
			rectangle.delete("all")
			rectangle.create_rectangle(0, 0, 300, 300, fill="black", outline = 'black')
			rectangle.create_rectangle(15, 15, 285, 285, fill="white", outline = 'blue') 
			# Row No 1
			rectangle.create_oval(50,  50, 85, 85, outline="#000",fill="#000")
			rectangle.create_oval(220,  52, 255, 87, outline="#000",fill="#000")
			# Row No 2
			rectangle.create_oval(50,  130, 85, 165, outline="#000",fill="#000")
			rectangle.create_oval(220,  128, 255, 163, outline="#000",fill="#000")
			# Row No 3
			rectangle.create_oval(50,  210, 85, 245, outline="#000",fill="#000")
			rectangle.create_oval(220,  208, 255, 243, outline="#000",fill="#000")
			rectangle.grid(row=0, column=0, padx=100, pady=65)
		elif dot == 1:
			rectangle = Canvas(master, width=500, height=430)
			rectangle.delete("all")
			rectangle.create_rectangle(0, 0, 300, 300, fill="black", outline = 'black')
			rectangle.create_rectangle(15, 15, 285, 285, fill="white", outline = 'blue') 
			rectangle.create_oval(130,  128, 165, 163, outline="#000",fill="#000")
			rectangle.grid(row=0, column=0, padx=100, pady=65)
		elif dot == 2:
			rectangle = Canvas(master, width=500, height=430)
			rectangle.delete("all")
			rectangle.create_rectangle(0, 0, 300, 300, fill="black", outline = 'black')
			rectangle.create_rectangle(15, 15, 285, 285, fill="white", outline = 'blue') 
			rectangle.create_oval(130,  88, 165, 123, outline="#000",fill="#000")
			rectangle.create_oval(130,  148, 165, 183, outline="#000",fill="#000")
			rectangle.grid(row=0, column=0, padx=100, pady=65)
		elif dot == 3:
			rectangle = Canvas(master, width=500, height=430)
			rectangle.delete("all")
			rectangle.create_rectangle(0, 0, 300, 300, fill="black", outline = 'black')
			rectangle.create_rectangle(15, 15, 285, 285, fill="white", outline = 'blue') 
			rectangle.create_oval(130,  58, 165, 93, outline="#000",fill="#000")
			rectangle.create_oval(130,  118, 165, 153, outline="#000",fill="#000")
			rectangle.create_oval(130,  178, 165, 213, outline="#000",fill="#000")
			rectangle.grid(row=0, column=0, padx=100, pady=65)
		elif dot == 4:
			rectangle = Canvas(master, width=500, height=430)
			rectangle.delete("all")
			rectangle.create_rectangle(0, 0, 300, 300, fill="black", outline = 'black')
			rectangle.create_rectangle(15, 15, 285, 285, fill="white", outline = 'blue') 
			# Row No 1
			rectangle.create_oval(50,  80, 85, 115, outline="#000",fill="#000")
			rectangle.create_oval(220,  82, 255, 117, outline="#000",fill="#000")
			# Row No 2
			rectangle.create_oval(50,  180, 85, 215, outline="#000",fill="#000")
			rectangle.create_oval(220,  178, 255, 213, outline="#000",fill="#000")
			rectangle.grid(row=0, column=0, padx=100, pady=65)
		elif  dot == 5:
			rectangle = Canvas(master, width=500, height=430)
			rectangle.delete("all")
			rectangle.create_rectangle(0, 0, 300, 300, fill="black", outline = 'black')
			rectangle.create_rectangle(15, 15, 285, 285, fill="white", outline = 'blue') 
			rectangle.create_oval(130,  128, 165, 163, outline="#000",fill="#000")
			# Row No 1
			rectangle.create_oval(50,  60, 85, 95, outline="#000",fill="#000")
			rectangle.create_oval(220,  62, 255, 97, outline="#000",fill="#000")
			# Row No 2
			rectangle.create_oval(50,  200, 85, 235, outline="#000",fill="#000")
			rectangle.create_oval(220,  198, 255, 233, outline="#000",fill="#000")
			rectangle.grid(row=0, column=0, padx=100, pady=65)
		else:
			return

		return

	def roll(self):
		# Frame For Dice
		self.dice_place = self.frame(500,430,0,52)
		roll_value = random.choice([1,2,3,4,5,6])
		self.dice(self.dice_place,roll_value)

	def gui_board(self):
		# Frame For Button
		self.button_place = self.frame(500,80,0,0)
		self.button_roll = Button(self.button_place, text='Roll Dice', command=self.roll)
		self.button_roll.grid(row=0, column=0, ipadx=5, ipady=5, padx=199, pady=10)


if __name__ == "__main__":
	root = Tk()
	window = App(root)
	root.mainloop()
