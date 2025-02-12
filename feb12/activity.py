import pandas as pd;
import seaborn as sns;
import matplotlib.pyplot as plt;
df = pd.read_csv('Sample_Data_for_Activity.csv')
df.head()
df.info()
plot1 = sns.displot(df['Normal_Distribution'], kde = True)
plot1.savefig("/my files/Data analytics/practice1/feb12/plot1.png")
plot2 = sns.displot(df['Normal_Distribution'], kde = True, bins = 50)
plot2.savefig("/my files/Data analytics/practice1/feb12/plot2.png")
plot3 = sns.jointplot(x='Normal_Distribution', y='Uniform_Distribution', data=df, kind='scatter')
plot3.savefig("/my files/Data analytics/practice1/feb12/plot3.png")
plot4 = sns.pairplot(df)
plot4.savefig("/my files/Data analytics/practice1/feb12/plot4.png")