def solution(casheSize, cities):
    from collections import deque
    hour = 0
    cashe_q = deque()
    length = len(cashe_q)
    for city in cities:
        city = city.lower()
        if city not in cashe_q:
            hour += 5
            if length < casheSize:
                cashe_q.append(city)
                length += 1
            else:
                cashe_q.append(city)
                cashe_q.popleft()
        else:
            hour += 1
            cashe_q.remove(city)
            cashe_q.append(city)
                
    return hour