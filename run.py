from ib_insync import *
import time
# util.startLoop()  # uncomment this line when in a notebook

def do_it():
    # sleep for 120seconds to give time for ib-gateway to initialize
    print("Sleeping for 120sec")
    time.sleep(120)
    print("Done sleeping")

    ib = IB()
    ib.connect('54.173.229.116', 4002, clientId=1)

    contract = Forex('EURUSD')
    bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

    # convert to pandas dataframe (pandas needs to be installed):
    df = util.df(bars)
    print(df)
    return


if __name__ == "__main__":
    do_it()
