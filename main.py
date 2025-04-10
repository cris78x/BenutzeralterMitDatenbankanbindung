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

