# Programmers - 풍선 터트리기
# https://programmers.co.kr/learn/courses/30/lessons/68646#
import random


def solution(a):
    answer = 0
    la = len(a)

    if la == 1:
        return 1
    elif la == 2:
        return 2

    # min_left = a[0]
    # min_right = min(a[2:])

    min_lefts = [0]*la
    min_rights = [0]*la

    min_left = a[0]
    min_lefts[0] = a[0]
    min_right = a[-1]
    min_rights[-1] = a[-1]

    for i in range(la-1, -1, -1):
        if min_right > a[i]:
            min_right = a[i]
        min_rights[i] = min_right

    for pi in range(1, len(a) - 1):
        pivot = a[pi]
        # min_left = min(a[:pi])
        # min_right = min(a[pi+1:])

        if min_left > pivot:
            min_left = a[pi]
        min_lefts[pi] = min_left

        if not (pivot > min_lefts[pi-1] and pivot > min_rights[pi+1]):
            answer += 1

        # print('min_left, pivot, min_right: ', min_left, pivot, min_right)

    answer += 2
    return answer


'''
def solution(a):
    answer = 0

    if len(a) == 1:
        return 1
    elif len(a) == 2:
        return 2

    # min_left = a[0]
    # min_right = min(a[2:])
    mini = a[0]
    idx_mini = 0

    for pi in range(1, len(a)):
        pivot = a[pi]

        if mini > pivot:
            answer += (pi-idx_mini) - 1
            mini = pivot
            idx_mini = pi
            print('mini, idx_mini, answer: ', mini, idx_mini, answer)

    # answer += 2
    return len(a)-answer
    
# 이렇게 만들게 되면 
# [-9, -15, 37, 11, 12, 31, -75, -56, -65, 33]
# 이런 케이스에서 오류남.
# -75 이후로 min update는 이루어지지 않지만 -56의 양쪽 min이 모두 -56보다 작기 때문.
# 따라서 이렇게 풀면 안 됨.

# 가장 vote가 높은 코드의 경우 이 코드와 풀이는 똑같았지만, 배열을 reverse 시켜서 똑같은 매커니즘으로 한 번 더 세 줌. 그러면 빠지는 것 없이 셀 수 있음.
###
# def solution(a):
#     answer = 1
#     M = min(a)
#     for _ in range(2):
#         m = a[0]
#         i = 1 # 첫번째 반복에서는 맨 뒤에 애를 셀 수 있고, 두번째 반복에서는 맨 첫번째 애를 셀 수 있다.
#         while m != M:
#             if m >= a[i]:
#                 m = a[i]
#                 answer += 1  # 나처럼 중간에 안되는 애들을 더해준게 아니라 min으로 업데이트 되는애 (가능한 애)를 세주는 방식을 취했다.
#             i += 1
#         a.reverse()
#     return answer
###
'''


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))

print(solution([-9, -15, 37, 11, 12, 31, -65, -56, -75, 33]))

# print(solution([-23 ,-63 ,80 ,99 ,51 ,61 ,44 ,66 ,56 ,-91 ,86 ,-28 ,85 ,93 ,24 ,87 ,17 ,12 ,-5 ,78]))
#
# for i in range(20):
#     print(random.randint(-100,100),',', end='')


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.25ms, 10.1MB)
테스트 4 〉	통과 (33.99ms, 15.2MB)
테스트 5 〉	통과 (122.66ms, 36.7MB)
테스트 6 〉	통과 (181.50ms, 50.3MB)
테스트 7 〉	통과 (244.02ms, 63.9MB)
테스트 8 〉	통과 (251.64ms, 63.9MB)
테스트 9 〉	통과 (243.85ms, 63.9MB)
테스트 10 〉	통과 (272.31ms, 63.8MB)
테스트 11 〉	통과 (253.88ms, 63.7MB)
테스트 12 〉	통과 (259.10ms, 63.7MB)
테스트 13 〉	통과 (253.94ms, 63.9MB)
테스트 14 〉	통과 (271.64ms, 63.8MB)
테스트 15 〉	통과 (279.18ms, 64MB)
'''