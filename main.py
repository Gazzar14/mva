from mva.inference import one_sample_chi2test
from mva.inference import hotteling1sample_test
import pandas as pd

hbat = pd.read_excel(r"C:\Users\k_abo\Desktop\Multivariate\15- HBAT Data.xlsx")


# H:0 mu = [3,7] for x9 and x6
print(hotteling1sample_test(hbat.loc[:,['x9', 'x6']], [3,7]))

print(one_sample_chi2test(hbat.loc[:,['x9', 'x6']], [3,7]))