import time
import csv
import os

class Notes:
    id = 1
    

    def write(head: str, body: str):
        if os.stat("data.csv").st_size != 0:
            with open("data.csv", "r", newline = "") as data:
                fields = ["id", "head", "body", "date"]
                reader = csv.DictReader(data, fieldnames= fields)
                for row in reader:
                    Notes.id += 1

        with open("data.csv", "a", newline = "") as data:
            fields = ["id", "head", "body", "date"]
            writer = csv.DictWriter(data, fieldnames = fields)
            localtime = time.strftime("%b %d %Y %H:%M", time.localtime(time.time())) 

            writer.writerow({"id": Notes.id,"head": head, "body": body, "date": localtime})
            return


