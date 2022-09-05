
def solution(queue1, queue2):
    
    from collections import deque
    queue1 = deque(queue1); queue2 = deque(queue2)
     
    def check(queue3,queue4):
        cnt = 0
        sum1, sum2 = sum(queue1), sum(queue2)
        length1, length2 = len(queue1), len(queue2)
        max_cnt = (length1 + length2) * 2
        while sum1 != sum2:
            if sum1 > sum2:
                # q1 = queue1.pop(0)
                q1 = queue1.popleft()
                # queue2.insert(length2, q1)
                queue2.append(q1)
                cnt += 1
                sum1 -= q1; length1 -= 1
                sum2 += q1; length2 += 1

            elif sum1 < sum2:
                # q2 = queue2.pop(0)
                q2= queue2.popleft()
                # queue1.insert(length1, q2)
                queue1.append(q2)
                cnt += 1
                sum2 -= q2; length2 -= 1
                sum1 += q2; length1 += 1
            if queue3 == queue1 or queue2 == queue4 or not queue1 or not queue2 or cnt > max_cnt:
                return -1
        return cnt
    import copy    
    queue3, queue4 = queue1.copy(), queue2.copy()
    cnt = check(queue3,queue4)
    return cnt
