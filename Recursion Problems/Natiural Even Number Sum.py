def NaturalEvenNumberSum(num:int) -> int:
    if num == 1:
        return 2
    return 2*num + NaturalEvenNumberSum(num - 1)

n = 10
print(f"Sum of first {n} even natural numbers: {NaturalEvenNumberSum(n)}")