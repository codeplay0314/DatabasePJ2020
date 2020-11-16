out = open('2020-01-01-012.json', 'w')

for i in range(0, 3):
    for line in open('2020-01-01-' + str(i) + '.json', 'r').readlines():
        out.write(line)