from tkinter import *
from RPi import GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)



class Spiel():
	def __init__(self):
		self.lampe_an = False
		self.window = Tk()
		self.label = Label(master=self.window,
			text=self.label_text())
		self.button = Button(master=self.window,
			text="schalter",
			command=self.schalter)
		self.button.pack()
		self.label.pack()
		self.window.mainloop()
	
	def label_text(self):
		return "Lampe an: %s" % self.lampe_an
	
	def schalter(self):
		self.lampe_an = not self.lampe_an
		self.label.config(text=self.label_text())
		GPIO.output(10, self.lampe_an)
	
	
				
Spiel()