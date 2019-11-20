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
japi.SeaTradeEvent += JAPI_Eventhandler.SeaTrade
japi.SeaReportEvent += JAPI_Eventhandler.SeaReport
japi.SeaQueryTradeEvent += JAPI_Eventhandler.QuerySeaTrade
japi.SeaQueryReportEvent += JAPI_Eventhandler.QuerySeaReport
japi.OptionGroupEvent += JAPI_Eventhandler.OptionGroup
japi.OptionDisGroupEvent += JAPI_Eventhandler.OptionDisGroup
japi.OptionDisAllGroupEvent += JAPI_Eventhandler.OptionDisAllGroup
japi.OptionAllGroupTrialEvent += JAPI_Eventhandler.OptionAllGroupTrial
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
#Foreign order
exchange = "4"
fu.seaorder(ibno, acc, symbol, bs, clientOrder, symbolflag, orderip, price, qty, exchange)
#Cancel foreign order
fu.seacancel_order(ibno, acc, clientOrder, orderip, order_no)
#Query foreign order report
fu.query_foreign_report(ibno, acc)
#Query foreign trade report
fu.query_foreign_trade(ibno, acc)
#Group Option-----------------------------------
#The Symbol you want to merge
symbol1 = ""
#The Symbol's Buy or Sell
bs1 = ""
#The second Symbol you want to merge
symbol2 = ""
#The second Symbol's Buy or Sell
bs2 = ""
fu.option_group(ibno, acc, PASS, symbol1, bs1, symbol2, bs2, qty, clientOrder)
#DisGroup Option
#The Symbol you want to separate
symbol = ""
#The Symbol's Buy or Sell
bs = ""
fu.option_dis_group(ibno, acc, PASS, symbol, bs, qty, clientOrder)
#DisAllGroup Option
#Separate All Symbol you have
fu.option_disall_group(ibno, acc, PASS, clientOrder)
#Option Trial
fu.option_allgroup_trial(ibno, acc, clientOrder)
fu.logout()