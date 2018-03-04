""" In this program we will find the repo rate as well as the purchase price for a given repo

	repo() will find the repo rate given on the terms that are provided
	repo(amount, repurchase, horizon)
	
	amount is the amount that is sold
	repurchase is the price that is repurchased at
	horizon is the length of time

	repo rate is give in a decimal that will yield a %/year





	repur() will find the repurchase price given on the terms that are provided
	repur(amount, repo, horizon)
	
	amount is the amount that is sold
	repo is given in a decimal form of %/year
	horizon is the length of time

	repur rate is give in $$$$


"""

def repo(amount,repurchase, horizon):
	first_term = (repurchase - amount) / amount
	second_term = 365.0 / horizon

	return(first_term*second_term)


def repur(amount, repo , horizon):
	return ((repo* amount*(horizon/365.0)) + amount)



