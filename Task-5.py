import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        refresh_list()
        clear_fields()
    else:
        messagebox.showwarning("Missing Info", "Name and phone number are required!")

def refresh_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = search_entry.get().lower()
    listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    selected = listbox.curselection()
    if selected:
        contacts.pop(selected[0])
        refresh_list()

def update_contact():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        contacts[idx] = {
            'name': name_entry.get(),
            'phone': phone_entry.get(),
            'email': email_entry.get(),
            'address': address_entry.get()
        }
        refresh_list()

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# UI Setup
root = tk.Tk()
root.title("Contact Book")

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Phone").grid(row=1, column=0)
tk.Label(root, text="Email").grid(row=2, column=0)
tk.Label(root, text="Address").grid(row=3, column=0)

name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_entry.grid(row=3, column=1)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=1)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=5, column=0)
tk.Button(root, text="Clear Fields", command=clear_fields).grid(row=5, column=1)

tk.Label(root, text="Search").grid(row=6, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=1)
tk.Button(root, text="Search", command=search_contact).grid(row=6, column=2)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=7, column=0, columnspan=3)

root.mainloop()