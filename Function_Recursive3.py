min = 2
max = 10
total = 100

memo = {}

def sol(remain, seated):
    key = str([remain, seated])

    if key in memo:
        return memo[key]
    if remain < 0:
        return 0
    if remain == 0:
        return 1
    
    count = 0
    for i in range(seated, max+1):
        count += sol(remain-i, i)
    
    memo[key] = count

    return count

print(sol(total, min))
    