# importing sql
import sqlite3
# importing pandas
import pandas as pd
conn=sqlite3.connect("database.sqlite")
print("connection is established")
#reading database file
readtables=pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';",conn)
print(readtables)

readmatch=pd.read_sql("SELECT * FROM Match;",conn)
print(readmatch.info())
readvenue=pd.read_sql("SELECT * FROM Venue;",conn)
print(readvenue.info())
readcity=pd.read_sql("SELECT * FROM City;",conn)
print(readcity.info())
readteam=pd.read_sql("SELECT * FROM Team;",conn)
print(readteam.info())
readingseasonid=pd.read_sql("SELECT Match_Id,Season_Id,V.Venue_Name,C.City_Name FROM Match INNER JOIN Venue as V ON Match.Venue_Id==V.Venue_Id INNER JOIN City as C ON C.City_Id==V.City_Id;",conn)
print(readingseasonid)
