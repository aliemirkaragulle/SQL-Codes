import csv

# We'll open the file with a reference called file,
# using the with keyword in Python that will close our file for us
with open("favorites.csv", "r") as file:
    # The csv library has a reader function that will create a reader variable
    # we can use to read in the file as a CSV
    reader = csv.reader(file)
    # Ignore the First Row (Timestamp, Title, Genre)
    # We'll call next to skip the first row, since that's the header row
    next(reader)
    # reader is a list
    # Then, we'll use a loop to print the second column in each row,
    # which is the title
    for row in reader:
        print(row[1])