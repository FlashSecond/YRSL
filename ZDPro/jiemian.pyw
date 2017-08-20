from tkinter import *
import DataFile
import datetime
import XiaDan
import fileR
import send
import tkinter.messagebox

root = Tk()
#--------------------------------操作函数------------------------------
#订单显示函数
def DingD():
    ShowDan.config(text = DataFile.DanMode[DinType.get()])
def XiaD():
    ShowXia.config(text = DataFile.XiaPer[XiaOption.get()])
#订单和下单人取消选择
def DXdel():
    try:
        DanRadio[DinType.get()].deselect()
        ShowDan.config(text = "")
    except:
        pass
    try:
        XiaRadio[XiaOption.get()].deselect()
        ShowXia.config(text = "")
    except:
        pass
#列表添加订单操作函数
def Listoper(DateNow,DanNum):
    ShowNum.delete(0,END)
    ShowNum.insert(0,DanNum)
    Listxt = ListDanShow.get(0,END)
    DinText.delete(0,END)
    ListDanShow.yview(MOVETO,1.0)
    fileR.Wrdata(DateNow,int(ShowNum.get()),int(ExtraNum.get()),DanNowDateNum.get())#函数
    fileR.FileW(Listxt,DateNow)#函数
#复制
def Textcopy(FinText):
    try:
        root.clipboard_clear()
    except _tkinter.TclError:
        pass
    try:
        root.clipboard_append(FinText)
    except TypeError:
        pass
#刷新订单列表
def ShowListTBtnEvent():
    DateNow = datetime.date.today() + datetime.timedelta(int(DanNowDateNum.get()))
    ListR = fileR.FileR(DateNow)#函数
    if int(ListDanShow.size()) != int(len(ListR)):
        DXdel()#函数
        DanNum = len(ListR) + int(ExtraNum.get()) + 1
        ShowNum.delete(0,END)
        ShowNum.insert(0,DanNum) 
        ListDanShow.delete(0,END)
        for i in ListR:
            ListDanShow.insert(END,i)
        ListDanShow.yview(MOVETO,1.0)
    DanInfo = fileR.Redata(DateNow,int(ShowNum.get()),int(ExtraNum.get()),DanNowDateNum.get())#函数
    if DanInfo:
        ShowNum.delete(0,END)
        ShowNum.insert(0,int(DanInfo[1]))
        ExtraNum.delete(0,END)
        ExtraNum.insert(0,int(DanInfo[2]))
#订单信息审核
def CheckDanInf(ReText):
    if ReText[2]:
        ShowPhoneNum['text'] =  ReText[2]
    else:
         tkinter.messagebox.showerror("温馨提示","客户手机有问题,请注意！")
    ShowGoods.delete(0,END)
    ShowMoney.delete(0,END)
     
#处理文本按钮事件
def WorkBtnEvent():
    ShowListTBtnEvent() #函数
    try:
        if DinText.get():
            if DataFile.XiaPer[XiaOption.get()] in DataFile.CaoPer.keys():
                    CaoRe=DataFile.CaoPer[DataFile.XiaPer[XiaOption.get()]]
            else:
                    CaoRe = ""
        if ShowDan["text"] != "" and ShowXia["text"] != "":
            if 2 == DinText.get().count("=") or "自提" in DinText.get() :
                DateNow = datetime.date.today() + datetime.timedelta(int(DanNowDateNum.get()))
                ReText = XiaDan.ChuDan(DinText.get(),\
                                       ShowDan["text"]+ShowNum.get(),\
                                       ShowXia["text"],\
                                       ShowGoods.get(),\
                                       ShowMoney.get(),\
                                       CaoRe)
                CheckDanInf(ReText) #函数
                FinText = ("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s") % ReText
                Textcopy(FinText)
                ListDanShow.insert(END,FinText)
                DanNum = int(ShowNum.get())  + 1
                send.sendinfo()
                Listoper(DateNow,DanNum)#函数
                DXdel()#函数
                
        else:
            tkinter.messagebox.showerror("温馨提示","请选择 订单类型  和  下单人")
    except:
            tkinter.messagebox.showerror("温馨提示","请选择 订单类型  和  下单人")
