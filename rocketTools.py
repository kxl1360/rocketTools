import sys
import psycopg2
import pandas as pd

#estab. connection to db
conn = psycopg2.connect(host="reddwarf@cs.rit.edu", port = 5432, database="p320_24", user="p320_24", password="AhXetae3Aithahy1aijo")

#create cursor obj
cur = conn.cursor()

def createDataDisplay(sql_query, database = conn):
    table = pd.read_sql_query(sql_query, database)
    return table

def run():
	""" Function to handle command line usage"""
	args = sys.argv
	args = args[1:] # First element of args is the file name
	if len(args) == 0:
		print('You have not passed any commands in!')
	else:
		for a in args:
			if a == '--help':
				print('RocketTools Command Line Program')
				print('Options:')
				print('    --help -> show this basic help menu.')
				print('    --ol -> show owner leaderboard')
				print('    --bl -> show borrower leaderboard')
			elif a == '--ol':
				createDataDisplay("SELECT u.name, own.cnt FROM "user" u JOIN (SELECT "ownerUNR", count("ownerUNR") AS cnt FROM "ownedTool" GROUP BY "ownerUNR") own ON u.unr = own."ownerUNR" ORDER BY cnt DESC LIMIT 10;")
			elif a == '--bl':
				createDataDisplay("SELECT u.name, borrow.cnt FROM "user" u JOIN (SELECT "borrowerUNR", count("borrowerUNR") AS cnt FROM "borrowedTool" GROUP BY "borrowerUNR") borrow ON u.unr = "borrowerUNR" ORDER BY cnt DESC LIMIT 10;")
			else:
				print('Unrecognised argument.')
if __name__ == '__main__':
	do_work()

cur.close()
conn.close()