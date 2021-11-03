file = open('aauth.log.1b.txt', 'r')
f = file.readlines()
for line in f:
    if line.find('Failed password') > 0 and line.find('invalid user') > 0:
        print(line[slice(line.find('user'), line.find('from'))])
