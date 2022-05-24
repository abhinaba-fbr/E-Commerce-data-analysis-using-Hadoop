import random

# Get date in tuple(year, month, day)
def getDate():
    year=random.randint(2015, 2022)
    month=random.randint(1, 12)
    date=random.randint(1, 28)
    return (year, month, date)

fsql=open("SQLFiles/Insert_RegisterDate.sql", "w")

fsql.write("use ABShopping\n")
fsql.write("\n")
fsql.write("INSERT INTO RegisterDates Values\n")
for i in range(1, 2001):
    (year, month, day)=getDate()
    fsql.write("("+str(i)+","+str(year)+","+str(month)+","+str(day)+"),\n")

fsql.close()

