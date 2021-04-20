s = input()

odd_count = 0
odd = ""
array = []

for i in range(26):
    alp = ord("A") + i
    c = s.count(chr(alp))
    if c % 2 == 1:
        if odd_count > 0:
            print("I'm Sorry Hansoo")
            exit()
        else:
            odd_count += 1
            odd = chr(alp)
    if c:
        array.append([chr(alp),c])

for i in range(len(array)):
    print(array[i][0] * (array[i][1]//2), end="")
print(odd,end="")
for i in range(len(array)-1,-1,-1):
    print(array[i][0] * (array[i][1]//2), end="")
    
