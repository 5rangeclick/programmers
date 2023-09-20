def solution(numbers, n):
    answer = 0
    idx = 0
    
    while answer <= n:
        answer += numbers[idx]
        idx += 1 
        
    return answer

#############

def solution(numbers, n):
    answer = 0
    for i in numbers:
        if answer > n:
            pass
        else:
            answer += i
    return answer