file = open('aauth.log.1b.txt', 'r')
f = file.readlines()
for line in f:
    if line.find('Failed password') > 0:
        print(line)
