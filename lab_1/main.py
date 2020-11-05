##
##

import levenshtein as lev
import time_test as t

def GetStrAndRun(function):
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    print("Расстояние между строками:", function(str1, str2))

def Menu():
    flag = True
    while (flag):
        case = input("Меню:\n \
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
        elif (case == "5"):
            t.time_test(3)
            t.time_test(5)
            t.time_test(7)
            t.time_test(10)
        else:
            flag = False



if __name__ == "__main__": 
    Menu()