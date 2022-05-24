use ABShopping;

set domain="Haryana";

CREATE TABLE tmp(
    ItemID int,
    TotalRequired int,
    TotalStock int
)
row format delimited
fields terminated by ',';


CREATE TABLE tmp_bucketed(
    ItemID int, 
    TotalRequired int,
    TotalStock int
)
clustered by(ItemID) into 5 buckets
row format delimited
fields terminated by ',';


insert into tmp
select one.itemid, one.req, two.stk from
(select itemid, sum(required) as req from cus_cart_partitioned where state=${hiveconf:domain} group by itemid) as one
LEFT OUTER JOIN
(select itemid, sum(stock) as stk from ven_stock_partitioned where state=${hiveconf:domain} group by itemid) as two
on one.itemid=two.itemid;


insert overwrite table tmp_bucketed select ItemID, TotalRequired, TotalStock from tmp;


CREATE TABLE new_tmp(
    ItemID int,
    ItemName varchar(255),
    Category varchar(255),
    TotalRequired int,
    TotalStock int
)
row format delimited
fields terminated by ',';


insert into new_tmp
select /*+ MAPJOIN(Items_Bucketed) */
Items_Bucketed.ItemID, Items_Bucketed.ItemName, Items_Bucketed.Category, tmp_bucketed.TotalRequired, tmp_bucketed.TotalStock
from Items_Bucketed
JOIN tmp_bucketed
on Items_Bucketed.ItemID=tmp_bucketed.ItemID;


-- drop table tmp;
-- drop table tmp_bucketed;
