import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid position")
        self.items.insert(position, item)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid position")
        return self.items.pop(position)

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.is_empty():
            return "Stack is empty"
        return " <- ".join(self.items)

    def display(self):
        if self.is_empty():
            return "Stack is Empty"
        return "\n".join(reversed(self.items))


stack = Stack()


# ---------------- GUI Functions ---------------- #

def update_display():
    stack_display.config(state="normal")
    stack_display.delete(1.0, tk.END)
    stack_display.insert(tk.END, stack.display())
    stack_display.config(state="disabled")


def insert_item():
    item = entry_item.get()
    pos = entry_position.get()

    if item == "" or pos == "":
        messagebox.showerror("Error", "Enter item and position")
        return

    try:
        stack.insert(item, int(pos))
        update_display()
        status.config(text=f"Inserted '{item}' at position {pos}", fg="green")
        entry_item.delete(0, tk.END)
        entry_position.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_item():
    pos = entry_position.get()

    if pos == "":
        messagebox.showerror("Error", "Enter position")
        return

    try:
        item = stack.delete(int(pos))
        update_display()
        status.config(text=f"Deleted '{item}'", fg="red")
        entry_position.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def peek_item():
    try:
        messagebox.showinfo("Top Element", stack.peek())
    except Exception as e:
        messagebox.showerror("Error", str(e))


def check_empty():
    if stack.is_empty():
        messagebox.showinfo("Stack", "Stack is Empty")
    else:
        messagebox.showinfo("Stack", "Stack is Not Empty")


def stack_size():
    messagebox.showinfo("Size", f"Stack Size: {stack.size()}")


def traverse_stack():
    messagebox.showinfo("Traverse", stack.traverse())


# ---------------- GUI Window ---------------- #

root = tk.Tk()
root.title("Stack Operations GUI")
root.geometry("600x550")
root.configure(bg="#EAF6F6")

title = tk.Label(
    root,
    text="STACK OPERATIONS",
    font=("Arial", 18, "bold"),
    bg="#EAF6F6",
    fg="#003366",
)
title.pack(pady=10)

frame = tk.Frame(root, bg="#EAF6F6")
frame.pack()

tk.Label(frame, text="Item:", bg="#EAF6F6",
         font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5)

entry_item = tk.Entry(frame, width=20)
entry_item.grid(row=0, column=1)

tk.Label(frame, text="Position:", bg="#EAF6F6",
         font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=5)

entry_position = tk.Entry(frame, width=20)
entry_position.grid(row=1, column=1)

# Buttons

btn_frame = tk.Frame(root, bg="#EAF6F6")
btn_frame.pack(pady=15)

buttons = [
    ("Insert", insert_item, "#4CAF50"),
    ("Delete", delete_item, "#F44336"),
    ("Peek", peek_item, "#2196F3"),
    ("Is Empty?", check_empty, "#9C27B0"),
    ("Size", stack_size, "#FF9800"),
    ("Traverse", traverse_stack, "#009688"),
]

row = 0
col = 0

for text, cmd, color in buttons:
    tk.Button(
        btn_frame,
        text=text,
        width=15,
        bg=color,
        fg="white",
        font=("Arial", 10, "bold"),
        command=cmd,
    ).grid(row=row, column=col, padx=8, pady=8)

    col += 1
    if col == 3:
        col = 0
        row += 1

# Stack Display

tk.Label(
    root,
    text="Stack Visualization (Top → Bottom)",
    font=("Arial", 12, "bold"),
    bg="#EAF6F6",
).pack()

stack_display = tk.Text(
    root,
    width=25,
    height=12,
    font=("Courier New", 14),
    state="disabled",
    bg="white",
)
stack_display.pack(pady=10)

status = tk.Label(
    root,
    text="Ready",
    font=("Arial", 11),
    bg="#EAF6F6",
    fg="blue",
)
status.pack(pady=5)

update_display()

root.mainloop()
