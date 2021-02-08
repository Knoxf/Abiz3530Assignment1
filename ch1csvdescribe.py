"""

Description: - This script will describe a CSV file from MGEX.

Requirements:
- Python 3
- Pandas library
- Numppy library

"""

import pandas as pd
import numpy as np

df = pd.read_csv("http://customer1.barchart.com/cgi-bin/mri/mgexdata.csv?sym=MWU19&ivol=Y&cc=MW&mon=U&year=19&data=d.csv")
df = df.replace(0, np.NaN)  # treating all zero values as missing values
print(df['Last'].describe())
input()

