infile = open(r"chapter12\phones.txt", "r", encoding="utf-8")
line = infile.readline()
while line != "":
    print(line) #줄바꿈
    line = infile.readline() #줄바꿈 포함상태로 출력
infile.close() 