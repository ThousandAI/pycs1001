# 運算子
"""
x = 5
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x**y)
print(x%y) # mod -> 5 / 3 = 1 ... 2
"""

# 餘數應用 (解答)
"""
num = int(input())
print(f"百位數字: {num // 100}")
print(f"十位數字: {(num//10)%10}")
print(f"個位數字: {num % 10}")
"""

# 交換數值 (解答)
"""
x = int(input("x: "))   # 5
y = int(input("y: "))   # 3

# tem = x  # temporary
# x = y
# y = tem

x, y = y, x

print(f"x: {x}, y: {y}")
"""

# 比較運算子
"""
x = 5
y = 3
print(x == y) # F
print(x != y) # T
print(x > y) # T
print(x < y) # F
print(x >= y) # T
print(x <= y) # F
"""

# 邏輯運算子
"""
x = 3
print(x > 1 and x < 3) # F
print(x > 1 or x < 3) # T
"""

# 控制流程
"""
num = int(input())
if num > 200:
    print(f"{num} > 200")
else:
    print(f"{num} <= 200")
"""

"""
if -1:
    print("This is True.")
else:
    print("This is False")

if 0:
    print("This is True.")
else:
    print("This is False")
"""

"""
num = int(input())
if num > 200:
    print(f"{num} > 200")
elif 100 <= num <= 200:
    print(f"100 <= {num} <= 200")
else:
    print(f"{num} < 100")
"""
"""
x = int(input())
y = int(input())
z = int(input())

if x > y:
    ans = x
else:
    ans = y

if ans < z:
    ans = z

print(ans)
"""

i = 0
while i < 10:
    print(i)
    i += 1







