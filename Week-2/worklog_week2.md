# WEEK -2 /DAY-1

## 1. Objective

Understand how to select appropriate data visualisation techniques based on the relationship, distribution, comparison, or trend that needs to be communicated.

## 2. Choosing the Right Chart Type

| No. | Data Relationship                              | Best-fit Chart Type(s)                                                | Why It Works                                                                   | Typical Use Case                                                               |
| --- | ---------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| 1   | **One-dimensional distribution**               | Histogram, Box plot, Density plot                                     | Shows frequency, shape, outliers, and skewness.                                | Distribution of daily footfall in a Bangalore mall.                            |
| 2   | **Categorical comparison**                     | Bar chart (vertical or horizontal), Column chart, Grouped/stacked bar | Easy to read absolute or relative sizes.                                       | Sales of each product category (Apparel, Electronics, Home) across 5 stores.   |
| 3   | **Part-to-whole**                              | Pie chart (only 3–5 slices), Donut chart, Stacked bar/area, Treemap   | Visualises proportion; treemap handles many slices.                            | Market share of FMCG brands in Delhi.                                          |
| 4   | **Trend over time**                            | Line chart, Area chart, Combo line-column                             | Emphasises direction and slope; multiple lines for series.                     | Monthly revenue of a fintech startup for the last 12 months.                   |
| 5   | **Two-dimensional relationship / correlation** | Scatter plot, Bubble chart, Heatmap                                   | Shows patterns, clustering, and outliers; bubble charts add a third dimension. | Price vs. discount % for items on Flipkart; bubble size represents units sold. |
| 6   | **Ranked order**                               | Sorted bar chart, Pareto chart                                        | Highlights top contributors; Pareto follows the 80/20 rule.                    | Top 10 best-selling SKUs in a grocery chain.                                   |
| 7   | **Distribution comparison**                    | Side-by-side box plots, Violin plot, Grouped histogram                | Displays median, spread, and shape for each group.                             | Delivery time distribution for three courier partners.                         |
| 8   | **Hierarchical / drill-down**                  | Treemap, Sunburst chart, Indented bar                                 | Represents parent-child relationships and portions within portions.            | Revenue by region → state → city for an Indian telecom.                        |
| 9   | **Geographic / spatial**                       | Choropleth map, Symbol map, Heat-map overlay                          | Uses map context to show regional patterns.                                    | Online order volume per PIN code in Maharashtra.                               |
| 10  | **Multi-category over time**                   | Stacked column/area chart, Streamgraph                                | Shows how each component contributes to the total over time.                   | Quarterly revenue split by product line for an Indian SaaS company.            |
| 11  | **KPI gauge / performance vs target**          | Bullet chart, Gauge/dial                                              | Communicates progress against a benchmark.                                     | Monthly sales target vs. actual for a sales representative.                    |
| 12  | **Distribution of a categorical variable**     | Bar chart (count), Pareto chart                                       | Shows the frequency of categories.                                             | Number of tickets per issue type in a help desk.                               |
| 13  | **Ratio / relationship of two parts**          | 100% stacked bar, Diverging stacked bar                               | Shows the proportion of each part relative to the whole.                       | Male vs. female enrollment percentages in engineering colleges.                |

---

## 3. Python Implementation: Pandas, Matplotlib and Seaborn

The following examples demonstrate how to create different visualisations using Python.

### 3.1 Histogram

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['footfall'], bins=30, kde=True)
plt.show()
```

### 3.2 Bar Chart — Categorical Comparison

```python
df.groupby('category')['sales'].sum().plot(kind='bar')
plt.show()
```

### 3.3 Pie Chart / Donut Chart

```python
df['brand'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)
plt.show()
```

### 3.4 Line Chart — Trend

```python
df.set_index('date')['revenue'].plot()
plt.show()
```

### 3.5 Scatter Plot — Correlation

```python
sns.scatterplot(
    x='price',
    y='discount',
    size='units_sold',
    data=df
)
plt.show()
```

### 3.6 Box Plot — Distribution Comparison

```python
sns.boxplot(
    x='courier',
    y='delivery_days',
    data=df
)
plt.show()
```

### 3.7 Heatmap — Correlation Matrix

```python
sns.heatmap(
    df.corr(),
    annot=True,
    cmap='RdYlGn'
)
plt.show()
```

### 3.8 Choropleth Map — Geographic Visualisation

```python
import geopandas as gpd

