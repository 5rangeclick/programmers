def solution(a, b):
    answer = 0
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    if int(ba) > int(ab):
        answer = ba
    else:
        answer = ab
    return int(answer)

##########################
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))