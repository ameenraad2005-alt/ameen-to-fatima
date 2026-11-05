import tkinter as tk
import random

root = tk.Tk()
root.title("Love Letter ❤️")
root.geometry("420x700")
root.configure(bg="#fff0e9")
root.resizable(False, False)

pink = "#e88b9b"
dark = "#3b2030"

canvas = tk.Canvas(
    root, width=420, height=700,
    bg="#fff0e9", highlightthickness=0
)
canvas.pack()

# Background hearts
for i in range(45):
    x = random.randint(10, 410)
    y = random.randint(10, 690)
    canvas.create_text(
        x, y, text="♥",
        fill=random.choice(["#f5b6c0", "#ee8296", "#ffd0d5"]),
        font=("Arial", random.randint(8, 18))
    )

# Main wind
canvas.create_rectangle(
    60, 140, 360, 555,
    fill="#f7c4ca", outline="#d87889", width=3
)

canvas.create_rectangle(
    60, 175, 360, 210,
    fill="#ed9ba8", outline=""
)

canvas.create_text(
    85, 192, text="LOVE",
    fill=dark, font=("Arial", 12, "bold")
)

canvas.create_text(
    330, 192, text="□  □  □",
    fill=dark, font=("Arial", 10)
)

canvas.create_text(
    210, 230, text="♥  ♥  ♥  ♥",
    fill="#e85d75", font=("Arial", 18)
)

# Message
message = canvas.create_text(
    210, 270,
    text="Happy 1 month, my love ♥\nStill love me?",
    fill=dark,
    font=("Arial", 14, "bold"),
    justify="center"
)

# Pixel cat
def draw_cat():
    pixel = 12
    pattern = [
        "0010000100",
        "0111001110",
        "1111111111",
        "1110110111",
        "1111111111",
        "1111111111",
        "0111111110",
        "0011111100",
        "0001101100",
    ]

    for row, line in enumerate(pattern):
        for col, value in enumerate(line):
            if value == "1":
                canvas.create_rectangle(
                    150 + col * pixel,
                    305 + row * pixel,
                    150 + (col+1) * pixel,
                    305 + (row+1) * pixel,
                    fill="#17121d",
                    outline="#17121d"
                )

    canvas.create_rectangle(175, 340, 187, 352, fill="white")
    canvas.create_rectangle(211, 340, 223, 352, fill="white")
    canvas.create_text(
        204, 365, text="♥",
        fill="#f04460", font=("Arial", 22)
    )

draw_cat()

# Buttons
yes_btn = tk.Button(
    root, text="YES ❤️",
    font=("Arial", 12, "bold"),
    bg="#e98b9b", fg="white",
    relief="flat", padx=15,
    command=lambda: celebrate()
)

no_btn = tk.Button(
    root, text="NO",
    font=("Arial", 12, "bold"),
    bg="white", fg="#d85b70",
    relief="flat", padx=15
)

yes_btn.place(x=135, y=490)
no_btn.place(x=245, y=490)

# NO button escapes
def escape(event=None):
    x = random.randint(90, 270)
    y = random.randint(430, 510)
    no_btn.place(x=x, y=y)

no_btn.bind("<Enter>", escape)
no_btn.config(command=escape)

# Celebration
def celebrate():
    canvas.delete("celebration")

    canvas.itemconfig(
        message,
        text="Yayyy! I love you! ❤️"
    )

    yes_btn.place_forget()
    no_btn.place_forget()

    canvas.create_text(
        210, 450,
        text="One month of happiness,\n"
             "and a lifetime to go! 💗",
        fill=dark,
        font=("Arial", 12, "bold"),
        justify="center",
        tags="celebration"
    )

    colors = ["#ff4568", "#ffb6c1", "#ffcc66", "#d78bff"]

    def confetti():
        for _ in range(5):
            x = random.randint(50, 370)
            y = random.randint(100, 600)

            canvas.create_text(
                x, y,
                text=random.choice(["♥", "★", "💗"]),
                fill=random.choice(colors),
                font=("Arial", random.randint(15, 25)),
                tags="celebration"
            )

        root.after(200, confetti)

    confetti()

root.mainloop()