def solution(myString):
    answer = ''
    for c in myString:
        if c == 'a':
            answer += 'A'
        elif c == 'A':
            answer += 'A'
        else:
            answer += c.lower()
    return answer