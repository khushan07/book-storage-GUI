import tkinter as tk
from tkinter import messagebox

def add_book():
    if title_entry.get() and author_entry.get() and date_entry.get():
        books.append({'title': title_entry.get(), 'author': author_entry.get(), 'date': date_entry.get(), 'read': False})
        title_entry.delete(0, tk.END); author_entry.delete(0, tk.END); date_entry.delete(0, tk.END)
        list_books()
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def list_books():
    book_listbox.delete(0, tk.END)
    for i, book in enumerate(books):
        read_status = "Read" if book['read'] else "Not Read"
        book_listbox.insert(tk.END, f"{i+1}. {book['title']} by {book['author']} ({book['date']}) - {read_status}")

def mark_as_read():
    selected = book_listbox.curselection()
    if selected:
        books[selected[0]]['read'] = True; list_books()

def delete_book():
    selected = book_listbox.curselection()
    if selected:
        books.pop(selected[0]); list_books()

root = tk.Tk(); root.title("Bookstore System"); books = []
tk.Label(root, text="Title").pack(); title_entry = tk.Entry(root); title_entry.pack()
tk.Label(root, text="Author").pack(); author_entry = tk.Entry(root); author_entry.pack()
tk.Label(root, text="Date").pack(); date_entry = tk.Entry(root); date_entry.pack()
tk.Button(root, text="Add Book", command=add_book).pack()
book_listbox = tk.Listbox(root, width=50); book_listbox.pack()
tk.Button(root, text="Mark as Read", command=mark_as_read).pack()
tk.Button(root, text="Delete Book", command=delete_book).pack()
root.mainloop()
