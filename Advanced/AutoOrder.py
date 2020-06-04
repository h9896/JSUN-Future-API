"""
Please use 32bit version to open the JSFAPI.dll
"""
import os
import sys
import threading
from JSFApi import SetApi, ApiFunc, CustomTimer
import time
from pathlib import Path
def main():
    path = Path(__file__).parent.absolute()
    Init = SetApi(os.path.join(path,"setting.cfg"))
    ID, PASS, IPSERVER, IbNo, Account, DLL_Path, Order_path, R_path, T_path = Init.setting()
    print("set ok!")
    jsf = ApiFunc(Init.loadDll(DLL_Path, R_path, T_path))
    print("load ok!")
    jsf.loginfunc(ID, PASS, IPSERVER)
    threshold = jsf.checkLoginStatus()
    count = 0
    timer = CustomTimer(5, jsf.checkLoginStatus)
    timer.start()
    while not threshold:
        threshold = timer.join()
        if count > 5:
            jsf.logout()
            relogin = CustomTimer(1, jsf.loginfunc, (ID, PASS, IPSERVER))
            relogin.start()
            count = 0
        count += 1
        timer.cancel()
        timer = CustomTimer(5, jsf.checkLoginStatus)
        timer.start()
    print("Login ok!")
    ordfile = open(Order_path, 'r')
    updateTime = os.stat(Order_path).st_mtime
    while True:
        if updateTime != os.stat(Order_path).st_mtime:
            line = ordfile.readline()
            print(line)
            line = line.replace('\n','')
            cmd = line.split(',')
            if cmd[0].upper() == "ORDER":
                if(len(cmd)<7):
                    jsf.orderfunc(IbNo, Account, cmd[1], cmd[2], cmd[3], cmd[4], cmd[5])
                else:
                    jsf.orderfunc(cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6], cmd[7])
            elif cmd[0].upper() == "QUERYPOSITION":
                if(len(cmd)<3):
                    jsf.queryPositionfunc(IbNo, Account)
                else:
                    jsf.queryPositionfunc(cmd[1], cmd[2])
            elif cmd[0].upper() == "QUERYREPORT":
                if(len(cmd)<3):
                    jsf.api.query_internal_report(IbNo, Account)
                else:
                    jsf.api.query_internal_report(cmd[1], cmd[2])
            elif cmd[0].upper() == "CANCEL":
                if(len(cmd)<6):
                    jsf.cancelfunc(IbNo, Account, cmd[1], cmd[2], cmd[3], cmd[4])
                else:
                    jsf.cancelfunc(cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6])
            elif cmd[0].upper() == "LOGOUT":
                jsf.logout()
                break
            updateTime = os.stat(Order_path).st_mtime
        time.sleep(0.1)
if __name__ == '__main__':
    main()