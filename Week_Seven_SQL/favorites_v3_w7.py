# Filter Out Duplicates
import csv

# Set ensures that all the values are unique
titles = set()

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Canonicalization
        title = row["title"].strip().upper()
        # Now, we can call add on the set, and
        # not have to check ourselves if it's already in the set
        titles.add(title)

for title in titles:
    print(title)