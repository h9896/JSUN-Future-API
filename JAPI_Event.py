class JAPI_Eventhandler():
    def LoginStatus(msgcode, msg):
        print(msgcode + ":" + msg)
    def TradeConnStatus(msgcode, msg):
        print(msgcode + ":" + msg)
    def QueryConnStatus(msgcode, msg):
        print(msgcode + ":" + msg)
    def Error(msgcode, msg, clientOrderNo):
        print(msgcode + ": " + msg + ", -->> " + clientOrderNo)

    def Report(*argv):
        name_list = ['Ibno', 'Account', 'AfterQty', 'BS', 'ClientOrdNo', 'ErrMsg', 'ErrorCode', 'Exchange', 'ExchangeRate', 'ExchangeServerReveiveTime', 'Marketflag', \
            'MatchQty', 'Orderfunc', 'OrderIP', 'OrderNo', 'PositionEffect', 'Price', 'Priceflag', 'QTY', 'SubAccount', 'Symbol', 'Tif', 'TradeServerReceiveTime', 'TimePeriod']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def Trade(*argv):
        name_list = ['Ibno', 'Account', 'BS', 'BS1', 'BS2', 'ClientOrderNo', 'DealTime', 'Exchange', 'ExchangeRate', 'Marketflag', 'OrderIP', 'OrderNo', \
            'PositionEffect', 'Price', 'Price1', 'Price2', 'Qty', 'Qty1', 'Qty2', 'SubAccount', 'Symbol', 'Symbol1', 'Symbol2', 'Tif', 'tradeNo', 'TimePeriod']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def QueryReport(*argv):
        name_list = ['Ibno', 'Account', 'AfterQty', 'BS', 'ClientOrdNo', 'ErrMsg', 'ErrorCode', 'Exchange', 'ExchangeRate', 'ExchangeServerReveiveTime', \
            'Marketflag', 'MatchQty', 'Orderfunc', 'OrderIP', 'OrderNo', 'PositionEffect', 'Price', 'Priceflag', 'QTY', 'SubAccount', 'Symbol', 'Tif', \
            'TradeServerReceiveTime', 'TimePeriod']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def QueryTrade(*argv):
        name_list = [ 'Ibno', 'Account', 'BS', 'BS1', 'BS2', 'ClientOrderNo', 'DealTime', 'Exchange', 'ExchangeRate', 'Marketflag', 'OrderIP', 'OrderNo', 'PositionEffect', \
            'Price', 'Price1', 'Price2', 'Priceflag', 'Qty', 'Qty1', 'Qty2', 'SubAccount', 'Symbol', 'Symbol1', 'Symbol2', 'Tif', 'tradeNo', 'TimePeriod']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def AccountData(Market, ibno, Account, subAccount = None):
        if (subAccount == None):
            print(Market + ":[" + ibno + "-" + Account + "]")
        else:
            print(Market + ":[" + ibno + "-" + Account + "-" + subAccount + "]")

    def Position(*argv):
        if (argv[-1] == "N"):
            print("無部位資料")
        else:
            name_list = ['Ibno', 'Account', 'SubAccount', 'BS', 'Symbol', 'Exchange_flag', 'ExchangeRate', 'Marketflag', 'B_AvgPrice', 'B_TotalQty', \
                'S_AvgPrice', 'S_TotalQty', 'Currency', 'Optionflag', 'YyyyMM', 'StrikePrice']
            data_list=[]
            for i in argv:
                data_list.append(i)
            for i in range(len(name_list)):
                print("{0} : {1}".format(name_list[i], data_list[i]))

    def Equity(*argv):
        name_list = [ "分公司", "帳號", "子帳號", "維持率", "帳戶權益", "今日存提款", "可用餘額", "平倉損益", "原始保証金", "維持保証金", "浮動損益", \
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

    def SeaReport(*argv):
        name_list = ['Ibno', 'Account', 'AfterQty', 'BeforeQty', 'BS', 'ClientOrdNo', 'ErrMsg', 'ErrorCode', 'Exchange', 'ExchangeRate', 'ExchangeServerReveiveTime', \
            'ExchangeServerReveiveTimeUTC', 'Marketflag', 'MatchQty', 'Orderfunc', 'OrderIP', 'OrderNo', 'PositionEffect', 'Price', 'PriceFraction', 'Priceflag', \
            'QTY', 'SubAccount', 'Symbol', 'Tif', 'TradeServerReceiveTime', 'TradeServerReceiveTimeUTC', 'StopPrice', 'StopPriceFraction', 'Ftf', 'GtdExpireday', \
            'MiniQty', 'Scf']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def SeaTrade(*argv):
        name_list = ['Ibno', 'Account', 'BS', 'BS1', 'BS2', 'ClientOrderNo', 'DealTime', 'DealTimeUTC', 'Exchange', 'ExchangeRate', 'Marketflag', 'OrderIP', 'OrderNo', \
            'PositionEffect', 'Price', 'Price1', 'Price2', 'Qty', 'Qty1', 'Qty2', 'SubAccount', 'Symbol', 'Symbol1', 'Symbol2', 'Tif', 'tradeNo', 'PriceFraction']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def QuerySeaReport(*argv):
        name_list = ['Ibno', 'Account', 'AfterQty', 'BeforeQty', 'BS', 'ClientOrdNo', 'ErrMsg', 'ErrorCode', 'Exchange', 'ExchangeRate', 'ExchangeServerReveiveTime', \
            'ExchangeServerReveiveTimeUTC', 'Marketflag', 'MatchQty', 'Orderfunc', 'OrderIP', 'OrderNo', 'PositionEffect', 'Price', 'PriceFraction', 'Priceflag', 'QTY', \
            'SubAccount', 'Symbol', 'Tif', 'TradeServerReceiveTime', 'TradeServerReceiveTimeUTC', 'StopPrice', 'StopPriceFraction', 'Ftf', 'GtdExpireday', 'MiniQty', 'Scf']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))

    def QuerySeaTrade(*argv):
        name_list = [ 'Ibno', 'Account', 'BS', 'BS1', 'BS2', 'ClientOrderNo', 'DealTime', 'DealTimeUTC', 'Exchange', 'ExchangeRate', 'Marketflag', 'OrderIP', 'OrderNo', \
            'PositionEffect', 'Price', 'Price1', 'Price2', 'Qty', 'Qty1', 'Qty2', 'SubAccount', 'Symbol', 'Symbol1', 'Symbol2', 'Tif', 'tradeNo', 'PriceFraction']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def OptionGroup(*argv):
        name_list = [ 'QueryFlag', 'Status', 'ErrorMessage', 'ClientOrderNo']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def OptionDisGroup(*argv):
        name_list = [ 'QueryFlag', 'Status', 'ErrorMessage', 'ClientOrderNo']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def OptionDisAllGroup(*argv):
        name_list = [ 'QueryFlag', 'Status', 'ErrorMessage', 'ClientOrderNo']
        data_list=[]
        for i in argv:
            data_list.append(i)
        for i in range(len(name_list)):
            print("{0} : {1}".format(name_list[i], data_list[i]))
    def OptionAllGroupTrial(*argv):
        name_list = ['QueryFlag', 'Ibno', 'Account', 'BS1', 'Symbol1', 'BS2', 'Symbol2', 'Qty', 'SpreadInitialMargin', 'SpreadMaintainMargin', 'Status', \
            'SumMarginReduceCurrency', 'SumInitialMarginReduce', 'SumMaintainMarginReduce', 'clientno']
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