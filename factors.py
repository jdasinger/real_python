number = input("Enter a positive integer: ")

def factors(number):
    number = int(number)
    for i in range(1,number+1):
        if number % i == 0:
            print("{0} is a divisor of {1}".format(i, number))


factors(number)

