import pymysql as my

try:
    con = my.connect(host='b3sqyzvrdy1lg4vsdtjz-mysql.services.clever-cloud.com', user='uvhhhh9bdv134leu', password='alfzAKZTOF6YKhbDDx89', database='b3sqyzvrdy1lg4vsdtjz')
    curs = con.cursor()

    actr = input('Enter the Actor Name : ')
    curs.execute("select * from Movies where actor = '%s'" %actr)
    data = curs.fetchall()

    no = 0
    if data:
        for rec in data:
            no += 1
            print(no, ' - ', rec[0])
            
    else: print('Sorry we dont have any movie of this actor in our database')
    con.close()

except Exception as error: print('Sorry we have error : ', error)