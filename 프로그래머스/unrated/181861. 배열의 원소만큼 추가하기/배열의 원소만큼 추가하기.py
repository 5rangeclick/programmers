# def solution(arr):
#     answer = []
#     for a in arr:
#         answer += str(a)*a
#     answer = [int(i) for i in answer]
    
def solution(arr):
    answer = [] 
    for i in arr:
        answer += [i]*i

    #컴프리헨션 안 쓸 경우
    # answ = []
    # for i in answer:
    #     answ.append(int(i))
    # return answ
    return answer