# 프로그래머스 - 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    direction = [(1, 0), (0, 1), (-1, -1)]

    #0
    for i in range(n):
        temp = []
        for j in range(i + 1):
            temp.append(0)
        answer.append(temp)

    #0
    # answer = [[0]*i for i in range(1,n+1)]  # 위에 다섯줄 + 선언까지 여섯줄을 한 줄로 만들어 버리셨다..

    #1
    # step = [(0, 1), (-1, -1), (1, 0)]
    # dx, dy = step[-1]  # 이거 상당히 좋아.
    # x, y = -1, 0  # 요런 식으로 한 번에 두개 각각 할당하는 건 알았는데, 위에 거처럼 튜플로 한번에 할당도 상당히 괜찮아.

    # print(answer)
    # final_number = n*(n+1)//2
    # number = n*(n+1)//2 - 1
    number = 1
    r = -1
    c = 0
    for i in range(n, 0, -1):
        for j in range(i):
            # answer[r][c]=final_number-number
            # number -= 1

            #2
            # x += dx
            # y += dy
            # 여길 이렇게 분리하시고 밑에 answer[x][y] = num 이렇게 때리셨구만

            r += direction[(n - i) % 3][0]
            c += direction[(n - i) % 3][1]

            answer[r][c] = number
            number += 1

            # print('r, c: ', r, c)

        #3
        #  dx, dy = step[(n-recur_num)%3]  # 여기서 이렇게 한 번에 하는거 상당히 엑셀런트 해. 그리고 for문 바깥에서 한번씩만 연산해줘서 아 좋아 상당히.

    #4
    real_answer = []
    for i in answer:
        for j in i:
            real_answer.append(j)

    return real_answer

    #4
    '''
    # 위에 말고 이렇게 하는거 상당히 핸섬해
    result = []
    for s in answer:
        result += s
    return result
    '''


print(solution(4))
print(solution(5))
print(solution(6))

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (2.06ms, 10.9MB)
테스트 5 〉	통과 (2.67ms, 10.9MB)
테스트 6 〉	통과 (1.63ms, 10.8MB)
테스트 7 〉	통과 (187.78ms, 58.6MB)
테스트 8 〉	통과 (185.54ms, 60.2MB)
테스트 9 〉	통과 (201.88ms, 60.2MB)
'''


# 인재님 코드를 싸그리 가져와야겠군.. 좋다.. 배울 점 많다..
# https://github.com/boostcamp-level1-27/algorithm/blob/main/week1/Q2_Injae.py
'''
def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    x, y = -1, 0
    num = 1
    step = [(0, 1), (-1, -1), (1, 0)]
    dx, dy = step[-1]
    for recur_num in range(n, 0, -1):
        for _ in range(recur_num):
            x += dx
            y += dy
            answer[x][y] = num
            num += 1
        dx, dy = step[(n - recur_num) % 3]

    result = []
    for s in answer:
        result += s
    return result
'''



"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.66ms, 10.8MB)
테스트 5 〉	통과 (0.72ms, 10.8MB)
테스트 6 〉	통과 (0.62ms, 10.9MB)
테스트 7 〉	통과 (80.75ms, 59.9MB)
테스트 8 〉	통과 (86.44ms, 60MB)
테스트 9 〉	통과 (82.26ms, 60MB)
"""