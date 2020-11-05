import unittest
import levenshtein as lev

class CalcTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(lev.levenshtein_matrix("",""),0)
        self.assertEqual(lev.levenshtein_rec_wrap("",""),0)
        self.assertEqual(lev.levenshtein_rec_matr_wrap("",""),0)
        self.assertEqual(lev.dameray_levenshtein("",""),0)
    
    def test_2(self):
        self.assertEqual(lev.levenshtein_matrix("abc","abc"),0)
        self.assertEqual(lev.levenshtein_rec_wrap("abc","abc"),0)
        self.assertEqual(lev.levenshtein_rec_matr_wrap("abc","abc"),0)
        self.assertEqual(lev.dameray_levenshtein("abc","abc"),0)

    def test_3(self):
        self.assertEqual(lev.levenshtein_matrix("abc","ab"),1)
        self.assertEqual(lev.levenshtein_rec_wrap("abc","ab"),1)
        self.assertEqual(lev.levenshtein_rec_matr_wrap("abc","ab"),1)
        self.assertEqual(lev.dameray_levenshtein("abc","ab"),1)
    
    def test_4(self):
        self.assertEqual(lev.levenshtein_matrix("abc","acb"),2)
        self.assertEqual(lev.levenshtein_rec_wrap("abc","acb"),2)
        self.assertEqual(lev.levenshtein_rec_matr_wrap("abc","acb"),2)
        self.assertEqual(lev.dameray_levenshtein("abc","acb"),1)

    def test_5(self):
        self.assertEqual(lev.levenshtein_matrix("abc","abd"),1)
        self.assertEqual(lev.levenshtein_rec_wrap("abc","abd"),1)
        self.assertEqual(lev.levenshtein_rec_matr_wrap("abc","abd"),1)
        self.assertEqual(lev.dameray_levenshtein("abc","abd"),1)