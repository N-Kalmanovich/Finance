import random
import pandas as pd
import numpy as np
from yahoo_historical import Fetcher
from datascience import *
import time
import csv

"""
This program will be able to take a list of tickets and provide us
with the optimal portfolio along with min variance protfolio
and the expected return and standard deviation based on historical
prices because we dont believe in the efficient market hypothesis.

"""


#Weight Generation:

"""
Weight Generation
We are generating the weight of each part of the 
porfolio given the number of stocks
"""

def weight_gen(n, total):
	weights = []
	while len(weights) != (n - 1):
		weights.append(random.uniform(-1,1))
	last = total - sum(weights)
	weights.append(last)
	
	if abs(weights[len(weights)-1]) <= 1:
		return weights
	else:
		return weight_gen(n, total)


"""
This is a stock class, it will give us all the info on the stock/ETF 
that we are interested in, to init: Stock("Ticker", start, end, cycle)
Ticker must be a string, start & end are in this format [yyyy,m,d]
Cycles can be 1d,1w, 1mo or 1y in string form
ex. SnP500 = Stock('^GSPC', [2017,1,1], None, "1mo")
"""

class Stock():
	
	def __init__(self, ticker, start = [2018,1,1], end = None, cycle = "1mo"):
		self.name = ticker
		self.info_array = run_Fetcher(ticker, start, end, cycle)

		self.var = np.var(self.info_array)
		self.sd = np.std(self.info_array)
		self.mean = np.mean(self.info_array)
		self.pureRet = (self.info_array[-1]-self.info_array[0])/self.info_array[0]
		self.rett = round(100*(self.info_array[-1]-self.info_array[0])/self.info_array[0], 3) , "%"


	def getArray(self):
		return self.info_array
	
	def getList(self):
		return list(self.info_array)

	def getVar(self):
		return self.var
	
	def getSD(self):
		return self.sd
	
	def getMean(self):
		return self.mean 

	def getPureRet(self):
		return self.pureRet

	def getRet(self):
		return self.rett

	def getAll(self):
		print("NAME:" , self.name)
		print("Mean:" , self.getMean())
		print("SD:" , self.getSD())
		print("Var:" , self.getVar())
		print("Returns:" , self.getRet())
		print(self.getArray())

def run_Fetcher(stock_name, start, end, cycle):
	#print(stock_name)
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

def chart_builder(tickers, start = [2018,1,1], market_maker = "^GSPC"):

	#double checks that tickers are a list and not a string from input
	if type(tickers) is not list:
		tickers = eval(tickers)

	#creates Table of Stocks and their tickers
	stocks = Table()	
	stocks = Table().with_columns('Ticker', np.asarray(tickers))
	
	#lists that will hold values temporarily
	sd = []
	var = []
	mean = []
	list_o_list = []
	puret = []
	
	#pupulating the lists using the stock class 
	for a in range(len(tickers)):
		b = Stock(tickers[a], start)
		sd.append(b.getSD())
		var.append(b.getVar())
		mean.append(b.getMean())
		list_o_list.append(b.getList())
		puret.append(b.getPureRet())

	#creating a new table with all the values
	stocks1 = stocks.with_columns('Mean', np.asarray(mean), 'SD', np.asarray(sd), 'Var', np.asarray(var), 'Return', np.asarray(puret), 'List Of Values', np.asarray(list_o_list))
	
	m = Stock(market_maker, start)
	market = Table()
	market = market.with_columns('Ticker', make_array(market_maker) ,'Mean', make_array(m.getMean()), 'SD', make_array(m.getSD()) , 'Var', make_array(m.getVar()) , 'Return', make_array(m.getPureRet()) , 'List Of Values', make_array(m.getList()) )
	

	return stocks1 , market
	
def corr_finder(st1, st2):
	return np.corrcoef(st1,st2)[1][0]



###NEEDS EDITING TO FIT NEW WAY#####

