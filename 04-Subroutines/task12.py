def sum(n):
    if n < 1:
        return None
    if n == 0 or n == 1:
        return 1
    return n + sum(n - 1)

print(sum(3))