import pymysql as my

try:
    con = my.connect(host='b3sqyzvrdy1lg4vsdtjz-mysql.services.clever-cloud.com', user='uvhhhh9bdv134leu', password='alfzAKZTOF6YKhbDDx89', database='b3sqyzvrdy1lg4vsdtjz')
    curs = con.cursor()
    nm = input('Enter Movie Name : ')

    curs.execute("select * from Movies where movie_name = '%s'" %nm)
    data = curs.fetchall()

    if data: print('Sorry this movie is already added in our database')
    else:
        yr = int(input('Enter Release Year of the Movie : '))
        imdb = float(input('Enter IMDb Rating out of 10 : '))
        actr = input('Enter the Name of Actor of the Movie : ')
        actrs = input('Enter the Name of Actress of the Movie : ')
        dir = input('Enter the Name of Director of the Movie : ')

        curs.execute("insert into Movies values('%s', %d, '%s', '%s', '%s', '%s')" %(nm, yr, str(imdb) + '/10', actr, actrs, dir))
        con.commit()

        print('Movie is added to our database')

    con.close()

except Exception as error: print('Sorry we have error : ', error)