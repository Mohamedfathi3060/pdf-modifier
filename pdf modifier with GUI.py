import PyPDF2
from tkinter import *
from tkinter import messagebox


def merge_files():
    path_1 = enter_1.get()
    path_2 = enter_2.get()
    file = PyPDF2.PdfFileMerger()
    file.append(PyPDF2.PdfFileReader(path_1, "rb"))
    file.append(PyPDF2.PdfFileReader(path_2, "rb"))
    new_file_name = "merged pdf"
    file.write(f"{new_file_name}.pdf")
    messagebox.showinfo("confirmation message", "done successfully!")


def extract_page():
    path = enter_1.get()
    page_number = int(enter_3.get())
    file = open(path, "rb")
    reader = PyPDF2.PdfFileReader(file)
    ###########################
    output = PyPDF2.PdfFileWriter()
    output.addPage(reader.getPage(page_number-1))
    with open(f"{page_number}_page.pdf", "wb") as output_stream:
        output.write(output_stream)
    messagebox.showinfo("confirmation message", "done successfully!")


def split_into_pages():
    path = enter_1.get()
    input_pdf = PyPDF2.PdfFileReader(path)
    for i in range(input_pdf.numPages):
        output = PyPDF2.PdfFileWriter()
        output.addPage(input_pdf.getPage(i))
        with open(f"{i+1}_page.pdf", "wb") as output_stream:
            output.write(output_stream)
    messagebox.showinfo("confirmation message", "done successfully!")


window = Tk()
window.title("pdf==>GUI")
window.minsize(width=1000, height=500)
img = PhotoImage(file="pdf_new.png")
label = Label(image=img)
label.place(x=580, y=0)
# label
label = Label(window, text="pdf modifier", font=("Arial", 30, "bold"))
label.place(x=150)

tip = Label(window, text="TIP:attach pdf files in the project file to be available", font=("Arial", 10))
tip.place(x=10, y=430)
# button

# entry
enter_1 = Entry(window, width=50)
enter_1.insert(0, "enter path followed by .pdf")
enter_1.place(x=250, y=175)

enter_2 = Entry(window, width=50)
enter_2.insert(0, "enter path 2 'if needed' followed by .pdf")
enter_2.place(x=250, y=235)

enter_3 = Entry(window, width=50)
enter_3.insert(0, "enter page number 'if needed'")
enter_3.place(x=250, y=295)

bt_merge = Button(text="merge two pdf files", command=merge_files, width=30 , height=1)
bt_merge.place(x=0, y=170)

bt_extract = Button(text="extract a page from pdf file", command=extract_page, width=30)
bt_extract.place(x=0, y=230)

bt_split = Button(text="split pdf file into pages", command=split_into_pages, width=30)
bt_split.place(x=0, y=290)

window.mainloop()

