import pymysql as my

try:
    con = my.connect(host='b3sqyzvrdy1lg4vsdtjz-mysql.services.clever-cloud.com', user='uvhhhh9bdv134leu', password='alfzAKZTOF6YKhbDDx89', database='b3sqyzvrdy1lg4vsdtjz')
    curs = con.cursor()
    file = open("Films.csv", "r")
    no = 0
    for rec in file:
        if no != 0:
            nm = rec.split(',')[0]
            yr = int(rec.split(',')[1])
            imdb = rec.split(',')[2]
            actr = rec.split(',')[3]
            actrs = rec.split(',')[4]
            dir = str(rec.split(',')[5])

            curs.execute("select * from Movies where movie_name = '%s'" %nm)
            data = curs.fetchall()

            if data: print('Sorry', nm, 'movie is already in our database')
            else:
                curs.execute("insert into Movies values('%s', %d, '%s', '%s', '%s', '%s')" %(nm, yr, imdb, actr, actrs, dir))
                con.commit()

                print(nm, 'Movie is added to our database')
        no += 1

    con.close()

except Exception as error: print('Sorry we have error : ', error)