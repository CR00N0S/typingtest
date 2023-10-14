import tkinter.messagebox
from tkinter import *
from wordlist import word_list
import random
from timeit import default_timer as timer

TITLE_FONT = "Arial"
TITLE = "#00ADB5"
WORD_FONT = "Times New Roman"
WORD = "#EEEEEE"
BACKGROUND = "#222831"
RANDOM_WORD = random.choice(word_list)
WORDS_TYPED = 0


def random1():
    global RANDOM_WORD
    RANDOM_WORD = random.choice(word_list)
    text_entry.delete(0, END)
    word_label.config(text=RANDOM_WORD)


def check(sv):
    global RANDOM_WORD, WORDS_TYPED
    time = timer()
    current_letter = (len(sv.get()) - 1)
    if time >= 300000:
        tkinter.messagebox.showinfo("Results", f"your speed is {(WORDS_TYPED / 5) / 0.5} wpm")

    if sv.get() == RANDOM_WORD:
        WORDS_TYPED += len(RANDOM_WORD)
        random1()
    elif sv.get():
        try:
            if sv.get()[current_letter] != RANDOM_WORD[current_letter]:
                word_label.config(text=f"{RANDOM_WORD}", bg="Red")
            else:
                word_label.config(text=f"{RANDOM_WORD}", bg=BACKGROUND)
        except IndexError:
            word_label.config(text=f"{RANDOM_WORD}", bg="Red")



root = Tk()
root.title('Typing Test')
root.config(padx=25, pady=25, bg=BACKGROUND)
root.geometry("750x500")

title_label = Label(text="Typing Test", font=(TITLE_FONT, 54, "bold"), fg=TITLE, bg=BACKGROUND)
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

word_label = Label(text=f"{RANDOM_WORD}", font=(WORD_FONT, 44), fg=WORD, bg=BACKGROUND)
word_label.place(relx=0.5, rely=0.5, anchor=CENTER)

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: check(sv))
text_entry = Entry(root, width=15, font=(f"{WORD_FONT}", 24), textvariable=sv)
text_entry.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
