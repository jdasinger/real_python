
while True:
    try:
        number = int(input("enter an integer: "))
        print("you entered ", number)
        break
    except ValueError:
        print("try again!")
    

    
