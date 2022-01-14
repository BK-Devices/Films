import pymysql as my

try:
    con = my.connect(host='b3sqyzvrdy1lg4vsdtjz-mysql.services.clever-cloud.com', user='uvhhhh9bdv134leu', password='alfzAKZTOF6YKhbDDx89', database='b3sqyzvrdy1lg4vsdtjz')
    curs = con.cursor()

    curs.execute("select * from Movies")
    data = curs.fetchall()

    no = 0
    if data:
        for rec in data:
            no += 1
            print(no, ' - ', rec[0])
            
    else: print('Sorry we dont have any movie in our database')
    con.close()

except Exception as error: print('Sorry we have error : ', error)