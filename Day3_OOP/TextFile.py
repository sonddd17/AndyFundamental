###write a script that creates a file, writes a few lines to it,
#then a separate read that prints its contents back.



# with open("D:/AndyProject/AndyFundamental/Day3_OOP/notes.txt", "a") as f:
#     f.write("\nline 4")
#     f.close
# with open("D:/AndyProject/AndyFundamental/Day3_OOP/notes.txt", "r") as f:
#     for line in f:
#         print(line.strip())

import csv
with open("D:/AndyProject/AndyFundamental/Day3_OOP/people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","age","city"])
    writer.writerow(["Andy", 25, "Ho Chi Minh City"])
    writer.writerow(["Binh", 30, "Hanoi"])

with open("D:/AndyProject/AndyFundamental/Day3_OOP/people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)