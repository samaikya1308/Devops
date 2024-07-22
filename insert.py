import pymysql
con=pymysql.connect(host='localhost',user='root',password='WJ28@KRHPS',database='aurora_fn',charset='utf8')
cur=con.cursor()
cur.execute("insert into candidate values('akhil',457668797,'2355667fge3','akhil')")
con.commit()
print("record inserted successfully..")
con.close()
cur.close()
 
