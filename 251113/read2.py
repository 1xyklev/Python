infile = open("C:/Python/251113/phones.txt", "r", encoding="utf-8")
line = infile.readline()
while line != "":
    print(line, end = "")
    line = infile.readline()
infile.close()