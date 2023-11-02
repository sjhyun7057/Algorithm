'''
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
'''

def solution(people, limit):
    answer = 0
    
    lst = []
    lmt = min(people)
    for p in range(len(people)):
        if people[p] + lmt > limit:
            answer += 1
        else:
            lst.append(people[p])
    
    lst.sort()
    start = 0
    end = len(lst) - 1
    while start <= end:
        if lst[start] + lst[end] <= limit:
            start += 1
            end -= 1
            answer += 1
        else:
            end -= 1
            answer += 1
    return answer