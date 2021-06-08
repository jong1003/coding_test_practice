
'''
DFS 문제
순환하는 곳을 찾는 문제로 보면 틀릴 수 있는 문제입니다
틀릴 수 있는 테스트 케이스
3 4
DLRL
DRLU
RRRU

3 4
RLLL
DRLU
RRRU
'''

def solution(n, m, board):
    visited = [[0]*m for row in range(n)]
    safe_box = set()
    idx = 1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if visited[i][j] > 0 : continue
            safe_box.add(search(i, j, idx, board, visited))
            idx += 1

    return len(safe_box)


def search(r, c, idx, board, visited):
    if visited[r][c] > 0:
        return visited[r][c]
    elif visited[r][c] == 0:
        visited[r][c] = idx

    if board[r][c] == "U":
        newR = r-1
        visited[r][c] = search(newR, c, idx, board, visited)
    elif board[r][c] == "D":
        newR = r+1
        visited[r][c] = search(newR, c, idx, board, visited)
    elif board[r][c] == "L":
        newC = c-1
        visited[r][c] = search(r, newC, idx, board, visited)
    else:
        newC = c+1
        visited[r][c] = search(r, newC, idx, board, visited)

    return visited[r][c]


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    board = list()
    for i in range(n):
        board.append(input())
    print(solution(n, m, board))