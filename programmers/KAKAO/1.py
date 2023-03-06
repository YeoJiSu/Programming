# 크레인 인형뽑기 게임
basket = []
def solution(board, moves):
    answer = 0
    for i in range(len(moves)):
        line = moves[i] 
        for j in range(len(board)):        
            value = board[j][line-1]
            if value==0:
                continue
            else:
                if len(basket)!=0:
                    if (basket[-1] == value):
                        basket.pop()
                        answer+=2
                    else:
                        basket.append(value)
                else:
                    basket.append(value)
                board[j][line-1] = 0 
                break
    return answer