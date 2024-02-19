import time
import csv
import os

class Notes:
    id = 1
    fields = ["id", "head", "body", "date"]

    def write(head: str, body: str):
        if os.stat("data.csv").st_size != 0: #sets the id counter
            with open("data.csv", "r", newline = "") as data:
                fields = ["id", "head", "body", "date"]
                reader = csv.DictReader(data, fieldnames= fields)
                for row in reader:
                    Notes.id += 1

        with open("data.csv", "a", newline = "") as data:
            writer = csv.DictWriter(data, fieldnames = Notes.fields)
            localtime = time.strftime("%b %d %Y %H:%M", time.localtime(time.time())) 

            writer.writerow({"id": Notes.id,"head": head, "body": body, "date": localtime})
        return
        
    def printHeaders():
        with open("data.csv", "r", newline = "") as data:
            reader = csv.DictReader(data, fieldnames = Notes.fields)
            for row in reader:
                print(row["id"], ". ", row["head"], ". Last changed at ", row["date"])
        return
    
    def printNote(num: int):
        with open("data.csv", "r", newline = "") as data:
            reader = csv.DictReader(data, fieldnames = Notes.fields)
            foundNote = False
            for row in reader:
                if row["id"] == num:
                    print("\n", row["id"], ". ", row["head"], "\n", row["body"], "\nLast changed at ", row["date"])
                    foundNote = True
                    break
            
            if not foundNote:
                print("The note wasn't found")
        return


