"""Importing required libraries"""
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from random import randint

"""Colours constants and global variables"""
BG_COLOUR = "#82F5F5"
WIN = "#27F506"
LOSE = "#E74C3C"
your_score = 0
computer_score = 0


def play(user_choice, computer_choice):
    """The Game's logic and score update."""
    global your_score
    global computer_score
    image_label.config(image=images_user[user_choice])
    image_label_2.config(image=images_comp[computer_choice])
    if user_choice == computer_choice:
        feedback.config(text="Draw!", fg="black")
    elif ((user_choice == 2 and computer_choice == 0) or
          (user_choice == 1 and computer_choice == 2) or
          (user_choice == 0 and computer_choice == 1)):
        your_score += 1
        feedback.config(text="You win!\n+1", fg=WIN)
    else:
        computer_score += 1
        feedback.config(text="You lose.", fg="red")
    player_label.config(text=f"Player's score: {your_score}")
    comp_label.config(text=f"Computer's score: {computer_score}")


def rock_command():
    """Choosing rock"""
    user_choice = 0
    computer_choice = randint(0, 2)
    play(user_choice, computer_choice)


def scissors_command():
    """Choosing scissors."""
    user_choice = 1
    computer_choice = randint(0, 2)
    play(user_choice, computer_choice)


def paper_command():
    """Choosing paper."""
    user_choice = 2
    computer_choice = randint(0, 2)
    play(user_choice, computer_choice)


def end():
    """Game end layout amd winner announcement based on final score."""
    image_label.config(image=images_user[0])
    image_label_2.config(image=images_comp[0])
    if your_score > computer_score:
        feedback.config(text=f"You won!\n{your_score}/{computer_score}", fg=WIN)
    elif computer_score > your_score:
        feedback.config(text=f"You Lost.\n{your_score}/{computer_score}", fg=LOSE)
    else:
        feedback.config(text=f"Draw!\n{your_score}/{computer_score}")


def restart():
    """Restarting the game"""
    global your_score
    global computer_score
    feedback.config(text="Ready!", fg="black")
    your_score = 0
    computer_score = 0
    player_label.config(text=f"Player's score: {your_score}")
    comp_label.config(text=f"Computer's score: {computer_score}")


"""Window setup"""
window = Tk()
window.title("Rock, paper and scissors Game.")
window.geometry("1180x600")
window.config(padx=20, pady=20, bg=BG_COLOUR)

"""Greeting and rules clarification message."""
ready = messagebox.askyesno(message="Welcome to Rock, Paper and Scissors game.\n"
                            "The game's rules are simple:\nRock beats scissors,\n"
                            "scissors beats paper\n"
                            "and paper beats rock.")
if ready:

    """Creating two frames one for user and other for computer."""
    frame_1 = Frame(window)
    frame_2 = Frame(window)
    frame_1.grid(row=2, column=0)
    frame_2.grid(row=2, column=2)

    """Getting images and resizing them."""
    rock_p = Image.open('rock.png')
    rock_p = rock_p.resize((200, 200))
    paper_p = Image.open('paper.png')
    paper_p = paper_p.resize((200, 200))
    scissor_p = Image.open('scissors.png')
    scissor_p = scissor_p.resize((200, 200))

    """Flipping images for the right side"""
    rock_c = rock_p.transpose(Image.FLIP_LEFT_RIGHT)
    paper_c = paper_p.transpose(Image.FLIP_LEFT_RIGHT)
    scissor_c = scissor_p.transpose(Image.FLIP_LEFT_RIGHT)

    """Addition of images to Tk"""
    rock_p = ImageTk.PhotoImage(rock_p)
    rock_c = ImageTk.PhotoImage(rock_c)
    paper_p = ImageTk.PhotoImage(paper_p)
    paper_c = ImageTk.PhotoImage(paper_c)
    scissor_p = ImageTk.PhotoImage(scissor_p)
    scissor_c = ImageTk.PhotoImage(scissor_c)

    """Lists of user images and computer images"""
    images_user = [rock_p, scissor_p, paper_p]
    images_comp = [rock_c, scissor_c, paper_c]

    """Placing images in frames with default shape."""
    image_label = Label(frame_1, image=rock_p)
    image_label_2 = Label(frame_2, image=rock_c)
    image_label.grid(row=2, column=0)
    image_label_2.grid(row=2, column=2)

    """Labels setup"""
    title_label = Label(text="Rock, Paper and Scissors.", bg=BG_COLOUR, highlightthickness=0)
    title_label.config(padx=10, pady=10, font=("Times New Roman", 38, "italic"), anchor="center")
    title_label.grid(row=0, column=1, sticky="N")
    player_label = Label(text="Player's score: ", bg=BG_COLOUR, highlightthickness=0)
    player_label.config(padx=10, pady=10, font=("Times New Roman", 25, "italic"), anchor="center")
    player_label.grid(row=3, column=0, sticky="W")
    comp_label = Label(text="Computer's score: ", bg=BG_COLOUR, highlightthickness=0)
    comp_label.config(padx=10, pady=10, font=("Times New Roman", 25, "italic"), anchor="center")
    comp_label.grid(row=3, column=2, sticky="W")
    comp_choice = Label(text="Computer's choice: ", bg=BG_COLOUR, highlightthickness=0)
    comp_choice.config(padx=10, pady=10, font=("Times New Roman", 25, "italic"), anchor="center")
    comp_choice.grid(row=1, column=2, sticky="W")
    player_choice = Label(text="Player's choice: ", bg=BG_COLOUR, highlightthickness=0)
    player_choice.config(padx=10, pady=10, font=("Times New Roman", 25, "italic"), anchor="center")
    player_choice.grid(row=1, column=0, sticky="W")
    feedback = Label(text="Ready!", bg=BG_COLOUR, highlightthickness=0)
    feedback.config(padx=10, pady=10, font=("Border", 30, "italic"), anchor="center")
    feedback.grid(row=2, column=1, sticky="N")

    """Buttons setup"""
    rock = Button(text="Rock", font=("Boulder", 14), bg=BG_COLOUR, highlightthickness=0,
                  width=8, command=rock_command)
    paper = Button(text="Paper", font=("Boulder", 14), bg=BG_COLOUR, highlightthickness=0,
                   width=8, command=paper_command)
    scissors = Button(text="Scissors", font=("Boulder", 14), bg=BG_COLOUR, highlightthickness=0,
                      width=8, command=scissors_command)
    end = Button(text="Exit", font=("Boulder", 14), bg=BG_COLOUR, highlightthickness=0,
                 width=8, command=end)
    restart = Button(text="Restart", font=("Boulder", 14), bg=BG_COLOUR, highlightthickness=0,
                     width=8, command=restart)
    rock.grid(row=4, column=0, sticky="N")
    paper.grid(row=4, column=1, sticky="N")
    end.place(x=730, y=500)
    restart.place(x=230, y=500)
    scissors.grid(row=4, column=2, sticky="N")
else:
    messagebox.showinfo(message="Whenever you are ready.")

window.mainloop()
