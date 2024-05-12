a = int(input("Enter a number: "))
match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 3:
        print("Case is 3")
    case 4:
        print("Case is 4")
    case 5:
        print("Case is 5")
    case _:
        print("No match found")

# Write a python program to print table of a number which is from 1 to 10

b = int(input("Enter a number: "))
match b:
    case 1:
        print(f"{b} x 1: {a * 1}")
    case 2:
        print(f"{b} x 2: {a * 2}")
    case 3:
        print(f"{b} x 3: {a * 3}")
    case 4:
        print(f"{b} x 4: {a * 4}")
    case 5:
        print(f"{b} x 5: {a * 5}")
    case 6:
        print(f"{b} x 6: {a * 6}")
    case 7:
        print(f"{b} x 7: {a * 7}")
    case 8:
        print(f"{b} x 8: {a * 8}")
    case 9:
        print(f"{b} x 9: {a * 9}")
    case 10:
        print(f"{b} x 2: {a * 10}")