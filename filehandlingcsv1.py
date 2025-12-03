import csv

with open("F:\Programming\Python\python_basic_BYTS\stress_factor.csv", "r", encoding="utf-8") as rf:
    csv_read = csv.reader(rf)

    with open("F:\Programming\Python\python_basic_BYTS\stress_factor1.csv", "w", encoding="utf-8") as wf:
        csv_write = csv.writer(wf, delimiter=",")
        
        for line in csv_read:
            csv_write.writerow(line)
 

