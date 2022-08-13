# A program that asks user for a show title and then prints its popularity
import csv

from cs50 import SQL

# Open favorites.db file
db = SQL("sqlite:///favorites.db")

# Prompt the user for a title
title = input("Title: ").strip()

# Execute a command
rows = db.execute("SELECT COUNT(*) AS counter FROM favorites WHERE title LIKE ?", title)

row = rows[0]

print(row["counter"])