#删除列表文本按钮
def ListDelBtnEvent():
    DateNow = datetime.date.today() + datetime.timedelta(int(DanNowDateNum.get()))
    if "--" in DinText.get():
        ListDanShow.delete(ListDanShow.curselection())
        Listxt = ListDanShow.get(0,END)
        DinText.delete(0,END)
        DanNum = int(ShowNum.get())  - 1
        ShowNum.delete(0,END)
        ShowNum.insert(0,DanNum)
        fileR.Wrdata(DateNow,int(ShowNum.get()),int(ExtraNum.get()),DanNowDateNum.get())#函数
        fileR.FileW(Listxt,DateNow)#函数
#添加列表订单按钮
def ListPlusBtnEvent():
    DateNow = datetime.date.today() + datetime.timedelta(int(DanNowDateNum.get()))
    ShowListTBtnEvent() #函数
    DanNum = int(ShowNum.get())
    Textcopy(DinText.get()) #函数
    send.sendinfo() #函数
    ListnTxt = DinText.get().split('\n')
    for T in ListnTxt:
        if 3 < T.count('\t'):
            ListDanShow.insert(END,T)
            DanNum = int(ShowNum.get())  + 1
            ShowNum.delete(0,END)
            ShowNum.insert(0,DanNum)
    Listoper(DateNow,DanNum)#函数
    

#插入文本地址分隔
def DinTextIn(event):
    DinText.icursor(0)
    DinText.xview_moveto(0)
#做单天数
def PlusDate():
    DanNowDate["text"] = datetime.date.today() + datetime.timedelta(int(DanNowDateNum.get()))
#订单数扩充
def PlusDanNum():
    SN = int(ListDanShow.size()) + 1
    ShowNum.delete(0,END)
    ShowNum.insert(0,SN + int(ExtraNum.get()))
#界面收拾
def RootO():
    root.withdraw()
    foot.deiconify()
def FootO():
    foot.withdraw()
    root.deiconify()
def footdel():
    root.destroy()
#--------------------------------------菜单函数------------------------------------
def Dantype():
    Mtype = Toplevel()
    Mtype.title("订单类型栏")
    Message(Mtype,text=DataFile.mtype,width = 800).pack()
def Danxia():
    Mxia = Toplevel()
    Mxia.title("下单人选择栏")
    Message(Mxia,text=DataFile.Mxia,width = 800).pack()
def Danatt():
    Matt = Toplevel()
    Matt.title("订单状态栏")
    Message(Matt,text=DataFile.Matt,width = 800).pack()
def Dantxt():
    Mtxt = Toplevel()
    Mtxt.title("订单内容")
    Message(Mtxt,text=DataFile.Mtxt,width = 800).pack()
def Danbc():
    Mbc = Toplevel()
    Mbc.title("订单补充内容栏")
    Message(Mbc,text=DataFile.Mbc,width = 800).pack()
def Danchk():
    Mchk = Toplevel()
    Mchk.title("订单处理按钮")
    Message(Mchk,text=DataFile.Mchk,width = 800).pack()
def Daninf():
    Minf = Toplevel()
    Minf.title("订单处理信息栏")
    Message(Minf,text=DataFile.Minf,width = 800).pack()
def Danlit():
    Mlit = Toplevel()
    Mlit.title("订单内容显示列表")
    Message(Mlit,text=DataFile.Mlit,width = 800).pack()
#-------------------------------------做单界面-----------------------------------
if __name__ == '__main__':
    
    root.title("野人森林做单工具")
    root.minsize(580,900)
    #root.maxsize(580,900)
    root.geometry(newGeometry = '%sx%s+%s+%s' % (root.winfo_x(), root.winfo_y(),\
                                                    int(root.winfo_screenwidth()-650), 0))
    root.wm_attributes('-topmost',1)
    
    foot = Toplevel()
    foot.minsize(30,50)
    foot.wm_attributes('-topmost',1)
    frame = Button(foot,width=10,height =10,text = "让我回来了！",command = FootO)
    foot.geometry(newGeometry = '%sx%s+%s+%s' % (root.winfo_x(), root.winfo_y(),\
                                                    int(root.winfo_screenwidth()-200), root.winfo_screenheight() - 150))
    foot.withdraw()
    foot.protocol(name = "WM_DELETE_WINDOW",func = footdel)
    frame.pack()
