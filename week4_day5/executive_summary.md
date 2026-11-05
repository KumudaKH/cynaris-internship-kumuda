# Executive Summary

## Software Professional Salary Analysis

**Project:** Data Analysis Capstone – Week 4, Day 5
**Role:** Data Analyst Intern
**Dataset:** Software Professional Salaries (Kaggle)
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy, Scikit-learn, Power BI

---

## 1. Business Problem

Understanding salary patterns across companies, job roles, locations and employment categories is important for both job seekers and recruitment organizations.

This project analyzes software professional salary data to identify compensation trends, compare employment categories, understand salary differences and generate actionable business recommendations.

The primary business question is:

**What factors influence software professionals' salaries, and how do salaries vary across job roles, locations, companies and employment categories?**

## 2. Dataset Overview

The analysis uses a public Kaggle dataset containing 22,770 records and 8 columns.

The dataset includes:

* Company Name
* Company Rating
* Job Title
* Salary
* Salaries Reported
* Location
* Employment Status
* Job Roles

### Data Cleaning

* Identified one missing value in the Company Name column.
* Replaced the missing company name with "Unknown".
* Checked for duplicate records; no duplicates were found.
* Examined numerical data types and salary distributions.
* Identified 1,156 salary outliers (5.08%) using the IQR method.
* Retained outliers for analysis because extreme salary values may represent genuine compensation observations.

## 3. Key Findings

### Salary Distribution

* Average salary: ₹6,95,387.
* Median salary: ₹5,00,000.
* Minimum salary: ₹2,112.
* Maximum salary: ₹9,00,00,000.
* Salary distribution is positively skewed.

### Job Role Analysis

Database-related roles recorded the highest average salary among the ten highest-paying job-role categories, followed by Mobile and SDE roles.

### Location Analysis

* Mumbai recorded the highest average salary at approximately ₹9.61 lakh.
* Bangalore followed at approximately ₹7.35 lakh.
* Kolkata, Pune and Hyderabad also appeared among the higher-paying locations.

### Company Analysis

Among companies with at least 30 salary records:

* Microsoft recorded a median salary of ₹12 lakh.
* Flipkart recorded a median salary of ₹12 lakh.
* Cisco Systems recorded a median salary of ₹11 lakh.
* Oracle recorded a median salary of ₹9 lakh.

### Employment Status Analysis

| Employment Status | Average Salary |
| ----------------- | -------------: |
| Full Time         |     ₹7.33 lakh |
| Contractor        |     ₹6.27 lakh |
| Intern            |     ₹3.57 lakh |
| Trainee           |     ₹3.24 lakh |

Full-time employees represent approximately 88% of the dataset.

## 4. Statistical Analysis

### Correlation Analysis

Pearson correlation between company rating and salary was approximately 0.025, indicating a very weak positive relationship.

The correlation between salary and the number of salary reports was also negligible.

### Hypothesis Testing

A Kruskal-Wallis test was performed to compare salary distributions among Full Time, Contractor and Intern employees.

Results:

* Test statistic: 1310.07
* P-value: 3.33 × 10⁻²⁸⁵
* Significance level: 0.05

Since the p-value is below 0.05, the null hypothesis was rejected.

**Conclusion:** There is statistically significant evidence of differences in salary distributions among the three employment categories.

## 5. Regression Model Comparison

Two regression models were developed and evaluated using an 80:20 train-test split.

| Evaluation Metric | Ridge Regression | Random Forest |
| ----------------- | ---------------: | ------------: |
| MAE               |        ₹3,47,489 |     ₹3,66,359 |
| RMSE              |        ₹5,49,287 |     ₹5,85,468 |
| R² Score          |           0.2559 |        0.1547 |

Ridge Regression performed better than Random Forest across all three evaluation metrics.

However, both models demonstrated limited predictive performance, indicating that the available dataset features do not sufficiently explain salary variations.

Additional variables such as work experience, educational qualifications and technical skills could potentially improve prediction accuracy.

## 6. Actionable Business Recommendations

### Recommendation 1: Develop Location-Based Compensation Strategies

Organizations should regularly compare compensation across different cities to establish competitive salary structures and attract skilled professionals.

### Recommendation 2: Encourage Specialized Technical Skill Development

Job seekers and educational institutions should investigate specialized technical roles such as Database Engineering, Mobile Development and Software Development Engineering to identify promising career opportunities.

### Recommendation 3: Improve Salary Benchmarking and Prediction

Recruitment teams should use median salary benchmarks rather than relying exclusively on average salaries. Collecting additional information about experience, education and technical skills could also improve salary estimation.

## 7. Dashboard Development

A Power BI dashboard was developed to present the analysis through three sections:

1. **Salary Overview:** Overall salary statistics, KPI cards and employment comparisons.
2. **Job & Location Analysis:** Salary comparisons across job roles and locations.
3. **Company Analysis:** Company salary rankings, company comparisons and employment analysis.

Interactive filters allow users to explore the dataset by job role, location, company and employment status.

## 8. Conclusion

This project demonstrates an end-to-end data analysis workflow, starting from raw dataset inspection and cleaning through exploratory data analysis, statistical testing and regression modelling.

The findings reveal meaningful salary differences across employment categories, job roles, locations and companies.

The analysis also highlights the importance of outlier investigation, median-based comparisons and statistical validation when developing business recommendations.

Overall, this project demonstrates how data analytics can transform raw salary information into meaningful insights that support compensation planning, recruitment decisions and career development.

---

**Project Status:** Data Analysis and Dashboard Development
**Final Deliverables:** Jupyter Notebook, Power BI Dashboard, Executive Summary and GitHub Repository.
