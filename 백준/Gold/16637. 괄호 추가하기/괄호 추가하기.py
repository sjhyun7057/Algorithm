import sys
input = sys.stdin.readline

length = int(input())
math_cal = input()

num = []; oper = []

def calculate(num, oper):
    while oper:
        op = oper.pop(0)
        x = num.pop(0); y = num.pop(0)
        if op == '+':
            num.insert(0, x + y)
        elif op == '-':
            num.insert(0, x - y) 
        elif op == '*':
            num.insert(0, x * y)
    return num[0]

def solve(cnt, num, oper):
    global result
    if cnt == length // 2 or len(num) == 1:
        result = max(result, calculate(num, oper))
        return
    
    solve(cnt+1, num[:], oper[:])
    
    try:
        x = num.pop(cnt); y = num.pop(cnt)
        op = oper.pop(cnt)
        if op == '+':
            num.insert(cnt, x + y)
        elif op == '-':
            num.insert(cnt, x - y) 
        elif op == '*':
            num.insert(cnt, x * y)

        solve(cnt+1, num[:], oper[:])
    except:
        0
for i in range(length):
    if i % 2:
        oper.append(math_cal[i])
    else:
        num.append(int(math_cal[i]))
        
result = -2**31 - 1     
solve(0, num, oper)
print(result)