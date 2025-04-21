def generate_magic_square(n):
    if n % 2 == 1:
        magic_square = [[0] * n for _ in range(n)]
        num = 1
        i, j = 0, n // 2
        while num <= n * n:
            magic_square[i][j] = num
            num += 1
            ni, nj = (i - 1) % n, (j + 1) % n
            if magic_square[ni][nj]:
                i = (i + 1) % n
            else:
                i, j = ni, nj
        return magic_square
    elif n % 4 == 0:
        magic_square = [[(n * i) + j + 1 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if (i % 4 == j % 4) or (i % 4 + j % 4 == 3):
                    magic_square[i][j] = n * n + 1 - magic_square[i][j]
        return magic_square
    else:
        def swap_cells(square, a, b, r):
            for i in range(r):
                square[i][a], square[i][b] = square[i][b], square[i][a]

        p = n // 2
        k = (n - 2) // 4
        sub_square = generate_magic_square(p)
        magic_square = [[0] * n for _ in range(n)]
        for i in range(p):
            for j in range(p):
                magic_square[i][j] = sub_square[i][j]
                magic_square[i + p][j + p] = sub_square[i][j] + p * p
                magic_square[i][j + p] = sub_square[i][j] + 2 * p * p
                magic_square[i + p][j] = sub_square[i][j] + 3 * p * p

        for i in range(p):
            for j in range(k):
                magic_square[i][j], magic_square[i + p][j] = magic_square[i + p][j], magic_square[i][j]
        for i in range(p):
            for j in range(n - k + 1, n):
                magic_square[i][j], magic_square[i + p][j] = magic_square[i + p][j], magic_square[i][j]
        magic_square[p // 2][0], magic_square[p // 2 + p][0] = magic_square[p // 2 + p][0], magic_square[p // 2][0]
        return magic_square

for n in range(4, 9):
    print(f"Magic Square for N={n}")
    square = generate_magic_square(n)
    for row in square:
        print(row)
    print()
