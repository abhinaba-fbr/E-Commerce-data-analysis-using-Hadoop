use ABShopping;

-- create table for storing the joined data
create table Cus_cart(
    CustomerID int,
    CustomerName varchar(255),
    State varchar(255),
    City varchar(255),
    ItemID int,
    Required int
)
row format delimited
fields terminated by ',';

create table Ven_stock(
    VendorID int,
    VendorName varchar(255),
    State varchar(255),
    City varchar(255),
    ItemID int,
    Stock int
)
row format delimited
fields terminated by ',';

-- queries for joining using MAPJOIN
insert into Cus_cart
select /*+ MAPJOIN(Customer_bucketed) */
Customers_bucketed.CustomerID, Customers_bucketed.CustomerName, Customers_bucketed.State, Customers_bucketed.City, Cart_bucketed.ItemID, Cart_bucketed.Required
from Customers_bucketed
JOIN Cart_bucketed
on Customers_bucketed.CustomerID = Cart_bucketed.CustomerID;

insert into Ven_stock
select /*+ MAPJOIN(Vendors_bucketed) */
Vendors_bucketed.VendorID, Vendors_bucketed.VendorName, Vendors_bucketed.State, Vendors_bucketed.City, Stocks_bucketed.ItemID, Stocks_bucketed.Stock
from Vendors_bucketed
JOIN Stocks_bucketed
on Vendors_bucketed.VendorID = Stocks_bucketed.VendorID;