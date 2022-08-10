from tkinter import *
import math
import datetime
from tkinter import filedialog
import pytz

# Create New File


def new_file():
    batchNumber.delete(0, END)
    batchReturnLabel.config(text="")
    productReturnLabel.config(text="")
    tankEntry.delete(0, END)
    tankReturnLabel.config(text="")
    sieveReturnLabel.config(text="")
    residueEntry1.delete(0, END)
    residueEntry2.delete(0, END)
    answer.config(text="")
    resReturn2.config(text="")
    resReturn1.config(text="")
    visEntry.delete(0, END)
    visReturn.config(text="")
    textbox.delete(1.0, END)
    root.title("New File - Lab Test")
    status_bar.config(text="New File - Ready", font=("TkDefaultFont, 12"))


def batchReturn(batch):
    batchReturnLabel.config(text=batchNumber.get())
    status_bar.config(text="Batch: " + batchNumber.get(),
                      font=("TkDefaultFont, 12"))


def productReturn(product):
    productReturnLabel.config(text=product)


def sieveReturn(sieve):
    sieveReturnLabel.config(text=sieve)


def tankReturn(tank):
    tankReturnLabel.config(text=tankEntry.get())


def residueReturn1(res1):
    resReturn1.config(text=residueEntry1.get())


def residueReturn2(res2):
    resReturn2.config(text=residueEntry2.get())


def residueFinal():
    try:
        x = float(resReturn1.cget("text"))
        y = float(resReturn2.cget("text"))

        answer.config(text=round((y / x) * 100, 2))
    except ValueError:
        answer.config(text="Error")


def viscosityReturn(vis):
    visReturn.config(text=visEntry.get())
    if productReturnLabel.cget("text") == "CRS-2P":
        try:
            a = int(visReturn.cget("text"))
            b = a * 0.97
            visReturn.config(text=round(b))
        except ValueError:
            visReturn.config(text="Error")


def visMinutes(minutes):
    try:
        min1 = int(visReturn.cget("text"))
        min1 = min1 // 60
        sec1 = int(visReturn.cget("text"))
        sec1 = sec1 - (min1 * 60)
        totalMin = ("{:02d}".format(min1) + ":" + "{:02d}".format(sec1))
        visMinReturn.config(text=totalMin)

    except:
        visMinReturn.config(text="Error")


def resultSend():
    file1 = open("Test_Results.txt", "a")
    file1.write("Batch: ")
    file1.write(str(batchReturnLabel.cget("text")))
    file1.write("\n")
    file1.write(str(timestamp))
    file1.write("\n")
    file1.write("Product: ")
    file1.write(str(productReturnLabel.cget("text")))
    file1.write("\n")
    file1.write("Tank: ")
    file1.write(str(tankReturnLabel.cget("text")))
    file1.write("\n")
    file1.write("Sieve: ")
    file1.write(str(sieveReturnLabel.cget("text")))
    file1.write("\n")
    file1.write("Residue: ")
    file1.write("(")
    file1.write(str(resReturn1.cget("text")))
    file1.write(",")
    file1.write(str(resReturn2.cget("text")))
    file1.write(") ")
    file1.write(str(answer.cget("text")))
    file1.write("\n")
    file1.write("Viscosity: ")
    file1.write(str(visReturn.cget("text")))
    file1.write(" (total sec), ")
    file1.write(str(visMinReturn.cget("text")))
    file1.write(" (min/sec)")
    file1.write("\n")
    file1.write("Comments: ")
    file1.write(textbox.get(1.0, END))
    file1.write("\n")
    file1.write("\n")
    file1.write("\n")
    file1.close()
    status_bar.config(text="File Submited to \n 'Test_Results.txt'",
                      font=("TkDefaultFont, 12"))


root = Tk()
root.title("Lab Test")
root.iconbitmap("report.png")
root.geometry("680x440")


frame1 = Frame(root, width=300, height=450)
frame1.pack(side=LEFT, anchor=N)

frame2 = LabelFrame(root, text="  Results  ", width=300,
                    height=400, highlightbackground="black", labelanchor="n")