def exp_return(stocks, rfr, market):
	#here we are getting the expected return on a stock using CAPM
	
	market_maker = market.select("SD", "Var", "Return", "List Of Values")
	stock = stocks.select("SD", "List Of Values")


	

	beta = (corr_finder(stock[1] , market_maker[3]) * market_maker[0] * stock[0] ) / market_maker[1]
	exp = rfr + (beta * (market_maker[2] - rfr))
	

	return exp

def portfolio_info (stocks, rfr, market):
	



	weights = weight_gen(stocks.num_rows, 1.0)
	
	exp = [exp_return(stocks.take(i) , rfr, market) for i in range(stocks.num_rows)]
	

	product = [a * b for a,b in zip(exp,weights)]
	
	portVar = 0
	
	
	for i in range(stocks.num_rows):
		
		a = stocks.take(i).select("SD", "List Of Values")

		for j in range(stocks.num_rows):
			
			b = stocks.take(j).select("SD", "List Of Values")

			portVar += weights[i] * weights[j] * a[0] * b[0] * corr_finder(a[1] , b[1] )
	
	
	sharpe = (sum(product) - rfr) / pow(portVar, 0.5)

	return [sum(product) , portVar, sharpe, weights]







def main():
	
	ticks = input("Enter the list of tickers: ")
	ticks = eval(ticks)
	#removed input that way vvv
	#input a lit like this: ['AAPL' , 'F' , 'AMZN'] 	

	start_time = input("Enter start time as:[yyyy,m,d]    ")
	start_time = eval(start_time)

	rfr = input("Enter the risk free rate: ")
	rfr = eval(rfr)

	#input the risk free rate as a decimal

	sims = input("Enter the number of simulations: ")
	cycle = eval(sims)
	#how many times we want to run our sim



	#Lets us select a market other than the SNP to compare
	market = input("Would you like to use the S&P500 as your market reference?: (Y/N) ")
	if market.upper() == 'Y':
		market_maker = "^GSPC"
	else:
		market_maker = input("Insert the ticker of the market you want: ")
	
	

	
	#starts a timer so i can see how efficient my program is LOL
	t0 = time.time()

	stocks, market = chart_builder(ticks, start_time, market_maker)


	Monte = []
	top = [0,0,0,[]]                 #max sharp ratio portfolio
	mint = [0,float('inf'),0,[]]     #minimum risk portfolio
	
	while cycle:
		newport = portfolio_info(stocks, rfr, market)
		
		if newport[2] > top[2]:
			top = newport
		if newport[1] < mint[1]:
			mint = newport
		cycle -= 1
		Monte.append(newport)
	

	print("After ", len(Monte), "simulations we found: ")
	print("Max Sharpe portfolio: ")  
	print("ExpReturn: " , top[0])
	print("PortVar: " ,top[1])
	print("PortSD: " ,pow(top[1],0.5)) 
	print("PortSharpe: ", top[2])
	print("PortWeights: ", [[ticks[i] , top[3][i]] for i in range(len(ticks))])


	print("Min Risk portfolio: ")
	print("ExpReturn: " , mint[0])
	print("PortVar: " ,mint[1])
	print("PortSD: " ,pow(mint[1],0.5)) 
	print("PortSharpe: ", mint[2])
	print("PortWeights: ", [[ticks[i] , mint[3][i]] for i in range(len(ticks))])
	
	t1 = time.time()
	print("Execution Time: " , round((t1-t0), 4)/60, "Minutes")

	ans = input("Would you like to vizualize your attempts?(Y/N): ")
	
	if ans.upper() == "Y":
		viz = Table()
		ssd = []
		rets = []
		for i in range(len(Monte)):
			rets.append(Monte[i][0][0])
			ssd.append(Monte[i][1][0])
		viz = viz.with_columns("Attempts", np.asarray(range(len(Monte))), "Returns", np.asarray(rets), "Risk", np.asarray(ssd))
		viz.scatter('Attempts')
		print(viz)
