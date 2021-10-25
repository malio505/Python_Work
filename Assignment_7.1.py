# A Dictionary showing ticker symbols for stocks and the price of stocks. 

stocks_0 = {
    'wmt':140.000, 'tgt':120.00, 'aapl':160.00, 'yum':125.00, 'levi':120.00,
    'ko':60.00, 'pep':160.00, 'gm':60.00, 'f':16.00, 'cvx':110.00,
    }

while(True):

    ticker_name = input("Please enter the ticker symbol(type exit to close): ").lower()

    #break from code if user enters exit
    if ticker_name == 'exit':
            break
        
    if ticker_name in stocks_0.keys():
        print('The price of the stock for '+ ticker_name + ' is ' + str('{:,}'.format(stocks_0[ticker_name]))) 
    else:
        print("Please check for any typos. Data not available for ",ticker_name) 