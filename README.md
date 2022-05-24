# E-Commerce-data-analysis-using-Hadoop
Pre-requsities-
---------------
1. Java version 8 or above. Both OpenJDK and Oracle JDK can be used. Project use OpenJDK 8
2. Hadoop framework. Project use Hadoop version 3.2.1
3. MySQL Server. Project use version 8
4. Apache Sqoop. Project use version 1.4.7
5. Apache Hive. Project use version 3.1.2

Instalation guide of Hadoop-
https://drive.google.com/drive/folders/1XdPbyAc9iWml0fPPNX91Yq3BRwkZAG2M

Sqoop instalation guide-
https://drive.google.com/drive/folders/1XdPbyAc9iWml0fPPNX91Yq3BRwkZAG2M

Hive instalation guide-
https://drive.google.com/drive/folders/1XdPbyAc9iWml0fPPNX91Yq3BRwkZAG2M

Overview-
---------
This project demonstrates how Hadoop and Hive can be used for processing e-commerce related big data, to generate useful insights, which can grow business stratergies. 

1. We are using a business architecture where each Indian state has an warehouse locally.
2. Total 26 state are considered and are also called domains.
3. Data is partitioned over these domains.

Our Analysis is comparing the stocks and requirement of products in a specified domain, inorder to increase or decrease the stocks in that particular domain.

Steps to be followed to reproduce the results-
----------------------------------------------
Note: Run all the commands and files from the root directory.

1. Start hadoop daemons from hadoop-3.2.1/sbin directory
```
$ ./start-all.sh
```
2. Use the Python Scripts(in Creating Data) to generate sql files/Use the generated .sql files(in SQLFiles) to populate mysql server.
3. Import data from mysql server to hadoop files using sqoop
```
sqoop import --connect jdbc:mysql://localhost/ABShopping --table Customers --username *use your username* -P --m 1
```
Similarly import the other tables into HDFS.
4. Create hive tables using the scripts in Hive int the following order -
  1. createNormalTables.sql
  2. createBucketedTables.sql
  3. createJoinTables.sql
  4. createPartitionedTables.sql
5. Open the file hiveQuery1.sql and rename the variable ```domain``` to the any state whose result is required.
6. Run DoQuery.sh with the name of the csv file as argument
```
$ ./DoQuery.sh OutputCsv
```
Note: Make sure a directory is created for storing the CSV in the root directory. 

