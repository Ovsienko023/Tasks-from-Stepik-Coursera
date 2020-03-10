class NonPositiveError(Exception):
   pass 


class PositiveList(list):
      def append(self,num):
            if num > 0:
                  super(PositiveList,self).append(num)
            else:
                  raise NonPositiveError('lolololo')

'''
a = PositiveList()

a.append(1)
print(a)
'''
print("!!!")






