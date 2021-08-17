# 프로그래머스 - 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    direction = [(1, 0), (0, 1), (-1, -1)]

    for i in range(n):
        temp = []
        for j in range(i + 1):
            temp.append(0)
        answer.append(temp)

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
            r += direction[(n - i) % 3][0]
            c += direction[(n - i) % 3][1]

            answer[r][c] = number
            number += 1

            # print('r, c: ', r, c)

    real_answer = []
    for i in answer:
        for j in i:
            real_answer.append(j)

    return real_answer


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