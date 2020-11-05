import time
import random
import string
import levenshtein as lev


def RandomString(strLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(strLength))

def time_test(len):
    start_time = time.time()
    for _ in range(100):
        str1 = RandomString(len)
        str2 = RandomString(len)
        lev.levenshtein_matrix(str1, str2)
    end_time = time.time()
    lev_matr_time = (end_time - start_time)*1000

    start_time = time.time()
    for _ in range(100):
        str1 = RandomString(len)
        str2 = RandomString(len)
        lev.levenshtein_rec_wrap(str1, str2)
    end_time = time.time()
    lev_rec_time = (end_time - start_time)*1000

    start_time = time.time()
    for _ in range(100):
        str1 = RandomString(len)
        str2 = RandomString(len)
        lev.levenshtein_rec_matr_wrap(str1, str2)
    end_time = time.time()
    lev_recmat_time = (end_time - start_time)*1000

    start_time = time.time()
    for _ in range(100):
        str1 = RandomString(len)
        str2 = RandomString(len)
        lev.dameray_levenshtein(str1, str2)
    end_time = time.time()
    damer_time = (end_time - start_time) *1000

    print("Time test with strings length = ", len,"\n \
\t1. Levenshtein_matrix: ", lev_matr_time,"\n \
\t2. Levenshtein_rec: ", lev_rec_time,"\n \
\t3. Levenshtein_rec_matr: ", lev_recmat_time,"\n \
\t4. Dameray_Levenshtein: ", damer_time,"\n")