map_df = gpd.read_file('india_states.shp')

merged = map_df.merge(
    df_state,
    left_on='state_name',
    right_on='state'
)

merged.plot(
    column='order_volume',
    cmap='Blues',
    legend=True
)
plt.show()
```

---

## 4. Best Practices for an Intern-Level Dashboard

1. **Start simple:** A clean bar or line chart is often more actionable than a fancy 3-D plot.
2. **Limit colours:** Use 2–3 brand-consistent hues; reserve bright colours for highlights, such as a target line.
3. **Add context:** Include axis titles, data source, and a short caption, such as *“Q3 2026 sales – 12% YoY growth.”*
4. **Responsive layout:** If using Plotly or Streamlit, set `fig.update_layout(autosize=True)` so the chart fits on mobile screens, which is important for field-sales dashboards in India.

---

## 5. Key Takeaway

**Pick the chart that makes the relationship instantly obvious; the rest is polishing.**

Selecting the right chart helps analysts communicate trends, comparisons, distributions, correlations, proportions, and geographic patterns effectively.

### Work Log Summary

| Field                   | Details                                                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------------------- |
| **Topic**               | Choosing the Right Chart for the Relationship You Want to Show                                        |
| **Focus Area**          | Data Visualisation                                                                                    |
| **Tools Covered**       | Pandas, Matplotlib, Seaborn, GeoPandas, Plotly and Streamlit                                          |
| **Concepts Covered**    | Chart selection, data relationships, distributions, trends, comparisons, and dashboard best practices |
| **Practical Component** | Python examples for eight types of visualisations                                                     |
| **Key Learning**        | Select the chart type that communicates the intended relationship clearly and effectively.            |

____________________________________________________________________________________________________________

## DAY - 2
# `pd.merge()` vs `pd.concat()`

| Feature              | **`pd.merge()`**                                                                                                                                    | **`pd.concat()`**                                                                                                                                            |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Purpose**          | Performs SQL-style joins to combine rows horizontally based on one or more key columns.                                                             | Combines DataFrames vertically (adds rows) or horizontally (adds columns) without matching records using keys.                                               |
| **Typical use case** | Adds related information to a dataset, such as attaching product details to individual sales records.                                               | Appends data from different periods, combines wide-format tables, or joins pre-aligned datasets, such as combining daily logs into monthly logs.             |
| **Key arguments**    | `how='inner'`, `how='left'`, and other join types.                                                                                                  | `axis=0` for vertical concatenation and `axis=1` for horizontal concatenation.                                                                               |
| **Result shape**     | Generally contains columns from both DataFrames, with duplicate join-key columns handled according to the merge configuration.                      | The number of rows or columns depends on the concatenation axis and the alignment rules applied to the input DataFrames.                                     |
| **Performance tip**  | For larger datasets, appropriate indexing and efficient key selection can improve performance. Sorting keys alone does not guarantee faster merges. | Efficiently combines multiple DataFrames. For many small pieces, use `pd.concat(list_of_dfs, ignore_index=True)` instead of repeatedly appending DataFrames. |

---

## Practical Data-Pipeline Example: Retail Sales in the Indian Context

### Goal

1. Load three monthly sales files for January, February, and March.
2. Combine them into a single sales table.
3. Enrich the consolidated sales data with product catalogue information, including price and category.
4. Generate a final report showing total sales for each product category in every state.

### 1. Load and Concatenate the Monthly Files

```python
import pandas as pd
import glob

# Assume files are stored as: sales_2026_01.csv, sales_2026_02.csv, sales_2026_03.csv
file_paths = glob.glob('data/sales_2026_*.csv')

monthly_dfs = [pd.read_csv(fp) for fp in file_paths]

# Add a month column while reading (optional)
for df, fp in zip(monthly_dfs, file_paths):
    df['month'] = pd.to_datetime(fp.split('_')[-1].split('.')[0], format='%m').month

