# Count Title Names
import csv

titles = {}

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1

# Sort by Value (Using a Lambda Function)
# We can write and pass in a lambda, or anonymous function, which has no name but
# takes in some argument or arguments, and returns a value immediately.
for title in sorted(titles, key = lambda title: titles[title], reverse = True):
    print(title, titles[title])