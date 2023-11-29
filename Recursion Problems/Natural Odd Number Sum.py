def NaturalOddNumberSum(num:int) -> int:
    if num == 1:
        return 1
    return (2*num - 1) + NaturalOddNumberSum(num - 1)

n = 10
print(f"Sum of first {n} odd natural numbers: {NaturalOddNumberSum(n)}")