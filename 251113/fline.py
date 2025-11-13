# "proverbs.txt" 파일을 읽기 모드로 열어 infile에 저장한다.
infile = open("C:/Python/251113/proverbs.txt")

# "output.txt" 파일을 쓰기 모드로 열어 outfile에 저장한다.
outfile = open("C:/Python/251113/output.txt", "w")

# 줄 번호를 나타내기 위한 변수 i를 1로 초기화한다.
i = 1

# "proverbs.txt" 파일의 각 줄을 반복하여 처리한다.
for line in infile:
    # 각 줄 앞에 번호를 붙여서 "output.txt" 파일에 쓴다.
    outfile.write(str(i) + ": " + line)
    
    # 다음 줄 번호를 나타내기 위해 i를 1 증가시킨다.
    i = i + 1

# 파일 닫음
infile.close()
outfile.close()