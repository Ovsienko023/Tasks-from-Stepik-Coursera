n = int(input())
comand = dict()


for i in range(n):
   cmd, namespace, arg = input().split() 
   comand[arg] = namespace
   if cmd == 'create':
      return
   
   if cmd == 'add':
      return
   
   if cmd == 'get':
      return
   



















for i,j in comand.items():
   print(i,j)
