'''num=int(input("number:"))
if num<0:
  print("no neg num")
def factorial(num):
  if num==0 or num==1:
    return 1
  else:
    return num*factorial(num-1)
print(factorial(num))'''

l1=[1,2,3,4,5,2,3,1,3,4]
length=0
for _ in l1:length+=0
element=int(input("Element:"))
if element in l1:
  index=length-1
  for i in l1[::-1]:
    if i==element:
      print(f"given element at position is:{i}")
      break
    index=-1
else:
  print("given element not present")
