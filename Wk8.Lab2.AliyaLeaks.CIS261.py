Aliya Leaks
CIS 261
Week8 Lab 2, Fibonacci 

print("Fibonacci series for the number 16")

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    for i in range(16):
        print(fib(i), end=", ")
    print("...")

if __name__ == "__main__":
    main()

