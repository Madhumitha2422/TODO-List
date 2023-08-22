import tkinter
from tkinter import*
import winsound

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.config(bg="pink3")
root.resizable(False,False)

task_list=[]

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("C:/Users/Madhumitha/Downloads/Image/tasklist.txt.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

        winsound.Beep(500,200)


def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("C:/Users/Madhumitha/Downloads/Image/tasklist.txt.txt","w")as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")

        listbox.delete( ANCHOR)        

        winsound.Beep(500,200)

def openTaskFile():

    try:
        global task_list
        with open("C:/Users/Madhumitha/Downloads/Image/tasklist.txt.txt","r") as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task!="\n":
                 task_list.append(task)
                 listbox.insert(END,task)


    except:
        file=open("C:/Users/Madhumitha/Downloads/Image/tasklist.txt.txt","w")
        file.close()


image_icon=PhotoImage(file="C:/Users/Madhumitha/Downloads/Image/task.png")
root.iconphoto(False,image_icon)

TopImage=PhotoImage(file="C:/Users/Madhumitha/Downloads/Image/topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="C:/Users/Madhumitha/Downloads/Image/dock.png")
Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)

noteImage=PhotoImage(file="C:/Users/Madhumitha/Downloads/Image/task.png")
Label(root,image=noteImage,bg="#32405b").place(x=340,y=25)

heading=Label(root,text="All TASK",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)

frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()


button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=("arial",12),width=40,height=16,bg="#324056",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

Delete_icon=PhotoImage(file="C:/Users/Madhumitha/Downloads/Image/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)
             


root.mainloop()
