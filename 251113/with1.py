with open("C:/Python/251113/proverbs.txt", "r",  encoding="utf-8") as file:
    for line in file:
        print(line.strip())          # 각 라인의 끝에 있는 개행 문자 제거 후 출력

# with 블록을 빠져나오면 파일이 자동으로 닫힘