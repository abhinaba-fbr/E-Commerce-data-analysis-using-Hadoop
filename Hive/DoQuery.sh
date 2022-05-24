#!/bin/bash

echo "Query Starting...."
hive -f hiveQuery1.sql --hiveconf state=$1
echo "Execution Done!!"
echo "Generating csv file output"
hive -e 'select itemid, itemname, category, totalrequired, totalstock from ABShopping.new_tmp' | sed 's/[[:space:]]\+/,/g' > /home/hdoop/CSVs/$1.csv
echo "Generated csv file!!"
echo "Cleaning up..."
hive -f hiveQuery2.sql
echo "Cleaned up enviroment!!"

