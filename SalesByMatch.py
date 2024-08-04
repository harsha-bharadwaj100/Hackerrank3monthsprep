def sockMerchant(n, ar):
    # Write your code here
    di = dict()
    for i in ar:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    pairs = 0
    for x in di:
        pairs += di[x] // 2
    print(pairs)


sockMerchant(7, [1, 2, 1, 2, 1, 3, 2])
