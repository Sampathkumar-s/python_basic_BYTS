#appending the data to existing csv file
import csv
with open("student_marks.csv", "a", encoding="utf-8") as af:
    csv_writer=csv.writer(af, delimiter=",")
    csv_writer.writerow(["4","Anita","ECE","460"])  
    csv_writer.writerow(["5","Asha","ECE","490"])  