#Begin with first two Fibonacci numbers
first = 1
second = 1
print("First 20 Fibonacci numbers:")
print("-" *80)
print(first, second, end=' ')

#Use loop to compute and display the next 18 numbers
for _ in range(18):
    next = first + second
    print(next, end=' ')
    first = second
    second = next
