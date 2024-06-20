# ✅ #4. Fibonaci series

# first if we not get the solution learn to change the view at problem

# pehele humne dekha ki series kaisi hai: we got (n+1)-(n+2)..........something

# ab directly series dekh kaisi dekhti : fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#                                               stp1       a  b  c  |  |
#                                               stp2          a  b  c  |
#                                               stp3             a  b  c

n = int(input("Enter the Number: "))


def fib(n):
    if n <= 0:
        print("Na beta na, number 0 se bada laa de")
    else:
        a = 0
        b = 1
        if n == 1:
            print(1)
        else:
            print(a)
            print(b)
            for i in range(2, n):
                c = a + b
                a = b
                b = c
                print(c)


fib(n)
