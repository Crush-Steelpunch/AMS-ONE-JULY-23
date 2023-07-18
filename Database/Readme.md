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

```SQL
CREATE TABLE people ( first_name VARCHAR(50), last_name VARCHAR(50), age INT, Date_of_birth  DATE )
```

### Table with Constraints

```SQL
CREATE TABLE people ( 
  ID  INT PRIMARY KEY AUTO_INCREMENT, 
  first_name VARCHAR(50) NOT NULL, 
  last_name INT, 
  age INT, 
  Date_of_birth  DATE, 
  living BOOL DEFAULT True,
  FOREIGN KEY (last_name) REFERENCES family(ID));
```

```SQL
CREATE TABLE family (
    ID INT PRIMARY KEY AUTO_INCREMENT, 
    Family_Name VARCHAR(50) NOT NULL 
    );
-- FOREIGN KEY: This is a fake column to say our tables PEOPLE_ID is linked to another column in another table
```

## INSERTING

`INSERT INTO tbl_name (col_name [, col_name] ...) VALUES ( value [, value] ... )`

`INSERT INTO family (Family_Name) VALUES ('Robinson')`

```SQL
INSERT people (first_name,last_name,age,Date_of_birth) VALUES ('Leon',1,21,'2002-10-21');
INSERT people (first_name,last_name,age,Date_of_birth) VALUES ('Brian',4,50,'1973-10-21');
INSERT people (first_name,last_name,age,Date_of_birth,living) VALUES ('Mr Peas',1,200,'1823-07-17',0);
```


## UPDATING

`UPDATE table_reference SET column1=value1, column2=value2  WHERE where_condition

Start with a SELECT
`SELECT age,Date_of_birth FROM people WHERE first_name="Leon";`

Modity to an UPDATE statement

`UPDATE people SET age=48,Date_of_birth='1976-10-21'  WHERE first_name="Leon";`

## DELETE

`DELETE FROM tbl_name WHERE where_condition`

`DELETE FROM people WHERE first_name="Mr Peas";`


SELECT Name FROM country WHERE Contienent='Asia';


## Nested Queries 

show the country in Asia with the MAX gnp

`SELECT Name, GNP FROM country WHERE GNP=(SELECT MAX(GNP) AS MAX_GNP FROM country WHERE Continent='Asia');`

SELECT ROW_NUMBER() OVER() AS ROWNUM, SUM(SurfaceArea) AS AREA, Continent FROM country GROUP BY Continent

Nested table in FROM 
```SQL
SELECT * FROM (
  SELECT ROW_NUMBER() OVER() AS ROWNUM, SUM(SurfaceArea) AS AREA, Continent FROM country GROUP BY Continent
  ) 
  AS Tab WHERE ROWNUM%2=0;
```

## Joins

SELECT * FROM Table1  JOIN table2 ON table1.PK = table2.FK;





`SELECT city.Name,country.Name FROM city LEFT JOIN country ON city.CountryCode = country.code;`