# import csv

class Item:
    all = []
    
    # class attribute : instance lev 에서도 접근 가능
    pay_rate = 0.8 # The pay rate after 20% discount

    # instance attribute (self 는 instance 의미)
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self) # list 에 instance 모두 저장

    # instance method : instance lev 에서 접근 가능

    def calculate_total_price(self): # Class 내부 함수는 method
        return self.price * self.quantity

    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        # pay_rate 만 사용하면 에러 : Class / instance lev 에서만 접근 가능하므로
        self.price = self.price * self.pay_rate
        # instance lev 에서 접근

    # Class / Static method : Class lev에서 보통 접근, instance lev 에서도 접근은 가능

    # Class method
    # @classmethod
    # def instantiate_from_csv(cls):
    #     with open("items.csv", "r") as f:
    #         reader = csv.DictReader(f)
    #         items = list(reader)
    # # instance를 csv 로부터 출력하는 method 이므로 parameter 로 self 를 사용하게 되면 오류
    # # Class를 parameter 로 넘기는 Class method 사용해야 함

    #     for item in items:
    #         Item(
    #             name=item.get('name'),
    #             price=int(item.get('price')),
    #             quantity=int(item.get('quantity'))
    #         )

    # Static method : instance 객체를 first param으로 받지 않음, 독립된 func 처럼 사용 가능
    # Cls 밖에서 정의해도 상관 없지만 내용상 Cls와 관련되어 있으므로 내부에서 staticmethod 로 정의
    # @staticmethod
    # def is_integer(num): 
    #     if isinstance(num, float):
    #         return num.is_integer() # is_integer 함수 : count out the floats that are point zero(ex) 7.0 : 정수로 간주)
    #     elif isinstance(num, int):
    #         return True
    #     else:
    #         return False

    # __repr__
    def __repr__(self): # 리스트에 있는 inst 객체를 입력한 포맷으로 변환
        return f"Item('{self.name}, {self.price}, {self.quantity})"

# item1 = Item("Phone", 100, 1)
# item1.apply_discount()
# print(item1.price)

# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# # self.price = self.price * Item.pay_rate 인 경우 class lev 접근으로 설정
# # self.price = self.price * self.pay_rate 와 같이 intance lev 에서 접근해야 값 따로 변경 가능
# item2.apply_discount()
# print(item2.price)

# item2.has_numpad = False # class 정의 밖에서 attribute 지정 가능

# print(Item.pay_rate) # Class lev 접근
# print(item1.pay_rate) # instance lev 접근
# print(Item.__dict__) # All the attributes for Class level
# print(item1.__dict__) # All the attributes for instance level

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# print(Item.all) # __repr__ 이용하여 객체 이름 알아보기 쉽게 변경
# Item.instantiate_from_csv() # Cls method 소환

# print(Item.is_integer(7)) # static method 소환