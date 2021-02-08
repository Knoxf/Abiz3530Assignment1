"""

Description: - This script will retrieve and display a CSV file from MGEX.

Requirements:
- Python 3
- Pandas library

"""

import pandas as pd

df = pd.read_csv("http://customer1.barchart.com/cgi-bin/mri/mgexdata.csv?sym=MWU19&ivol=Y&cc=MW&mon=U&year=19&data=d.csv")
print(df)
input()
