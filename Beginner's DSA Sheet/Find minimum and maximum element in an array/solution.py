def getMinMax( a, n):
    min_ = float('inf')
    max_ = float('-inf')
    for i in a:
        if i < min_:
            min_ = i
        if i > max_:
            max_ = i
    return min_, max_