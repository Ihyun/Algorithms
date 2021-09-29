import sys

for sentence in sys.stdin:
    sentence = sentence.lower()
    if 'problem' in sentence:
        print('yes')
    else:
        print('no')
