import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mariadb

conn = mariadb.connect(
    user="projekt",
    password="admin123",
    host="localhost",
    port=3306,
    database="schlumpfshop3"
)

cur = conn.cursor()

def kunden_filtern():
    alter = entry.get()
    if alter:
        alter = int(alter)  
        if alter < 0:
            messagebox.showwarning("Fehler", "Bitte gültiges Alter eingeben.")
            return
        
        cur.execute("""
            SELECT Anrede, Vorname, Name, Telefon 
            FROM Kunden
            WHERE TIMESTAMPDIFF(YEAR, Geburtsdatum, CURDATE()) < ?
        """, (alter,))
        
        kunden = cur.fetchall()

        if kunden:
            update_listbox(kunden)
        else:
            messagebox.showinfo("Keine Ergebnisse", "Es wurde kein Kunde gefunden der jünger ist.")
    else:
        messagebox.showwarning("Fehler!!!", "Bitte ein Alter eingeben!")

def update_listbox(kunden):
    listbox.delete(0, tk.END)
    for kunde in kunden:
        listbox.insert(tk.END, f"{kunde[0]} {kunde[1]} {kunde[2]} - {kunde[3]}")

fenster = tk.Tk()
fenster.title("Kunden Filtern")
fenster.geometry("800x600")

alter_label = tk.Label(fenster, text="Bitte Alter eingeben:")
alter_label.pack(pady=10)

entry = ttk.Entry(fenster, width=40)
entry.pack(pady=10)

filter_button = ttk.Button(fenster, text="Kunden Filtern", width=20, command=kunden_filtern)
filter_button.pack(pady=5)

listbox = tk.Listbox(fenster, width=60, height=10, bg="pink")
listbox.pack(pady=10)

fenster.mainloop()

cur.close()
conn.close()


