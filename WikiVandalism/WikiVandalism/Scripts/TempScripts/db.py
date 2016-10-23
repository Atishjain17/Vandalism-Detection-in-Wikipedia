import sqlite3 as sql
import pandas as pd

page_df = pd.read_csv("pages.csv", header=0)
user_df = pd.read_csv("Users.csv", header=0)
features_df = pd.read_csv("TrainTest.csv", header=0)
userdata = pd.read_csv("userdata.csv", header=0)

conn = sql.connect("VandalDB.db",true)
page_df.to_sql("Page", conn)
user_df.to_sql("User", conn)
features_df.to_sql("Features", conn)
userdata.to_sql("UserData", conn)