# Stack the three months vertically → one big sales DataFrame
sales_all = pd.concat(monthly_dfs, axis=0, ignore_index=True)
print(sales_all.shape)      # e.g. (90 000, 7)
```

**Why use `concat()`?**

* All the monthly files contain the same columns, so their records can be combined directly without matching keys.
* `concat()` stacks the rows efficiently, with approximately O(N) work for straightforward concatenation.

### 2. Load the Product Catalogue (Master Data)

```python
products = pd.read_csv('data/product_master.csv')
# product_master columns: product_id, product_name, category, cost_price, selling_price
```

The product catalogue acts as a master reference table containing product identifiers, names, categories, cost prices, and selling prices.

### 3. Merge the Sales Data with Product Information

```python
# Join on the key `product_id`
sales_enriched = pd.merge(
    left   = sales_all,
    right  = products,
    how    = 'left',          # keep every sales row even if a product is missing
    on     = 'product_id',
    suffixes= ('_sale', '_prod')
)

# Quick sanity check
print(sales_enriched[['product_id', 'product_name', 'category', 'selling_price']].head())
```

**Why use `merge()`?**

* The objective is to enrich each sales transaction with its corresponding product information.
* A left join preserves every sales record, even when a matching product entry is unavailable.
* This operation is equivalent to the following SQL query:

```sql
SELECT *
FROM sales
LEFT JOIN products
ON sales.product_id = products.product_id;
```

### 4. Aggregate the Data to Generate the Final Report

```python
# Add a computed column: revenue = qty * selling_price
sales_enriched['revenue'] = sales_enriched['qty'] * sales_enriched['selling_price']

# Group by state and product category
report = (sales_enriched
          .groupby(['state', 'category'], as_index=False)
          .agg(total_qty=('qty', 'sum'),
               total_rev=('revenue', 'sum')))

