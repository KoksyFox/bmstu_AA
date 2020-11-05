public static int[][] MultStand(int[][] mart1, int[][] matr2)
        {
            int n1 = mart1.Length;
            int n2 = matr2.Length;

            if (n1  == 0 || n2 == 0)
                return null;

            int m1 = mart1[0].Length;
            int m2 = matr2[0].Length;

            if (m1 != n2)
                return null;

            int[][] res = new int[n1][];
            for (int i = 0; i < n1; i++)
                res[i] = new int[m2];

            for (int i = 0; i < n1; i++)
                for (int j = 0; j < m2; j++)
                    for (int k = 0; k < m1; k++)
                        res[i][j] += mart1[i][k] * matr2[k][j];

            return res;
        }