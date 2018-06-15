import numpy as np
from yahoo_historical import Fetcher
from datascience import *
import csv

def run_Fetcher(stock_name, start, end, cycle):
	
	AAPL = Fetcher(stock_name, start , end , cycle)
	date_close = AAPL.getDatePrice()
	close = date_close.ix[:,[1]]

	summ = 0
	ar = np.empty

	for i in range(len(close)):
		summ += close.ix[i][0]
		ar = np.append(ar, close.ix[i][0])
	
	ar = ar[1:]
	
	return ar


def Sds_and_Mean(stock_table):
	running_numbers = []
	running_sds = []
	running_avg = []


	for k in range(stock_table.num_rows):
		st = stock_table.take(k)
		running_numbers.append(st[1])
		if k < 19:
			running_sds.append(np.std(running_numbers))
			running_avg.append(np.mean(running_numbers))
		else:
			last_20 = running_numbers[len(running_numbers)-19:]
			running_sds.append(np.std(last_20))
			running_avg.append(np.mean(last_20))

	return running_sds , running_avg

def main():
	
	ticker = input("Insert the ticker for the stock: ")
	

	start = input("Inser the start time [yyyy,m,d]: ")
	start = eval(start)
	



	#aapl is used as a place holder for the stocks bc when i was developing/running 
	#the tests i was hard coding aapl in the Fetcher
	aapl = run_Fetcher(ticker, start, None, '1d')
	
	st = Table().with_column('Day', np.asarray(range(1, len(aapl) + 1)) ,'Stock', np.asarray(aapl))
	sds, avg = Sds_and_Mean(st)
	st = st.with_column('Rumning Avg', np.asarray(avg) ,'SDs', np.asarray(sds))
	
	upper_bound = [avg[i] + (sds[i] * 2.0) for i in range(len(sds))]
	lower_bound = [avg[i] - (sds[i] * 2.0) for i in range(len(sds))]

	st = st.with_column('Lower', np.asarray(lower_bound), 'Upper', np.asarray(upper_bound))
	print(st)


	ans = input("Would you like to vizualize your Band?(Y/N): ")
	
	if ans.upper() == "Y":
	
		
		header = ["Day", "Stock" , "Running Avg" , "SDs" , "Lower" , "Upper"]

		with open('Bollinger.csv', 'w') as csvfile:
			writer = csv.writer(csvfile)
			
			writer.writerow(header) #header
			
			for k in range(st.num_rows):
				writer.writerow([st[0][k],st[1][k],st[2][k], st[3][k], st[4][k], st[5][k]])