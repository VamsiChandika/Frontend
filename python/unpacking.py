'''a=[1,2,3,4,5,6,7,8,9,10]
x,*y,z=a
print(x)
print(y)
print(z)'''

'''x='hello'
a,b,c,d,*e=x
print(a)
print(b)
print(c)
print(d)
print(e)'''

'''def display():
  return 1,2,3,4,5,6,7,8,9,10
a,b,c,*res=display()
print(a)
print(b)
print(c)
print(res)'''

'''d1={1:2,3:4,5:6,7:8,9:10}
a,b,*c=d1
print(a)
print(b)
print(c)'''


#RECURSION FUNTIONS

#1)  1 to n numbers
'''def display(start,num):
  if start<=num:
    print(start)
    display(start+1,num)
num=int(input("NUMBER:"))
display(1,num)'''

#2)  maximum number from given list
'''def maximum(index,max1,length):
  if index<length:
    if max1<l1[index]:
      max1=l1[index]
    maximum(index+1,max1,length)
  else:
    print(max1)
l1=[10,20,30,40,100,-2,-3] 
maximum(0,l1[0],7)'''


def maximum(index,min1,length):
  if index<length:
    if max1<l1[index]:
      max1=l1[index]
    maximum(index+1,max1,length)
  else:
    print(max1)
l1=[10,20,30,40,100,-2,-3] 
maximum(0,l1[0],7)