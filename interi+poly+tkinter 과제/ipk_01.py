from tkinter import*

class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        raise NotImplementedError("이것은 추상 메소드입니다.")
    
class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."

class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."
    
car = Car("car1")
truck = Truck("truck1")

root = Tk()
root.title("문제 1")
root.geometry("400x300")
label1 = Label(root, text = "버튼을 눌러보세요.").pack(pady = 10)

frame = Frame(root)
frame.pack(pady = 10)

def s_car():
    result.set(car.drive())

def s_truck():
    result.set(truck.drive())

Button(frame, text = "자동차 주행", command = s_car).pack(side="left", padx=10)
Button(frame, text = "트럭 주행", command = s_truck).pack(side="left", padx=10)

result = StringVar(value="")
label2 = Label(root, textvariable=result).pack(pady=10)


root.mainloop()