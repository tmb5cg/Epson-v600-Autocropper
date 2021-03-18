from pdf2image import convert_from_path 
from tkinter import *
from tkinter import messagebox 
import pdfsplitter

from tkinter import filedialog
from tkinter import *
import tkinter.font as TkFont

def browse_input():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global input_pdf_path
    filename = filedialog.askopenfilename()
    input_pdf_path.set(filename)
    print(filename)

def browse_output():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global output_folder_path
    filename = filedialog.askdirectory()
    output_folder_path.set(filename)
    print(filename)

def pdf2img(): 
    try: 
        images = convert_from_path(str(e2.get())) 
        for img in images: 
            img.save('new_folder\output.jpg', 'JPEG') 
  
    except  : 
        Result = "NO pdf found"
        messagebox.showinfo("Result", Result) 
  
    else: 
        Result = "success"
        messagebox.showinfo("Result", Result) 
  
  
  
def runner():
    month = str(month_var.get())
    year = str(year_var.get())
    print(month + "  " + year) 
    pdfsplitter.split_pdf(input_pdf_path.get(), output_folder_path.get(), month, year)



root = Tk()
root.title("Batch AutoCropper")
fontStyle = TkFont.Font(family="Helvetica",size=12, slant="italic")
fontStyle2 = TkFont.Font(family="Helvetica",size=12,weight="bold")


# // Select input folder path
input_pdf_path = StringVar()
Label(root, text="Consolidated PDF: ", font=fontStyle2).grid(row=0, column=0, sticky=W, padx=5, pady=5)

input_pdf_label = Label(master=root,textvariable=input_pdf_path, font = fontStyle)
input_pdf_label.grid(row=0, column=1,  padx=5, pady=5)
input_browse_button = Button(text="Browse", command=browse_input)
input_browse_button.grid(row=0, column=2)


# // Select output
output_folder_path = StringVar()
Label(root, text="Output folder: ", font=fontStyle2).grid(row=1, column=0, sticky=W,  padx=5, pady=5)

output_folder_label = Label(master=root,textvariable=output_folder_path, font = fontStyle)
output_folder_label.grid(row=1, column=1, padx=5, pady=5)
output_browse_button = Button(text="Browse", command=browse_output)
output_browse_button.grid(row=1, column=2,  padx=5, pady=5)

# Select date (optional)
OPTIONSMONTH = [
"none",
"Jan",
"Feb",
"Mar",
"Apr",
"May",
"Jun",
"Jul",
"Aug",
"Sept",
"Oct",
"Nov",
"Dec"
]

OPTIONSYEAR = [
"1980",
"1981",
"1982",
"1983",
"1984",
"1985",
"1986",
"1987",
"1988",
"1989",
"1990",
"1991",
"1992",
"1993",
"1994",
"1995",
"1996",
"1997",
"1998",
"1999",
"2000",
"2001",
"2002",
"2003",
"2004",
"2005",
"2006",
"2007",
"2008",
"2009",
"2010",
"none"
]

month_var = StringVar()
month_var.set(OPTIONSMONTH[0]) # default value

month_dropdown = OptionMenu(root, month_var, *OPTIONSMONTH)
month_dropdown.grid(row=3, column=0)

# reverse so we set default value year to None
OPTIONSYEAR.reverse()
year_var = StringVar()
year_var.set(OPTIONSYEAR[0]) # default value

year_dropdown = OptionMenu(root, year_var, *OPTIONSYEAR)
year_dropdown.grid(row=3, column=1)


# // Autocrop button
autocrop_button = Button(text="Autocrop", command=runner)
autocrop_button.grid(row=4, column=0, columnspan=3, padx=5,pady=5)

mainloop()