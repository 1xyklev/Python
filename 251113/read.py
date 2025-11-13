import os

base_dir = os.path.dirname(__file__)       # 현재 파이썬 파일 위치
file_path = os.path.join(base_dir, "phones.txt")
infile = open(file_path, "r", encoding="utf-8")
s = infile.read() 
print(s)
infile.close() 