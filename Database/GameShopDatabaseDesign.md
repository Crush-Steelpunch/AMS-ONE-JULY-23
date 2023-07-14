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






product_id 	product_name 	              developer_id 	developer           price
1 	        Sitar Hero 	                  103 	        StockRAR 	        5.99
2 	        Paint Drying Simulator 	      101 	        Gr9 Games 	        3.95
3 	        Extreme ChessBoxing 2021      102 	        MashButton Ltd 	    1.19
4           Grow My Flowers EXTREME 2023  101           Gr9 Games           4.02
5           Windwaching                   101           Gr9 Games Ltd       2.27

### ERD

![GameDB ERD Diagram](gamedb-erd.png)