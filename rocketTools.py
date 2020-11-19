import sys
import psycopg2
import pandas as pd

#estab. connection to db
conn = psycopg2.connect(host="reddwarf@cs.rit.edu", port = 5432, database="p320_24", user="p320_24", password="AhXetae3Aithahy1aijo")

#create cursor obj
cur = conn.cursor()

def run():
	""" Function to handle command line usage"""
	args = sys.argv
	args = args[1:] # First element of args is the file name
	if len(args) == 0:
		print('You have not passed any commands in!')
	else:
		for a in args:
			if a == '--help':
				print('Basic command line program')
				print('Options:')
				print('    --help -> show this basic help menu.')
				print('    --ol -> show owner leaderboard')
				print('    --bl -> show borrower leaderboard')
			elif a == '--ol':
				cur.execute("""SELECT u.name, own.cnt
							FROM "user" u
							JOIN (SELECT "ownerUNR", count("ownerUNR") AS cnt
									FROM "ownedTool"
									GROUP BY "ownerUNR") own ON u.unr = own."ownerUNR"
							ORDER BY cnt DESC
							LIMIT 10;""")
				query_results = cur.fetchall()
				print(query_results)
			elif a == '--bl':
				cur.execute("""SELECT u.name, borrow.cnt
							FROM "user" u
							JOIN (SELECT "borrowerUNR", count("borrowerUNR") AS cnt
									FROM "borrowedTool"
									GROUP BY "borrowerUNR") borrow ON u.unr = "borrowerUNR"
							ORDER BY cnt DESC
							LIMIT 10;""")
				query_results = cur.fetchall()
				print(query_results)
			else:
				print('Unrecognised argument.')
if __name__ == '__main__':
	do_work()