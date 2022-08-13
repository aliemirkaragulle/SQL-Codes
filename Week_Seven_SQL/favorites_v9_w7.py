# Regular Expressions
import csv
import re

# We can also use regular expressions, a standardized
# way to represent a pattern that a string must match

counter = 0

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        # The re library has a function, search, to which we can pass a pattern and string to see if there is a match.
        # We can change our expression to "^(OFFICE|THE.OFFICE)$", which will match either OFFICE or THE OFFICE, but only if they
        # start at the beginning of the string, and stop at the end of the string (i.e., there are no other words before or after).
        # We can even change THE OFFICE to THE.OFFICE, allowing any character (like a typo) to be in between those words.
        if re.search("^(OFFICE|THE.OFFICE)$", title):
            counter += 1

print(f"Number of people who like The Office: {counter}")