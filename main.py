import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

while run:
    root = Tk()
    root.geometry('905x700')
    root.title('HANG MAN')
    root.config(bg="#E7FFFF")

    count = 0
    win_count = 0

    index = random.randint(0, 853)
    with open('words.txt', 'r') as file:
        words = file.readlines()
        selected_word = words[index].strip()


    letter_labels = []
    x = 250
    for i in range(len(selected_word)):
        x += 60
        label = Label(root, text="_", bg="#E7FFFF", font=("arial", 40))
        label.place(x=x, y=450)
        letter_labels.append(label)


    letter_images = {letter: PhotoImage(file=f"assets/{letter}.png") for letter in "abcdefghijklmnopqrstuvwxyz"}

    hangman_images = [PhotoImage(file=f"assets/h{i}.png") for i in range(1, 8)]
    hangman_label = Label(root, bg="#E7FFFF", image=hangman_images[0])
    hangman_label.place(x=300, y=-50)


    button_positions = [
        ['a', 0, 595], ['b', 70, 595], ['c', 140, 595], ['d', 210, 595],
        ['e', 280, 595], ['f', 350, 595], ['g', 420, 595], ['h', 490, 595],
        ['i', 560, 595], ['j', 630, 595], ['k', 700, 595], ['l', 770, 595],
        ['m', 840, 595], ['n', 0, 645], ['o', 70, 645], ['p', 140, 645],
        ['q', 210, 645], ['r', 280, 645], ['s', 350, 645], ['t', 420, 645],
        ['u', 490, 645], ['v', 560, 645], ['w', 630, 645], ['x', 700, 645],
        ['y', 770, 645], ['z', 840, 645]
    ]

    buttons = {}
    for letter, x, y in button_positions:
        buttons[letter] = Button(
            root, bd=0, command=lambda l=letter: check(l),
            bg="#E7FFFF", activebackground="#E7FFFF",
            font=10, image=letter_images[letter]
        )
        buttons[letter].place(x=x, y=y)

    def check(letter):
        """Check if the guessed letter is in the word."""
        global count, win_count, score, run


        buttons[letter].destroy()

        if letter in selected_word:
            for i, char in enumerate(selected_word):
                if char == letter:
                    win_count += 1
                    letter_labels[i].config(text=letter.upper())

            if win_count == len(selected_word):
                score += 1
                answer = messagebox.askyesno('GAME OVER', 'YOU WON! \nWANNA PLAY AGAIN?')
                if answer:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            if count < len(hangman_images):
                hangman_label.config(image=hangman_images[count])
            if count == 6:
                answer = messagebox.askyesno('GAME OVER', 'YOU LOST! \nWANNA PLAY AGAIN?')
                if answer:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()


    def close():
        global run
        answer = messagebox.askyesno('ALERT', 'DO YOU WANT TO EXIT THE GAME?')
        if answer:
            run = False
            root.destroy()

    exit_img = PhotoImage(file='assets/exit.png')
    exit_button = Button(root, bd=0, command=close, bg="#E7FFFF",
                         activebackground="#E7FFFF", font=10, image=exit_img)
    exit_button.place(x=770, y=10)


    score_label = Label(root, text=f"SCORE: {score}", bg="#E7FFFF", font=("arial", 25))
    score_label.place(x=10, y=10)

    root.mainloop()
