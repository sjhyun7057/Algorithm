'''
cap: 트럭에 실을 수 있는 재활용 택배 상자
deliveries: 배달할 상자 개수
pickups: 수거할 상자 개수
'''


def solution(cap, n, deliveries, pickups):
    pickups = pickups[::-1]
    deliveries = deliveries[::-1]
    answer = 0
    deliver = 0; pickup = 0
    for i in range(n):
        deliver += deliveries[i]
        pickup += pickups[i]
        
        while deliver > 0 or pickup > 0: # 만약 deliver나 pickup이 cap보다 큰 경우 그 곳을 한번 더 방문
            deliver -= cap 
            pickup -= cap
            answer += (n-i) * 2
    return answer