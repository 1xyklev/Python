class Book:
    def __init__(self, title, author, borrowed=0):
        self.title = title
        self.author = author
        self.borrowed = borrowed

    def borrow(self):
        if self.borrowed == 0:
            self.borrowed = 1
            print(f"{self.title}이(가) 대출되었습니다.")
        else:
            print(f"{self.title}은(는) 이미 대출 중입니다.")

    def return_book(self):
        if self.borrowed == 1:
            self.borrowed = 0
            print(f"{self.title}이(가) 반납되었습니다.")
        else:
            print(f"{self.title}은(는) 대출되지 않았습니다.")

b1 = Book("파이썬 프로그래밍", "홍길동")
b1.borrow()       
b1.borrow() 
b1.return_book()   
