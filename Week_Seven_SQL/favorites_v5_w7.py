# Count Title Names
import csv

# We can use a dictionary to count the number of times we've seen each title, with the keys being
# the titles and the values being an integer counting the number of times we see each of them:
titles = {}

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1
        # if not title in titles:
        #   titles[title] = 0
        # titles[title] += 1

# We can sort by the values in the dictionary by changing our loop to:
# We define a function, f, which just return the value of a title in the dictionary with titles[title].
# The sorted function, in turn, will take in that function as they key to sort the dictionary.
# And we'll also pass in reverse = True to sort from largest to smallest, instead of smallest to largest.
def get_value(title):
    return titles[title]

for title in sorted(titles, key = get_value, reverse = True):
    print(title, titles[title])