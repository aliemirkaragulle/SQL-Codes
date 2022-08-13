import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    # reader is a dict
    for row in reader:
        print(row["title"])