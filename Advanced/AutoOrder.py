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
                elif col_val[0] == "R_path":
                    R_path = col_val[1]
                elif col_val[0] == "T_path":
                    T_path = col_val[1]
        return ID, PASS, IPSERVER, IbNo, Account, DLL_Path, Event_path, Order_path, R_path, T_path
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:{0}".format(sys.exc_info()[0]))
        print("Unexpected error value: {0}\n".format(sys.exc_info()[1]))
        print("Unexpected error line: {0}\n".format(sys.exc_info()[2].tb_lineno))
        raise

def loadDll(dll_path, event_path, r_path, t_path):
    try:
        clr.AddReference(dll_path)
        from Jsunfutures import API
        os.chdir(event_path)
        from JAPI_Event import JAPI_Eventhandler, JAPI_Fuction
        japi = API()
        J_Event = JAPI_Eventhandler(r_path, t_path)
        japi.LoginStatusEvent += J_Event.LoginStatus
        japi.TradeConnStatusEvent += J_Event.TradeConnStatus
        japi.QueryConnStatusEvent += J_Event.QueryConnStatus
        japi.ErrorEvent += J_Event.Error
        japi.ReportEvent += J_Event.Report
        japi.TradeEvent += J_Event.Trade
        japi.QueryReportEvent += J_Event.QueryReport
        japi.QueryTradeEvent += J_Event.QueryTrade
        japi.AccountDataEvent += J_Event.AccountData
        japi.PositionEvent += J_Event.Position
        japi.EquityEvent += J_Event.Equity
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
    def __init__(self, api):
        self.api = api
    def orderfunc(self, ibno, acc, symbolflag, symbol, bs, price, qty):
        clientOrder = datetime.now().strftime('%H%M%S')
        self.api.order(ibno, acc, symbol, bs, clientOrder, symbolflag, None, price, qty)
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
    def cancelfunc(self, ibno, acc, bs, symbolflag, order_no, symbol):
        clientOrder = datetime.now().strftime('%H%M%S')
        self.api.cancel_order(ibno, acc, bs, clientOrder, symbolflag, None, order_no, symbol)
    def queryPositionfunc(self, ibno, acc):
        clientOrder = datetime.now().strftime('%H%M%S')
        self.api.query_internal_position(ibno, acc, None, clientOrder = datetime.now().strftime('%H%M%S'))
def main():
    ID, PASS, IPSERVER, IbNo, Account, DLL_Path, Event_path, Order_path, R_path, T_path = setting("setting.cfg")
    print("set ok!")
    jsf = ApiFunc(loadDll(DLL_Path,Event_path, R_path, T_path))
    print("load ok!")
    if jsf.loginfunc(ID, PASS, IPSERVER):
        ordfile = open(Order_path, 'r')
        updateTime = os.stat(Order_path).st_mtime
        while True:
            if updateTime != os.stat(Order_path).st_mtime:
                line = ordfile.readline()
                print(line)
                line = line.replace('\n','')
                cmd = line.split(',')
                if cmd[0].upper() == "ORDER":
                    jsf.orderfunc(cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6], cmd[7])
                elif cmd[0].upper() == "QUERYPOSITION":
                    jsf.queryPositionfunc(cmd[1], cmd[2])
                elif cmd[0].upper() == "QUERYREPORT":
                    jsf.api.query_internal_report(cmd[1], cmd[2])
                elif cmd[0].upper() == "CANCEL":
                    jsf.cancelfunc(cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6])
                elif cmd[0].upper() == "LOGOUT":
                    jsf.api.logout()
                    break
                updateTime = os.stat(Order_path).st_mtime
            time.sleep(0.1)

if __name__ == '__main__':
    main()