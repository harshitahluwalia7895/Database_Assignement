import pymysql as pm

try:
    con = pm.connect(host='localhost', database='acadview', user='root', password='root')
    cursor = con.cursor()
    query1 = "Select * from Publishers where Publisher_ID=13"
    cursor.execute(query1)
    data = cursor.fetchall()
    for row in data:
        print('Publisher_ID: {}, Name: {}, Street_Adress: {}, Suite_Number: {}, Zip_Code_ID: {}' \
              .format(row[0], row[1], row[2], row[3], row[4]))

    query2 = "Update Publishers set Street_Address='Ramvilas Enclave' where Publisher_ID=14"
    cursor.execute(query2)
    con.commit()

    print("\nUpdated Table:")
    query3 = "Select * from Publishers"
    cursor.execute(query3)
    d = cursor.fetchall()
    for row in d:
        print('Publisher_ID: {}, Name: {}, Street_Adress: {}, Suite_Number: {}, Zip_Code_ID: {}' \
              .format(row[0], row[1], row[2], row[3], row[4]))

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('\nDONE!!')