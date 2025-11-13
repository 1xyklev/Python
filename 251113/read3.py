infile = open(r"chapter12\phones.txt", "r", encoding="utf-8")
for line in infile:
    line = line.rstrip()
    print(line)
infile.close() 