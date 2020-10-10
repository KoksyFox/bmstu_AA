##
##

import levenshtein as lev

def GetStrAndRun(function):
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    res = function(str1, str2)
    print("Дистанция между строками = ", res)

def Menu():
    flag = True
    while (flag):
        case = input("Menu:\n \
\t1. Левенштейн с матрицей\n \
\t2. Левенштейн с рекурсией\n \
\t3. Левенштейн рекурсивный с матрицей\n \
\t4. Дамерау-Левенштейн\n \
\t5. Анализ времени\n \
\t0. Выход\n")
        if (case == "1"):
            GetStrAndRun(lev.levenshtein_matrix)
        elif (case == "2"):
            GetStrAndRun(lev.levenshtein_rec_wrap)
        elif (case == "3"):
            GetStrAndRun(lev.levenshtein_rec_matr_wrap)
        elif (case == "4"):
            GetStrAndRun(lev.dameray_levenshtein)      
        else:
            flag = False



if __name__ == "__main__": 
    Menu()