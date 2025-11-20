#1. 이진 파일에 바이트 데이터 쓰기
outfile = open("sample.bin", "wb")  # wb = write binary

# 0~255 범위의 값으로 구성된 바이트 배열 만들기
data_to_write = bytes ([255, 128, 0, 1, 10, 50])

# 파일에 기록
outfile.write(data_to_write)
outfile.close()
print("sampl.bin 파일에 바이트 데이터를 저장했습니다. \n")

#2. 이진 파일에서 바이트 데이터 읽기
infile = open("sample.bin", "rb")   # rb = read binary

# 파일 전체 일기
bytesArray = infile.read()
infile.close()

print("읽어온 bytesArray:", bytesArray)
print("타입:", type(bytesArray))    # <clas 'bytes'>

#3. 개별 바이트 접근 ===
print("\n개별 바이트 값 출력:")
for i, b in enumerate(bytesArray):
    print(f"{i}번째 바이트 = ", b)