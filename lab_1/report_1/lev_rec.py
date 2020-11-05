def levenshtein_recursive(s1, s2, i, j):
    if min(i, j) == 0:
        return max(i, j)
    else:
        m = 0 if s1[i-1] == s2[j-1] else 1
        return min(levenshtein_recursive(s1, s2, i-1, j) + 1,
                   levenshtein_recursive(s1, s2, i, j-1) + 1,
                   levenshtein_recursive(s1, s2, i-1, j-1) + m)