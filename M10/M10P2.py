from program_functions import wall_area_function, ceiling_area_function
import math
total_wall_gallons = 0
total_ceiling_gallons = 0
room_count = 0

#Loop
answer = input("Would you like to enter room data? Enter Yes to continue: ")

while answer.lower() == "yes":
    length = float(input("Enter room length in feet: "))
    width = float(input("Enter room width in feet: "))
    height = float(input("Enter room height in feet: "))

    #Compute wall area and gallons
    wall_area = wall_area_function(length, width, height)
    wall_gallons = math.ceil(wall_area / 50)
    #Math.ceil: https://docs.python.org/3.9/library/math.html?highlight=math%20ceil#math.ceil
    #https://www.geeksforgeeks.org/python/floor-ceil-function-python/

    #Compute ceiling/floor area and gallons
    ceiling_area = ceiling_area_function(length, width)
    ceiling_gallons = math.ceil(ceiling_area / 50)

    #Display results
    print("\nRoom Paint Estimate")
    print("-" * 30)
    print(f"Wall square footage: {wall_area} sq ft")
    print(f"Gallons needed for walls: {wall_gallons}")
    print(f"Ceiling/Floor area: {ceiling_area} sq ft")
    print(f"Gallons needed for ceiling/floor: {ceiling_gallons}")
    print("-" * 30)

    #Update count
    total_wall_gallons += wall_gallons
    total_ceiling_gallons += ceiling_gallons
    room_count += 1

    answer = input("\nWould you like to enter another room? Enter Yes to continue: ")

#Final summary
print("\nSummary of All Rooms")
print("-" * 30)
print(f"Total rooms entered: {room_count}")
print(f"Total gallons for walls: {total_wall_gallons}")
print(f"Total gallons for ceiling/floor: {total_ceiling_gallons}")
print("-" * 30)
