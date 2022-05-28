"""
Created on Sat May 28 21:22:11 2022
W8E11P18
@author: Diana Armanikian
Modify Listing 9.14 (tkinterlight.py)
so that it models a light with a single
on/off yellow lamp.

"""
from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame


def do_button_press():

    global color
    if color == 'black':
        color = 'yellow'
        canvas.itemconfigure(yellow_lamp, fill='yellow')  # Turn red off
    elif color == 'yellow':
        color = 'black'
        canvas.itemconfigure(yellow_lamp, fill='black')  # Turn yellow on


# Create and initialize global variables
color = 'black'  # The light's current color
root = Tk()  # Create the main window
root.title("on/off Light")
frame = Frame(root)  # Create a frame to hold the widgets
frame.pack()  # Make the frame fill the entire window
# Create a drawing surface within the frame
canvas = Canvas(frame, width=150, height=300)
# Set up the visual aspects of the light
# the light frame
canvas.create_rectangle(50, 20, 150, 280, fill='gray')
# Yellow lamp
yellow_lamp = canvas.create_oval(70, 120, 130, 180, fill='black')
# Create a graphical button and ensure it calls the do_button_press
# function when the user presses it
button = Button(frame, text='Change', command=do_button_press)
# Position button in the containing frame's first row, first column,
# and position canvas in the first row, second column (zero origin,
# like list indices).
button.grid(row=0, column=0)
canvas.grid(row=0, column=1)
# Start the GUI event loop
root.mainloop()
