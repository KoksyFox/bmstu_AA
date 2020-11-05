def levenshtein_recursive_matrix(s1, s2, i, j, matrix):
    if min(i, j) == 0:
        matrix[i][j] = max(i, j)
    else:
        if matrix[i][j] == -1:
            m = 0 if s1[i-1] == s2[j-1] else 1
            matrix[i][j] = min(levenshtein_recursive_matrix(s1, s2, i-1, j, matrix) + 1,
                               levenshtein_recursive_matrix(s1, s2, i, j-1, matrix) + 1,
                               levenshtein_recursive_matrix(s1, s2, i-1, j-1, matrix) + m)
    return matrix[i][j]