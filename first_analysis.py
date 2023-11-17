import pandas as pd
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv('data/ckd.csv')

# create the first exploratory plot
plt.figure()
plt.scatter(df['Age'], df['Blood Pressure'])
plt.show() 