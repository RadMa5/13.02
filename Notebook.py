import time
import csv
import os
import re

id = int(1)
fields = ["id", "head", "body", "date"]

def write(head: str, body: str):
    id = 1
    if os.stat("data.csv").st_size != 0: #sets the id count
        with open("data.csv", "r", newline = "") as data:
            fields = ["id", "head", "body", "date"]
            reader = csv.DictReader(data, fieldnames= fields)
            for row in reader:
                id += 1

    with open("data.csv", "a", newline = "") as data:
        fields = ["id", "head", "body", "date"]
        writer = csv.DictWriter(data, fieldnames = fields)
        localtime = time.strftime("%b %d %Y %H:%M", time.localtime(time.time())) 

        writer.writerow({"id": id,"head": head, "body": body, "date": localtime})
    return
    
def printHeaders():
    print("\nList of all notes:")
    with open("data.csv", "r", newline = "") as data:
        fields = ["id", "head", "body", "date"]
        reader = csv.DictReader(data, fieldnames = fields)
        for row in reader:
            print(row["id"], ". ", row["head"], ". Last changed at ", row["date"])
    return

def printNote(num: int):
    with open("data.csv", "r", newline = "") as data:
        fields = ["id", "head", "body", "date"]
        reader = csv.DictReader(data, fieldnames = fields)
        foundNote = False
        for row in reader:
            if row["id"] == num:
                body = row["body"]
                if body == "":
                    body = "[No body]"
                print("\n", row["id"], ". ", row["head"], "\n", body, "\nLast changed at ", row["date"])
                foundNote = True
                break
        
        if not foundNote:
            print("The note wasn't found")
    return

def redactNote(num: int):
    with open("data.csv", "r+", newline = "") as data:
        with open("ndata.csv", "w", newline="") as ndata:
        
            fields = ["id", "head", "body", "date"]
            reader = csv.DictReader(data, fieldnames = fields)
            writer = csv.DictWriter(ndata, fieldnames = fields)
            foundNote = False
            for row in reader:
                if row["id"] == num:
                    newHead = input("Input new header. Leave blank to keep old header: ")
                    if newHead == "":
                        newHead = row["head"]
                    newBody = input("Input new body. Leave blank to keep old body: ")
                    if newBody == "":
                        newBody = row["body"]
                    localtime = time.strftime("%b %d %Y %H:%M", time.localtime(time.time()))
                    writer.writerow({"id": num,"head": newHead, "body": newBody, "date": localtime})
                    foundNote = True
                else:
                    writer.writerow(row)

            if not foundNote:
                print("The note wasn't found")

    os.remove("data.csv")
    os.rename("ndata.csv", "data.csv")
    return

def removeNote(num: int):
    with open("data.csv", "r+", newline = "") as data:
        with open("ndata.csv", "w", newline="") as ndata:
        
            fields = ["id", "head", "body", "date"]
            reader = csv.DictReader(data, fieldnames = fields)
            writer = csv.DictWriter(ndata, fieldnames = fields)
            foundNote = False
            for row in reader:
                if row["id"] == num:
                    foundNote = True
                    continue
                else:
                    writer.writerow(row)

            if not foundNote:
                print("The note wasn't found")

    os.remove("data.csv")
    os.rename("ndata.csv", "data.csv")
    return