# https://www.acmicpc.net/problem/10491

import sys

for sentence in sys.stdin:
    sentence = sentence.lower()
    if 'problem' in sentence:
        print('yes')
    else:
        print('no')
