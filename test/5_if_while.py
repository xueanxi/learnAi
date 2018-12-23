number = 24
isRunning = True
while isRunning:
    guess = int(input("please input a number:"))
    if number == guess:
        print("you right")
        isRunning = False
    elif guess < number:
        print("small")
    elif guess > number:
        print("big")
    else:
        print("error")
print("Done")
