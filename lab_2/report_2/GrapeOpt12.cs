int m1Mod2 = m1 % 2;
int n2Mod2 = n2 % 2;

for (int i = 0; i < n1; i++)
{
	for (int j = 0; j < (m1 - m1Mod2); j += 2)
	{
		mulH[i] += mtrx1[i][j] * mtrx1[i][j + 1];
	}
}

for (int i = 0; i < m2; i++)
{
	for (int j = 0; j < (n2 - n2Mod2); j += 2)
	{
		mulV[i] += mtrx2[j][i] * mtrx2[j + 1][i];
	}
}