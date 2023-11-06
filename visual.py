import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

top_15_country=df.sort_values(by='Deaths',ascending=False).head(15)
plt.figure(figsize=(6,6))
plt.pie(top_15_country['Deaths'],labels=top_15_country['Country/Region'],autopct='%1.1f%%')
plt.title("top 15 active cases")
plt.show()


plt.figure(figsize=(12,6))
for state in top_15_country['Country/Region']:
    data=df[df['Country/Region']==state]
    plt.plot(data['Deaths'],data['Deaths'],label=state)
    plt.xlabel('Country/Region')
    plt.ylabel('Deaths')
    plt.legend()
    plt.show()


top_15_country=df.sort_values(by='Deaths',ascending=False).head(15)
plt.figure(figsize=(10,6))
sns.violinplot(x=top_15_country['Deaths'],palette='Set2')
plt.show


plt.figure(figsize=(12, 6))
plt.bar(top_15_country['Country/Region'], top_15_country['Deaths'])
plt.xlabel('State')
plt.ylabel('Death Cases')
plt.title('Top 10 Death Cases by State')
plt.xticks(rotation=45)
plt.show()


top_5_affected = df.sort_values(by='Confirmed', ascending=False).head(5)
print(top_5_affected[['Country/Region', 'Confirmed']])

correlation_matrix = df.corr()
print(correlation_matrix)

fatality_ratio = (df['Deaths'].sum() / df['Confirmed'].sum()) * 100
print(fatality_ratio, '%')

plt.figure(figsize=(10,6),dpi=100)
data=df.sort_values(by='Confirmed',ascending=True).head(10)
data.boxplot()
plt.title("outlier")
plt.ylabel("deaths")
plt.xticks([1], ['Confirmed'])
plt.show()
