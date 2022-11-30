decide = int(input("Enter number 1 for 1., 2 for 2.: "))

if decide == 1:
    try:
        print("This will execute first")
    except:
        print("This will only execute if error in try")


if decide == 2:
    try:
        a = int(input("Enter num 1: "))
        b = int(input("Enter num 2: "))
        print(a/b)
        print(a+b)
    
    except ValueError: #runs if value error
        print("Could not convert to integer")

    except ZeroDivisionError: #runs if try to divide by 0
        print("Can't divide by zero")

    except: #run if unspecified error occur
        print("Something unexpected happend")