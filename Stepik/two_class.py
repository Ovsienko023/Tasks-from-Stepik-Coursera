class Buffer:
    def __init__(self):
        self.lst = list()
        self.rest = list()      
    
    def add(self,*a):
        self.lst = self.rest
        self.lst += a        
        if len(self.lst) >=5:
            self.rest = self.lst[5:]
            print(sum(self.lst[:5]))
            while len(self.rest) >=5: 
                self.lst[:5] = []
                self.rest = self.lst
                if len(self.rest) >=5:
                    print(sum(self.lst[:5]))
  
    def get_current_part(self):       
        return self.rest
        

buf = Buffer()
buf.add(1,2,3)
buf.get_current_part()

buf.add(4,5,6)
buf.get_current_part()

buf.add(7, 8, 9, 10) 
buf.get_current_part()

buf.add(1,1,1,1,1,1,1,1,1,1,1) 
buf.get_current_part()