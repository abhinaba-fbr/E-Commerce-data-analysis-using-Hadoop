use ABShopping;

-- creating bucketed table each of 5 buckets
create table Customers_bucketed(
    CustomerID int,
    CustomerName varchar(255),
    DOB date,
    Contact varchar(255),
    State varchar(255),
    City varchar(255)
)
clustered by(CustomerID) into 5 buckets
row format delimited
fields terminated by ',';

create table Vendors_bucketed(
    VendorID int,
    VendorName varchar(255),
    State varchar(255),
    City varchar(255)
)
clustered by(VendorID) into 5 buckets
row format delimited
fields terminated by ',';

create table Items_bucketed(
    ItemID int,
    ItemName varchar(255),
    Category varchar(255)
)
clustered by(ItemID) into 5 buckets
row format delimited
fields terminated by ',';

create table Cart_bucketed(
    CustomerID int,
    ItemID int,
    required int
)
clustered by(CustomerID) into 5 buckets
row format delimited
fields terminated by ',';

create table Stocks_bucketed(
    VendorID int,
    ItemID int,
    stock int
)
clustered by(VendorID) into 5 buckets
row format delimited
fields terminated by ',';

-- loading data 
insert overwrite table Customers_bucketed select * from Customers_normal;

insert overwrite table Vendors_bucketed select * from Vendors_normal;

insert overwrite table Items_bucketed select * from Items_normal;

insert overwrite table Cart_bucketed select * from Cart_normal;

insert overwrite table Stocks_bucketed select * from Stocks_normal;

-- if select * throws an error mention the individual attributes in the select list