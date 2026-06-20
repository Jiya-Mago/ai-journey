# FILE OBJECTS
f = open('week-1/vessels.txt', 'r')
# print()
# print(f.name)
# print(f.mode)
# f.close()
#or
# with open('week-1/vessels.txt', 'r') as f:  #context managers
#     pass
# print(f.closed)  

# #1
# with open('week-1/vessels.txt', 'r') as f: 
#     f_contents =f.read()
#     f_contents_1 = f.readline()
#     f_contents_2 = f.readlines()
#     print(f_contents)
#     print()
#     print(f_contents_1)
#     print()
#     print(f_contents_2)
#     print()

#     for line in f:
#         print(line, end='')
    
#     f_contents =f.read(100)
#     print(f_contents, end='')
# with open('week-1/vessels.txt', 'r') as f:
#     size_to_read = 100
#     f_contents = f.read(size_to_read)

#     print("Characters read:", len(f_contents))
#     print("File position:", f.tell())

#     f.seek(0)
#     # while len(f_contents) > 0:
#     #     print(f_contents, end='*')
#     #     f_contents = f.read(size_to_read)
#2
with open('vessels2.txt', 'w') as f:
    f.write('Vessel')
    # f.seek(0)
    # f.write('L')
    f.seek(0)
    f.write('Vessels')
#3
with open('week-1/vessels.txt', 'r') as rf:
    with open('vessels2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('week-1/pink.jpg', 'rb') as rf:
    with open('pink_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

print("---------------------------------------------")

with open("week-1/customers.csv", "r") as f:
    lines = f.readlines()

header = lines[0]
resolved_reports = []

for line in lines[1:]:
    parts = line.strip().split(",")

    customer = parts[0]
    vessel = parts[1]
    report_date = parts[2]
    status = parts[3]
    response_days = int(parts[4])

    if status == "resolved":
        resolved_reports.append(line)

with open("customers2.csv", "w") as f:
    f.write(header)

    for report in resolved_reports:
        f.write(report)

print("Done!")
print(f"{len(resolved_reports)} resolved reports copied.")