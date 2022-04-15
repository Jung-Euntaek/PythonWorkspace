from item import Item

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