# Sort for presentation
report = report.sort_values(['state', 'total_rev'], ascending=[True, False])
print(report.head(10))
```

**Result:** The final output is a structured report that finance or marketing teams can use to evaluate regional sales performance. For example, it could indicate that Karnataka's **Electronics** category generated ₹2.3 crore in Q1.

---

## Quick Decision Guide

| Requirement                                                                                | Recommended Function                                  |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| Combine multiple files with the same schema, such as daily logs into monthly data.         | `pd.concat(list_of_frames, axis=0)`                   |
| Add information from a lookup table, such as a product or customer master.                 | `pd.merge(df_left, df_lookup, how='left', on='key')`  |
| Combine wide-format tables that share the same index but contain different metric columns. | `pd.concat([df_q1, df_q2], axis=1)`                   |
| Perform a many-to-many join between orders and order items.                                | `pd.merge(orders, items, how='inner', on='order_id')` |
| Combine preprocessed data chunks generated independently or in parallel.                   | `pd.concat(chunks, ignore_index=True)`                |

---

## Tips for a Data Analyst Intern

1. **Inspect the output after every operation:** Check `.shape` and `.head()` after performing a merge or concatenation to verify the resulting data.

2. **Handle duplicate column names carefully:** Use `suffixes` or rename columns before merging to prevent ambiguity.

3. **Choose appropriate data types:** Using the `category` data type for columns with a small number of unique string values can reduce memory consumption, especially when working with large datasets.

4. **Investigate duplicate join keys:** When merging on non-unique keys, check whether the resulting Cartesian multiplication of matching rows is expected. Duplicate keys can cause the number of output rows to increase substantially.

5. **Use `ignore_index=True` when appropriate:** When concatenating rows, this option creates a new sequential index instead of retaining the original row indexes.

By understanding these two functions, you can manage most common data-ingestion and data-enrichment operations in retail analytics pipelines. These skills are particularly useful for a **Data Analyst Intern working with an e-commerce company in Bangalore**.

____________________________________________________________________________________________________________

# DAY - 3

# 📋 Standard EDA Checklist for Professional Data Analysts

> A reusable checklist that you can copy into a Jupyter Notebook, Google Colab, or VS Code project and use for every new data analysis task.

| Phase                                             | Checklist Item                                                                                                                                                                                                                                                                                                                                                                                 | Why It Matters                                                                                                           | Typical Pandas / Plotting Code                                                                                                                                                                 |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1️⃣ Understand the Problem**                    | • Examine the business brief and KPI definitions.<br>• Identify the required tables and data sources.                                                                                                                                                                                                                                                                                          | Defines the scope of the analysis and determines which variables are necessary.                                          | `# No code – just read the spec`                                                                                                                                                               |
| **2️⃣ Load and Catalogue Data**                   | • Import all required files from CSV, Excel, databases, or APIs.<br>• Verify row and column counts and inferred data types.                                                                                                                                                                                                                                                                    | Ensures that the analysis uses the exact data supplied by the stakeholder.                                               | `python`<br>`import pandas as pd`<br>`df = pd.read_csv('sales.csv')`<br>`print(df.shape)`<br>`print(df.head())`                                                                                |
| **3️⃣ Data Dictionary and Metadata**              | • Create a table mapping each column to its description, data type, expected range, and business meaning.                                                                                                                                                                                                                                                                                      | Helps every team member, including yourself in the future, interpret the dataset correctly.                              | `metadata = pd.DataFrame({'col':df.columns, 'type':df.dtypes})`                                                                                                                                |
| **4️⃣ Initial Data Profiling**                    | • Use `df.info()` to inspect data types and non-null counts.<br>• Run `df.describe(include='all')`.<br>• Check missing values with `df.isnull().sum()` and their percentages.<br>• Use `df.nunique()` to examine cardinality.                                                                                                                                                                  | Helps identify data-quality issues early, including incorrect data types, excessive missing values, and low variability. | `python`<br>`df.info()`<br>`print(df.describe(include='all'))`<br>`print(df.isnull().mean().sort_values(ascending=False))`                                                                     |
| **5️⃣ Clean and Preprocess**                      | • Convert columns to appropriate data types using `astype` and `pd.to_datetime`.<br>• Handle missing values by dropping, imputing, or flagging them.<br>• Remove duplicates using `drop_duplicates`.<br>• Trim whitespace and correct inconsistent categories, such as “Bengaluru” and “B’lore”.<br>• Detect outliers using IQR or Z-scores and decide whether to retain, cap, or remove them. | Produces an analysis-ready DataFrame and helps prevent poor-quality input from affecting the results.                    | `python`<br>`# Example: date parsing & category cleaning`<br>`df['order_dt'] = pd.to_datetime(df['order_dt'], errors='coerce')`<br>`df['city'] = df['city'].str.strip().str.title()`           |
| **6️⃣ Feature Engineering (Optional but Common)** | • Derive time-based features such as year, month, weekday, and quarter.<br>• Calculate ratios or per-unit metrics, such as `sales_per_qty`.<br>• Encode categorical variables using `pd.get_dummies` or ordinal mapping.                                                                                                                                                                       | Creates more informative variables for subsequent modelling and deeper analysis.                                         | `python`<br>`df['order_month'] = df['order_dt'].dt.month`                                                                                                                                      |
| **7️⃣ Univariate Exploration**                    | • Use histograms or KDE plots for numerical columns.<br>• Create bar plots for categorical frequencies.<br>• Use box plots to examine distributions and outliers.                                                                                                                                                                                                                              | Helps reveal the distribution of individual variables, including skewness, multiple peaks, and gaps.                     | `python`<br>`import matplotlib.pyplot as plt`<br>`import seaborn as sns`<br>`sns.histplot(df['sales'], kde=True)`<br>`sns.countplot(y='city', data=df, order=df['city'].value_counts().index)` |
| **8️⃣ Bivariate and Multivariate Analysis**       | • Calculate correlation matrices using `df.corr()` and visualise them with heatmaps.<br>• Create scatter plots or line plots for numerical variables.<br>• Use box plots or violin plots to compare numerical and categorical variables.<br>• Generate pivot tables and group-by aggregations for business KPIs.                                                                               | Helps uncover relationships, potential drivers, and patterns that may warrant further investigation into causality.      | `python`<br>`sns.heatmap(df.corr(), annot=True, cmap='coolwarm')`<br>`sns.boxplot(x='category', y='sales', data=df)`                                                                           |
| **9️⃣ Segmentation Checks**                       | • Group data by important dimensions such as store, city, product line, and month.<br>• Compare KPIs across segments, such as average basket size.                                                                                                                                                                                                                                             | Aligns the analysis with business reporting structures and hierarchies.                                                  | `python`<br>`df.groupby(['city','month'])['sales'].sum().reset_index()`                                                                                                                        |
| **🔟 Data-Quality Audit**                         | • Recheck missing values after cleaning.<br>• Validate totals against source reports, such as monthly revenue.<br>• Record assumptions and manual corrections.                                                                                                                                                                                                                                 | Improves stakeholder confidence and creates an auditable record of the analysis.                                         | `assert df['sales'].sum() == reported_total`                                                                                                                                                   |
| **1️⃣1️⃣ Summary and Storytelling**               | • Prepare a one-page “EDA Insights” slide covering key statistics, major patterns, data-quality observations, and recommended next steps.<br>• Include at least one visual for every major finding.                                                                                                                                                                                            | Converts raw exploration into actionable business intelligence.                                                          | Use PowerPoint, Google Slides, or a Markdown notebook export.                                                                                                                                  |
| **1️⃣2️⃣ Save Analysis Artifacts**                | • Export the cleaned DataFrame using `df.to_parquet('cleaned_sales.parquet')`.<br>• Save visualisations using `fig.savefig('sales_by_city.png')`.<br>• Track the notebook using Git.                                                                                                                                                                                                           | Supports reproducibility and makes it easier to hand over work or use the results in downstream modelling.               | `python`<br>`df.to_parquet('data/clean_sales.parquet')`<br>`fig.savefig('outputs/sales_hist.png')`                                                                                             |

