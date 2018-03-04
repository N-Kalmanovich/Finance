""" Bond DF and Spot Finder for a list of bonds that is given to use from the outside"""
from datascience import *
import pandas
import numpy as np


class Bond:
	def __init__(self, maturity, coupon, price, principal = 100, n = 2):
		self.maturity = maturity
		self.coupon = coupon
		self.price = price
		self.principal = principal
		self.n = n

"""
HOW TO RUN THIS CODE:
This code will run by using the run function with the name of the file that will be in the same folder
***it mainly works with a csv file		
	
	ex. 		run('Book1.csv')

the first column will include the maturity date, MUST BE NAMED <Maturity>
the second column will have the coupon percent, MUST BE NAMED <Coupon>
the third column will be the current price, MUST BE NAMED <Price>


	The program will then output a nice table with all the info needed


THIS PROGRAM ASSUMES U.S. TREASURY BONDS THAT ARE SEMI-ANNUAL

"""
def run(name_file):
	bond_table = (Table.read_table(name_file)).select("Maturity", "Coupon", "Price")
	bond_list = []
	for a in range(bond_table.num_rows):
		table2 = bond_table.take(a)
		bond_list.append(Bond(table2[0][0],table2[1][0],table2[2][0]))

	dfl, spl = df(bond_list)
	full_table = bond_table.with_columns('Discount Factor', np.asarray(dfl),'Spot Rate', np.asarray(spl))
	print(full_table)


"We are passing in a list of bonds"
def df(bond_list):

	df = []
	spot = []
	
	for a in range(len(bond_list)):
		current = bond_list[a]
		new_df = (current.price - sum(df) * (current.coupon / current.n)) / (current.principal + (current.coupon / current.n))
		df.append(new_df)
		new_spot = 2.0 * ((1.0 / pow(new_df, (1.0 / (a + 1.0) ) )) -1.0)
		spot.append(new_spot)

	return(df, spot)


"Prints all the DFs"
def pr_df(df):
	print("DF:")
	for a in range(len(df)):
		print(df[a])
	return None


"Prints all the Spot Rates"
def pr_spt(spot):
	print("Spot:")
	for a in range(len(spot)):
		print(spot[a])
	return None 