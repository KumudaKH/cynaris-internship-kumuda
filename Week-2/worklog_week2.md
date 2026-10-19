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
