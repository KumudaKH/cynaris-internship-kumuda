# PandasAI vs Manual Pandas Comparison

## Objective
To evaluate the accuracy of PandasAI by comparing its natural-language query results with equivalent calculations performed using traditional Pandas operations.

## Dataset
- Dataset: Salary_Dataset_with_Extra_Features.csv
- Total records: 22,770
- Total columns: 8

## Comparison Results

Three questions were selected for comparison:

1. Average salary
2. Number of unique companies
3. Top 5 most common job titles

All three PandasAI results matched the corresponding Manual Pandas results.

## Findings

- PandasAI successfully interpreted all three natural-language questions.
- Manual Pandas produced the same numerical results.
- Both approaches identified the same five most common job titles and their frequencies.
- Manual Pandas execution was very fast, with each calculation taking less than 0.01 seconds in this test.

## Conclusion

PandasAI demonstrated accurate results for the three tested questions. Manual Pandas remains useful for precise, reproducible calculations, while PandasAI makes data analysis more accessible through natural-language interaction.

Further validation is required for complex queries and unusual salary values before using AI-generated results in production.

## Salary Outlier Validation

A salary validation analysis was performed to identify unusually high salary values in the dataset.

### Findings
- Total salary records: 22,770
- Average salary: ₹695,387
- Median salary: ₹500,000
- Maximum salary: ₹90,000,000
- Records above ₹1,000,000: 4,242
- Records above ₹5,000,000: 43

### Observations

Thapar University had the highest individual salary value of ₹90,000,000. Several other companies also had unusually high salary values.

These observations indicate potential outliers or data-entry inconsistencies.

### Conclusion

AI-generated analysis must be validated against the original dataset. PandasAI can produce accurate calculations while still reporting unusual values present in the underlying data. Therefore, data-quality checks are necessary before interpreting results or making business decisions.