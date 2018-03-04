""" This is an arbitrage finder for covered interest partity,
	all the interest rates must be given in decimals and 
	forward and spot rates are FOR/DOM
	ammount is ammount borrowed from the bank

	[spot, forward, domestic_IR, foreign_IR, time_horizon, amount]

	"""


def test_arb(list_prices):

	def breakdown(tl):
		return(tl[0],tl[1],tl[2],tl[3],tl[4],tl[5])

	def test(spot, forward, domestic, foreign, time=1):
		if (spot*pow((1+foreign),time)) > (forward*pow((1+domestic),time)):
			return borrowDomestic()
		elif (spot*pow((1+foreign),time)) < (forward*pow((1+domestic),time)):
			return borrowForeign()
		else:
			return("Covered Interest Holds")

	def borrowDomestic():
		print("Today")
		print("Borrow from the Domestic bank at" , domestic, "IR")
		print("Use spot rate to convert into the foreign currentcy having a total of: ", amount * spot)
		print("Deposit at a foreign bank at ", foreign, "IR")
		print("Enter a forward agreement at ", (1/forward))

		print("At Expiration")
		print("Withdraw the deposit from the foreign bank having a total of:", amount*spot*pow((1+foreign),time) )
		print("Use the Forward to convert back to domestic having a total of:", (1/forward)*amount*spot*pow((1+foreign),time))
		print("Repay Domestic bank:", amount * pow((1+domestic),time))
		print("Make the profit of:", (1/forward)*amount*spot*pow((1+foreign),time) - amount*pow((1+domestic),time) )
	

	def borrowForeign():
		print("Today")
		print("Borrow from the foreign bank at" , foreign, "IR")
		print("Use spot rate to convert into the domestic currentcy having a total of: ", amount * (1/spot))
		print("Deposit at a domestic bank at ", domestic, "IR")
		print("Enter a forward agreement at ", forward)

		print("At Expiration")
		print("Withdraw the deposit from the domestic bank having a total of:", amount*(1/spot)*pow((1+domestic),time) )
		print("Use the Forward to convert back to foreign currency having a total of:", (1/spot)*amount*forward*pow((1+domestic),time))
		print("Repay foreign bank:",  amount* pow((1+foreign),time))
		print("Make the profit of:", (1/spot)*amount*forward*pow((1+domestic),time) - amount*pow((1+foreign),time))
	

	spot, forward, domestic, foreign, time, amount = breakdown(list_prices)
	return test(spot, forward, domestic, foreign, time)