# ETL_JOBS
learning data preprocessing
---------------------------------------------------------------------------------------------------------------------
Datatype of each column in  the cleaned csv file csv

PassengerId int64
Survived int64
Pclass int64
Name object
Sex object
Age float64
SibSp int64
Parch int64
Ticket object
Fare float64
Cabin object
Embarked object
--------------------------------------------------------------------------------------------------------------------
Datatype of each column in table in with the csv in imported


mydbetl=# \d+ titanic
                                         Table "public.titanic"
   Column    |       Type       | Collation | Nullable | Default | Storage  | Stats target | Description 
-------------+------------------+-----------+----------+---------+----------+--------------+-------------
 passengerid | integer          |           | not null |         | plain    |              | 
 survived    | integer          |           | not null |         | plain    |              | 
 pclass      | integer          |           | not null |         | plain    |              | 
 name        | text             |           | not null |         | extended |              | 
 sex         | text             |           | not null |         | extended |              | 
 age         | double precision |           | not null |         | plain    |              | 
 sibsp       | integer          |           | not null |         | plain    |              | 
 parch       | integer          |           | not null |         | plain    |              | 
 ticket      | text             |           | not null |         | extended |              | 
 fare        | double precision |           | not null |         | plain    |              | 
 cabin       | text             |           | not null |         | extended |              | 
 embarked    | text             |           | not null |         | extended |              | 
Indexes:
    "titanic_pkey" PRIMARY KEY, btree (passengerid)


