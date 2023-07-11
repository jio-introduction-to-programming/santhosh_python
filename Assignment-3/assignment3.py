#Question1
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    if num == 3:
        break
    total += num
print("solution1: ",total)

#Question2
print("solution2")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
    
    
#Question3
i = 0
while i < 5:
    if i == 3:
        break
    i += 1
print("solution3: ",i)

#Question4
x = 10
y = 5
if x > y:
    print("Solution4: x is greater than y")
elif x == y:
    print("solution4: x is equal to y")
else:
    print("solution4: x is less than y")
    
#Question5
i = 0
print("Answer5: ")
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')
    
#Question6
num6 = [1, 2, 3, 4, 5]
total = 0
for num6 in numbers:
    if num6 % 2 != 0:
        total += num6
print("Solution6: ",total)

#Question7
x = 5
y = 3
print("Answer7: ")
if x > y:
    if x % y == 0:
        print("x is divisible by y")
    else:
        print("x is not divisible by y")
else:
    print("Invalid comparison")
    
#Question8
numbers = [1, 2, 3, 4, 5]
print("Solution8: ")
for num in numbers:
    if num % 2 == 0:
        break
    print(num)
else:
    print("All numbers are even")    
    
#Question9
i = 0
print("Answer9: ")
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')
else:
    if i == 5:
        print("Loop completed successfully", end=' ')
        
        
#Question10
x = 100
print("Answer10: ")
while x > 0:
    print(x, end=' ')
    x = x // 2
