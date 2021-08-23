# Programmers - 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    answer = 0
    sol = len(s)
    dic = {}
    '''
    for i in range (1, len(s)//2+1):
        dic.clear()
        for j in range (0,len(s)+1-i,i):
            if s[j,j+i] in dic:
                dic[s[j,j+i]]+=1
            else:
                dic[s[j,j+1]]=0
    '''
    # 이렇게 짜면 연달아서 중복된게 아니라 띄엄띄엄 중복된것도 함께 카운팅하게 되어서 오류남

    for i in range(1, len(s) // 2 + 1):
        tempstr = s[0:i]
        tempsol = i + len(s) % i
        tempcnt = 1
        for j in range(i, len(s) + 1 - i, i):
            if tempstr != s[j:j + i]:
                tempstr = s[j:j + i]
                tempsol += i
                if tempcnt > 1:
                    tempsol += len(str(tempcnt))
                tempcnt = 1
            else:
                '''
                if (already == 0):
                    tempsol +=1
                    already = 1
                '''
                # 카운트가 두자리수 이상이면 자릿수가 +1 뿐만 아니라 +n 이 되는건데 간과하였음
                tempcnt += 1
        if tempcnt > 1:
            tempsol += len(str(tempcnt))
        if tempsol < sol:
            sol = tempsol

    return sol