---

## Quick-Start Template

Copy and adapt the following template for a new EDA project.

```python
# -------------------------------------------------
# 1️⃣ Load
# -------------------------------------------------
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')

# -------------------------------------------------
# 2️⃣ Profile
# -------------------------------------------------
print(df.shape)
df.info()
print(df.isnull().mean().sort_values(ascending=False))

# -------------------------------------------------
# 3️⃣ Clean
# -------------------------------------------------
df['order_dt'] = pd.to_datetime(df['order_dt'], errors='coerce')
df['city'] = df['city'].str.title().str.strip()
df.drop_duplicates(inplace=True)

# -------------------------------------------------
# 4️⃣ Feature engineering
# -------------------------------------------------
df['order_month'] = df['order_dt'].dt.month

# -------------------------------------------------
# 5️⃣ Univariate
# -------------------------------------------------
sns.histplot(df['sales'], kde=True)
plt.title('Sales distribution')
plt.show()

# -------------------------------------------------
# 6️⃣ Bivariate
# -------------------------------------------------
sns.boxplot(x='city', y='sales', data=df)
plt.xticks(rotation=45)
plt.show()

# -------------------------------------------------
# 7️⃣ Group-by KPI
# -------------------------------------------------
monthly_sales = (
    df.groupby('order_month')['sales']
    .sum()
    .reset_index()
)
print(monthly_sales)

# -------------------------------------------------
# 8️⃣ Save
# -------------------------------------------------
df.to_parquet('clean_sales.parquet')
```

---

## Tips for Indian-Centric Projects

* **Fiscal calendar:** Many Indian companies follow a financial year from April to March. Create an `fy` column using the following code:

  ```python
  df['fy'] = df['order_dt'].dt.year + (df['order_dt'].dt.month >= 4)
  ```

* **Currency formatting:** Format sales values in Indian rupees for reporting:

  ```python
  df['sales'].apply(lambda x: f'₹{x:,.2f}')
  ```

* **Regional encoding:** If your dataset contains state-level information, map state names to ISO-2 codes to simplify geographical visualisation, for example, using `plotly.express.choropleth`.

Follow the checklist, mark each completed item, and maintain a **reproducible, stakeholder-ready EDA workflow** for every project. 🚀

____________________________________________________________________________________________________________

## CIA Research Activity: Handling Missing Values in Time-Series Data

**Query:** What is the best strategy for handling missing values in a time-series dataset?

### Key Learnings

1. Identify the percentage and pattern of missing values before selecting an imputation method.
2. Forward-fill carries the last known value forward and can be useful when observations change gradually.
3. Backward-fill uses the next known value, but may introduce future information into past observations.
4. Linear interpolation estimates missing values between known observations.
5. Seasonal and model-based methods may be appropriate when data has strong seasonal patterns or long missing intervals.
6. Add missing-value indicators when the absence of data may itself provide useful information.
7. Validate imputation methods using visualisation, statistical comparisons, and back-testing.

### Conclusion

The best imputation method depends on the dataset, missing-data pattern, time interval, and business requirements. Time-series data should retain its temporal order, and future information must not leak into past observations during forecasting.

### Application to Data Cleaning

For my Software Professional Salaries 2022 dataset, I used appropriate missing-value handling techniques based on column types. The time-series methods researched here would be more suitable for datasets containing time-ordered observations.
