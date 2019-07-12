import pandas as pd
import numpy as np

ser = pd.Series(np.random.random(8))

# Cambio porcentual
ser.pct_change()
# 0         NaN
# 1   -0.345789
# 2    0.637453
# 3    0.492323
# 4    0.005850
# 5   -0.154860
# 6   -0.040910
# 7   -0.504911
# dtype: float64

# Cambio porcentual en dataframe
df = pd.DataFrame(np.random.randn(10, 4), columns=list('abcd'))
df.pct_change()
#           a          b          c         d
# 0       NaN        NaN        NaN       NaN
# 1 -0.710466  -4.834160  -0.916337 -1.609003
# 2 -1.734407  -0.683812 -22.352205 -1.522788
# 3  6.769367  -0.144734  -1.499859 -2.577870
# 4 -0.652108  -0.927917  -0.071551 -2.025651
# 5  0.873166  50.142358  -1.914286 -0.592367
# 6 -0.048065  -1.191069   0.906343  3.472670
# 7 -1.647889  -1.297322   0.957855 -1.372812
# 8 -0.190365   4.175188  -0.716981 -2.926031
# 9 -3.112031  -1.905184   0.536850 -1.082202

# Que es la varianza
s = pd.Series(np.repeat(65, repeats=1000))
s.var()
# 0.0

# En una distribucion normal
s2 = pd.Series(np.random.randn(1000))
s2.var()
# 1.0441843569089062

# Covarianza
s3 = pd.Series(np.random.randn(1000))
s3.cov(s2)
# 0.004279714683136323

s4 = pd.Series(np.repeat(65, repeats=1000))
s5 = pd.Series(np.repeat(65, repeats=1000))
s4.cov(s5)
# 0.0

# Pearsons correlation
df['a'].corr(df['b'])
# -0.3499692166273486

# Spearman Correlation
df['a'].corr(df['b'], method='spearman')

s = pd.Series(np.random.randint(low=1, high=20, size=5))
s.rank(method='max')
df = pd.DataFrame({'s': s, 's_rank': s.rank()})
df.sort_values(by='s')
#     s  s_rank
# 0   7     1.0
# 3   8     2.0
# 2  12     3.0
# 1  14     4.0
# 4  16     5.0
