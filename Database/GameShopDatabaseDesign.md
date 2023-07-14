# Game Shop database Design

## Data we want to track in a DB

- Game Name
- Customer
- email
- Customer accounts?
- Stock Level / Inventory
- Sales Transaction
- Genre
- Game Compatibility
- Suppliers
- Ratings / Reviews
- Prices


## Organising data in to tables

- Data Type
- Which data is going into which table
- Primary unique column like an ID.


**Customers**

| Field | Type | Constraints |
|----|-----|---------|
| CUSTOMERID | INT | PRI KEY |
|NAME  | VARCHAR | NOT NULL |
|EMAIL | VARCHAR | NOT NULL |


**Stock**

| Field | Type | Constraints |
|----|-----|---------|
| GAMEID | INT | PRIMARY KEY |
| GAMENAME | VARCHAR | NOT NULL |
| STOCK_LEVEL | INT | NOT NULL |
| SUPPLIER | NAME | |
| PRICE | DECIMAL | |


**Transaction**

| Field | Type | Constraints |
|----|-----|---------|
| ID | INT | PRIMARY KEY |
| GAMEID | INT | FK_STOCK_GAMEID |
| CUSTOMERID | INT | FK_CUSTOMER_CUSTOMERID |
| QUANTITY | INT | DEFAULT=1 |
| SALE | DATETIME |  NOT NULL |