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
    
    #TODO ask user to isntall poppler, if installed choose path and save it to file.
    
    try:
        pages = pdf2image.convert_from_path( filename, dpi=500, output_file="tmp.jpg" ,poppler_path='C:\\Program Files (x86)\\newPath\\poppler-0.68.0\\bin')
    except:
        print("You need to install Poppler and and it to PATH!\n\nDownlaod Poppler at https://github.com/oschwartz10612/poppler-windows/releases/")
        input("Press Enter to exit.")
        return
    for i, image in enumerate(pages):
        fname = 'image_'+str(i)+'.jpg'
        image.save(fname, "JPEG")
    
        get_data(fname)
      
open_pdf_gui()
