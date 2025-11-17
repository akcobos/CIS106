#Problem 1 
def display_student_grades(student_grades):
    print(f"{'Student':<15}{'Grade':>6}")
    print("-" * 21)
    total = 0
    for name, grade in student_grades.items():
        print(f"{name:<15}{grade:>6}")
        total += grade
    class_average = total / len(student_grades)
    print("\nClass Average:", round(class_average, 2))



#Problem 2
def compute_student_averages(student_grades):
    averages = []
    for name, grades in student_grades.items():
        avg = sum(grades) / len(grades)
        averages.append([name, avg])
    return averages

def compute_class_averages(student_grades):
    grade_totals = [0, 0, 0]
    count = len(student_grades)
    for grades in student_grades.values():
        for i in range(3):
            grade_totals[i] += grades[i]
    return [round(total / count, 2) for total in grade_totals]

def display_student_averages(student_grades):
    print(f"{'Student':<15}{'Average':>8}")
    print("-" * 25)
    for name, avg in compute_student_averages(student_grades):
        print(f"{name:<15}{avg:>8.2f}")
    class_avgs = compute_class_averages(student_grades)
    print("\nClass Averages for Each Grade:")
    for i, avg in enumerate(class_avgs, start=1):
        print(f"Grade {i}: {avg}")


#Problem 3
def load_player_data(filename):
    player_dict = {}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            player_dict[parts[0]] = float(parts[1])
    return player_dict

def display_players(player_dict):
    print(f"{'Player':<15}{'Average':>10}")
    print("-" * 25)
    for name, avg in player_dict.items():
        print(f"{name:<15}{avg:>10.3f}")


#Problem 4
def search_player(player_dict, search_name):
    search_name = search_name.lower()
    found = False
    for name, avg in player_dict.items():
        if name.lower() == search_name:
            print(f"{name} has a batting average of {avg:.3f}")
            found = True
            break
    if not found:
        print("Name not found.")


#Problem 5
import math

def compute_paint_gallons(length, width, height):
    area = 2 * height * (length + width)
    gallons = math.ceil(area / 50)        
    return gallons

def collect_room_data():
    room_dict = {}
    while True:
        room_name = input("\nEnter room name (or 'done' to finish): ")
        if room_name.lower() == "done":
            break
        length = float(input("Enter room length (ft): "))
        width = float(input("Enter room width (ft): "))
        height = float(input("Enter room height (ft): "))
        gallons = compute_paint_gallons(length, width, height)
        room_dict[room_name] = gallons
    return room_dict

def display_paint_requirements(room_dict):
    print(f"\n{'Room':<15}{'Gallons':>10}")
    print("-" * 25)
    for room, gallons in room_dict.items():
        print(f"{room:<15}{gallons:>10}")
