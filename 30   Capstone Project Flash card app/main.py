from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("data/french_words.csv")
    # print(original_file)
    to_learn = original_file.to_dict(orient="records")
else:
    # to_learn = data.to_dict(orient="index")
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(canvas_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text="French", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}")
    canvas.itemconfig(canvas_background, image=back_image)


def known_words():
    to_learn.remove(current_card)
    # print(len(to_learn))
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Create a Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 265, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_word = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_word.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
known_word = Button(image=right_image, highlightthickness=0, command=known_words)
known_word.grid(column=1, row=1)

next_card()

window.mainloop()
