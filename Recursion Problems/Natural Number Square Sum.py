def NaturalNumberSquareSum(num:int) -> int:
    if num == 1:
        return 1
    return num ** 2 + NaturalNumberSquareSum(num - 1)

n = 10
print(f"Sum of square of first {n} natural numbers: {NaturalNumberSquareSum(n)}")