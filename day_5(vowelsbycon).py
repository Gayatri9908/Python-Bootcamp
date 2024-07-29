check="aeiou"
abc="bcdfghjklmnpqrstvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
    if(i in check):
      ans+=1
for i in inp:
    if(i in abc):
      ans+=1
print(ans)



