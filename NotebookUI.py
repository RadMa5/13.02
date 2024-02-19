import Notebook

fc = open("data.csv", "a", newline="")
fc.close()
test1 = True
test2 = True

print("\nWelcome to the Notebook\n\nList of options:\n1. Show the list of all notes\n2. Open a specific note\n3. Create a new note\n4. Redact an existing note\n5. Delete an existing note")

ch = int(input("Input your choice: "))
while True:
    if ch <= 0 or ch >= 6:
        ch = int(input("Input is incorrect, please, try again: "))
    else:
        break



# head = input("Input header: ")
# while head == "":
#     head = input("Header input is empty, please, input a proper header: ")

# body = input("Input body: ")

# Notebook.Notes.write(head, body)