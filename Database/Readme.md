# Database and SQL

   00101101011001 

- Binary number representing 2905
- Decimal Number   101,101,011,001 
- Integer Number   AS above
- Phone Number   001 0110 1011001
- Date?


## Database Data Types

- Numerical
  - Integer Numbers
  - Floating Point Number
  - Boolean
- Text
  - String (varchar)
- Date / Time

## SELECT STATEMENT

SELECT select_expr FROM table_reference 
SELECT ITEM_ID,ITEM_NAME FROM foods;

SELECT title,description FROM film;

### Filtering

`SELECT select_expr FROM table_references WHERE where_condition`

`SELECT release_year FROM film WHERE length="100"`

`SELECT title, description FROM film WHERE length="100";`

`help Functions; help Comparison Operators; `

### Sorting

`SELECT select_expr FROM table_references WHERE where_condition ORDER BY col_name`
`SELECT title, description, length FROM film WHERE length BETWEEN "97" AND "100" ORDER BY length DESC;`


### Data Definition Language

`CREATE DATABASE db_name`

`CREATE TABLE tbl_name (create_definition)`

```
create_definition = col_name column_definition

column_definition = data_type  constraints
```

### Simple table

`CREATE TABLE people ( first_name VARCHAR(50), last_name VARCHAR(50), age INT, Date_of_birth  DATE )`

### Table with Constraints


`CREATE TABLE people ( ID  INT PRIMARY KEY AUTO_INCREMENT , first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50), age INT, Date_of_birth  DATE, living BOOL DEFAULT True );`


### ERD

![GameDB ERD Diagram](gamedb-erd.png)