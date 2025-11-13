import os
base_dir = os.path.dirname(__file__)
filename = input("파일명을 입력하세요: ").strip()
filepath = os.path.join(base_dir, filename)

# 입력받은 파일명으로 파일을 읽기 모드로 열어 infile에 저장한다.
infile = open(filepath, "r", encoding="utf-8")

freqs = {} # 문자의 빈도수를 저장할 빈 사전 freqs를 생성한다.

# 파일의 각 줄에 대하여 문자를 추출한다.
# 각 문자를 사전 freqs에 추가하며, 이미 있는 문자면 빈도수를 증가시킨다.
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1

print(freqs) # 문자의 빈도수를 출력한다.
infile.close()