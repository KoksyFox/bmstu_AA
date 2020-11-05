for (int i = 0; i < n1; i++)
{
	for (int j = 0; j < m2; j++)
	{
		int buff = -(mulH[i] + mulV[j]);
		for (int k = 0; k < (m1 - m1Mod2); k += 2)
		{
			buff += (mtrx1[i][k + 1] + mtrx2[k][j])*\
			(mtrx1[i][k] + mtrx2[k + 1][j]);
		}
		result[i][j] = buff;
	}
}