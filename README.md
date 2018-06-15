# Finance

In this folder most of my regular finance oriented files will be stored.

Short descriptions
# Portfolio_builder.py
      This program will be able to take a list of tickers and provide us 
      with the optimal portfolio along with min variance protfolio
      and the expected return and standard deviation based on historical
      prices. Can also create as csv with data that can visualized the efficient
      frontier using Berkeley's datahub with an additional piece of code.

# datahub_portfolio_builder.py
    This is the code to visualize the efficient frontier on datahub

# BollingerBands.py
    This program will take in a ticker and a start date and will find the moving average 
    and moving SDs for the selected stock over the last 20 days, then can save a file to 
    visualize it using datahub
    
# datahub_BollingerBands.py
    This is the code to visualize the bands on datahub
     
# KeltnerChannel.py & datahub_KeltnerChannel.py
    This is similar to the Bollinger Bands yet uses the strategy created Keltner by using the 
    previous 10 days only for the moving averages

# bond_p.py 
    This program calculates the prices for annuity, perpetuity and zero coupon bonds.

# spot_forward_rate_finder.py
    This program calculates the rates of spot, forwards and future spot rates based on LOOP.
    
# repo.py
    This program calculates the repo rate as well as the costs of the repurchase based on a repo rate.

# Put_call.py
    This program finds arbitrage opprotunities for puts and calls and outlines the steps that are needed.
    Also includes a put-call pricer.
    
# Covered_interest.py 
    This program finds arbitrage opprotunities for foreign exchange markets based on the spot, 
    forwards and interest rates in the countries.

# df_spot.py 
    This program takes in a csv file with a list of bonds and finds the Discount Factor and Spot rates. 
    It returns it all in a nice data table using the datascience package.
