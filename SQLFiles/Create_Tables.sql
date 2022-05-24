create database ABShopping;

use ABShopping;

-- create Customers

CREATE TABLE Customers(
    CustomerID int AUTO_INCREMENT PRIMARY KEY,
    CustomerName varchar(255),
    DOB date,
    Contact varchar(255),
    State varchar(255),
    City varchar(255)
);


-- create RegisterDates

CREATE TABLE RegisterDates(
    CustomerID int PRIMARY KEY,
    Year int,
    Month int,
    Day int
);


-- create Vendors

CREATE TABLE Vendors(
    VendorID int AUTO_INCREMENT PRIMARY KEY,
    VendorName varchar(255),
    State varchar(255),
    City varchar(255)
);


-- create Items

CREATE TABLE Items(
    ItemID int AUTO_INCREMENT PRIMARY KEY,
    ItemName varchar(255),
    Category varchar(255)
);


-- create Stocks

CREATE TABLE Stocks(
    VendorID int,
    ItemID int,
    Stock int,
    PRIMARY KEY (VendorID, ItemID)
);


-- create Cart

CREATE TABLE Cart(
    CustomerID int,
    ItemID int,
    Require int,
    PRIMARY KEY(CustomerID, ItemID)
);


-- create Orders

CREATE TABLE Orders(
    CustomerID int, 
    ItemID int,
    Year int, 
    Month int,
    Day int,
    PRIMARY KEY(CustomerID, ItemID)
);