import tkinter as tk
from tkinter import filedialog
import pdf2image

def get_data(filename):
    from img2text import get_text
    print(get_text(filename))

def open_pdf_gui():  
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(filetypes=[('PDF files', '.pdf')])
    #replace in filename "/" with "\\"
    filename = filename.replace("/", "\\")
    pages = pdf2image.convert_from_path( filename, dpi=500, output_file="tmp.jpg" ,poppler_path='C:\\Program Files (x86)\\newPath\\poppler-0.68.0\\bin')
    for i, image in enumerate(pages):
        fname = 'image_'+str(i)+'.jpg'
        image.save(fname, "JPEG")
    
        get_data(fname)
      
open_pdf_gui()
