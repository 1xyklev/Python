infile = open(r"chapter12\proverbs.txt", "r")
for line  in infile:
    line=line.rstrip() #잘바꿈 기호 삭제
    print(line)
infile.close() 