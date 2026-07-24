print("swati bind")

import tkinter as tk
from tkinter import messagebox, simpledialog


class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return False
        self.queue.append(item)
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def traverse(self):
        return self.queue


def update_list():
    listbox.delete(0, tk.END)
    for i, item in enumerate(queue.traverse(), start=1):
        listbox.insert(tk.END, f"{i}. {item}")


def enqueue():
    item = simpledialog.askstring("Enqueue", "Enter item:")
    if item:
        if queue.enqueue(item):
            messagebox.showinfo("Success", f'"{item}" Enqueued Successfully')
            update_list()
        else:
            messagebox.showerror("Error", "Queue is Full")


def dequeue():
    item = queue.dequeue()
    if item is None:
        messagebox.showerror("Error", "Queue is Empty")
    else:
        messagebox.showinfo("Dequeued", f'"{item}" Removed Successfully')
        update_list()


def peek():
    item = queue.peek()
    if item is None:
        messagebox.showerror("Error", "Queue is Empty")
    else:
        messagebox.showinfo("Front Item", f"Front Item: {item}")


def traverse():
    if queue.is_empty():
        messagebox.showinfo("Queue", "Queue is Empty")
    else:
        messagebox.showinfo("Queue Elements", " -> ".join(queue.traverse()))


def check_empty():
    if queue.is_empty():
        messagebox.showinfo("Status", "Queue is Empty")
    else:
        messagebox.showinfo("Status", "Queue is Not Empty")


def check_full():
    if queue.is_full():
        messagebox.showinfo("Status", "Queue is Full")
    else:
        messagebox.showinfo("Status", "Queue is Not Full")


root = tk.Tk()
root.title("Queue Operations Using GUI")
root.geometry("500x500")
root.configure(bg="lightblue")

size = simpledialog.askinteger(
    "Queue Size",
    "Enter Maximum Queue Size:",
    minvalue=1
)

if size is None:
    root.destroy()
    exit()

queue = Queue(size)

title = tk.Label(
    root,
    text="QUEUE OPERATIONS",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title.pack(pady=10)

listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack()

tk.Button(button_frame, text="Enqueue", width=15, bg="green", fg="white",
          command=enqueue).grid(row=0, column=0, padx=5, pady=5)

tk.Button(button_frame, text="Dequeue", width=15, bg="red", fg="white",
          command=dequeue).grid(row=0, column=1, padx=5, pady=5)

tk.Button(button_frame, text="Peek", width=15,
          command=peek).grid(row=1, column=0, padx=5, pady=5)

tk.Button(button_frame, text="Traverse", width=15,
          command=traverse).grid(row=1, column=1, padx=5, pady=5)

tk.Button(button_frame, text="Check Empty", width=15,
          command=check_empty).grid(row=2, column=0, padx=5, pady=5)

tk.Button(button_frame, text="Check Full", width=15,
          command=check_full).grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Exit", width=20, bg="black", fg="white",
          command=root.destroy).pack(pady=20)

root.mainloop()
