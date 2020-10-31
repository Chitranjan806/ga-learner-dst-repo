# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)


#Code starts here
# STEP 1
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var.shape)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var.shape)

print("*"*60)

# STEP 2
banks = bank.drop(['Loan_ID'], axis=1)

print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)

print(banks.shape)
print(banks.isnull().sum())
print("*"*60)

# STEP 3
avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc='mean')
print(avg_loan_amount['LoanAmount'])
print("*"*60)

# STEP 4
loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].shape[0]
print("loan_approved_se: "+str(loan_approved_se))
loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].shape[0]
print("loan_approved_nse: "+str(loan_approved_nse))

Loan_Status_Count = banks['Loan_Status'].value_counts().sum()

percentage_se = round((loan_approved_se/Loan_Status_Count)*100, 2)
print(percentage_se)

percentage_nse = round((loan_approved_nse/Loan_Status_Count)*100, 2)
print(percentage_nse)
print("*"*60)

# STEP 5
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x/12))

big_loan_term=len(loan_term[loan_term>=25])

print(big_loan_term)
print("*"*60)

# STEP 6
loan_groupby = banks.groupby(['Loan_Status'])

loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.agg([np.mean], 2)

print(mean_values)



