import pathlib
import datetime
import tkinter as tk

root= tk.Tk()

def writeToFile(entry):
    file = pathlib.Path("diary.txt")
    if file.exists ():
        f = open("diary.txt", "a")
        timestamp = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        f.write("\n" +  timestamp+ ": " + entry)
        f.close()

    else:
        print ("File not exist")
    
    return

def makeEntry():
    entry = entry1.get()
    writeToFile(entry)


canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Daily Notes')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)


entry1 = tk.Entry (root)
canvas1.create_window(150, 140, window=entry1)


    
button1 = tk.Button(text='Add', command=makeEntry, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(150, 280, window=button1)

root.mainloop()
