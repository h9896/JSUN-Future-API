import os
from datetime import datetime
class JAPI_Eventhandler(object):
    def __init__(self, ReportPath, TradePath):
        self.ReportPath = ReportPath
        if not os.path.isfile(ReportPath):
            name_list ="Ibno, Account, AfterQty, BS, ClientOrdNo, ErrMsg, ErrorCode, Exchange, ExchangeRate, ExchangeServerReveiveTime, Marketflag, \
            MatchQty, Orderfunc, OrderIP, OrderNo, PositionEffect, Price, Priceflag, QTY, SubAccount, Symbol, Tif, TradeServerReceiveTime, TimePeriod"
            with open(ReportPath, 'a') as f:
                f.write(name_list+'\n')
        self.TradePath = TradePath
        if not os.path.isfile(TradePath):
            name_list ="Ibno, Account, BS, BS1, BS2, ClientOrderNo, DealTime, Exchange, ExchangeRate, Marketflag, OrderIP, OrderNo, \
            PositionEffect, Price, Price1, Price2, Qty, Qty1, Qty2, SubAccount, Symbol, Symbol1, Symbol2, Tif, tradeNo, TimePeriod"
            with open(TradePath, 'a') as f:
                f.write(name_list+'\n')
    def LoginStatus(self,msgcode, msg):
        print(msgcode + ":" + msg)
    def TradeConnStatus(self,msgcode, msg):
        print(msgcode + ":" + msg)
    def QueryConnStatus(self,msgcode, msg):
        print(msgcode + ":" + msg)
    def Error(self,msgcode, msg, clientOrderNo):
        print(msgcode + ": " + msg + ", -->> " + clientOrderNo)

    def Report(self, *argv):
        name_list = ['Ibno', 'Account', 'AfterQty', 'BS', 'ClientOrdNo', 'ErrMsg', 'ErrorCode', 'Exchange', 'ExchangeRate', 'ExchangeServerReveiveTime', 'Marketflag', \
            'MatchQty', 'Orderfunc', 'OrderIP', 'OrderNo', 'PositionEffect', 'Price', 'Priceflag', 'QTY', 'SubAccount', 'Symbol', 'Tif', 'TradeServerReceiveTime', 'TimePeriod']
        data_list=[]
        str = ""
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
            str = str + ", {0}".format(data_list[i])
        str = str[2:] + "\n"
        with open(self.ReportPath, 'a') as f:
                f.write(str)
    def Trade(self,*argv):
        name_list = ['Ibno', 'Account', 'BS', 'BS1', 'BS2', 'ClientOrderNo', 'DealTime', 'Exchange', 'ExchangeRate', 'Marketflag', 'OrderIP', 'OrderNo', \
            'PositionEffect', 'Price', 'Price1', 'Price2', 'Qty', 'Qty1', 'Qty2', 'SubAccount', 'Symbol', 'Symbol1', 'Symbol2', 'Tif', 'tradeNo', 'TimePeriod']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def QueryReport(self,*argv):
        name_list = ['Ibno', 'Account', 'AfterQty', 'BS', 'ClientOrdNo', 'ErrMsg', 'ErrorCode', 'Exchange', 'ExchangeRate', 'ExchangeServerReveiveTime', \
            'Marketflag', 'MatchQty', 'Orderfunc', 'OrderIP', 'OrderNo', 'PositionEffect', 'Price', 'Priceflag', 'QTY', 'SubAccount', 'Symbol', 'Tif', \
            'TradeServerReceiveTime', 'TimePeriod']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def QueryTrade(self,*argv):
        name_list = [ 'Ibno', 'Account', 'BS', 'BS1', 'BS2', 'ClientOrderNo', 'DealTime', 'Exchange', 'ExchangeRate', 'Marketflag', 'OrderIP', 'OrderNo', 'PositionEffect', \
            'Price', 'Price1', 'Price2', 'Priceflag', 'Qty', 'Qty1', 'Qty2', 'SubAccount', 'Symbol', 'Symbol1', 'Symbol2', 'Tif', 'tradeNo', 'TimePeriod']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def AccountData(self,Market, ibno, Account, subAccount = None):
        if (subAccount == None):
            print(Market + ":[" + ibno + "-" + Account + "]")
        else:
            print(Market + ":[" + ibno + "-" + Account + "-" + subAccount + "]")

    def Position(self,*argv):
        if (argv[-1] == "N"):
            print("無部位資料")
        else:
            name_list = ['Ibno', 'Account', 'SubAccount', 'ClientNo', 'BS', 'Symbol', 'Exchange_flag', 'ExchangeRate', 'Marketflag', 'B_AvgPrice', 'B_TotalQty', \
                'S_AvgPrice', 'S_TotalQty', 'Currency', 'Optionflag', 'YyyyMM', 'StrikePrice']
            data_list=[]
            for i in argv:
                data_list.append(i)
            for i in range(len(name_list)):
                print("{0} : {1}".format(name_list[i], data_list[i]))

    def Equity(self,*argv):
        name_list = [ "分公司", "帳號", "子帳號", "序號", "維持率", "帳戶權益", "今日存提款", "可用餘額", "平倉損益", "原始保証金", "維持保証金", "浮動損益", \
            "帳戶餘額", "權利金收入與支出", "預扣權利金", "買方市值", "賣方市值", "前日權益", "前日帳戶餘額", "今日總手續費", "今日總交易稅", "權益總值", \
            "風險指標(總權益維持率)", "浮動報酬率", "足額原始保証金", "足額維持保証金", "足額可用餘額", "足額維持率", "足額總權益維持率", "當沖未平倉註記", \
            "最佳化註記", "昨日權益總市值", "IB代碼", "有價證券抵繳", "有價可用", "現金可用", "足額現金可用", "未實現利得", "委託原始保證金", "委託維持保證金", \
            "委託足額原始保證金", "委託足額維持保證金", "加收保證金", "超額/追繳保證金", "到期履約損益", "未沖銷賣權買方選擇權市值", "未沖銷賣權賣方選擇權市值", \
            "未沖銷買權買方選擇權市值", "未沖銷買權賣方選擇權市值", "加收保證金指標" ]
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def SeaReport(self,*argv):
        name_list = ['Ibno', 'Account', 'AfterQty', 'BeforeQty', 'BS', 'ClientOrdNo', 'ErrMsg', 'ErrorCode', 'Exchange', 'ExchangeRate', 'ExchangeServerReveiveTime', \
            'ExchangeServerReveiveTimeUTC', 'Marketflag', 'MatchQty', 'Orderfunc', 'OrderIP', 'OrderNo', 'PositionEffect', 'Price', 'PriceFraction', 'Priceflag', \
            'QTY', 'SubAccount', 'Symbol', 'Tif', 'TradeServerReceiveTime', 'TradeServerReceiveTimeUTC', 'StopPrice', 'StopPriceFraction', 'Ftf', 'GtdExpireday', \
            'MiniQty', 'Scf']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def SeaTrade(self,*argv):
        name_list = ['Ibno', 'Account', 'BS', 'BS1', 'BS2', 'ClientOrderNo', 'DealTime', 'DealTimeUTC', 'Exchange', 'ExchangeRate', 'Marketflag', 'OrderIP', 'OrderNo', \
            'PositionEffect', 'Price', 'Price1', 'Price2', 'Qty', 'Qty1', 'Qty2', 'SubAccount', 'Symbol', 'Symbol1', 'Symbol2', 'Tif', 'tradeNo', 'PriceFraction']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def QuerySeaReport(self,*argv):
        name_list = ['Ibno', 'Account', 'AfterQty', 'BeforeQty', 'BS', 'ClientOrdNo', 'ErrMsg', 'ErrorCode', 'Exchange', 'ExchangeRate', 'ExchangeServerReveiveTime', \
            'ExchangeServerReveiveTimeUTC', 'Marketflag', 'MatchQty', 'Orderfunc', 'OrderIP', 'OrderNo', 'PositionEffect', 'Price', 'PriceFraction', 'Priceflag', 'QTY', \
            'SubAccount', 'Symbol', 'Tif', 'TradeServerReceiveTime', 'TradeServerReceiveTimeUTC', 'StopPrice', 'StopPriceFraction', 'Ftf', 'GtdExpireday', 'MiniQty', 'Scf']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def QuerySeaTrade(self,*argv):
        name_list = [ 'Ibno', 'Account', 'BS', 'BS1', 'BS2', 'ClientOrderNo', 'DealTime', 'DealTimeUTC', 'Exchange', 'ExchangeRate', 'Marketflag', 'OrderIP', 'OrderNo', \
            'PositionEffect', 'Price', 'Price1', 'Price2', 'Qty', 'Qty1', 'Qty2', 'SubAccount', 'Symbol', 'Symbol1', 'Symbol2', 'Tif', 'tradeNo', 'PriceFraction']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def OptionGroup(self,*argv):
        name_list = [ 'QueryFlag', 'Status', 'ErrorMessage', 'ClientOrderNo']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def OptionDisGroup(self,*argv):
        name_list = [ 'QueryFlag', 'Status', 'ErrorMessage', 'ClientOrderNo']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def OptionDisAllGroup(self,*argv):
        name_list = [ 'QueryFlag', 'Status', 'ErrorMessage', 'ClientOrderNo']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def OptionAllGroupTrial(self,*argv):
        name_list = ['QueryFlag', 'Ibno', 'Account', 'BS1', 'Symbol1', 'BS2', 'Symbol2', 'Qty', 'SpreadInitialMargin', 'SpreadMaintainMargin', 'Status', \
            'SumMarginReduceCurrency', 'SumInitialMarginReduce', 'SumMaintainMarginReduce', 'clientno']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def Withdraw(self,*argv):
        name_list = ["QueryFlag", "Status", "ErrorMessage"]
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def WithdrawInquire(self,*argv):
        name_list = ["QueryFlag", "Date", "Time", "TXCode", "Amount", "CancelFlag", "BankID", "BankNo", "str", "seq"]
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def CancelWithdraw (self,*argv):
        name_list = ["QueryFlag", "Status", "ErrorMessage"]
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def CancelInquire (self,*argv):
        name_list = ["QueryFlag", "CancelFlag", "Date", "Time", "Amount", "Account", "seqno", "str"]
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def Tranfer (self,*argv):
        name_list = ["QueryFlag", "Status", "ErrorMessage"]
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def TranferInquire (self,*argv):
        name_list = ["QueryFlag", "TransferFlag", "Account", "Date", "Time", "BankID", "BankNo", "Amount", "Currency", "Status", "Seqno", "str"]
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def SeaCancelInquire (self,*argv):
        name_list = ["QueryFlag", "TransferFlag", "Account", "Date", "Time", "BankID", "BankNo", "Amount", "Currency", "Status", "Seqno", "str"]
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
class JAPI_Fuction(object):
    def __init__(self, api):
        self.api = api
    def login(self, ID, PASS, IPSERVER):
        self.api.Login(ID, PASS, IPSERVER, "5", "6")
    def logout(self):
        self.api.Logout()
    def LoginStatusFlag(self):
        return self.api.LoginStatusFlag
    def order(self, ibno, acc, symbol, bs, clientOrder, symbolflag, orderip, price, qty):
        self.api.NewOrder(ibno, acc, symbol, bs, clientOrder, symbolflag, orderip, price, qty)
    def cancel_order(self, ibno, acc, bs, clientOrder, symbolflag, orderip, order_no, symbol):
        self.api.CancelOrder(ibno, acc, bs, clientOrder, symbolflag, orderip, order_no, symbol)
    def modify_qty_order(self, ibno, acc, bs, clientOrder, symbolflag, orderip, order_no, qty, symbol):
        self.api.ModifyQtyOrder(ibno, acc, bs, clientOrder, symbolflag, orderip, order_no, qty, symbol)
    def modify_price_order(self, ibno, acc, bs, clientOrder, symbolflag, orderip, order_no, symbol, price):
        self.api.ModifyPriceOrder(ibno, acc, bs, clientOrder, symbolflag, orderip, order_no, symbol, price)
    def query_internal_report(self, ibno, acc):
        self.api.QueryReport("2", ibno, acc)
    def query_internal_trade(self, ibno, acc):
        self.api.QueryTrade("2", ibno, acc)
    def seaorder(self, ibno, acc, symbol, bs, clientOrder, symbolflag, orderip, priceString, qty, exchange):
        self.api.SeaNewOrder(ibno, acc, symbol, bs, clientOrder, symbolflag, orderip, priceString, qty, "1", "1", "4", None, exchange)
    def seacancel_order(self, ibno, acc, clientOrder, orderip, order_no):
        self.api.SeaCancelOrder(ibno, acc, clientOrder, orderip, order_no)
    def query_foreign_report(self, ibno, acc):
        self.api.QueryReport("5", ibno, acc)
    def query_foreign_trade(self, ibno, acc):
        self.api.QueryTrade("5", ibno, acc)
    def option_group(self, ibno, acc, PASS, symbol1, bs1, symbol2, bs2, qty, clientOrder):
        self.api.OptionGroup("2", ibno, acc, PASS, symbol1, bs1, symbol2, bs2, qty, clientOrder)
    def option_dis_group(self, ibno, acc, PASS, symbol, bs, qty, clientOrder):
        self.api.OptionDisGroup("2", ibno, acc, PASS, symbol, bs, qty, clientOrder)
    def option_disall_group(self, ibno, acc, PASS, clientOrder):
        self.api.OptionDisAllGroup("2", ibno, acc, PASS, clientOrder)
    def option_allgroup_trial(self, ibno, acc, clientOrder):
        self.api.OptionAllGroupTrial("2", ibno, acc, clientOrder)
    def margin_internal_withdraw(self, ibno, acc, PASS, amount, toCurrency, fromCurrency, exchangeCurrency):
        self.api.MarginWithdraw("2", ibno, acc, PASS, amount, toCurrency, fromCurrency, exchangeCurrency)
    def margin_foreign_withdraw(self, ibno, acc, PASS, amount, toCurrency, fromCurrency, exchangeCurrency):
        self.api.MarginWithdraw("5", ibno, acc, PASS, amount, toCurrency, fromCurrency, exchangeCurrency)
    def margin_internal_transfer(self, transfer, ibno, acc, PASS, amount, fromCurrency, toCurrency, exchangeCurrency):
        self.api.MarginTransfer(transfer, "2", ibno, acc, PASS, amount, fromCurrency, toCurrency, exchangeCurrency)
    def margin_foreign_transfer(self, transfer, ibno, acc, PASS, amount, fromCurrency, toCurrency, exchangeCurrency):
        self.api.MarginTransfer(transfer, "5", ibno, acc, PASS, amount, fromCurrency, toCurrency, exchangeCurrency)
    def margin_internal_cancel(self, ibno, acc, PASS, setCurrency, seqIDX, fromDate, toDate, toCurrency):
        self.api.CancelMarginWithdraw("2", ibno, acc, PASS, setCurrency, seqIDX, fromDate, toDate, toCurrency)
    def margin_foreign_cancel(self, ibno, acc, PASS, setCurrency, seqIDX, fromDate, toDate, toCurrency):
        self.api.CancelMarginWithdraw("5", ibno, acc, PASS, setCurrency, seqIDX, fromDate, toDate, toCurrency)
    def query_internal_margin(self, ibno, acc, fromDate, toDate):
        self.api.QueryMarginStatement("2", ibno, acc, fromDate, toDate)
    def query_foreign_margin(self, ibno, acc, fromDate, toDate):
        self.api.QueryMarginStatement("5", ibno, acc, fromDate, toDate)
    def query_internal_margin_withdraw(self, ibno, acc, setCurrency, fromDate, toDate):
        self.api.QueryMarginWithdraw("2", ibno, acc, setCurrency, fromDate, toDate)
    def query_foreign_margin_withdraw(self, ibno, acc, setCurrency, fromDate, toDate):
        self.api.QueryMarginWithdraw("5", ibno, acc, setCurrency, fromDate, toDate)
    def query_margin_transfer(self, ibno, acc, setCurrency, fromDate, toDate):
        self.api.QueryMarginTransfer (ibno, acc, setCurrency, fromDate, toDate)
    def query_internal_position(self, ibno, acc, subAccount = None, clientOrder = None):
        self.api.QueryPOSITIONS("2", ibno, acc, subAccount, clientOrder)
    def query_foreign_position(self, ibno, acc, subAccount = None, clientOrder = None):
        self.api.QueryPOSITIONS("5", ibno, acc, subAccount, clientOrder)
    def query_internal_equilty(self, ibno, acc, subAccount = None, clientOrder = None):
        self.api.QueryEquilty("2", ibno, acc, subAccount, clientOrder)
    def query_foreign_equilty(self, ibno, acc, subAccount = None, clientOrder = None):
        self.api.QueryEquilty("5", ibno, acc, subAccount, clientOrder)