def Factorial(num:int) -> int:
    if num == 0:
        return 1
    return num * Factorial(num - 1)

n = 20
print(f"Factorial of {n}: {Factorial(n)}")