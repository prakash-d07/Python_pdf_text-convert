
##Import libraries

import tkinter as tk
from PIL import Image, ImageTk
import PyPDF2
from tkinter.filedialog import askopenfile

root=tk.Tk()
root.title("Python app")

## mak
mycanvas=tk.Canvas(root,width=600,height=300)
mycanvas.grid(columnspan=3,rowspan=2)


logo=Image.open('logo.png')
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.grid(column=1,row=0)


instructions=tk.Label(root,text="Select a PDF file from your computer to extract all its text", font="bold")
instructions.grid(columnspan=3, column=0,row=1)


browse_text= tk.StringVar()
browse_button=tk.Button(root,textvariable=browse_text,command=lambda:open_file(),height=2,width=15,bg='black',fg='white')
browse_text.set("Browse")
browse_button.grid(column=1,row=2)

def open_file():
    
    browse_text.set('Loading')
    file=askopenfile(parent=root,mode='rb',title="choose a file",filetypes=[("Pdf file","*.pdf")])
    if file:
        read_pdf=PyPDF2.PdfFileReader(file)
        page=read_pdf.getPage(0)
        page_content=page.extractText()


        text_box=tk.Text(root,height=5,width=100,padx=15,pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_add
        text_box.grid(column=1,row=3)

        browse_text.set("Browse")



mycanvas=tk.Canvas(root,width=100,height=100)
mycanvas.grid()


root.mainloop()