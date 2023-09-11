from typing import List
from sys import stdin

input = stdin.readline


def solution(wines: List[int]) -> int:
    dp = [0 for _ in range(len(wines) + 2)]
    dp[2] = wines[0]

    for i in range(3, len(wines) + 2):
        dp[i] = max(
            dp[i - 3] + wines[i - 3] + wines[i - 2],
            dp[i - 2] + wines[i - 2],
            dp[i - 1],
        )

    return dp[-1]


if __name__ == "__main__":
    n = int(input())
    wines = [int(input()) for _ in range(n)]
    print(solution(wines))
