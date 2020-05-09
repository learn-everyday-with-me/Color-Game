from tkinter import *
from tkinter import messagebox, ttk
root = Tk()
root.title("Game")
root.configure(bg="#BCF5A9")
root.geometry("225x190")
b = [[2,2,0],[1,1,0],[2,0,1]]
def check():
    global b
    for i in range(0,3):
         for j in range(0,3):
             if(b[i][j] == 0):
                 eval("a"+str(3*i + j + 1)).configure(bg="white")
             elif(b[i][j] == 1):
                 eval("a"+str(3*i + j + 1)).configure(bg="#E6E6E6")
             elif(b[i][j] == 2):
                 eval("a"+str(3*i + j + 1)).configure(bg="#6E6E6E")
def submitted():
    a = messagebox.askyesno(title="Are you sure to submit?",message = "All the boxes should be black to win the game")
    if(a==1):
        p = 1
        for _ in b:
            for __ in _:
                p *= __
        if (p == 2**9):
            messagebox.showinfo(title = "Hurray",message = "YOW WON")
            root.quit()
        else:
            messagebox.showinfo(title = "RETRY",message = "YOU LOSE  ---  RETRY")
    else:
        pass
def refresh():
    global b
    b = [[2,2,0],[1,1,0],[2,0,1]]
    check()
def change(d,c):
    global b
    if (d==0 and c==0):
        b[0][0] = (b[0][0] + 1) % 3
        b[0][1] = (b[0][1] + 1) % 3
        b[1][0] = (b[1][0] + 1) % 3
        b[1][1] = (b[1][1] + 1) % 3
    if (d==0 and c==1):
        b[0][0] = (b[0][0] + 1) % 3
        b[0][1] = (b[0][1] + 1) % 3
        b[0][2] = (b[0][2] + 1) % 3
    if (d==0 and c==2):
        b[0][1] = (b[0][1] + 1) % 3
        b[0][2] = (b[0][2] + 1) % 3
        b[1][1] = (b[1][1] + 1) % 3
        b[1][2] = (b[1][2] + 1) % 3
    if (d==1 and c==0):
        b[0][0] = (b[0][0] + 1) % 3
        b[1][0] = (b[1][0] + 1) % 3
        b[2][0] = (b[2][0] + 1) % 3
    if (d==1 and c==1):
        b[0][1] = (b[0][1] + 1) % 3
        b[1][0] = (b[1][0] + 1) % 3
        b[1][1] = (b[1][1] + 1) % 3
        b[1][2] = (b[1][2] + 1) % 3
        b[2][1] = (b[2][1] + 1) % 3
    if (d==1 and c==2):
        b[0][2] = (b[0][2] + 1) % 3
        b[1][2] = (b[1][2] + 1) % 3
        b[2][2] = (b[2][2] + 1) % 3
    if (d==2 and c==0):
        b[2][0] = (b[2][0] + 1) % 3
        b[2][1] = (b[2][1] + 1) % 3
        b[1][0] = (b[1][0] + 1) % 3
        b[1][1] = (b[1][1] + 1) % 3
    if (d==2 and c==1):
        b[2][0] = (b[2][0] + 1) % 3
        b[2][1] = (b[2][1] + 1) % 3
        b[2][2] = (b[2][2] + 1) % 3
    if (d==2 and c==2):
        b[2][1] = (b[2][1] + 1) % 3
        b[2][2] = (b[2][2] + 1) % 3
        b[1][1] = (b[1][1] + 1) % 3
        b[1][2] = (b[1][2] + 1) % 3
    check()
ttk.Label(root,text = "Make all the boxes black",background = "#BCF5A9").grid(row=0,columnspan=3)
a1 = Button(root,text = "1",command = lambda: change(0,0),width=5,bg="white")
a1.grid(row=0+1,column=0,padx=10,pady=10)
a2 = Button(root,text = "2",command = lambda: change(0,1),width=5,bg="white")
a2.grid(row=0+1,column=1,padx=10,pady=10)
a3 = Button(root,text = "3",command = lambda: change(0,2),width=5,bg="white")
a3.grid(row=0+1,column=2,padx=10,pady=10)
a4 = Button(root,text = "4",command = lambda: change(1,0),width=5,bg="white")
a4.grid(row=1+1,column=0,padx=10,pady=10)
a5 = Button(root,text = "5",command = lambda: change(1,1),width=5,bg="white")
a5.grid(row=1+1,column=1,padx=10,pady=10)
a6 = Button(root,text = "6",command = lambda: change(1,2),width=5,bg="white")
a6.grid(row=1+1,column=2,padx=10,pady=10)
a7 = Button(root,text = "7",command = lambda: change(2,0),width=5,bg="white")
a7.grid(row=2+1,column=0,padx=10,pady=10)
a8 = Button(root,text = "8",command = lambda: change(2,1),width=5,bg="white")
a8.grid(row=2+1,column=1,padx=10,pady=10)
a9 = Button(root,text = "9",command = lambda: change(2,2),width=5,bg="white")
a9.grid(row=2+1,column=2,padx=10,pady=10)
submit = Button(root,text="Submit",command = submitted,bg="light green")
submit.grid(row=4,column=0)
check()
refresh_button = Button(root,text = "Refresh",command = refresh,bg="light blue")
refresh_button.grid(row=4,column=2)
root.mainloop()
