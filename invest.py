

def invest(amount, rate, time):
    print("principal amount: ", amount)
    print("annual rate of return: ", rate)
    for i in range(1, time+1):
        rr = amount * (1 + rate)
        print("year {}: $".format(i)+str(rr))
        amount = rr
    print() 
invest(200000, .07, 5)
invest(2000, .025, 5)
