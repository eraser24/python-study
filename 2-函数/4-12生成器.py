def tail(filename):
    f = open(filename,encoding='utf-8')
    while True:
        line = f.readline()
        if line.strip():
            print('****',line.strip())
tail('file')
