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
