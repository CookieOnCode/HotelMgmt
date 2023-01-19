import mysql.connector as sqltor
import random as r

##          Creating table          ##
mycon=sqltor.connect(host="localhost", user="root", passwd="Password@123", database="hotelmgmt")
cursor=mycon.cursor()
cursor.execute("CREATE TABLE if not exists attribute_table(hotel_num int primary key, floor int, room_type varchar(250))")
cursor.execute("CREATE TABLE if not exists transaction_table(hotel_num int primary key, occupancy_status int)")

##          Fetching Room Data          ##

def fetchdata(btn_num):
    cursor.execute(f"select * from attribute_table where hotel_num = {btn_num}")
    data=cursor.fetchall()
    return data
def check_occ(btn_num):
    cursor.execute(f"select occupancy_status from transaction_table where hotel_num={btn_num}")
    occupied=cursor.fetchall()[0][0]
    return int(occupied)
def updatestatus(room_num):
    occupied= check_occ(room_num)
    if occupied == 0:
        cursor.execute(f"update transaction_table set occupancy_status = 1 where hotel_num={room_num}")
    else:
        cursor.execute(f"update transaction_table set occupancy_status = 0 where hotel_num={room_num}")

    mycon.commit()
##          Initializing Room Data          ##

if __name__=="__main__":
    try: 
        for j in range (1,5):
            for i in range (j*100+1, j*100+13):
                cursor.execute(f"insert into transaction_table values({i}, {r.choice((0, 1))})")
                mycon.commit()
    except sqltor.errors.IntegrityError:
        pass
    try: 
        for j in range (1,5):
            for i in range (j*100+1, j*100+13):
                if j*100+1<=i<=j*100+4:
                    type="Single"
                elif j*100+5<=i<=j*100+8:
                    type="Double"
                elif j*100+9<=i<=j*100+12:
                    type="Suite"
                cursor.execute(f"insert into attribute_table values({i}, {int(str(i)[0])}, '{type}' )")
                mycon.commit()
    except sqltor.errors.IntegrityError:
        pass


