memory_lst = [0]*11

memory_lst[0] = 1
memory_lst[1] = 2
memory_lst[2] = 4

def plus_ott(x):
    if x <= 3:
        return memory_lst[x-1]
    else:
        return plus_ott(x-1)+plus_ott(x-2) + plus_ott(x-3)
    
for i in range(int(input())):
    print(plus_ott(int(input())))