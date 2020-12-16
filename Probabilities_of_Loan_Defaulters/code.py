# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
# TASK - 1
p_a = len(df[df['fico'].astype(float)>700])/len(df)
print("p_a : ", p_a)

p_b = len(df[df['purpose']=='debt_consolidation'])/len(df)
print("p_b : ",p_b)

df1 = df[df['purpose'] == 'debt_consolidation']

p_a_b = len(df1[df1['fico'].astype(float)>700])/len(df1)
print("p_a_b : ", p_a_b)

result = p_a_b == p_a
print("Result : ",result)


# TASK - 2
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df)
print(prob_lp)

prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df)
print(prob_cs)

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)
print(prob_pd_cs)

bayes = round((prob_pd_cs * prob_lp) / prob_cs, 4)
print(bayes)

# TASK - 3
df['purpose'].value_counts().plot(kind='bar')
plt.title("Distribution Graph of 'Purpose'")
plt.show()

df1 = df[df['paid.back.loan'] == 'No']
print(df1.shape)

df1['purpose'].value_counts().plot(kind='bar')
plt.title("Purpose Distribution for Paid.Back.Loan = No")
plt.show()

# TASK - 4
inst_median = df['installment'].median()
print("inst_median : ", inst_median)

inst_mean = df['installment'].mean()
print("inst_mean : ", inst_mean)

df['installment'].plot(kind='hist')
plt.title("Distribution of Installment")
plt.axvline(x=inst_mean, color='red')
plt.axvline(x=inst_median, color='blue')
plt.show()

df['log.annual.inc'].plot(kind='hist')
plt.title("Distribution of Log Annual Income")
plt.show()



