def sayHello():
    print("Hello world.")

sayHello()
sayHello()

def compare(number1,number2):
    if number1 > number2:
        print("{} is bigger than {}".format(number1,number2))
    elif number2 > number1:
        print("{} is bigger than {}".format(number2,number1))
    else:
        print("{} and {} is equal".format(number1,number2))


compare(4,4)



