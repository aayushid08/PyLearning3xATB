# try, except and finally

try:
    num1 = int(input("Enter a Number 1\n"))
    num2 = int(input("Enter a Number 2\n"))
    result = num1/num2
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
else:
    print(f'Result is {result}')
finally:
    print("I will be executed anyhow!!")

    # this is how we can read the text of any text file
    # with open('pramod.txt', 'r') as file: # r means read mode
    #     print(file.read())
    #     file.close()

    # it is necessary to close the file
    # Kyuki interpretor ne usko khol rakha hai aur vo hamesha print hote rahegi console me aur present bhi rahegi in the memory.
    # it would be like wastage of memory
