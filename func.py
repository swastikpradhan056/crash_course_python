def greetHello(name):
    print(f"Your name is {name}")

fullName = input("Enter your name: ")

greetHello(fullName)


def letterGenerator(name, date):
    st = f"Hi ma'am, This is {name} and I will not come to school on {date}"
    print(st)

letterGenerator("Swastik", "April 1st")
letterGenerator("Rishav", "September 3rd")