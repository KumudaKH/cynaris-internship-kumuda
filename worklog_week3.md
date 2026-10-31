# Week 3 — Day 1: Power BI Fundamentals

**Date:** 26 October 2026
**Day:** Monday
**Topic:** Power BI Fundamentals and Executive Dashboard Design

## 1. What I Worked On Today

Worked on Power BI fundamentals with a focus on designing professional, executive-ready dashboards for business intelligence and data analysis. Reviewed dashboard layout principles, KPI visualizations, data storytelling, interactive filters, and effective visual selection.

Studied how to organize business metrics into a clear narrative, highlight important performance indicators, compare sales across regions and products, and present actionable insights to support executive decision-making.

Also reviewed Power BI report publishing, view-only sharing, and Git/GitHub version-control requirements for submitting internship deliverables.

## 2. Topics Covered

* Power BI Desktop fundamentals
* KPI cards and business performance metrics
* Dashboard layout and visual hierarchy
* Data visualization and storytelling
* Power Query and data transformation concepts
* DAX measures and calculations
* Interactive slicers, bookmarks, and drill-through
* Executive dashboard design principles
* Performance optimization
* Row-Level Security (RLS) and data governance
* Power BI Service publishing and sharing
* Git branching, commits, pushing, and Pull Requests

## 3. Tools and Technologies Used

* Microsoft Power BI Desktop
* Power Query
* DAX
* Power BI Service
* Git
* GitHub
* Google Drive

## 4. CIA Insights: Designing Executive-Ready Power BI Dashboards

Reviewed CIA insights on best practices for designing executive dashboards that communicate business performance clearly and support faster decision-making.

### Key Findings

**1. Start with a Clear Business Story**

Define the business question before designing the dashboard. Organize KPIs and charts in a logical sequence so executives can quickly understand performance and identify areas requiring attention.

**2. Keep the Dashboard Simple**

Use a focused, single-page layout with approximately 8–10 or fewer visuals. Avoid unnecessary charts and excessive filters to maintain readability.

**3. Prioritize Important KPIs**

Place headline metrics such as revenue, profit margin, active stores, and sales targets prominently. Use cards and KPI visuals to make business performance easy to understand at a glance.

**4. Select Appropriate Visualizations**

* Bar and column charts for comparisons.
* Line charts for monthly and yearly trends.
* Doughnut charts for a small number of categories.
* Maps for geographical sales analysis.
* Tables for detailed product and regional comparisons.

**5. Maintain Consistent Colors and Formatting**

Use a consistent corporate color palette, clear titles, readable fonts, and appropriate units. Use red to highlight negative performance and green for positive performance where appropriate.

**6. Design for Different Screen Sizes**

Use a widescreen 16:9 layout and consider Power BI's mobile layout for executives accessing reports on phones and tablets.

**7. Add Useful Interactivity**

Use high-level slicers, bookmarks, tooltips, and drill-through pages to let users explore important business questions without overcrowding the main dashboard.

**8. Optimize Report Performance**

Reduce unnecessary data, optimize data models, and use appropriate storage modes. Test report performance to ensure that executives can access important metrics without unnecessary delays.

**9. Apply Data Security and Governance**

Use Row-Level Security (RLS) where required so users can access only the data they are authorized to view. Maintain consistent, trusted data definitions.

**10. Present Actionable Insights**

Include brief interpretations and recommended next steps. The dashboard should help decision-makers understand what happened, why it matters, and what action they should consider.

## 5. Executive Dashboard Layout

Reviewed a retail sales dashboard layout with the following components:

* **Header:** Dashboard title, company branding, and last-refreshed timestamp.
* **Top section:** KPI cards for revenue, profit margin, and active stores.
* **Middle section:** Monthly revenue-versus-target trend and Top 5 stores by sales.
* **Bottom section:** Geographical sales analysis and navigation to a detailed margin-analysis page.

The layout emphasizes a clear visual hierarchy, consistent formatting, and quick access to business-critical information.

## 6. Mini-Implementation Checklist

* [ ] Define 3–5 core business KPIs.
* [ ] Create a focused dashboard in Power BI Desktop.
* [ ] Apply a consistent corporate color theme.
* [ ] Configure RLS roles if required.
* [ ] Configure scheduled refresh if supported and needed.
* [ ] Publish the report to an appropriate workspace if access permits.
* [ ] Configure view-only sharing permissions.
* [ ] Test report performance.
* [ ] Collect feedback and improve the dashboard.
* [ ] Save the Power BI project and dashboard screenshot.

## 7. Challenges / Blockers

The main challenge is completing the Power BI Service publishing and view-only sharing workflow. Access, permissions, or licensing restrictions may affect the ability to publish and share a live report.

