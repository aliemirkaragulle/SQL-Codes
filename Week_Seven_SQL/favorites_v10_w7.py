# Generic Function for a Specific Title
import csv

# We ask for the user input, and then open our CSV file. Since we're looking
# for just one title, we can have one counter variable that we increment.
# We check for a match after standardizing both the user's input and each row's title.

title = input("Title: ").strip().upper()

counter = 0

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["title"].strip().upper() == title:
            counter += 1

print(counter)