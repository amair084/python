from math import sqrt as squareRoot

squareRoot(5)
def safe_root(a, b):
    if a >= 0:
        answer = a ** (1 / b)
    else:
        if a % 2 == 0:
            answer = "Result is an imaginary number"
        else:
            answer = -(-a) ** (1 / b)
    return answer

print(safe_root(1, 1))