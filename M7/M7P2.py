#Input start, stop, and increment values
start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
increment = int(input("Enter increment value: "))

#Begin current value
current = start

#Display numbers from start to stop with increment
print("\nNumbers from {} to {} by {}:".format(start, stop, increment))
while current <= stop:
    print(current)
    current += increment