Further work is required to complete and validate the dashboard, verify the DAX measures, and ensure that all required deliverables are committed to GitHub.

## 8. Deliverables

**Google Drive Deliverable:**
https://drive.google.com/file/d/1vu02PCGy6A0MRHWNDJOldtz94m3zYR1j/view?usp=sharing

**Project deliverables:**

* Power BI dashboard project (.pbix)
* Dashboard screenshot
* Git commit and push
* GitHub Pull Request containing the deliverable reference
* Published Power BI report link, if successfully published and sharing is available


Learned how executive dashboard design combines KPI prioritization, appropriate chart selection, consistent formatting, interactivity, performance optimization, and data governance.

These practices help transform raw business data into clear, actionable insights that support faster and more informed decisions.

____________________________________________________________________________________________________________
# Week 3 — Day 2
# CIA Activity: Difference Between a DAX Measure and a Calculated Column

## Objective

To understand the differences between DAX measures and calculated columns in Power BI, including their calculation methods, storage requirements, and applications in business reporting.

## 1. Calculated Column

A calculated column creates a value for each row in a table using a DAX expression. The results are calculated during data refresh and stored in the data model.

**Example:**

```dax
LineTotal = Sales[Qty] * Sales[UnitPrice]
```

**Explanation:**
This formula calculates the total amount for each sales transaction by multiplying the quantity by the unit price. The result can be used in table visuals, filters, and other calculations.

**Applications:**

* Calculating profit for individual transactions.
* Creating product categories or customer classifications.
* Generating row-level flags for business analysis.

## 2. DAX Measure

A measure performs calculations dynamically when a visual or query requests a result. Its output depends on the current filter context, including slicers, report filters, and visual selections.

**Example:**

```dax
Total Sales = SUM(Sales[LineTotal])
```

**Explanation:**
This measure calculates total sales by adding the values in the LineTotal column. The result automatically changes when users filter the report by store, product, or date.

**Applications:**

* Calculating total sales and profit.
* Monitoring key performance indicators (KPIs).
* Comparing monthly and yearly business performance.
* Creating interactive dashboards.

## 3. Key Differences

| Aspect       | Calculated Column                          | Measure                                                  |
| ------------ | ------------------------------------------ | -------------------------------------------------------- |
| Calculation  | Evaluated for each row                     | Evaluated when a result is requested                     |
| Storage      | Results are stored in the model            | Stores the expression rather than a result for every row |
| Context      | Primarily uses row context                 | Primarily uses filter context                            |
| Common usage | Row-level calculations and classifications | Aggregations and dynamic business metrics                |
| Example      | Line Total                                 | Total Sales                                              |

## 4. Business Application

Retail companies can use calculated columns to determine the value of individual transactions and measures to analyse overall sales performance.

For example, a retail company can calculate the total amount of each transaction using a calculated column and then create a measure to display total revenue by store, product category, or month.

This helps managers identify high-performing products, compare store performance, and make informed business decisions.

## 5. Key Insights Learned

* Calculated columns are suitable for row-level calculations and values that need to be stored in the data model.
* Measures are useful for dynamic calculations that respond to filters and slicers.
* Measures generally avoid the storage required for a separate calculated value in every row, although their performance depends on the calculation and data model.
* Choosing the correct approach helps improve the efficiency and flexibility of Power BI reports.

## Conclusion

This CIA activity helped me understand when to use DAX measures and calculated columns in Power BI. I learned that calculated columns are appropriate for row-level calculations, whereas measures are better suited for dynamic aggregations and business performance analysis. These concepts are essential for developing interactive dashboards and effective business intelligence solutions.

____________________________________________________________________________________________________________

# Week 3 – Day 3: Excel for Analysis

## 1. Objective

The objective of this session was to understand and apply Excel's advanced data analysis features, focusing on Power Query, PivotTables, PivotCharts, KPI calculations, and dashboard development.

## 2. Key Learnings

I explored several Excel features commonly used by professional data analysts:

* **Excel Tables:** Learned how structured tables automatically expand when new records are added and support easier formula management.
* **Dynamic Array Functions:** Reviewed functions such as FILTER, SORT, UNIQUE, XLOOKUP, and SEQUENCE for retrieving, sorting, and manipulating data efficiently.
* **Conditional Formatting:** Understood how to highlight important values, identify negative margins, and flag KPIs that fall outside defined thresholds.
* **Data Validation:** Learned how dropdown lists and validation rules help maintain consistent and accurate data entry.
* **PivotTables and PivotCharts:** Practised summarising sales data by region, product, and quarter to identify business performance patterns.
* **Slicers and Timelines:** Explored how interactive filters can make dashboards easier to navigate.
* **Power Query:** Learned how to import, combine, clean, and transform multiple CSV files through a repeatable data preparation workflow.
* **Power Pivot and DAX:** Reviewed how related datasets and DAX measures can support more advanced calculations and reporting.
* **What-If Analysis and Solver:** Studied how Goal Seek, Scenario Manager, Data Tables, and Solver can support forecasting and business optimisation.
* **Data Analysis ToolPak:** Explored its applications in statistical analysis, regression, and histogram generation.
* **Advanced Visualisation:** Reviewed combo charts, waterfall charts, funnel charts, map charts, and sparklines for presenting analytical insights.
* **Automation and Integration:** Learned about VBA macros, external data connections, and Power BI integration for improving reporting efficiency.

## 3. Practical Work Completed

During this session, I worked on a sales analysis workbook using Q1 and Q2 sales datasets.

The practical activities included:

1. Importing sales records from multiple CSV files.
2. Using Power Query to prepare and combine quarterly datasets.
3. Creating calculated columns for Margin and Margin Percentage.
4. Developing a PivotTable to summarise revenue and margin by region, product, and quarter.
5. Creating a KPI dashboard displaying total revenue, total cost of goods sold (COGS), total margin, overall margin percentage, units sold, and total sales records.
6. Building a regional revenue and margin summary.
7. Calculating quarterly revenue and growth percentage.
8. Creating charts to visualise regional and quarterly sales performance.
9. Formatting financial values using Indian Rupee currency formatting.

## 4. Business Applications

These techniques can be applied to retail sales reporting, financial analysis, inventory management, regional performance monitoring, and automated business reporting.

For example, a retail analyst can combine sales files from different quarters, compare revenue across regions, calculate profitability, and present the results through a dashboard for management review.

## 5. Additional Insights

I learned that Excel remains a useful tool for data analysts because it supports rapid exploration, reporting, and business communication. Power Query reduces repetitive data preparation, while PivotTables and charts simplify summarisation and visual analysis.

For larger datasets and more complex analytical requirements, Excel can be complemented by Python, SQL, and Power BI.

## 6. Conclusion

This session strengthened my understanding of Excel-based data analysis and reporting. By working with quarterly sales data, I gained practical experience in data preparation, profitability calculations, PivotTable analysis, KPI reporting, and dashboard visualisation.

These skills provide a foundation for developing more efficient, accurate, and business-oriented analytical reports.

____________________________________________________________________________________________________________

# WEEK 3 – DAY 4

## Looker Studio – Interactive Dashboard Development
**Technology:** Google Looker Studio, Google Sheets, CSV
**Task:** Build an interactive dashboard and understand client-presentation best practices.

### 1. Objective

The objective of this task was to develop an interactive and visually appealing dashboard using Google Looker Studio, connected to structured datasets.

The dashboard aims to transform historical Indian stock market data into meaningful visual insights that help stakeholders understand market performance, stock trends, sector performance, and financial risks.

### 2. Activities Performed

**Task 1: Dashboard Development**

Developed a five-page Indian Stock Market Analytics Dashboard covering:

1. Market Overview
2. Stock Performance Analysis
3. Risk & Drawdown Analysis
4. Trading Patterns & Sector Analysis
5. Market Trends & Insights

**Task 2: Data Visualization**

Implemented different visualization techniques:

* Scorecards for important market KPIs.
* Line charts for historical market trends.
* Bar charts for stock and sector comparisons.
* Pie charts for proportional analysis.
* Tables for detailed stock market information.

**Task 3: Interactive Dashboard Features**

Worked with interactive dashboard components, including:

* Stock selection filters.
* Macro_Cycle filter.
* Date selection controls.
* Interactive charts and tables.

**Task 4: Sector Analysis Improvements**

Enhanced the Trading Patterns & Sector Analysis page by working on:

* Sector-wise company distribution.
* Sector performance comparison.
* Number of companies by sector.
* Market cycle-based sector analysis.

### 3. CIA Learning – Client-Presentation Best Practices

Explored the CIA resource titled:

**Looker Studio Dashboard – Client-Presentation Playbook**

The following best practices were identified:

**A. Understand the Audience**

* Identify the intended dashboard users.
* Understand the business decisions the dashboard should support.
* Select KPIs according to stakeholder requirements.

**B. KPI Selection**

* Focus on 3–5 important KPIs.
* Avoid unnecessary metrics.
* Ensure every KPI provides meaningful business information.

**C. Dashboard Layout**

* Place the dashboard title and date selector at the top.
* Display important scorecards prominently.
* Use the central area for important trend visualizations.
* Position supporting charts and filters logically.

**D. Chart Selection**

