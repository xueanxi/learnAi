isRunning = True
while isRunning:
    inputString = str(input("please input a string:"))
    if inputString == "quit":
        break
    else:
        print("your input string {} ,length = {}".format(inputString,len(inputString)))
