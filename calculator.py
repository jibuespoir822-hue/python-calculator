import tkinter as tk

# --- LOGIQUE ---
def click(value):
    current = entry_var.get()
    entry_var.set(current + str(value))

def clear():
    entry_var.set("")

def backspace():
    entry_var.set(entry_var.get()[:-1])

def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Erreur")

# --- FENETRE ---
root = tk.Tk()
root.title("Calculator")
root.geometry("320x500")
root.configure(bg="#0d0d0d")

entry_var = tk.StringVar()

# --- ECRAN ---
entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Arial", 28),
    bg="#0d0d0d",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)
entry.pack(fill="both", ipadx=10, ipady=25, padx=10, pady=10)

# --- FRAME BOUTONS ---
frame = tk.Frame(root, bg="#0d0d0d")
frame.pack(expand=True, fill="both")

# --- STYLE BOUTONS ---
def create_button(text, row, col, command, bg="#1a1a1a", fg="white"):
    btn = tk.Button(
        frame,
        text=text,
        font=("Arial", 16),
        bg=bg,
        fg=fg,
        bd=0,
        activebackground="#333333",
        command=command
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# --- GRILLE ---
for i in range(6):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

# --- LIGNE 1 ---
create_button("C", 0, 0, clear, fg="red")
create_button("%", 0, 1, lambda: click("%"), fg="#00ff99")
create_button("⌫", 0, 2, backspace, fg="#00ff99")
create_button("÷", 0, 3, lambda: click("/"), fg="#00ff99")

# --- LIGNE 2 ---
create_button("7", 1, 0, lambda: click("7"))
create_button("8", 1, 1, lambda: click("8"))
create_button("9", 1, 2, lambda: click("9"))
create_button("×", 1, 3, lambda: click("*"), fg="#00ff99")

# --- LIGNE 3 ---
create_button("4", 2, 0, lambda: click("4"))
create_button("5", 2, 1, lambda: click("5"))
create_button("6", 2, 2, lambda: click("6"))
create_button("-", 2, 3, lambda: click("-"), fg="#00ff99")

# --- LIGNE 4 ---
create_button("1", 3, 0, lambda: click("1"))
create_button("2", 3, 1, lambda: click("2"))
create_button("3", 3, 2, lambda: click("3"))
create_button("+", 3, 3, lambda: click("+"), fg="#00ff99")

# --- LIGNE 5 ---
create_button("0", 4, 0, lambda: click("0"))
create_button(".", 4, 1, lambda: click("."))
create_button("=", 4, 2, calculate, bg="#00cc66", fg="white")

# bouton = prend 2 colonnes
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)

equal_btn = tk.Button(
    frame,
    text="=",
    font=("Arial", 16),
    bg="#00cc66",
    fg="white",
    bd=0,
    command=calculate
)
equal_btn.grid(row=4, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

root.mainloop()