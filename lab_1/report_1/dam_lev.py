def dameray_levenshtein(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    matrix = [[0 for j in range(n2+1)] for i in range(n1+1)]

    for i in range(n1+1):
        matrix[i][0] = i

    for j in range(n2+1):
        matrix[0][j] = j

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            m = 0 if s1[i-1] == s2[j-1] else 1
            if i > 1 and j > 1 and s1[i-2] == s2[j-1] and s1[i-1] == s2[j-2]:
                matrix[i][j] = min(matrix[i-1][j] + 1,
                                   matrix[i][j-1] + 1,
                                   matrix[i-1][j-1] + m,
                                   matrix[i-2][j-2] + 1)
            else:
                matrix[i][j] = min(matrix[i-1][j] + 1,
                                   matrix[i][j-1] + 1,
                                   matrix[i-1][j-1] + m)
    
    return matrix[-1][-1]