* Line charts for time-series analysis.
* Pie charts for proportional distribution.
* Bar charts for comparisons and rankings.
* Tables for detailed information.
* Scorecards for important numerical indicators.

**E. Branding and Formatting**

* Maintain consistent colours throughout the dashboard.
* Use readable fonts and appropriate text sizes.
* Maintain sufficient contrast.
* Avoid overcrowding the dashboard.

**F. Interactivity**

* Include date range controls.
* Use dropdown filters where appropriate.
* Provide useful tooltips.
* Enable appropriate sharing permissions.

**G. Data Storytelling**
Organise the dashboard presentation into five stages:

1. Context
2. Current State
3. Trend
4. Root Cause
5. Actionable Insights

### 4. Application to My Project

Applied the client-presentation principles to the Indian Stock Market Analytics Dashboard.

Key applications include:

* Organising the dashboard into five analytical pages.
* Using KPI scorecards to summarise market information.
* Using line charts to explain historical market trends.
* Using bar charts to compare stock and sector performance.
* Using a pie chart to represent sector distribution.
* Adding explanatory insights to communicate analytical findings.
* Improving the visual hierarchy and consistency of dashboard components.

### 5. Key Learning Outcomes

Through this task, I gained practical knowledge of:

1. Developing interactive dashboards using Google Looker Studio.
2. Connecting structured datasets to reporting tools.
3. Selecting appropriate charts for different analytical requirements.
4. Designing KPI scorecards.
5. Creating interactive filters and date controls.
6. Applying dashboard design and branding principles.
7. Communicating business insights through data visualization.
8. Preparing dashboards for professional client presentations.

### 6. Challenges and Improvements

Identified the following areas for further improvement:

* Improving chart readability and label formatting.
* Ensuring date filters work correctly.
* Avoiding unnecessary data aggregation.
* Improving sector-level comparisons.
* Verifying data freshness and refresh settings.
* Optimising dashboard loading performance.
* Checking public sharing permissions.

### 7. Conclusion

Successfully developed a five-page Indian Stock Market Analytics Dashboard using Google Looker Studio and explored professional dashboard design practices through the CIA Client-Presentation Playbook.

This task improved my understanding of business intelligence, interactive reporting, data visualization, and stakeholder-oriented dashboard development.

**Overall Outcome:** Gained practical experience in transforming historical financial datasets into structured, interactive, and presentation-ready analytical dashboards.

____________________________________________________________________________________________________________

# # WEEK 3 – DAY 4
## KPI Design

### KPI vs. Metric vs. Measure – Understanding the Differences

As part of today's learning, I explored the differences between measures, metrics, and Key Performance Indicators (KPIs), and how they are connected when analysing business performance.

**1. Measure**

A measure is a basic numerical value collected directly from a data source. It represents raw information that can be used for further analysis.

Example: `sales_qty` – the number of products sold in a transaction.

**2. Metric**

A metric is a calculated value obtained by combining or analysing one or more measures. It helps understand business performance through totals, averages, percentages, and ratios.

Example: Total Sales = SUM(Quantity × Unit Price).

**3. KPI (Key Performance Indicator)**

A KPI is an important metric linked to a specific business goal. It helps organisations evaluate whether they are achieving their objectives. KPIs are generally monitored against predefined targets.

Example: Year-over-Year Sales Growth with a target of achieving more than 15% growth.

### How They Are Connected

The relationship can be understood through the following hierarchy:

* **Measure:** Provides the raw numerical data.
* **Metric:** Converts raw data into meaningful calculations.
* **KPI:** Uses important metrics to evaluate progress towards business goals.

Measures usually represent detailed information, metrics provide analytical insights, and KPIs focus on overall business performance.

### Practical Example – Indian Retail Industry

Consider a retail business that wants to monitor its sales performance.

| Level   | Example                                                    |
| ------- | ---------------------------------------------------------- |
| Measure | Quantity of products sold (`order_qty`)                    |
| Metric  | Daily sales revenue calculated using quantity and price    |
| KPI     | Average Order Value (AOV) with a target of ₹2,500 or above |

For example, SQL can be used to calculate daily sales using SUM(), while average order value can be calculated using AVG().

### Key Learnings

* Understood the difference between measures, metrics, and KPIs.
* Learned how raw data is transformed into meaningful business insights.
* Understood the importance of setting targets and benchmarks for KPIs.
* Learned how to select relevant KPIs based on business objectives.
* Understood how KPIs help management monitor performance and make better decisions.

### Conclusion

This learning helped me understand that not every metric is a KPI. A KPI is a carefully selected metric that measures progress towards an important business objective. Understanding these differences is essential for designing effective dashboards and presenting meaningful insights to decision-makers.

