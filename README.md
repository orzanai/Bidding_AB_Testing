
# Comparison of Bidding Methods with AB Testing

Facebook recently introduced a new bidding type called "average bidding" as an alternative to the existing "maximum bidding" bidding type.
One of our clients, -.com, decided to test this new feature and wants to conduct an A/B test to determine if average bidding brings more conversions than maximum bidding. The A/B test has been running for 1 month, and now -.com is expecting you to analyze the results of this A/B test.
The ultimate success metric for -.com is Purchase. Therefore, Purchase metric should be the focus for statistical tests.


## Dataset
This dataset contains information about a company's website, including the number of ads viewed and clicked by users, as well as revenue generated from these ads.
There are two separate data sets, one for the control group and one for the test group. 
These data sets are located on separate sheets of the ab_testing.xlsx Excel file. Maximum Bidding was applied to the control group, while Average Bidding was applied to the test group.


## Methods

- Shapiro-Wilk test for normality assumption
- Levene test for homogeneity of variances assumption
- Parametric test
- Wilson Lower Bound Scoring



## Results

According to the test study, although there was a difference of 32 units between the average sales of the test and control groups, this difference was found to be not statistically significant. In other words, it can be said that the difference in averages may have occurred due to different factors other than this update by chance. The difference between the two groups may be based on seasonal effects, different updates, and processes. In summary, it is observed that the use of new Average Bidding does not have a clear advantage over Max Bidding in terms of return.
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

This project completed as a part of Miuul Data Science & Machine Learning Bootcamp. Dataset was provided by Miuul and private.

