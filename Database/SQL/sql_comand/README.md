## ๐ SQL์ด๋?

SQL์ Structured Query Language ๋๋ ์์ด๋ก Structured Query Language์ ์ฝ์์๋๋ค. Relational Database์ ์ฟผ๋ฆฌ ์ธ์ด์๋๋ค .

## Contents
- [๐ SQL์ด๋?](#-sql์ด๋)
- [Contents](#contents)
- [SELECT](#select)
  - [DISTINCT](#distinct)
  - [SQL WHERE](#sql-where)
  - [Operators in The WHERE Clause](#operators-in-the-where-clause)
- [AND, OR, NOT](#and-or-not)
- [ORDER BY](#order-by)
- [SELECT TOP](#select-top)

 ## [SELECT](https://www.w3schools.com/sql/sql_select.asp)

SELECT๋ ๋ฐ์ดํฐ๋ฒ ์ด์ค์์ ๋ฐ์ดํฐ๋ฅผ ์ ํํ๋ ๋ฐ ์ฌ์ฉ๋ฉ๋๋ค. ์ ํํ  ์ด์ ์ง์ ํ๊ฑฐ๋ ๋ณํ๋ฅผ ์ฌ์ฉํ์ฌ ์ฟผ๋ฆฌ๋ฅผ ์ํํ  ํ์ด๋ธ์ ๋ชจ๋  ์ด์ ์ ํํ  ์ ์์ต๋๋ค.

~~~~sql
SELECT column1, column2 FROM table_name
~~~~
~~~~sql
SELECT * FROM table_name
~~~~

  ### [DISTINCT](https://www.w3schools.com/sql/sql_distinct.asp)
  
์ ํํ ํ๋์ ์ค๋ณต ๋ฐ์ดํฐ๊ฐ ํฌํจ๋ ๋ ์ฝ๋๋ฅผ ์๋ตํฉ๋๋ค. ์ฟผ๋ฆฌ ๊ฒฐ๊ณผ์ ํฌํจํ๋ ค๋ฉด SELECT ๋ฌธ์ ๋์ด๋ ๊ฐ ํ๋์ ๊ฐ์ ๊ณ ์ ํด์ผ ํฉ๋๋ค.

~~~~sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
~~~~

~~~~sql
SELECT DISTINCT Country FROM Customers;
~~~~

~~~~sql
SELECT COUNT(DISTINCT Country) FROM Customers;
~~~~
  ### [SQL WHERE](https://www.w3schools.com/sql/sql_where.asp)

WHERE๋ ์กฐ๊ฑด์ ๋ฐ๋ผ ํน์  ํํฐ๋ฅผ ์ํํ๋ ๋ฐ ์ฌ์ฉ๋ฉ๋๋ค.

~~~~sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
~~~~
~~~~sql
SELECT * FROM Customers
WHERE Country='Mexico';
~~~~
~~~~sql
SELECT * FROM Customers
WHERE CustomerID=1;
~~~~

WHERE๋ฅผ ์ฌ์ฉํ๋ฉด ๋ผ๋ฆฌ ์ฐ์ฐ์๋ฅผ ์ฌ์ฉํ์ฌ ๋ค๋ฅธ ์ ๋ณด๋ฅผ ๊ฒ์ํ๊ฑฐ๋ ๊ฒ์ ๋ฒ์๋ฅผ ์ ์ํ  ์ ์์ต๋๋ค. ์๋๋ ์ฐ์ฐ์๊ฐ ์๋ ํ์๋๋ค.

### Operators in The WHERE Clause
    
| Operator | Description |
| --- | --- |
| = | Equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |
| <> | Not equal. Note: In some versions of SQL this operator may be written as != |
| BETWEEN | Between a certain range |
| LIKE | Search for a pattern |
| IN | To specify multiple possible values for a column	|
 
์ฐ์ฐ์๋ฅผ ์ฌ์ฉํ ๊ตฌ๋ฌธ

~~~~sql
SELECT CustomerID, CustomerName FROM Customer
WHERE CustomerID > =  15  AND CustomerID <=  50
~~~~ 
 
## [AND, OR, NOT](https://www.w3schools.com/sql/sql_and_or.asp)
  
AND, OR, NOT์ WHERE์ ๊ณผ ๊ฒฐํฉ ๋  ์์์ต๋๋ค.  
AND, OR ์ฐ์ฐ์๋ ํ๊ฐ ์ด์์ ์กฐ๊ฑด์ ํํฐ๋ง ํ๋๋ฐ ์ฌ์ฉ๋ฉ๋๋ค.

AND
~~~~sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
~~~~
OR
~~~~sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
~~~~
NOT
~~~~sql
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
~~~~~
AND Example
~~~~sql
SELECT * FROM Customers
WHERE Country='Germany' AND City='Berlin';
~~~~
OR Example
~~~~sql
SELECT * FROM Customers
WHERE City='Berlin' OR City='Mรผnchen';
~~~~

NOT Example
~~~~sql
SELECT * FROM Customers
WHERE NOT Country='Germany';
~~~~
    
 ## [ORDER BY](https://www.w3schools.com/sql/sql_orderby.asp)
 
ORDER BY ํค์๋๋ ๊ฒฐ๊ณผ๋ฅผ ์ค๋ฆ์ฐจ์ ๋๋ ๋ด๋ฆผ์ฐจ์์ผ๋ก ์ ๋ ฌํ๋ ๋ฐ ์ฌ์ฉ๋ฉ๋๋ค. ๊ธฐ๋ณธ์ ์ผ๋ก ๊ฒฐ๊ณผ๋ ์ค๋ฆ์ฐจ์์ผ๋ก ๋ฐํ๋ฉ๋๋ค. ๋ฐ๋ผ์ ๋ด๋ฆผ์ฐจ์์ผ๋ก ์ ๋ ฌํ๋ ค๋ฉด ์ ๋ ฌํ  ์ด ์ด๋ฆ ๋ค์ DESC ํค์๋๋ฅผ ์ฌ์ฉํด์ผ ํฉ๋๋ค.
 
 ORDER BY Syntax
 
 ~~~~sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
 ~~~~

ORDER BY DESC Example

 ~~~~sql
SELECT * FROM Customers
ORDER BY Country DESC;
 ~~~~

ORDER BY Several Columns Example

 ~~~~sql
SELECT * FROM Customers
ORDER BY Country, CustomerName;
 ~~~~

ORDER BY Several Columns Example 2

 ~~~~sql
SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;
 ~~~~
 
 ## [SELECT TOP](https://www.w3schools.com/sql/sql_top.asp)
