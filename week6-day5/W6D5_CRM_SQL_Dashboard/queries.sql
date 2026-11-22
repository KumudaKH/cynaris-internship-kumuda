-- Total customers
SELECT COUNT(*) AS total_customers FROM customers;

-- Opportunities by stage
SELECT stage, COUNT(*) AS deal_count FROM opportunities GROUP BY stage ORDER BY stage;

-- Won revenue
SELECT SUM(amount) AS won_revenue FROM opportunities WHERE stage = 'Won';

-- Top won revenue region
SELECT c.region, SUM(o.amount) AS revenue FROM opportunities o JOIN customers c ON c.customer_id=o.customer_id WHERE o.stage='Won' GROUP BY c.region ORDER BY revenue DESC LIMIT 1;

-- Average deal value by stage
SELECT stage, ROUND(AVG(amount),2) AS avg_amount FROM opportunities GROUP BY stage ORDER BY stage;

-- Total opportunities
SELECT COUNT(*) AS total_opportunities FROM opportunities;

-- Won deals
SELECT COUNT(*) AS won_deals FROM opportunities WHERE stage = 'Won';

-- Customers by region
SELECT region, COUNT(*) AS customer_count FROM customers GROUP BY region ORDER BY region;

-- Top 5 opportunities
SELECT opportunity_id, amount FROM opportunities ORDER BY amount DESC, opportunity_id LIMIT 5;

-- Won revenue by industry
SELECT c.industry, SUM(o.amount) AS revenue FROM opportunities o JOIN customers c ON c.customer_id=o.customer_id WHERE o.stage='Won' GROUP BY c.industry ORDER BY c.industry;
