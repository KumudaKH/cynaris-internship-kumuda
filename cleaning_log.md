# Week 2 Day 4: Data Cleaning Log

## Dataset Information
- Dataset: Software Professional Salaries 2022
- Source: Kaggle
- Tools: Python, Pandas, NumPy

## Data Quality Summary

| Metric | Before Cleaning | After Cleaning |
|---|---:|---:|
| Rows | 22770 | 22774 |
| Columns | 8 | 6 |
| Missing Values | 1 | 0 |
| Duplicate Rows | 0 | 0 |

## Cleaning Techniques
1. Identified missing values using isnull().sum().
2. Removed duplicate rows using drop_duplicates().
3. Applied median imputation to suitable numerical columns.
4. Applied mode imputation to suitable categorical columns.
5. Detected potential outliers using the IQR method.
6. Capped only reviewed numerical columns where appropriate.
7. Removed leading and trailing whitespace from text columns.

## Limitations
- Imputation may affect data distributions.
- Extreme salary values may be genuine observations.
- Outlier capping decisions should be justified by the data.
- Further validation may be required before predictive modelling.

## Conclusion
The dataset was examined and cleaned using appropriate data-cleaning
techniques. Before-and-after data quality metrics were calculated
to document the changes.
