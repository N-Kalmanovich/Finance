""" In this program we are finding the fowards,current or future spot rates given on a time horizon and another rate using the idea of Law of one Price 

	in this situation we are playing around with the following equation

	(1 + rti)^ ti     *  (1 + te F ti)^ te    = (1+ rT) ^ T
			s.t.   T = te + ti

	te = time to expiration
	ti = time into the position

	T is the total time in years

		RATES ARE GIVEN AS DECIMALS!
	r are the type of spot rates
	F is the forward rate, which follows this format: (time to go from forward, F, time that past before)


	find_cur(future, T, ti , forward)
		->       rT, T, ti ,   F


	def find_for(future, T, ti, curspot)
		->	         rT, T, ti,  rti


	def find_fut(curspot, T, ti, forward)
		->           rti, T, ti,  F

"""


def find_cur(future, T, ti, forward)
	inside = (pow((1+future), T) / pow((1+forward),(T-ti)))
	return pow(inside, (1/ti)) - 1.0

def find_for(future, T, ti, curspot)
	inside = (pow((1+future), T) / pow((1+curspot),(ti)))
	return pow(inside, (1/(T-ti))) - 1.0

def find_fut(curspot, T, ti, forward)
	inside = (pow((1+curspot), ti) * pow((1+forward),(T-ti)))
	return pow(inside, (1/T)) - 1.0