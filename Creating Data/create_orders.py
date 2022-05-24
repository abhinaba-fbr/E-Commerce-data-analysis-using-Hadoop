import random

no_of_order_entries=3000

no_of_customers=2000
no_of_items=619

cus_map={}

# Get a random cid(customer id)
def getCid():
    cid=random.randint(1, no_of_customers)
    return cid

# Get a random item id
def getItemid(cid):
    if(cid in cus_map.keys()):
        itemid=random.randint(1, no_of_items)
        while(itemid in cus_map[cid]):
            itemid=(7*itemid)%no_of_items+1
        cus_map[cid].append(itemid)
        return itemid
    else:
        cus_map[cid]=[]
        itemid=random.randint(1, no_of_items)
        cus_map[cid].append(itemid)
        return itemid

# Get date in tuple(year, month, day)
def getDate():
    year=random.randint(2015, 2022)
    month=random.randint(1, 12)
    date=random.randint(1, 28)
    return (year, month, date)

fsql=open("SQLFiles/Insert_Orders.sql", "w")

fsql.write("use ABShopping\n")
fsql.write("\n")
fsql.write("INSERT INTO Orders Values\n")
for i in range(0, no_of_order_entries):
    cid=getCid()
    itemid=getItemid(cid)
    (year, month, day)=getDate()
    fsql.write("("+str(cid)+","+str(itemid)+","+str(year)+","+str(month)+","+str(day)+"),\n")

fsql.close()