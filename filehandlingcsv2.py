import csv
with open("student_marks.csv", "w", encoding="utf-8") as wf:
    csv_writer=csv.writer(wf, delimiter=",")
    csv_writer.writerow(["id","name","courses","marks"])
    csv_writer.writerow(["1","Hari","ECE","450"])
    csv_writer.writerow(["2","Guru","ECE","480"])
    csv_writer.writerow(["3","Ravi","ECE","470"])