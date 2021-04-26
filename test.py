import csv
scoreNK = 15
scoreCH = 20 
totalscore = 35

with open("data.csv","r") as f:
        data = csv.DictReader(f)
        for row in data:
            if row["username"] == "mo":
                row