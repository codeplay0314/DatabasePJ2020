import json

fname = '2020-01-01-0.json'
fhand = open(fname, 'r', encoding='UTF-8')
write = open('content.txt', 'w', encoding='UTF-8')

t = 0
cnt = 0
quote = False
for line in fhand:
    t = t + 1
    if t > 10: break
    for c in line:
        if quote is True and c != '"':
            print(c, end = '', file = write)
            continue
        if c == '{':
            cnt = cnt + 1
            print(c, end = '', file = write)
            print(file = write)
            for i in range(cnt):
                print('    ', end = '', file = write)
        elif c == ',':
            print(c, file = write)
            for i in range(cnt):
                print('    ', end = '', file = write)
        elif c == '}':
            cnt = cnt - 1
            print(file = write)
            for i in range(cnt):
                print('    ', end = '', file = write)
            print(c, end = '', file = write)
        elif c == ': ':
            print(':', end = '', file = write)
        elif c == '"':
            if quote is True: quote = False
            else: quote = True;
            print(c, end = '', file = write)
        elif c != ' ':
            print(c, end = '', file = write)
