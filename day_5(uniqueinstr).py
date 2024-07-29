vowel="aeiou"
consonants="bcdfghjklmnpqurstvwxyz"
ans=" "
i="hello world"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=1
print(ans)
