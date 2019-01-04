"""
Please use 32bit version to open the JSFAPI.dll
"""
import os
import clr
import time
from datetime import datetime
#-----------------------Login----------------------
ID = "Your ID"
PASS = "Your Passward"
IPSERVER = "Jsunfutures IP Address"
#-----------------------Symbol---------------------
ibno = "Your IB Number"
acc = "Your Account"
symbol = ""
#bs: 1 is buy, 2 is sell
bs = "1"
#clientOrder: whatever u want
clientOrder = datetime.now().strftime('%H%M%S')
# Symbolflag : (1- Futures, 2-Options, 3-Multiple Option, 4-Futures Spread)
symbolflag = "1"
#orderip: Your computer IP
orderip = "0.0.0.0"

price = "1000"
qty = "10"

#-----------------------API DLL--------------------
#dll_path : JSFAPI.dll path
dll_path = "JSFAPI.dll"
clr.AddReference(dll_path)
from Jsunfutures import API
#change dir to JAPI_Event.py path
JAPI_Event_path = ""
os.chdir(JAPI_Event_path)
from JAPI_Event import JAPI_Eventhandler, JAPI_Fuction
japi = API()
japi.LoginStatusEvent += JAPI_Eventhandler.LoginStatus
japi.TradeConnStatusEvent += JAPI_Eventhandler.TradeConnStatus
japi.QueryConnStatusEvent += JAPI_Eventhandler.QueryConnStatus
japi.ErrorEvent += JAPI_Eventhandler.Error
japi.ReportEvent += JAPI_Eventhandler.Report
japi.TradeEvent += JAPI_Eventhandler.Trade
japi.QueryReportEvent += JAPI_Eventhandler.QueryReport
japi.QueryTradeEvent += JAPI_Eventhandler.QueryTrade
japi.AccountDataEvent += JAPI_Eventhandler.AccountData
japi.PositionEvent += JAPI_Eventhandler.Position
japi.EquityEvent += JAPI_Eventhandler.Equity

fu = JAPI_Fuction(japi)
#--------------------------------------------------
#login
fu.login(ID, PASS, IPSERVER)
time.sleep(5)
#order
fu.order(ibno, acc, symbol, bs, clientOrder, symbolflag, orderip, price, qty)
#cancel order
#order_no is order id
fu.cancel_order(ibno, acc, bs, clientOrder, symbolflag, orderip, order_no, symbol)
#Query domestic order report
fu.query_internal_report(ibno, acc)
#Query domestic trade report
fu.query_internal_trade(ibno, acc)
fu.logout()