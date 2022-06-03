import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400,bg='black')
canvas1.pack()



entry1 = tk.Entry (root)
entry2 = tk.Entry (root)
canvas1.create_window(100, 80, window=entry1)
canvas1.create_window(300, 80, window=entry2)

def getSquareRoot ():  
    x1 = entry1.get()
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(200, 40, window=label1)
def getsum ():
  x1 = entry1.get()
  x2 = entry2.get()
  label1 = tk.Label(root, text= int(x1) + int(x2))
  label1.config(font=('helvetica', 12, 'bold', 'underline'),fg='black')
  canvas1.create_window(200, 40, window=label1)
def getdifference():
  x1 = entry1.get()
  x2 = entry2.get()
  label1 = tk.Label(root, text= int(x1) - int(x2))
  label1.config(font=('helvetica', 12, 'bold', 'underline'),fg='black')
  canvas1.create_window(200, 40, window=label1)
def getproduct():
  x1 = entry1.get()
  x2 = entry2.get()
  label1 = tk.Label(root, text= int(x1) * int(x2))
  label1.config(font=('helvetica', 12, 'bold', 'underline'),fg='black')
  canvas1.create_window(200, 40, window=label1)
def getquotient():
  x1 = entry1.get()
  x2 = entry2.get()
  label1 = tk.Label(root, text= int(x1) / int(x2))
  canvas1.create_window(200, 40, window=label1)

button1 = tk.Button(text='Get the Sum', command=getsum)
button2 = tk.Button(text='Get the Difference', command=getdifference)
button3 = tk.Button(text='Get the Product', command=getproduct)
button4 = tk.Button(text='Get the Quotient', command=getquotient)
button5=tk.Button(text='Get the square root',command=getSquareRoot)
canvas1.create_window(200, 130, window=button1)
canvas1.create_window(200, 180, window=button2)
canvas1.create_window(200, 230, window=button3)
canvas1.create_window(200, 280, window=button4)
canvas1.create_window(200,330,window=button5)

root.mainloop()
