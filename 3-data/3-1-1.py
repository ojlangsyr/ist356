import pandas as pd
import numpy as np
df=pd.DataFrame({
    's1': [1, 2,3,4],
    's2': [2.2, np.nan,3.0,1.5],
    's3': ['q','q','z','z']})

df.index = ['a', 'b', 'c', 'd']
print(df)