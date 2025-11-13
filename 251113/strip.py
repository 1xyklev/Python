infile = open("C:/Python/251113/proverbs.txt", "r")
for line  in infile:
    line=line.rstrip() #줄바꿈 기호 삭제
    print(line)
infile.close() 