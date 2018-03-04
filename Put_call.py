""" Arbitrage finder within put call parity

	We enter the following info into a list
	[stock, put, call, strike, IR, time ]

	IR is given in a decimal (4% is 0.04)
	time is given in years (3 months is 0.25 years)


	below this there is the addition of the call and put pricing calculator



"""
from math import log, exp,sqrt
from math import *

def test_arb(list_prices):

	def breakdown(tl):
		return(tl[0],tl[1],tl[2],tl[3],tl[4],tl[5])

	def test(stock, put, call, strike, IR, time):
		if (stock + put > (call + strike*exp(-1* time *IR))):
			return shortSP()
		elif (stock + put < (call + strike*exp(-1* time *IR))):
			return longSP()
		else:
			return("Put Call Holds")

	def longSP():
		print("Today")
		print("Long a Stock at: $" , stock)
		print("Long a Put at: $" , put)
		print("Short a Call at: $" , call)
		print("Borrow $" , (stock+put-call) , "from the Bank at " ,IR)
		print("At Expiration")
		print("S > $" , strike , "the call will be excresized against us, put is out of the money")
		print("S < $" , strike , "we will excresize our put, call is out of the money")
		print("We now payback the bank: $", (stock+put-call)*exp(1* time *IR))
		print("Our profit for the trade is: $", strike - (stock+put-call)*exp(1* time *IR))

	def shortSP():
		print("Today")
		print("Short a Stock at: $" , stock)
		print("Short a Put at: $" , put)
		print("Long a Call at: $" , call)
		print("Deposit $" , (stock+put-call) , "at the Bank at " ,IR)
		print("At Expiration")
		print("S > $" , strike , "the put will be excresized against us, call is out of the money")
		print("S < $" , strike , "we will excresize our call, put is out of the money")
		print("We now payback the bank: $", (stock+put-call)*exp(1* time *IR))
		print("Our profit for the trade is: $", (stock+put-call)*exp(1* time *IR) - strike)

	stock, put, call, strike, IR, time = breakdown(list_prices)
	return test(stock, put, call, strike, IR, time)


""" 
	Below is the put call pricer, we can use this to find the price 
    of a put and a call for our arbitrage finder if we dont have the prices
	
	To work with the prices we input the following data into run()

	run(Stock, Strike, Risk_Free_Rate, Time_to_Expiry, Volatility)
	
	there is a given input for run() incase you want to run to test the validity of the data:
	run() will have the following parameteres: Stock=100.0000 ,Strike = 105.0000, Risk_Free_Rate = 0.0600, Time_to_Expiry=0.5000, Volatility=0.2783
	approx:
	the call price is: 6.9999
	the put price is:  8.896697

"""



def erfcc(x):
    """Complementary error function."""
    z = abs(x)
    t = 1. / (1. + 0.5*z)
    r = t * exp(-z*z-1.26551223+t*(1.00002368+t*(.37409196+
        t*(.09678418+t*(-.18628806+t*(.27886807+
        t*(-1.13520398+t*(1.48851587+t*(-.82215223+
        t*.17087277)))))))))
    if (x >= 0.):
        return r
    else:
        return 2. - r
   


def NormalDist(x):
    return 1. - 0.5*erfcc(x/(2**0.5))

def give_d1(Stock,Strike, Risk_Free_Rate, Time_to_Expiry, Volatility):
	srt = Volatility * sqrt(Time_to_Expiry)
	d1 = (log(Stock) - log(Strike) + Time_to_Expiry * Risk_Free_Rate  + (0.5 * Time_to_Expiry * Volatility ** 2)) / srt
	return d1

def give_d2(d1, Time_to_Expiry, Volatility):
	srt = Volatility * (Time_to_Expiry ** 0.5)
	d2 = d1 - srt
	return d2

def get_Call_price(Stock,Strike, Risk_Free_Rate, Time_to_Expiry,d1,d2):
	call = Stock * NormalDist(d1) - Strike * exp(-1.0 * Time_to_Expiry * Risk_Free_Rate) * NormalDist(d2)
	return call

def get_put_price(Stock,Strike, Risk_Free_Rate, Time_to_Expiry,d1,d2):
	put = Strike * exp(-1.0 * Time_to_Expiry * Risk_Free_Rate) * NormalDist(-d2) - Stock * NormalDist(-d1)
	return put

def run(Stock=100.0000 ,Strike = 105.0000, Risk_Free_Rate = 0.0600, Time_to_Expiry=0.5000, Volatility=0.2783):
	d1 = give_d1(Stock, Strike, Risk_Free_Rate , Time_to_Expiry , Volatility)
	print("d1 is: ", d1)
	d2 = give_d2(d1, Time_to_Expiry, Volatility)
	print("d2 is: ", d2)
	call = get_Call_price(Stock, Strike, Risk_Free_Rate , Time_to_Expiry , d1, d2)
	print("Call Price for the option is: ", call)
	put = get_put_price(Stock, Strike, Risk_Free_Rate , Time_to_Expiry , d1, d2)
	print("Put price for the option is: ", put)
	return d1,d2,call,put