a = 0
b = 1
limit = 50000
result = 75025
while b <= 50000:
    print(b, end = ",")
    a, b = b, a + b
print(b)
print(f"Die erste Fibonacci-Zahl über {limit} ist {result}")




