def NaturalNumberSum(num:int) -> int:
    if num == 1:
        return 1
    return num + NaturalNumberSum(num - 1)

n = 5
print(f"Sum of first {n} natural numbers: {NaturalNumberSum(n)}")