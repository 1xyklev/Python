class BankAccount(object):

    interest_rate = 0.3 # 클래스 변수   

    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("입금 성공")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("인출 성공")
        else:
            print("잔액 부족")

user1 = BankAccount("chung", "1111111", 1000)
print("초기 잔고:", user1.balance)
user1.deposit(500)
print("저축 후 잔고:", user1.balance)
user1.withdraw(200)
print("인출 후 잔고:", user1.balance)
user1.withdraw(10000)