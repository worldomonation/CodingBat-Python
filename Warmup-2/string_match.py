def string_match(a, b):
    count = 0
    c = zip(a, b)

    for x in range(len(c)-1):
        count = count+1 if (c[x][0] == c[x][1] and c[x+1][0] == c[x+1][1]) else count

    return count
