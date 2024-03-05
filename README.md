# Data Engineer Interview

👋 Welcome to the GfK Data Engineer Technical Test - **SQL Focus**

## Objective
This readme contains instructions to run a specific postgres db using docker. The db will be populated with some fake sales data. You will be required to write SQL queries to answer some questions about the data. Your answers should be as performant as possible and you should be prepared to discuss your choices during the feedback session.

*Note: You can see the Schema definition of the sales db in schema.sql*

## How to get started

### Prerequisites
- Docker (installation instructions [here](https://docs.docker.com/get-docker/)
- A SQL client (e.g. [psql](https://www.timescale.com/blog/how-to-install-psql-on-mac-ubuntu-debian-windows/), [DBeaver](https://dbeaver.io/), [pgAdmin](https://www.pgadmin.org/), etc.)


### Start postgres
This creates a `sales` database
```bash
docker-compose up -d
```
*Note: if you have something running locally on port 5432 which will conflict with the postgres docker container then you can change the local port mapping in `docker-compose.yml` like so:*
```yaml
    ports:
      - "6543:5432"
``` 

### Connect to the database
These commands use psql cli but you can connect to the database using the environment variables provided and use any SQL client you prefer.
#### Mac / Linux
```bash
PGHOST=localhost PGPORT=5432 PGDATABASE=sales PGUSER=postgres PGPASSWORD=mysecretpassword psql
```

#### Windows
```bash
set PGHOST=localhost
set PGPORT=5432
set PGDATABASE=sales
set PGUSER=postgres
set PGPASSWORD=mysecretpassword
psql
```

## Tasks to be completed
- **TIMEBOX: 2 hours** - Please do not spend more than 2 hours on this task.
- **Dificulty** - The tasks increase in difficulty from 1 to 10.
- **Format** - Create a SQL file for each of the tasks. Write SQL that answers the question and publish to a public git repository.

1) **Total Sales by Product**
Write a SQL query to calculate the total sales amount for each product, sorted by the total sales amount in descending order.

2) **Average Sales Price by Product**
Write a SQL query to calculate the average selling price of each product, along with the product name. Sort the results by the average selling price in descending order. Consider how to efficiently handle any variations in price.

3) **Sales Growth by Quarter**
Write a SQL query to calculate the percentage growth in sales (in terms of quantity sold) from one quarter to the next for each product. Include product name in the results and sort by the highest growth to identify the fastest growing products.

4) **Customer Reach by Retailer**
Write a SQL query to count the number of unique products sold by each retailer, indicating the diversity of their offerings. Sort the results by the count of unique products in descending order.

5) **Most Profitable Retailer Location**
Write a SQL query to determine the most profitable location for each retailer, based on the total sales amount. Group the results by retailer and location, and sort by the total sales amount in descending order.

6) **Monthly Sales Comparison to Previous Year**
Write a SQL query that compares the total sales amount for each month to the same month in the previous year. The result should include the month, year, total sales for the current month, total sales for the same month previous year, and the growth or decline percentage.

7) **Utilization of Window Functions for Ranking Products**
Leverage window functions to rank products within each category by total sales quantity. Include product name, category, and rank in the output, sorted by category and then by rank.

8) **Yearly Sales Trend for Top 5 Products**
Identify the top 5 products by total sales amount across all time, then write a SQL query to show the yearly sales trend for these top products. Include product name, year, and total sales amount in the output, sorted by product and year.

9) **Efficient Retrieval of Top 10% Selling Days**
Write a SQL query to identify the top 10% of days with the highest total sales volume. Consider an efficient way to perform this percentile calculation and sort the results by date.

10) **Creation and Use of a Materialized View**
Create a materialized view that summarizes total sales by retailer and month. Then, write a query using this view to find the retailer with the highest sales for each month, including the retailer name, month, and total sales amount.