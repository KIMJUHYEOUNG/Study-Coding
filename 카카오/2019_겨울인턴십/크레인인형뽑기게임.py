def solution(board, moves):
    holes = []
    answer = 0
    for move in moves:
        move -= 1
        n = 0
        for loc in board:
            if loc[move]:
                holes.append(loc[move])
                loc[move] = 0
                board[n] = loc
                if len(holes) > 1 and holes[-1] == holes[-2]:
                    holes.pop(-1)
                    holes.pop(-1)
                    answer += 1
                break
            n += 1
        
    return answer*2
