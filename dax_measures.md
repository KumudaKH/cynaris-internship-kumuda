# Week 3 — Day 2: DAX Basics

## 1. Objective

To understand DAX fundamentals and create calculated columns and measures in Power BI for dynamic business reporting.

## 2. Dataset

A sample retail sales dataset containing the following columns:

* OrderDate
* Product
* Category
* Sales
* Cost

## 3. DAX Expressions

### Expression 1: Total Sales

```dax
Total Sales = SUM(Sales[Sales])
```

**Type:** Measure

**Explanation:** Calculates the sum of sales values. The result changes according to the filters applied in the report.

**Business application:** Used to monitor total revenue and evaluate business performance.

### Expression 2: Electronics Sales Using CALCULATE()

```dax
Electronics Sales =
CALCULATE(
    [Total Sales],
    Sales[Category] = "Electronics"
)
```

**Type:** Measure

**Explanation:** CALCULATE evaluates the Total Sales measure after applying the Electronics category filter.

**Business application:** Helps compare sales performance across product categories.

### Expression 3: Year-to-Date Sales

```dax
YTD Sales =
CALCULATE(
    [Total Sales],
    DATESYTD(DateTable[Date])
)
```

**Type:** Measure

**Explanation:** Calculates cumulative sales from the beginning of the year through the last date in the current date context.

**Prerequisite:** Create and mark a Date table, then establish a relationship between DateTable[Date] and Sales[OrderDate].

**Business application:** Helps management monitor year-to-date revenue and compare performance across periods.

### Expression 4: Running Total Using EARLIER()

```dax
Running Total Column =
CALCULATE(
    SUM(Sales[Sales]),
    FILTER(
        Sales,
        Sales[OrderDate] <= EARLIER(Sales[OrderDate])
    )
)
```

**Type:** Calculated column

**Explanation:** Uses EARLIER to reference the outer row's order date while FILTER evaluates rows with dates up to that date.

**Business application:** Demonstrates cumulative sales calculations in a row-based context.

**Limitation:** Rows with the same date can receive the same cumulative total. A unique ordering key is needed for a strict row-by-row running total.

### Expression 5: Profit Margin Percentage

First create the Profit calculated column:

```dax
Profit =
Sales[Sales] - Sales[Cost]
```

Then create the Profit Margin column:

```dax
Profit Margin % =
DIVIDE(
    Sales[Profit],
    Sales[Sales],
    0
) * 100
```

**Type:** Calculated column

**Explanation:** Calculates profit as sales minus cost, then calculates profit margin as a percentage of sales.

**Business application:** Helps businesses measure profitability and compare products.

**Formatting:** Use a decimal number format because the expression multiplies the ratio by 100.

## 4. Measure vs. Calculated Column

| Feature     | Measure                                           | Calculated Column                     |
| ----------- | ------------------------------------------------- | ------------------------------------- |
| Evaluation  | At query time, according to filter context        | During data refresh                   |
| Storage     | Stores the definition, not a result for every row | Stores calculated values for each row |
| Context     | Primarily filter context                          | Row context                           |
| Typical use | KPIs and aggregated calculations                  | Row-level categories and calculations |
| Example     | Total Sales                                       | Profit                                |

## 5. Row Context and Filter Context

**Row context:** Evaluates an expression for the current row, such as calculating profit for an individual transaction.

**Filter context:** Determines which data is included in a calculation, such as sales for Electronics in a selected year.

**Context transition:** CALCULATE can convert row context into filter context.

## 6. Conclusion

This exercise introduced DAX measures, calculated columns, CALCULATE, DATESYTD, EARLIER, profit margin calculations, and context transition. These concepts support the creation of interactive Power BI dashboards for business reporting and decision-making.
