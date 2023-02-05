import psycopg2
import json

conn = psycopg2.connect(
   database="new_db", user='user', password='usr', host='127.0.0.1', port= '5432'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
code = 'T_601'
title = 'Yojimbo'
did = 106
date_prod = ''1961-06-16''
kind = 'Drama'
cursor.execute(f"INSERT INTO films (code, title, did, date_prod, kind) VALUES ({code}, {title}, {did}, {date_prod}, {kind})")

#Fetching 1st row from the table
# result = cursor.fetchone();
# print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
# print(result[0])

my_var = {}
new_list = []

for row in result:
    my_var['id'] = row[0]
    my_var['name'] = row[1]
    my_var['location'] = row[2]
    new_list.append(my_var.copy())

# print(new_list)

app_json = json.dumps(new_list)

print(app_json)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()