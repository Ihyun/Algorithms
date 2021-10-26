T = int(input())
for t in range(T):
    N = int(input())
    prices = [*map(int, input().split())]
    print('Case #%d: '%(t+1), end='')  # f'~{t+1}' 이렇게 쓰는게 제일 빠름
    while prices:
        discounted = prices.pop(0)
        print(discounted, '', end='')
        prices.remove(discounted*4//3)