frame2.pack(side=LEFT, anchor=N, ipady=3, ipadx=0, padx=10)
# Status bar on bottom
status_bar = Label(root, text="Ready", font=("TkDefaultFont, 12"), anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


# Menu
my_menu = Menu(root)
root.config(menu=my_menu)
# Menu Items
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Time display/ configuration
mtntime = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
timestamp = mtntime.strftime('%m/%d/%Y %I:%M:%S %p')
timeLabel = Label(frame1, text=timestamp)
timeLabel.grid(row=0, column=0, columnspan=4, sticky="w")


# Batch Number
batchLabel = Label(frame1, text="Batch #:")
batchNumber = Entry(frame1, width=4)
batchNumber.bind("<Return>", batchReturn)
batchLabel.grid(row=1, column=0, sticky="w")
batchNumber.grid(row=1, column=1, sticky="w")
batchReturnLabel = Label(frame2)
batchReturnLabel.grid(row=1, column=4, sticky="w", pady=(4, 0))

# Product Label/Buttons
productLabel = Label(frame1, text="Product:")
productReturnLabel = Label(frame2)
product1 = Button(frame1, text="CSS-1H",
                  command=lambda: productReturn("CSS-1H"))
product2 = Button(frame1, text="CRS-2P",
                  command=lambda: productReturn("CRS-2P"))
product3 = Button(frame1, text="CQS-1HP",
                  command=lambda: productReturn("CQS-1HP"))


# Product Button layout
productLabel.grid(row=2, column=0, sticky="w")
product1.grid(row=2, column=1, sticky="w")
product2.grid(row=2, column=2, sticky="w")
product3.grid(row=2, column=3, sticky="w")
productReturnLabel.grid(row=2, column=4, sticky="w", pady=(9, 0))


# Tank Label/ Entry / layout
tankLabel = Label(frame1, text="Tank:")
tankEntry = Entry(frame1, width=4)
tankEntry.bind("<Return>", tankReturn)
tankLabel.grid(row=3, column=0, sticky="w")
tankEntry.grid(row=3, column=1, sticky="w")
tankReturnLabel = Label(frame2)
tankReturnLabel.grid(row=3, column=4, sticky="w", pady=2)


# Sieve Label/ Buttons
sieveLabel = Label(frame1, text="Sieve:")
sieveReturnLabel = Label(frame2)
sievePass = Button(frame1, text="PASS", command=lambda: sieveReturn("PASS"))
sieveFail = Button(frame1, text="FAIL", command=lambda: sieveReturn("FAIL"))


# Sieve Button Layout
sieveLabel.grid(row=4, column=0, sticky="w")
sievePass.grid(row=4, column=1, sticky="w")
sieveFail.grid(row=4, column=2, sticky="w")
sieveReturnLabel.grid(row=4, column=4, sticky="w", pady=1)

# Residue return


# Residue Label/ Entries
residueLabel1 = Label(frame1, text="Residue 1:")
residueEntry1 = Entry(frame1, width=4)
residueEntry1.bind("<Return>", residueReturn1)
residueLabel2 = Label(frame1, text="Residue 2:")
residueEntry2 = Entry(frame1, width=4)
residueEntry2.bind("<Return>", residueReturn2)
residueLabel3 = Label(frame1, text="Final Residue:")
calculate = Button(frame1, text="Calculate", command=residueFinal)
answer = Label(frame2)
resReturn2 = Label(frame2)
resReturn1 = Label(frame2)

# Residue layout
residueLabel1.grid(row=5, column=0, sticky="w")
residueEntry1.grid(row=5, column=1, sticky="w")
residueLabel2.grid(row=6, column=0, sticky="w")
residueEntry2.grid(row=6, column=1, sticky="w")
residueLabel3.grid(row=7, column=0, sticky="w")
resReturn1.grid(row=5, column=4, sticky="w", pady=1)
resReturn2.grid(row=6, column=4, sticky="w", pady=1)
calculate.grid(row=7, column=1, columnspan=2, sticky="w")
answer.grid(row=7, column=4, sticky="w", pady=4)

# Viscosity entry
visLabel = Label(frame1, text="Viscosity (Seconds):")
visEntry = Entry(frame1, width=4)
visEntry.bind("<Return>", viscosityReturn, add="+")
visEntry.bind("<Return>", visMinutes, add="+")
visReturn = Label(frame2)
visMinReturn = Label(frame2)
visLabel.grid(row=8, column=0, sticky="w")
visEntry.grid(row=8, column=1, sticky="w")
visReturn.grid(row=8, column=4, sticky="w", pady=1)
visMinReturn.grid(row=8, column=5, sticky="w", pady=1)
# Comments box
clabel = Label(frame2, text="Comments:")
clabel.grid(row=9, column=0, columnspan=100, sticky="nw", pady=(8, 0))
textbox = Text(frame2, width=20, height=5, wrap=WORD)
textbox.grid(row=10, column=0, columnspan=100, sticky="w")

result_send = Button(frame2, text="Submit", command=resultSend)
result_send.grid(row=11, column=3, columnspan=100, padx=18)

root.mainloop()
