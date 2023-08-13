from tkinter import *
from tkinter import messagebox
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
WHITE_COLOR = "#ffffff"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
current_card = {}


def know_the_word():
    global current_card, to_learn
    try:
        to_learn.remove(current_card)
        dict_df = pandas.DataFrame(to_learn)
        dict_df.to_csv("data/words_to_learn.csv", index=False)
        new_key()
    except:
        messagebox.showinfo(title="Congrats!",
                            message="You already known all the words! Remaking words_to_learn list...")
        data = pandas.read_csv("data/french_words.csv")
        to_learn = data.to_dict(orient="records")
        df = pandas.DataFrame(to_learn)
        df.to_csv("data/words_to_learn.csv", index=False)


def new_key():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    front_card.itemconfig(image, image=front_card_image)
    front_card.itemconfig(card_word, text=current_card["French"], fill="black")
    front_card.itemconfig(card_title, text="French", fill="black")
    flip_timer = screen.after(3000, func=change_card)


def change_card():
    front_card.itemconfig(image, image=back_card_image)
    front_card.itemconfig(card_word, text=current_card["English"], fill="white")
    front_card.itemconfig(card_title, text="English", fill="white")


screen = Tk()
screen.title("Flash Card French Learning")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = screen.after(3000, func=change_card)

front_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
image = front_card.create_image(400, 263, image=front_card_image)
front_card.grid(row=1, column=1)
card_title = front_card.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = front_card.create_text(400, 283, text="word", font=("Arial", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_key)
wrong_button.place(x=200, y=530)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=know_the_word)
right_button.place(x=500, y=530)

nothing_label = Label(text="", highlightthickness=0, height=100, bg=BACKGROUND_COLOR)
nothing_label.grid(column=0, row=2)
new_key()

screen.mainloop()
