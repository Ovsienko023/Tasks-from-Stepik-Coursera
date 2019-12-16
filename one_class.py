class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coin = 0

    def can_add(self):
        
        if self.coin <= self.capacity:
            print("Свободно мест: ", self.capacity - self.coin)
            return True
        else:
            print("копилка переполнена")
            return False
    
    def add(self, v):
         self.v = v
         if self.can_add() == True:
            self.coin += v
            print("!!!")
            

       

money = MoneyBox(10)
money.can_add()

money.add(8)
money.can_add()

money.add(2)
money.can_add()