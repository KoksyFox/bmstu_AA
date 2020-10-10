def print_matrix(s1, s2, matrix):
    print("\n   ", end = " ")
    for i in s2:
        print(i, end = " ")

    for i in range(len(matrix)):
        if i:
            print("\n" + s1[i-1], end = " ")
        else:
            print("\n ", end = " ")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
    print("\n")


def levenshtein_matrix(s1, s2):
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
            matrix[i][j] = min(matrix[i-1][j] + 1,
                               matrix[i][j-1] + 1,
                               matrix[i-1][j-1] + m)

    print_matrix(s1, s2, matrix)
    
    return matrix[-1][-1]


def levenshtein_rec_wrap(s1, s2):
    return levenshtein_recursive(s1, s2, len(s1), len(s2))


def levenshtein_recursive(s1, s2, i, j):
    if min(i, j) == 0:
        return max(i, j)
    else:
        m = 0 if s1[i-1] == s2[j-1] else 1
        return min(levenshtein_recursive(s1, s2, i-1, j) + 1,
                   levenshtein_recursive(s1, s2, i, j-1) + 1,
                   levenshtein_recursive(s1, s2, i-1, j-1) + m)

def levenshtein_rec_matr_wrap(s1, s2):
    n = len(s1)
    m = len(s2)
    matrix = [[-1 for j in range(m+1)] for i in range(n+1)]

    levenshtein_recursive_matrix(s1, s2, len(s1), len(s2), matrix)

    print_matrix(s1, s2, matrix)
    
    return matrix[-1][-1]


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
    print_matrix(s1, s2, matrix)
    
    return matrix[-1][-1]



def main():
    s1 = "telo"
    s2 = "stolb"
    print("Расстояние между строками:", levenshtein_rec_matr_wrap(s1, s2))


if __name__ == "__main__":
    main()
