import pickle

notes = []

# TODO: Using the pickle module...

# A. If notes.pickle exists, read it in using pickle and assign the content to
#   the notes variable
try:
    with open('notes.pickle', 'rb') as file:
        notes = pickle.load(file)
        file.close()
except IOError:
    print("File couldn't be opened.")
    

# B. Print out notes

print(notes)

# C. Read in a string from the user using input() and append it to notes

notes.append(input("string to append: "))

# D. Save notes to notes.pickle
with open('notes.pickle', 'wb') as file:
    pickle.dump(notes, file)
    file.close()
