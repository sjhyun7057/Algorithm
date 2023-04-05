def solution(n, k):
    k_word = ''

    def find_top_k(n, k):
        top = 0
        while n > k:
            if n // k:
                n //=  k
                top += 1
            else:
                break
        return top
    
    top = find_top_k(n, k)
    print(top)
    def find_p(top, k, n): 
        nonlocal k_word
        for t in range(top, -1, -1):
            if n == 0:
                k_word += '0'
                continue
            for i in range(k-1, 0, -1):
                if i*(k**t) <= n:
                    k_word += str(i)
                    n -= i*(k**t)
                    break
            else:
                k_word += '0'
    
    find_p(top, k, n)

    def check_prime(num_lst):
        cnt = 0
        for num in num_lst:
            if num == '1' or num == '':
                continue
            else:
                num = int(num)
            if num == 2:
                cnt += 1
            if not num % 2:
                continue
            else:
                for i in range(3, num+1, 2):
                    if i * i > num:
                        cnt += 1
                        break
                    if not num % i:
                        break
        return cnt
    
    answer = check_prime(k_word.split('0'))


    return answer