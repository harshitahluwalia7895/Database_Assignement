import pymysql as pm

try:
    con = pm.connect(host='localhost', database='acadview', user='root', password='root')
    cursor = con.cursor()
    query1 = "insert into Authors values (101,'','Desi','Firangee'),(102,'Nirma','Washing','Powder'),\
    (103,'Yuvraj','Stuart','Broad'),(104,'Raman','Pratap','Solanki'),(105,'Rahul','NamToSunaHiHoga','Gupta')"
    cursor.execute(query1)

    query2 = "insert into Zip_Codes values (1,'UttarPradesh','Lucknow',249014),(2,'Dehradun','Uttarakhand',248001),\
    (3,'Maharashtra','Mumbai',34987),(4,'UttarPradesh','Lucknow',249014),(5,'Rajasthan','Jaipur',123456)"
    cursor.execute(query2)

    query3 = "insert into Publishers values(10,'VK Pharg','Old Warriors Colony',51,2),(11,'Praful Kumar','Prasang Vihar',53,4),\
    (12,'All Duhai','Vijender Nagar',55,3),(13,'Rahul Gupta','Ramvilas Vihar',54,1),(14,'Mati Verma','Sharol Bagh',57,5)"
    cursor.execute(query3)

    query4 = "insert into Titles values (21,'ASongOfIce',1001,12,2005),(22,'GobletOfFire',1002,11,2003),\
    (23,'TheLoadRunner',1003,10,2014),(24,'FivePointThreeTw',1004,14,2012),(25,'NeedNoReasons',1005,13,2015)"
    cursor.execute(query4)

    query5 = "insert into Books values (201,21,'Hyderabad','Thriller'),(202,23,'Bangalore','Classic'),\
    (203,22,'NewDelhi','Romantic'),(204,25,'Kolkata','HateStory'),(205,24,'Chandigarh','Comedy')"
    cursor.execute(query5)

    query6 = "insert into Authors_Titles values (501,102,21),(502,101,22),(504,103,24),(505,105,23),(503,104,25)"
    cursor.execute(query6)

    con.commit()


except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')