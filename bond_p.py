""" Here we are creating a bond pricer for the different types of bonds that we are going to be looking at:

	for the Zero Coupon Bond we are using the simple equation to price it:
		Pzcb(t) = Facevalue / (1 + (yield/n))^nt

	for the Perpetuity bond, its pretty simple we just use the geometric series to bring it down to C/Y  and pays forever

	for the annuity we will use something different, the derivation simplifies into a formula that looks like this:

	(c/y) * (     1 - [1 / (1 + (yield/n))^nt)]     )

	
	zcb(Facevalue, Yield, n, Time)
	perp(CashFlow, Yield)
	annu(CashFlow, Yield, n, Time)

	Facevalue is $ amount
	CashFlow is $ amount paid per year by the bond
	Yield is in DECIMAL of a %/year
	n is number of payments per year
	Time is time in years



"""


def zcb(Facevalue, Yield, n, Time):
	bottom = pow((1 + (Yield / n)) , (n * Time))
	return Facevalue / bottom

def perp(CashFlow, Yield):
	return CashFlow / Yield

def annu(CashFlow, Yield, n, Time):
	inside = (1 - (1 / pow((1 + (Yield / n)) , (n * Time))))
	front = CashFlow / Yield
	return front * inside

