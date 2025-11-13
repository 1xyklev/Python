import os

def parse_file(path):
    infile = open(path) # 파일을 읽기 모드로 열어 infile에 저장
    
    spaces = 0 #변수 초기화
    tabs = 0

    # 파일을 한 줄씩 읽어서 스페이스와 탭의 개수를 센다.
    for line in infile:
        spaces += line.count(' ')  # 스페이스의 개수를 세어 spaces에 더한다.
        tabs += line.count('\t')   # 탭의 개수를 세어 tabs에 더한다.
    
    # 파일을 닫는다.
    infile.close()

    # 스페이스와 탭의 개수를 반환한다.
    return spaces, tabs

base_dir = os.path.dirname(__file__) #현재경로

filename = input("파일 이름을 입력하시오: ")

# base_dir과 입력한 파일 이름을 결합해 전체 경로 생성
filepath = os.path.join(base_dir, filename)

# parse_file 함수를 호출하여 스페이스와 탭의 개수를 계산하고 출력한다.
spaces, tabs = parse_file(filepath)
print("스페이스 수 = %d, 탭의 수 = %d" % (spaces, tabs))