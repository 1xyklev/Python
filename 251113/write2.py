import os.path

outfile = open("C:/Python/251113/phones.txt", "w",  encoding="utf-8")

if os.path.isfile("phones.txt"):
    print("동일한 이름의 파일이 이미 존재합니다. ")
else :
    outfile.write("홍길동 010-1234-5678\n")
    outfile.write("김철수 010-1234-5679\n")
    outfile.write("김영희 010-1234-5680\n")

outfile.close() 