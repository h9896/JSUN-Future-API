import os
import sys
import clr  #pip install pythonnet
from event.JAPI_Event import JAPI_Eventhandler, JAPI_Fuction
import time
from datetime import datetime
from threading import Timer
class SetApi(object):
    def __init__(self, config_path):
        self.config_path = config_path
    def setting(self):
        try:
            with open(self.config_path, 'r') as f:
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
                    elif col_val[0] == "Order_path":
                        Order_path = col_val[1]
                    elif col_val[0] == "R_path":
                        R_path = col_val[1]
                    elif col_val[0] == "T_path":
                        T_path = col_val[1]
            return ID, PASS, IPSERVER, IbNo, Account, DLL_Path, Order_path, R_path, T_path
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:{0}".format(sys.exc_info()[0]))
            print("Unexpected error value: {0}\n".format(sys.exc_info()[1]))
            print("Unexpected error line: {0}\n".format(sys.exc_info()[2].tb_lineno))
            raise
    def loadDll(self, dll_path, r_path, t_path):
        try:
            clr.AddReference(dll_path)
            from Jsunfutures import API
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
    def cancelfunc(self, ibno, acc, bs, symbolflag, order_no, symbol):
        clientOrder = datetime.now().strftime('%H%M%S')
        self.api.cancel_order(ibno, acc, bs, clientOrder, symbolflag, None, order_no, symbol)
    def queryPositionfunc(self, ibno, acc):
        self.api.query_internal_position(ibno, acc, None, clientOrder = datetime.now().strftime('%H%M%S'))
    def checkLoginStatus(self):
        return self.api.LoginStatusFlag()
    def logout(self):
        self.api.logout()
class CustomTimer(Timer):
    def __init__(self, interval, function, args=[], kwargs={}):
        self._original_function = function
        super(CustomTimer, self).__init__(
            interval, self._do_execute, args, kwargs)
    def _do_execute(self, *a, **kw):
        self.result = self._original_function(*a, **kw)

    def join(self):
        super(CustomTimer, self).join()
        return self.result
    