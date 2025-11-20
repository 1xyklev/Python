try:
    dividend = int(input("나눠지는 수를 입력하세요: "))
    divisor = int(input("나누는 수를 입력하세요: "))
    result = dividend / divisor
    print(f"{dividend}를 {divisor}로 나눈 결과는 {result}입니다.")

except ValueError:
    print("정수를 입력해야 합니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print(f"오류가 발생했습니다: {e}")
else:
    print("나누기 연산 성공!")
finally:
    print("프로그램을 종료합니다.")