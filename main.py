#upload librairie 
import pandas as pd
import numpy as ny
import re

#upload file
data = 'personnes.csv'

#read file
data_display = pd.read_csv(data)

#display file
print(data_display)
