import unittest
import pyminerva as mi

WATCH_TICKERS2 = {
    'US':[{'stock':['SPY',]}, {'bond':['',]}, {'commodity':['']}, {'currency':['']}, ],
    'KR':[{'stock':['^KS200', ]}, {'bond':['',]}, {'commodity':['']}, {'currency':['']}, ],    
}
TIMEFRAMES = ['1min', '1hour', '1day']
'''
Main Fuction
'''

if __name__ == "__main__":
    
    for x in WATCH_TICKERS2['US']:

        for asset, tickers in x.items():

            for ticker in tickers:

                if ticker == '':
                    continue

                # settings.py 에서 get_stock_history with timeframe 파일 만들어 줌.
                print('')                
                print(f' ##### {ticker}')

                mi.get_stock_history(ticker, TIMEFRAMES)
                mi.timing_strategy(ticker, 20, 200) # 200일 이평 vs 20일 이평

                # volatility_bollinger_strategy(ticker, TIMEFRAMES) # 임계값 찾는 Generic Algorithm 보완했음.

                # vb_genericAlgo_strategy(ticker) # Bolinger Band Strategy + 임계값 찾는 Generic Algorithm       

                # vb_genericAlgo_strategy2(ticker) # Bolinger Band Strategy + 임계값 찾는 Generic Algorithm           

                # reversal_strategy(ticker, TIMEFRAMES) 

                # trend_following_strategy(ticker)  # 단기 매매 아님. 중장기 매매 기법, 1day 데이터만으로 실행

                # control_chart_strategy(ticker)

                # gaSellHoldBuy_strategy(ticker)