#菜单框架--------------------------------------------------
    DanMenu = Menu(root)
    Teach = Menu(DanMenu,tearoff = False)
    Teach.add_command(label = "订单类型栏",command = Dantype)
    Teach.add_command(label = "下单人选择栏",command = Danxia)
    Teach.add_command(label = "订单状态栏",command = Danatt)
    Teach.add_command(label = "订单内容",command = Dantxt)
    Teach.add_command(label = "订单补充内容栏",command = Danbc)
    Teach.add_command(label = "订单处理按钮",command = Danchk)
    Teach.add_command(label = "订单处理信息栏",command = Daninf)
    Teach.add_command(label = "订单内容显示列表",command = Danlit)
    DanMenu.add_cascade(label = "说明",menu = Teach)
    root.config(menu = DanMenu)
#订单类型框架---------------------------------------------
    DanModeF = LabelFrame(root,text="订单类型栏",font = ("黑体","13"),padx=1,pady=1)
    DanModeF.pack()
        #生成订单类型选项
    DanModeG = []
    DanRadio = []
    DinType= IntVar()
    for D,DI,DD in zip(DataFile.DanMode,DataFile.DanModeID,DataFile.DanModeImg):
        DI = PhotoImage(file="img\\" + DD)
        DanModeG.append(DI)
        DT = Radiobutton(DanModeF,text=D,image = DanModeG[-1],variable=DinType,value=DataFile.DanMode.index(D),\
                         activebackground = "blue",selectcolor = "black",indicatoron = False,command = DingD)
        DanRadio.append(DT)
        DanRadio[0].deselect()
        DT.grid(row=1,column =DataFile.DanMode.index(D))
    DanRadio[0].deselect()
