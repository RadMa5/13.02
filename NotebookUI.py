import Notebook

fc = open("data.csv", "a", newline="")
fc.close()

working = True
while working:
    incorrectInput = True

    print("\nWelcome to the Notebook\n\nList of options:\n1. Show the list of all notes\n2. Open a specific note\n3. Create a new note\n4. Redact an existing note\n5. Delete an existing note\n6. Exit")
    ch = 0
    while incorrectInput:
        try:
            ch = int(input("Input your choice: "))
            if ch <= 0 or ch >= 7:
                print("Incorrect input")
            else:
                incorrectInput = False
        except ValueError:
            print("Incorrect input")


        if ch == 1:
            Notebook.printHeaders()
        elif ch == 2:
            chId = input("Input the number of the note: ")
            Notebook.printNote(chId)
        elif ch == 3:
            head = input("Input header for new note: ")
            while head == "":
                head = input("Each note must have a header: ")
            body = input("Input body of new note: ")
            Notebook.write(head, body)
        elif ch == 4:
            chId = input("Input the number of the note: ")
            Notebook.redactNote(chId)
        elif ch == 5:
            chId = input("Input the number of the note: ")
            Notebook.removeNote(chId)
        else:
            working = False
            break





