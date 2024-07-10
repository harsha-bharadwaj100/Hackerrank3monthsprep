def flippingBits(n):
    # Write your code here
    l32 = ["0"] * 32
    res = bin(n)[2:]
    for x in range(len(res)):
        del l32[-1]
    l32 += res
    for x in range(len(l32)):
        if l32[x] == "0":
            l32[x] = "1"
        else:
            l32[x] = "0"
    return int("".join(l32), base=2)


print(flippingBits(int(input().strip())))
