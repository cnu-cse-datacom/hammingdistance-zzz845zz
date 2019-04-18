def hamming(a, b):
    #print(list(zip(a, b)))
    #print([i for i in filter(lambda x: x[0]!=x[1], zip(a, b))])
    return len([i for i in filter(lambda x: x[0]!=x[1], zip(a, b))])
