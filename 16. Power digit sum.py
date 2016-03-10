# What is the sum of the digits of the number 2^1000?

x, total = 2 ** 1000, 0
for i in str(x):
    total += int(i)
print(total)
    
