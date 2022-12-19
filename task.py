"""
topic:task
author:nikhil
"""
#printing 1 to 10 numbers
n=int(input())
for i in range(1,n+1):
    print(i,end=" ") #1 2 3 4 5 6 7 8 9 10
 #2nd method
# a=1
while(a<=10):
    print(a)
    a+=1   
#display evens m to n
m=int(input())#2
n=int(input())#10
for i in range(m,n,2):
    print(i,end=' ')#2 4 6 8
#display 1 to 110
for i in range(100,111):
  print(i,end=' ')
#display 100to110 even
for i in range(100,111,2):
    print(i,end=' ') #100 102 104 106 108 110   
#display letters to strings
name='program'
for i in name:
    print(i,end=" ")    #p r o g r a m