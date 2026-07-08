import customtkinter as ctk
import random

# ------------------- Appearance -------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ------------------- Window -------------------

app = ctk.CTk()
app.title("🎯 Number Guessing Game")
app.geometry("1000x700")
app.resizable(False, False)

# ------------------- Variables -------------------

secret_number = random.randint(1, 100)
attempts = 0

# ------------------- Functions -------------------

def check_guess(event=None):
    global attempts

    value = entry.get().strip()

    if value == "":
        result_label.configure(
            text="⚠ Please enter a number.",
            text_color="orange"
        )
        return

    try:
        guess = int(value)
    except:
        result_label.configure(
            text="❌ Enter numbers only!",
            text_color="red"
        )
        return

    attempts += 1
    attempt_label.configure(text=f"Attempts : {attempts}")

    if guess < secret_number:
        result_label.configure(
            text="📉 Too Low!\nTry a bigger number.",
            text_color="#00BFFF"
        )

    elif guess > secret_number:
        result_label.configure(
            text="📈 Too High!\nTry a smaller number.",
            text_color="#FF6961"
        )

    else:
        result_label.configure(
            text=f"""🎉 Congratulations!

✅ You guessed the correct number.

🏆 Total Attempts : {attempts}
""",
            text_color="#00FF66"
        )


def new_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    attempt_label.configure(text="Attempts : 0")

    result_label.configure(
        text="Guess a number between 1 and 100",
        text_color="white"
    )

    entry.delete(0, "end")


# ------------------- Title -------------------

title = ctk.CTkLabel(
    app,
    text="🎯 NUMBER GUESSING GAME",
    font=("Segoe UI", 34, "bold")
)
title.pack(pady=(20,5))

subtitle = ctk.CTkLabel(
    app,
    text="Can you guess the secret number?",
    font=("Segoe UI", 20)
)
subtitle.pack(pady=(0,20))

# ------------------- Card -------------------

frame = ctk.CTkFrame(
    app,
    width=700,
    corner_radius=25
)

frame.pack(pady=10, padx=30)

# ------------------- Heading -------------------

heading = ctk.CTkLabel(
    frame,
    text="Enter a Number (1 - 100)",
    font=("Segoe UI", 24, "bold")
)

heading.pack(pady=(30,20))

# ------------------- Entry -------------------

entry = ctk.CTkEntry(
    frame,
    width=320,
    height=50,
    font=("Segoe UI", 22),
    justify="center",
    placeholder_text="Type your guess..."
)

entry.pack()

entry.bind("<Return>", check_guess)

# ------------------- Buttons -------------------

guess_btn = ctk.CTkButton(
    frame,
    text="Check Guess",
    width=250,
    height=45,
    font=("Segoe UI", 18, "bold"),
    command=check_guess
)

guess_btn.pack(pady=(25,15))

new_btn = ctk.CTkButton(
    frame,
    text="🔄 New Game",
    width=250,
    height=45,
    font=("Segoe UI", 18, "bold"),
    fg_color="green",
    hover_color="#006400",
    command=new_game
)

new_btn.pack()

# ------------------- Attempts -------------------

attempt_label = ctk.CTkLabel(
    frame,
    text="Attempts : 0",
    font=("Segoe UI", 18, "bold"),
    text_color="cyan"
)

attempt_label.pack(pady=(25,10))

# ------------------- Result -------------------

result_label = ctk.CTkLabel(
    frame,
    text="Guess a number between 1 and 100",
    font=("Segoe UI", 20, "bold"),
    wraplength=600,
    justify="center"
)

result_label.pack(pady=(10,30))

app.mainloop()