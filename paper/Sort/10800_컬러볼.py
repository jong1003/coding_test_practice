'''
방법 1
1. 제일 위에서부터 완전 탐색을 하면서 자신보다 작고 다른 색깔을 가진 공들을 탐색한다 -> O(N^2)
방법 2
1. 크기가 가벼운 순으로 정렬을 한다
2. 크기가 제일 작은 순부터 비교를 한다
    2-1. 자신과 같은 크기라면 탐색을 종료하면서 맵에다가 자신의 색깔에 크기를 등록 하고 전체 크기+
    2-2. 자신보다 큰수를 만나면 누적된 크기 가져오기 자신을 등록하고 끝
o = index, 1 = color 2 = size
'''


def solution(n, balls):
    answer = [0]*n
    ball_map = dict()
    ball_list = list()
    for i in range(len(balls)):
        ball_list.append((i, balls[i][0], balls[i][1]))
    ball_list.sort(key=lambda x: x[2])

    sum = 0
    size = len(ball_list)
    tmp = dict()
    for i in range(len(ball_list)):
        idx, c, s = ball_list[i]
        if size < s:
            for key in tmp.keys():
                if key in ball_map.keys():
                    ball_map[key] += tmp[key]
                else:
                    ball_map[key] = tmp[key]
                sum += tmp[key]
            tmp.clear()
        if c in tmp.keys():
            tmp[c] += s
        else:
            tmp[c] = s
        answer[idx] += sum
        if c in ball_map.keys():
            answer[idx] -= ball_map[c]
        size = s

    return answer


if __name__ == "__main__":
    n = int(input())
    balls = list()
    for i in range(n):
        balls.append(list(map(int, input().split())))
    for ans in solution(n, balls):
        print(ans)