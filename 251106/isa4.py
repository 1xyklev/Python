class Employee:
    def work(self):
        print("직원이 일합니다.")

class Manager(Employee):
    super().work()  # 부모 클래스(Employee)의 work() 호출
    print("관리자가 팀을 관리합니다.")

m = Manager()
m.work()