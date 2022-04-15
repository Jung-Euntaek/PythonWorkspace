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

    # __repr__
    def __repr__(self): # 리스트에 있는 inst 객체를 입력한 포맷으로 변환
        return f"{self.__class__.__name__}('{self.name}, {self.price}, {self.quantity})"
    # __class__.__name__ : instance의 Cls 이름 반환

class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super func. to have access to all attr. / methods
        # attribute 따로 정의 필요 없음 (Item Cls attr. 그대로 상속)
        super().__init__(
            name, price, quantity
        )
        
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"
        
        # Assign to self object
        self.broken_phones = broken_phones
        
        # Actions to execute
        Phone.all.append(self) # list 에 instance 모두 저장

# phone1 = Phone("jscPhonev10", 500, 5)
# print(phone1.calculate_total_price())
# phone2 = Phone("jscPhonev20", 700, 5)

# print(Item.all)
# print(Phone.all)