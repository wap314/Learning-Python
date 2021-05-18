def linecount(filename):
    count = 0
    for line in open(filename):
        count = count + 1
    return count