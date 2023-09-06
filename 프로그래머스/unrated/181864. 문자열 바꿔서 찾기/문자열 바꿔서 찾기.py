def solution(myString, pat):
    ab = ''
    for i in myString:
        if i == 'A':
            ab+='B'
        else:
            ab+='A'
    return 1 if pat in ab else 0
