with open("C:/Python/251113/proverbs.txt", 'rb') as file:
    # 파일 포인터를 파일의 10번째 바이트로 이동
    file.seek(10, 0)

    # 파일 포인터의 현재 위치 확인
    position = file.tell()
    print("현재 파일 포인터 위치:", position)

    # 해당 위치에서 5바이트를 읽음
    data = file.read(5)
    print("읽은 데이터:", data)      # b'가 앞에 붙은 바이트 배열로 출력된다. 