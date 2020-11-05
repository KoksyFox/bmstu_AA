public static int[][] MultVinOpt(int[][] matr1, int[][] matr2)
        {
            int n1 = matr1.Length;
            int n2 = matr2.Length;

            if (n1 == 0 || n2 == 0)
                return null;

            int m1 = matr1[0].Length;
            int m2 = matr2[0].Length;

            if (m1 != n2)
                return null;

            int[] mulH = new int[n1];
            int[] mulV = new int[m2];

            int[][] res = new int[n1][];
            for (int i = 0; i < n1; i++)
                res[i] = new int[m2];

            int m1Mod2 = m1 \% 2;
            int n2Mod2 = n2 \% 2;

            for (int i = 0; i < n1; i++)
            {
                for (int j = 0; j < (m1 - m1Mod2); j += 2)
                {
                    mulH[i] += matr1[i][j] * matr1[i][j + 1];
                }
            }

            for (int i = 0; i < m2; i++)
            {
                for (int j = 0; j < (n2 - n2Mod2); j += 2)
                {
                    mulV[i] += matr2[j][i] * matr2[j + 1][i];
                }
            }

            for (int i = 0; i < n1; i++)
            {
                for (int j = 0; j < m2; j++)
                {
                    int buff = -(mulH[i] + mulV[j]);
                    for (int k = 0; k < (m1 - m1Mod2); k += 2)
                    {
                        buff += (matr1[i][k + 1] + matr2[k][j]) * \
                                (matr1[i][k] + matr2[k + 1][j]);
                    }
                    res[i][j] = buff;
                }
            }

            if (m1Mod2 == 1)
            {
                int m1Min_1 = m1 - 1;
                for (int i = 0; i < n1; i++)
                {
                    for (int j = 0; j < m2; j++)
                    {
                        res[i][j] += matr1[i][m1Min_1] * \
                                     matr2[m1Min_1][j];
                    }
                }
            }
            
            return res;
        }