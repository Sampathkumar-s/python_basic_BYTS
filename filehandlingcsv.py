import csv

with open("stress_factor.csv", "r", encoding="utf-8") as rf:
    csv_read = csv.reader(rf)

    for row in csv_read:
        print(row)

