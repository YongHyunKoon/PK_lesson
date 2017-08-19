import tkinter

root = tkinter.Tk()

val = tkinter.IntVar()
val.set(0)

#def tbox_enter(event):
#  label.config(text = int(tbox.get()))
#def tbox_enter2(event):
#  label.config(text = int(tbox_2.get()))
def result():
    val.set(int(tbox.get())+int(tbox_2.get()))
    label.config(text = "Result = %d" % val.get())    
def add_event(event): #버튼은 event bind가 안되기 때문에 랩핑을 해야하므로 함수를 한개 더쓴다
    result()

label = tkinter.Label(root, text='Result= %d' % val.get())
label.pack(side="top")

label2 = tkinter.Label(root, text=' + ')

tbox = tkinter.Entry(root, width=7)
tbox_2 = tkinter.Entry(root, width=7)
button = tkinter.Button(root, text="add", command=result)

#tbox.bind('<Return>', tbox_enter)
#tbox_2.bind('<Return>', tbox_enter2)

tbox.bind('<Return>', add_event)
tbox_2.bind('<Return>', add_event)

tbox.pack(side="left")
label2.pack(side="left")
tbox_2.pack(side="left")
button.pack(side="left")

root.mainloop()
