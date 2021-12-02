# Add Trino Connection
trino://admin@trino-service:8080/

# Create Hive Tables
```sql
CREATE TABLE hive.default.customers (
  customerId varchar,
  gender varchar,
  seniorCitizen varchar,
  partner varchar,
  dependents varchar,
  tenure varchar
)
WITH (format = 'CSV',
  skip_header_line_count = 1,
  EXTERNAL_LOCATION='s3a://rawdata/customers'
)


CREATE TABLE hive.default.products
    (

         customerID VARCHAR,
         PhoneService VARCHAR,
         MultipleLines VARCHAR,
         InternetService VARCHAR,
         OnlineSecurity VARCHAR,
         OnlineBackup VARCHAR,
         DeviceProtection VARCHAR,
         TechSupport VARCHAR,
         StreamingTV VARCHAR,
         StreamingMovies VARCHAR,
         Contract VARCHAR,
         PaperlessBilling VARCHAR,
         PaymentMethod VARCHAR,
         MonthlyCharges VARCHAR,
         TotalCharges VARCHAR,
         Churn VARCHAR
    )
WITH (format = 'CSV',
  skip_header_line_count = 1,
  EXTERNAL_LOCATION='s3a://rawdata/products'
)
```


## Query for Hive Table
```sql
SELECT products.*, customers.*  
from hive.default.products products,
 	hive.default.customers customers
where cast(products.customerId as VARCHAR) = customers.customerId
```
