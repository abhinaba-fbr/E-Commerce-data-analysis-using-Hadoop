use ABShopping;

-- creating tables
create table Customers_normal(
    CustomerID int,
    CustomerName varchar(255),
    DOB date,
    Contact varchar(255),
    State varchar(255),
    City varchar(255)
)
row format delimited
fields terminated by ',';

create table Vendors_normal(
    VendorID int,
    VendorName varchar(255),
    State varchar(255),
    City varchar(255)
)
row format delimited
fields terminated by ',';

create table Items_normal(
    ItemID int,
    ItemName varchar(255),
    Category varchar(255)
)
row format delimited
fields terminated by ',';

create table Cart_normal(
    CustomerID int,
    ItemID int,
    required int
)
row format delimited
fields terminated by ',';

create table Stocks_normal(
    VendorID int,
    ItemID int,
    stock int
)
row format delimited
fields terminated by ',';

create table Orders_normal(
    CustomerID int,
    ItemID int,
    year int,
    month int,
    day int
)
row format delimited
fields terminated by ',';


-- loading data
load data inpath '/user/hdoop/Customers' into table Customers_normal;

load data inpath '/user/hdoop/Vendors' into table Vendors_normal;

load data inpath '/user/hdoop/Items' into table Items_normal;

load data inpath '/user/hdoop/Cart' into table Cart_normal;

load data inpath '/user/hdoop/Stocks' into table Stocks_normal;

load data inpath '/user/hdoop/Orders' into table Orders_normal;