"""
Please use 32bit version to open the JSFAPI.dll
"""
import os
import sys
import clr  #pip install pythonnet
import time
from datetime import datetime

def setting(path):
    try:
        with open(path, 'r') as f:
            sr = f.read().splitlines()
        for i in sr:
            if i != "":
                col_val = i.split('=')
                if col_val[0] == "ID":
                    ID = col_val[1]
                elif col_val[0] == "PASS":
                    PASS = col_val[1]
                elif col_val[0] == "IPSERVER":
                    IPSERVER = col_val[1]
                elif col_val[0] == "IbNo":
                    IbNo = col_val[1]
                elif col_val[0] == "Account":
                    Account = col_val[1]
                elif col_val[0] == "DLL_Path":
                    DLL_Path = col_val[1]
                elif col_val[0] == "Event_path":
                    Event_path = col_val[1]
                elif col_val[0] == "Order_path":
                    Order_path = col_val[1]
        return ID, PASS, IPSERVER, IbNo, Account, DLL_Path, Event_path, Order_path
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:{0}".format(sys.exc_info()[0]))
        print("Unexpected error value: {0}\n".format(sys.exc_info()[1]))
        print("Unexpected error line: {0}\n".format(sys.exc_info()[2].tb_lineno))
        raise

def loadDll(dll_path, event_path):
    try:
        clr.AddReference(dll_path)
        from Jsunfutures import API
        os.chdir(event_path)
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
        return JAPI_Fuction(japi)
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:{0}".format(sys.exc_info()[0]))
        print("Unexpected error value: {0}\n".format(sys.exc_info()[1]))
        print("Unexpected error line: {0}\n".format(sys.exc_info()[2].tb_lineno))
        raise

class ApiFunc(object):
    def __init__(self, api, ibno, acc):
        self.api = api
        self.ibno = ibno
        self.acc = acc
    def orderfunc(self, symbolflag, symbol, bs, price, qty):
        clientOrder = datetime.now().strftime('%H%M%S')
        self.api.order(self.ibno, self.acc, symbol, bs, clientOrder, symbolflag, None, price, qty)
    def loginfunc(self, ID, PASS, IPSERVER):
        self.api.login(ID, PASS, IPSERVER)
        i = 0
        while True:
            if self.api.LoginStatusFlag:
                return True
            if i > 5:
                self.api.logout()
                i = 0
                time.sleep(3)
                self.api.login(ID, PASS, IPSERVER)
            time.sleep(3)
            i += 1
    def logoutfunc(self):
        self.api.logout()
def main():
    ID, PASS, IPSERVER, IbNo, Account, DLL_Path, Event_path, Order_path = setting("D:\\www\\setting.cfg")
    print("set ok!")
    jsf = ApiFunc(loadDll(DLL_Path,Event_path), IbNo, Account)
    print("load ok!")
    if jsf.loginfunc(ID, PASS, IPSERVER):
        ordfile = open(Order_path, 'r')
        updateTime = os.stat(Order_path).st_mtime
        while True:
            if updateTime != os.stat(Order_path).st_mtime:
                line = ordfile.readline()
                print(line)
                if "Exit Now" not in line:
                    if ',' in line:
                        symbolflag, symbol, bs, price, qty = line.split(',')
                        jsf.orderfunc(symbolflag, symbol, bs, price, qty)
                else:
                    break
                updateTime = os.stat(Order_path).st_mtime
            time.sleep(0.1)

if __name__ == '__main__':
    main()