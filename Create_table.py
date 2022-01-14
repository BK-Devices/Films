import pymysql as my

try:
    con = my.connect(host='b3sqyzvrdy1lg4vsdtjz-mysql.services.clever-cloud.com', user='uvhhhh9bdv134leu', password='alfzAKZTOF6YKhbDDx89', database='b3sqyzvrdy1lg4vsdtjz')
    curs = con.cursor()

    curs.execute("show tables like 'Movies'")
    data = curs.fetchall()

    if data: print('Table is already exists in database')

    else:
        curs.execute("create table Movies(movie_name varchar(100) primary key not null, release_year int, IMDb_rating varchar(10), actor varchar(50), actress varchar(50), director varchar(50))")
        con.commit()
        print('Table has been created')

    con.close()

except Exception as error: print('Sorry we have error : ', error)