from tkinter import *
import time
from tkinter import messagebox
sample = 'Some people combine touch typing and hunt and peck by using a buffering method. In the buffer method, the typist looks at the source copy, mentally stores one or several sentences, then looks at the keyboard and types out the buffer of sentences. This eliminates frequent up and down motions with the head and is used in typing competitions in which the typist is not well versed in touch typing. Not normally used in day-to-day contact with keyboards, this buffer method is used only when time is of the essence.'
start_time = 0
cnt = 0
highscore_speed = 0
highscore_accuracy = 0

#--- check ---#
def start(event):
    global start_time
    global cnt
    if cnt == 0:
        start_time = time.time()
        print('hi')
    cnt += 1

def check():
    global cnt
    global highscore_speed
    global highscore_accuracy
    words = 0
    for i in range(len(entry.get().split(' '))):
        if entry.get().split(' ')[i] == sample.split(' ')[i]:
            words += 1
    end_time = time.time()
    speed = round(words/(end_time-start_time),2)
    accuracy = round(words/len(sample)*100,2)
    if speed > highscore_speed and accuracy > highscore_accuracy:
        msg = messagebox.showinfo(title='Test Completed!',message=  f'Congrats! Your words per second is {speed} and accuracy is {accuracy}%! You beat your highscore of {highscore_speed} words per second and {highscore_accuracy}% accuracy')
        highscore_speed = speed
        highscore_accuracy = accuracy
    else:
        msg = messagebox.showinfo(title='Test Completed!',message=  f'Your words per second is {speed}! and accuracy is {accuracy}%! Your current highscore is {highscore_speed} words per second and {highscore_accuracy}% accuracy' )
    words = 0
    cnt = 0
    entry.delete(0,'end')

#--- UI ---#
window = Tk()
window.title('Typing Speed Test')
window.config(padx=50,pady=50)

label = Label(text=sample,wraplength=500,justify=CENTER,padx=50,pady=50,bg='white',font=30)
label.grid(row=0,column=0,columnspan=2)

entry = Entry(width=80)
entry.grid(row=1,column=1)
entry.bind('<Key>', start)
label = Label(text='Type here:',pady=20,font=('Courier',15,'bold'))
label.grid(row=1, column=0)
button = Button(text='Done', command=check,font=('Courier',15,'bold'))
button.grid(row=2,column=0,columnspan=2,padx=5,pady=5,ipadx=100)


window.mainloop()



