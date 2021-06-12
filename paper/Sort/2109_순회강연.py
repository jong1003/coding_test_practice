import heapq
from functools import reduce

'''
빈날짜를 찾아가기
빈날짜가 존재하지 않을때 제일 적은 페이를 주는 날과 비교해서 자신보다 작다면 교체하기
'''


def solution(n, pd):
    day = [0]*10001
    pd.sort(key=lambda x: (x[1], -x[0]))
    pq = []

    for idx in range(len(pd)):
        d = pd[idx][1]
        p = pd[idx][0]
        if day[d] != 0:
            flag = False
            for j in range(d-1, 0, -1):
                if day[j] == 0:
                    day[j] = p
                    flag = True
                    break
            if not flag:
                for j in range(d-1, 0, -1):
                    heapq.heappush(pq, (day[j], j))
                if pq:
                    d1 = heapq.heappop(pq)[1]
                    day[d1] = max(day[d1], p)
                pq.clear()
        else:
            day[d] = p

    return reduce(lambda x, y: x + y, day)


if __name__ == "__main__":
    n = int(input())
    pd = list()
    for i in range(n):
        pd.append(list(map(int, input().split())))
    print(solution(n, pd))