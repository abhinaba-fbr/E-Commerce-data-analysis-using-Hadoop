import random

def getDate():
    year=random.randint(2020, 2022)
    month=random.randint(1, 12)
    if(month<10):
        month='0'+str(month)
    else:
        month=str(month)
    date=random.randint(1, 28)
    if(date<10):
        date='0'+str(date)
    else:
        date=str(date)
    return str(year)+"-"+month+"-"+date

def smallerOne(date1, date2):
    if(int(date1[:4])<=int(date2[:4])):
        if(int(date1[5:7])<=int(date2[8:])):
            if(int(date1[8:])<=int(date2[8:])):
                return date1
            else:
                return date2
        else:
            return date2
    else:
        return date2

def largerOne(date1, date2):
    if(int(date1[:4])>=int(date2[:4])):
        if(int(date1[5:7])>=int(date2[8:])):
            if(int(date1[8:])>=int(date2[8:])):
                return date1
            else:
                return date2
        else:
            return date2
    else:
        return date2


f=open("Login_Details.sql", "w")
f.write("use OnlineShopping;\n")
f.write("Create table Login(id int AUTO_INCREMENT PRIMARY KEY, reg_date date, last_login date);\n")
f.write("insert into Login(reg_date, last_login) values\n")
for i in range(0, 542):
    date1=getDate()
    date2=getDate()
    registerDate=smallerOne(date1, date2)
    lastLoginDate=largerOne(date1, date2)
    if(i!=542-1):
        f.write("('"+registerDate+"','"+lastLoginDate+"'),\n")
    else:
        f.write("('"+registerDate+"','"+lastLoginDate+"')\n")

f.close()