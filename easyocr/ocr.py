import os
import fitz

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Pdf to Jpg')
root.resizable(False, False)
root.geometry('300x150')


def pdf2jpg(file_name):
    pdf_file_path=file_name
    zoom_x=2
    zoom_y=2
    mat = fitz.Matrix(zoom_x,zoom_y)
    doc = fitz.open(pdf_file_path)

    file= file_name.rsplit('.',maxsplit=1)[0]
    #
    for page in doc:
        img_path = f"{file}_{page.number}.jpg"
        pix = page.get_pixmap(matrix = mat)
        pix.save(img_path)


def select_file():
    filetypes = (('pdf files', '*.pdf'),('All files', '*.*'))

    filename = fd.askopenfilename(title='Open a file',initialdir='/',
        filetypes=filetypes)
    file= filename.rsplit('.',maxsplit=1)[0]
    showinfo( title='Selected File',message=filename+" to "+ file +".jpg" )
    pdf2jpg(filename)

# open button
open_button = ttk.Button(root ,text='Open a File',command=select_file)

open_button.pack(expand=True)







# run the application
root.mainloop()