import random

no_of_stock_entries=2000

no_of_vendors=300
no_of_items=619

ven_map={}

# Get a random vid(vendor id)
def getVid():
    vid=random.randint(1, no_of_vendors)
    return vid

# Get a random item id
def getItemid(vid):
    if(vid in ven_map.keys()):
        itemid=random.randint(1, no_of_items)
        while(itemid in ven_map[vid]):
            itemid=(7*itemid)%no_of_items+1
        ven_map[vid].append(itemid)
        return itemid
    else:
        ven_map[vid]=[]
        itemid=random.randint(1, no_of_items)
        ven_map[vid].append(itemid)
        return itemid

# Get a random stock of an item
def getStocks():
    stk=random.randint(1, 50)
    return stk

fsql=open("SQLFiles/Insert_Stocks.sql", "w")

fsql.write("use ABShopping\n")
fsql.write("\n")
fsql.write("INSERT INTO Stocks Values\n")
for i in range(0, no_of_stock_entries):
    vid=getVid()
    itemid=getItemid(vid)
    stk=getStocks()
    fsql.write("("+str(vid)+","+str(itemid)+","+str(stk)+"),\n")

fsql.close()