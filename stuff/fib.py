import sys

def fibonacci(num):
    if num == 1 or num == 0:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(int(sys.argv[1])))
