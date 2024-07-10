def diagonalDifference(arr):
    # Write your code here
    d1sum, d2sum = 0, 0
    i, j = 0, 0
    while i < len(arr) and j < len(arr):
        d1sum += arr[i][j]
        i += 1
        j += 1

    i, j = 0, len(arr) - 1
    while i < len(arr) and j >= 0:
        d2sum += arr[i][j]
        i += 1
        j -= 1

    return abs(d1sum - d2sum)


if __name__ == "__main__":

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
