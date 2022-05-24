use ABShopping;

-- set dynamic partitioning configurations
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict

-- create partitioned tables based on state(domains)
create table Cus_cart_partitioned (
    CustomerID int,
    CustomerName varchar(255),
    City varchar(255),
    ItemID int,
    Required int
)
partitioned by (State varchar(255)),
row format delimited
fields terminated by ',';

create table Ven_cart_partitioned (
    VendorID int,
    VendorName varchar(255),
    City varchar(255),
    ItemID int,
    Stock int
)
partitioned by (State varchar(255)),
row format delimited
fields terminated by ',';

-- loading data into the partitioned tables
insert int Cus_cart_partitioned
partition(State)
select CustomerID, CustromerName, City, ItemID, Required,
State
from table Cus_cart; 

insert int Ven_stock_partitioned
partition(State)
select VendorID, VendorName, City, ItemID, Stock,
State
from table Ven_stock;