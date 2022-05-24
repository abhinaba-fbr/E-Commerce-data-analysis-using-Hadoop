import random

no_of_cart_entries=5000

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

# Get a random requirement of an item
def getRequirement():
    req=random.randint(1, 10)
    return req

fsql=open("SQLFiles/Insert_Cart.sql", "w")

fsql.write("use ABShopping\n")
fsql.write("\n")
fsql.write("INSERT INTO Cart Values\n")
for i in range(0, no_of_cart_entries):
    cid=getCid()
    itemid=getItemid(cid)
    requirement=getRequirement()
    fsql.write("("+str(cid)+","+str(itemid)+","+str(requirement)+"),\n")

fsql.close()




