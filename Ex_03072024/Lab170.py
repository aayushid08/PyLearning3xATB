
try:
    with open("TestData.txt", "r") as file:
        content = file.readlines()      #agar ek single line rahi to apan file.read()
        print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    file.close()
