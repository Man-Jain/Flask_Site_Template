import sqlite3 as sl
import json,csv

data_dict={}
data_dict['items']=[]

def write_data(name,price):
	data_dict['items'].append({name:price})
	connect()
	insert(name,price)
	with open("items.json","w") as file:
		json.dump(data_dict,file)
	write=csv.writer(open("items.csv","a"))
	write.writerow([name,price])
	return 'Done'

def connect():
	con=sl.connect("price.db")
	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS item(name TEXT,price INTEGER)")
	con.commit()
	con.close()
	return 'OK'

def insert(name,price):
	con=sl.connect("price.db")
	cur=con.cursor()
	cur.execute("INSERT INTO item values(?,?)",(name,price))
	con.commit()
	con.close()
	return 'OK'

