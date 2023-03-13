#####################################################
# Comparison of Bidding Methods with AB Testing
#####################################################

#####################################################
# Business Problem
#####################################################

# Facebook recently introduced a new bidding type called "average bidding" as an alternative to the existing "maximum bidding" bidding type.
# One of our clients, -.com, decided to test this new feature and wants to conduct an A/B test to determine if average bidding brings more conversions than maximum bidding. The A/B test has been running for 1 month, and now -.com is expecting you to analyze the results of this A/B test.
# The ultimate success metric for -.com is Purchase. Therefore, Purchase metric should be the focus for statistical tests.

#####################################################
# Story of dataset
#####################################################

# This dataset contains information about a company's website, including the number of ads viewed and clicked by users, as well as revenue generated from these ads.
# There are two separate data sets, one for the control group and one for the test group. These data sets are located on separate sheets of the ab_testing.xlsx Excel file. Maximum Bidding was applied to the control group, while Average Bidding was applied to the test group.

# impression: The number of ad impressions
# Click: The number of clicks on the displayed ad
# Purchase: The number of products purchased after clicking on the ads
# Earning: The profit obtained after purchasing the products


#####################################################
# Data Preprocessing and Analysis
#####################################################

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
pd.set_option("display.width", 500)



df_cont = pd.read_excel("Week 4/measurement_problems/Case Studies/ABTesti/ab_testing.xlsx", "Control Group")
df_test = pd.read_excel("Week 4/measurement_problems/Case Studies/ABTesti/ab_testing.xlsx", "Test Group")


def check_df(dataframe):

    print(dataframe.shape)
    print("#######################################")
    print(dataframe.dtypes)
    print("#######################################")
    print(dataframe.head())
    print("#######################################")
    print(dataframe.tail())
    print("#######################################")
    print(f"Null Entries {dataframe.isnull().sum()}")
    print("#######################################")
    print(dataframe.describe().T)

check_df(df_cont)
check_df(df_test)

df_conc = pd.concat([df_cont, df_test], axis=0, ignore_index=True)

#####################################################
# Define Hypothesis for AB Testing
#####################################################

# H0: M1 = M2 (There is no statistically significant difference between Average Bidding and Maximum Bidding.)
# H1: M1 != M2 (There is a statistically difference.)

print(f"Control Group Mean: {df_cont['Purchase'].mean()} \nTest Group Mean: {df_test['Purchase'].mean()}")


######################################################
# AB Testing (Two-Sample T Test)
######################################################

# Normality test:
# H0: Normal distribution.     P-value < 0.05 Rejects H0.
# H1: Nonnormal distribution.  P-value > 0.05 Rejects H1.

def normal_check(group_name, test=False):
    if test:
       shap_stat, pvalue = shapiro(df_test[group_name])
       print("p_value %.4f" % (pvalue))
    else:
       shap_stat, pvalue = shapiro(df_cont[group_name])
       print("p_value %.4f" % (pvalue))

normal_check("Purchase")
normal_check("Purchase", test=True)

# Homogeneity of variance test:
# H0: The variances are homogeneous.   P-value < 0.05 Reject H0.
# H1: Not homogeneous.                 P-value > 0.05 Reject H1.

def var_check(group_name_1, group_name_2):
    var_stat, pvalue = levene(df_test[group_name_1],
                              df_cont[group_name_2])
    print("p_value %.4f" % (pvalue))

var_check("Purchase", "Purchase")

# Both of the hypothesis for variances and normality are provided. Because of that, we use parametric test.

non_stats, pvalue = ttest_ind(df_cont["Purchase"], df_test["Purchase"], equal_var=True)
print("p_value %.4f" % (pvalue))



