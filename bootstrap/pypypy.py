l1=[[1,-2],[2,3],[4,-5],[6,7]]
res=[]
r=[]
k=2
length=0
for _ in l1:length+=1
if k<=length:
  index=0
  while index<length:
    if l1[index]<[0]:
      res=[]
    else:
      res+=l1[index]
      r.append(res)
  index+=1
k-=1
print(r)