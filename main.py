from tkinter import *
import random

result_list = ["It is certain", "As I see it, yes", "Reply hazy, try again", "Don't count on it", "It is decidedly so",
               "Most likely", "Ask again later", "My reply is no", "Without a doubt", "Outlook good",
               "Better not tell you now", "My sources say no", "Yes - definitely", "Yes", "Cannot predict now",
               "Outlook not so good", "You may rely on it", "Signs point to yes", "Concentrate and ask again",
               "Very doubtful"]

root = Tk()

answer = IntVar()
question = StringVar()

root.geometry('600x500')
root.resizable(0, 0)
root.title("Magic 8-Ball")
root.configure(bg='black')

canvas = Canvas(root, bg='black', height=500, width=400, highlightthickness=0)
canvas.pack(expand=YES, fill=None)
canvas.create_polygon(25, 40, 400, 40, 200, 350, 25, 40, fill='blue', outline='dark blue', width=4)


def get_answer():
    if question.get() != "":
        canvas.delete("result")
        answer.set(random.randint(1, 20))
        canvas.create_text(210, 120, width=200, text=result_list[answer.get()], fill='white', font='arial 18 bold',
                           tag="result")
        question.set("")


def _exit():
    root.destroy()


Label(root, bg='black', foreground='white', font='arial 14 bold', text='Ask a question:').place(x=20, y=350)
Entry(root, font='arial 14', textvariable=question, bg='ghost white').place(x=350, y=350)
Button(root, font='arial 14 bold', bg='blue', foreground='white', text='CLICK FOR ANSWER', padx=2, command=get_answer).\
    place(x=200, y=400)

Button(root, font='arial 14 bold', bg='red', foreground='white', text='EXIT', padx=2, command=_exit).place(x=275, y=450)

root.mainloop()