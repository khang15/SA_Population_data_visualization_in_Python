import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Read data from csv file
df = pd.read_csv("F:\HUST\Python\py-app\py\Projet1\PopulationAgeSex.csv")

# Data processing
df['Location'] = df['Location'].str.strip().astype('category')
df['Sex'] = df['Sex'].str.strip().astype('category')
for col in df.columns:
    if df[col].dtypes == object:
        df[col] = df[col].str.replace(" ", "").astype(float)
df.set_index("Year", inplace=True)
