import tkinter
import pandas as pd

##
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
##

# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

# Create an instance of tkinter frame
window = Tk()

# Set the geometry of tkinter frame
window.geometry("700x350")
window.title('CSV-file comparer')

filepath_list = list()
filepath_1 = 'null'
filepath_2 = ''

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')])
    if file:
        filepath = os.path.abspath(file.name)
        Label(window, text="The File is located at : " + str(filepath), font=('Aerial 11')).pack()
        filepath_list.append(filepath)
        
# Add a Label widget
label = Label(window, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button
ttk.Button(window, text="File 1 - Browse", command=open_file).pack(pady=20)
ttk.Button(window, text="File 2 - Browse", command=open_file).pack(pady=20)

window.mainloop()

print(filepath_list)
