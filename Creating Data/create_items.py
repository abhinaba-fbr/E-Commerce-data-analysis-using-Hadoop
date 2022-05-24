categories=['Books', 'Medicines', 'Phones', 'Laptops', 'Appliances', 'Foods']

fsql=open("SQLFiles/Insert_Items.sql", "w")

fsql.write("use ABShopping\n")
fsql.write("\n")
fsql.write("INSERT INTO Items Values\n")
count=0
for category in categories:
    cat_file_name=category.lower()
    fcat=open(cat_file_name+".txt", "r")
    items=fcat.readlines()
    count+=len(items)
    for item in items:
        fsql.write("('"+item.strip()+"','"+category+"'),\n")
    fcat.close()

print(count)

fsql.close()


