import re
ReDan = "13502377825     =帝景湾维也纳北二门13号1003= 一个6斤左右熟的金枕榴莲（开肉送 拍视频） 20元百香果  转账   莉莉"
DingDan = ""
XiaDan = ""
CaoRe = ""

#正则表达式预处理
#预处理电话号码
SubPa= re.compile("(?<=\d{3})[ -]|\s")
#预处理收款方式
Gcash = re.compile(r"现金|收现转账都可以")
Gvip = re.compile(r"会员消费|电子卡消费")
Gtran = re.compile(r"转帐|已转账|已收现")
Gmon = re.compile(r"月底结算")
#获取电话号码
Phone = re.compile(r"[01]\d{10}[/]?(?<=[/])\d*|[01]\d{10}|(?<!\d)[2]\d{6}")
#获取收款方式
SkPa = re.compile(r"收现|转账|会员卡消费|月结")
#获取送货地址
AddressPa = re.compile(r"(?==).*(?<==)|自提")
#处理商品赘余信息
GoodsPa= re.compile(r"[ ，,。.]{2,}")
#获取时间
TimeDPa = re.compile(r"(明天|今天|[大]?后天[之以前后左右间]{0,2}[送到]{0,2})(?![吃可])")
TimeTPa = re.compile(r"早上|上午|下午|晚上|[今明][早晚][之以前后左右间]{0,2}[送到]{0,2}")
TimePa = re.compile(r"(?<![大小生熟满黄青绿硬软黑红好靓吃圆裂看身冷冻热])(([\d一二三四五六七八九十两现][\d一二在]?点[半多]{0,2}[之以前后左右间]{0,2}[送到]{0,2}[,.，。 ]?){1,2})")
#获取操作人
Czuo = re.compile(r"(陈)|(莉莉)|(秋)")

def ChuDan(ReDan,DingDan,XiaDan,Goods,Money,CaoRe):
    #预处理电话的分隔符
    Substr = SubPa.sub("",ReDan)
    #匹配电话号码
    PhoneRe = Phone.search(Substr)
    #没有匹配到电话号码
    try:
        PhoneNum =PhoneRe.group()
        Phonestart = PhoneRe.start()
        Phonend = PhoneRe.end()
        First = Substr[:Phonestart]+Substr[Phonend:]
    except AttributeError:
        PhoneNum = ""
        First = Substr

    #匹配送货地址
    AddressRe = AddressPa.search(First)
    try:
        Address = AddressRe.group()
        Addresstart = AddressRe.start()
        Addressend = AddressRe.end()
        Second = First[:Addresstart]+First[Addressend:]
    except AttributeError:
        Address = ""
        Second = First
        
    #收款方式预处理
    Second = Gcash.sub("收现",Second)
    Second = Gvip.sub("会员卡消费",Second)
    Second = Gtran.sub("转账",Second)
    Second = Gmon.sub("月结",Second)
    #匹配收款方式
    SkRes = SkPa.search(Second)
    try:
        SkRe = SkRes.group()
        Skstart =SkRes.start()
        Skend = SkRes.end()
    except AttributeError:
        SkRe = "收现"
        Skend = 0
    if Skend:
        Second = Second[:Skstart] + Second[Skend:]
    if CaoRe == "":
        #匹配操作人
        CaoRes = Czuo.search(Second)
        try:
            CaoRe = CaoRes.group()
            Caostart = CaoRes.start()
            Caoend = CaoRes.end()
        except AttributeError:
            CaoRe = ""
            Caoend = 0
        if Caoend:
            Second = Second[:Caostart] + Second[Caoend:]
    if "++" in Goods:
        Second = Second + Goods[1:]
    elif Goods:
        Second = Goods
    if XiaDan == "商城":
        SkRe = "商城转账"
    if DingDan[:2] == "充值" or DingDan[:2] == "售后" or DingDan[:2] == "活动":
        SkRe = "转账"
   # return ("%s\t%s\t%s\t%s\t%s\t%s\t%s\t\t\t%s") % (DingDan,XiaDan,PhoneNum,Address[1:-1],Second,Money,SkRe,CaoRe)
  #匹配订单时间
   #日期段
    TimeDate = TimeDateAdd = ""
    DateTime = TimeDPa.search(Second)
    if DateTime:
        TimeDate = TimeDate + DateTime.group()
        DTS = DateTime.start()
        DTE = DateTime.end()
        Second = Second[:DTS] + Second[DTE:]
    #时间段
    DateTime = TimeTPa.search(Second)
    if DateTime:
        TimeDate = TimeDate + DateTime.group()
        DTS = DateTime.start()
        DTE = DateTime.end()
        Second = Second[:DTS] + Second[DTE:]
    #具体时间段
    DateTime = TimePa.search(Second)
    if DateTime:
        TimeDate = TimeDate + DateTime.group()
        DTS = DateTime.start()
        DTE = DateTime.end()
        Second = Second[:DTS] + Second[DTE:]
    Second = GoodsPa.sub("",Second)
    if TimeDate:
        TimeDateAdd = "【"+ TimeDate +"】"
    
    if Address == "自提":
        return (DingDan,XiaDan,PhoneNum,TimeDateAdd+Address,Second,Money,SkRe,"","",CaoRe,"",TimeDate)
    else:
        return (DingDan,XiaDan,PhoneNum,TimeDateAdd+Address[1:-1],Second,Money,SkRe,"","",CaoRe,"",TimeDate)


if __name__ == '__main__':
    ReDan = "18日上午9点到店自提，13502339444，一个好一点的果篮，蜜瓜，奇异果，莲雾，提子，蓝莓，车厘子，红火龙，红心芭乐，释迦等，会员消费"
    DingDan = ""
    XiaDan = ""
    Goods = ""
    Money = 100
    CaoRe = ""
    ChuDan(ReDan,DingDan,XiaDan,Goods,Money,CaoRe)

