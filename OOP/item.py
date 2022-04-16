import csv

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
        self.__name = name # _ / __ : 변수 변경 막는 약속 표시
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self) # list 에 instance 모두 저장

    # Getter & Setter
    @property
    def price(self):
        self.__price

    def apply_discount(self):
    # self.price = self.price * Item.pay_rate
    # pay_rate 만 사용하면 에러 : Class / instance lev 에서만 접근 가능하므로
        self.__price = self.__price * self.pay_rate
        # instance lev 에서 접근

    def apply_increment(self, increment_value): # __price 변수에 직접 접근 불가, method 통해서는 가능
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decorator = Read-Only Attribute
    def name(self): # instanc의 name attribute 호출 시 해당 함수 통해 호출
        return self.__name

    @name.setter # 변경 불가한 read-only 이름 변경 가능한 setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    # instance method : instance lev 에서 접근 가능
    def calculate_total_price(self): # Class 내부 함수는 method
        return self.__price * self.quantity


    # Class / Static method : Class lev에서 보통 접근, instance lev 에서도 접근은 가능

    # Class method
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
    # instance를 csv 로부터 출력하는 method 이므로 parameter 로 self 를 사용하게 되면 오류
    # Class를 parameter 로 넘기는 Class method 사용해야 함

        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    # Static method : instance 객체를 first param으로 받지 않음, 독립된 func 처럼 사용 가능
    # Cls 밖에서 정의해도 상관 없지만 내용상 Cls와 관련되어 있으므로 내부에서 staticmethod 로 정의
    @staticmethod
    def is_integer(num): 
        # is_integer 함수 : count out the floats that are point zero(ex) 7.0 : 정수로 간주)
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # __repr__
    def __repr__(self): # 리스트에 있는 inst 객체를 입력한 포맷으로 변환
        return f"Item('{self.name}, {self.__price}, {self.quantity})"

    # @property # property 는 attribute 와 달리 초기 설정값 변경 불가
    # def read_only_name(self):
    #     return "AAA"

    def __connect(self):
        pass

    def __prepare_body(self):
        pass

    def __send(self):
        pass

    def send_email(self): # 원칙 : 필요한 method만 쓸 수 있게 만들고 나머지는 "__" 이용하여 숨기기(해당 함수에는 instance lev에서 접근 불가)
        self.__connect()
        self.__prepare_body()
        self.__send()