#下单人名称框架----------------------------------------------
    XiaPerF = LabelFrame(root,text="下单人选择栏",font = ("黑体","13"),padx=1,pady=1)
    XiaPerF.pack()
        #生成下单人选项
    XiaPerG = []
    XiaRadio = []
    XiaOption = IntVar()
    RO = 1
    for O,OI,OD in zip(DataFile.XiaPer,DataFile.XiaPerID,DataFile.XiaPerImg):
        OI = PhotoImage(file="img\\" + OD)
        XiaPerG.append(OI)
        OP = Radiobutton(XiaPerF,text=O,image= XiaPerG[-1],variable=XiaOption,value=DataFile.XiaPer.index(O),\
                         activebackground = "blue",selectcolor = "black",indicatoron = False,command = XiaD)
        XiaRadio.append(OP)
        OP.grid(row = RO + DataFile.XiaPer.index(O) // 9 ,\
                column =(DataFile.XiaPer.index(O)  - 9 *(DataFile.XiaPer.index(O) // 9)))
    XiaRadio[0].deselect()
#订单状态显示栏框架------------------------------------------
    DanModeL = LabelFrame(root,text="订单状态栏",font = ("黑体","13"),padx=1,pady=1)
    DanModeL.pack()
        #显示选择订单类似
    ShowDan =Label(DanModeL ,width = 5,height = 1,text = "")
    ShowDan.grid(row=1,column =1)
        #显示订单号
    ShowNum =Spinbox(DanModeL,width = 4,buttonbackground = "pink",font= ("雅黑","12"),\
                     justify = CENTER,from_ = 1,to = 9999)
    ShowNum.grid(row=1,column =2)
        #添加单数
    ExtraDan =Label(DanModeL ,width = 2,height = 1,text = "<+")
    ExtraDan.grid(row=1,column =3)
    ExtraNum =Spinbox(DanModeL,width = 4,buttonbackground = "pink",font= ("雅黑","12"),\
                      justify = CENTER,from_ = -9999,to = 9999,command = PlusDanNum)
    ExtraNum.delete(0,END)
    ExtraNum.insert(0,0)
    ExtraNum.grid(row=1,column =4)
        #显示下单人状态
    ShowXia =Label(DanModeL ,width = 5,height = 1,text = "")
    ShowXia.grid(row=1,column =5)
        #显示做单日期
    DanNowDateL =Label(DanModeL ,width = 7,height = 1,text = "做单日期>")
    DanNowDateL.grid(row=1,column =6)
    DanNowDate =Label(DanModeL ,width = 9,height = 1,text = datetime.date.today())
    DanNowDate.grid(row=1,column =7)
        #添加天数
    EDanNowDate =Label(DanModeL ,width = 2,height = 1,text = "<+")
    EDanNowDate.grid(row=1,column =8)
    DanNowDateNum =Spinbox(DanModeL,width = 4,buttonbackground = "pink",font= ("雅黑","12"),justify = CENTER,\
                           from_ = 0,to = 99,command = PlusDate)
    DanNowDateNum.grid(row=1,column =9)

#待处理订单内容框架---------------------------------------------
    DinTextF = LabelFrame(root,text="订单内容:",font = ("黑体","13"),padx=1,pady=1)
    DinTextF.pack()
        #水平滚动条
    DinScb = Scrollbar(DinTextF,orient = HORIZONTAL)
    DinScb.pack(side=BOTTOM,fill = X)
        #文本输入框
    DinText = Entry(DinTextF,width=77,xscrollcommand = DinScb.set)
    DinText.bind("<Control-KeyRelease-v>",DinTextIn)
    DinText.bind("<Control-KeyRelease-V>",DinTextIn)
    DinText.icursor(0)
    DinText.pack(fill=BOTH)
        #输入框与水平滚动条关联
    DinScb.config(command=DinText.xview)
#订单补充内容栏---------------------------------------------
    DinTextB = LabelFrame(root,text="订单补充内容:",font = ("黑体","13"),padx=1,pady=1)
    DinTextB.pack()
            #补充送货商品
    ShowGoodsL =Label(DinTextB ,width = 7,height = 2,text = "补加商品:")
    ShowGoodsL.grid(row=1,column =1,sticky = W)
    ShowGoods=Entry(DinTextB ,width = 69)
    ShowGoods.grid(row=1,column =2,sticky = W)
        #补充金额
    ShowMoneyL =Label(DinTextB ,width = 7,height = 2,text = "所需金额:")
    ShowMoneyL.grid(row=2,column =1)
    ShowMoney=Entry(DinTextB ,width = 10)
    ShowMoney.grid(row=2,column =2,sticky = W)
#订单内容处理按钮框架----------------------------------------------
    DinBTNF = LabelFrame(root,text = "订单处理按钮组",font = ("黑体","13"),padx = 1,pady =1)
    DinBTNF.pack()
        #订单处理按钮
    WorkBtn = Button(DinBTNF,text="订单内容处理",command = WorkBtnEvent)
    WorkBtn .grid(row = 1,column = 1)
        #显示列表订单状态
    ShowListTBtn = Button(DinBTNF,text="刷新列表订单",command = ShowListTBtnEvent)
    ShowListTBtn .grid(row = 1,column = 2)
        #添加列表订单
    ListplusBtn = Button(DinBTNF,text="添加列表订单",command = ListPlusBtnEvent)
    ListplusBtn.grid(row = 1,column = 3)
        #列表内容删除按钮
    ListchangeBtn = Button(DinBTNF,text="删除列表订单",command = ListDelBtnEvent)
    ListchangeBtn.grid(row = 1,column = 4)
    #收起按钮
    BackBtn = Button(DinBTNF,text = "收起界面",command = RootO)
    BackBtn.grid(row = 1,column = 5)
#订单处理信息框架------------------------------------------------
    DanModeC = LabelFrame(root,text="订单处理信息栏",font = ("黑体","13"),padx=1,pady=1)
    DanModeC.pack()
        #显示手机号码
    ShowPhoneL =Label(DanModeC ,width = 10,height = 2,text = "客户手机:")
    ShowPhoneL.grid(row=1,column =1)
    ShowPhoneNum=Label(DanModeC ,width = 45,height = 1,text ="")
    ShowPhoneNum.grid(row=1,column =2,columnspan = 5,sticky = W)
#列表订单内容显示框架---------------------------------------------------
    ListDanF = LabelFrame(root,text="订单内容显示:",font = ("黑体","13"),padx=1,pady=1)
    ListDanF.pack()
        #垂直滚动条
    ListScbV = Scrollbar(ListDanF)
    ListScbV.pack(side=RIGHT,fill=Y)
        #水平滚动条
    ListScbH = Scrollbar(ListDanF,orient = HORIZONTAL)
    ListScbH.pack(side=BOTTOM,fill=X)
        #列表
    ListDanShow = Listbox(ListDanF,xscrollcommand = ListScbH.set,yscrollcommand = ListScbV.set,\
                          height = 5,width=50,selectmode = EXTENDED,font=("雅黑","15"))
    ListDanShow.pack(padx=10,fill=BOTH)
        #列表与滚动条关联
    ListScbV.config(command=ListDanShow.yview)
    ListScbH.config(command=ListDanShow.xview)
    
    mainloop()
