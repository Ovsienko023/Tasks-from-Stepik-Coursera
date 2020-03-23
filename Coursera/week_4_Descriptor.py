class Value:
    """ Descriptor with commission  """

    def __init__(self):
        self.value = None


    def __get__(self, obj, type_obj):
        return self.value 

    
    def __set__(self, obj, value):
        percent = value - (value * obj.commission)
        self.value = int(percent)
        return self.value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
    
    
def main():
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)

