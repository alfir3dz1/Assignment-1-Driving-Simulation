num = []
ans = []
#Modulo 42
def mod(x):
    y = 42
    return x%y

#range to 10
for i in range(10):
    text = int(input("Input numbers: "))
    num.append(text)
    print(num)
#Answer
for i in num:
    ans.append(mod(int(i)))
#Distinct
output = []
for j in set(ans):
    output.append(j)
print("\nDistinct ans: ", len(output))
