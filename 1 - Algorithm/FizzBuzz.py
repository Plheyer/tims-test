import sys

if len(sys.argv) < 2:
    print("No number given")
    exit(1)
elif len(sys.argv) > 2:
    print("Too many parameters.")
    exit(1)

def fizzBuzz(number):
    for i in range(1, number + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzBuzz(int(sys.argv[1]))