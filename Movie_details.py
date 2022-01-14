import pymysql as my

try:
    con = my.connect(host='b3sqyzvrdy1lg4vsdtjz-mysql.services.clever-cloud.com', user='uvhhhh9bdv134leu', password='alfzAKZTOF6YKhbDDx89', database='b3sqyzvrdy1lg4vsdtjz')
    curs = con.cursor()
    nm = input('Enter Movie Name : ')

    curs.execute("select * from Movies where movie_name = '%s'" %nm)
    data = curs.fetchall()

    if data:
        print()
        print('Movie Name       : %s' %data[0][0])
        print('Year of Release  : %d' %data[0][1])
        print('IMDb Rating      : %s' %data[0][2])
        print('Actor Name       : %s' %data[0][3])
        print('Actress Name     : %s' %data[0][4])
        print('Director Name    : %s' %data[0][5])

    else: print('Sorry this movie is not in our database')
    con.close()

except Exception as error: print('Sorry we have error : ', error)