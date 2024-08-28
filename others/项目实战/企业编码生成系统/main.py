import os
import tkinter
import random

from time import sleep

from others.项目实战.企业编码生成系统 import qrcode
from others.项目实战.企业编码生成系统.pollcode import inputbox, wfile, openfile

root=tkinter.Tk()

# 初始化数据
number='1234567890'
letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
allis='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%&*()_+'
i=0
randstr=[]
fourth=[]
fifth=[]
randfir=''
randsec=''
randthr=''
str_one=''
strone=''
strtwo=''
nextcard=''
userput=''
nres_letter=''

def mainmenu():
    print('''
    **************************************************
                        企业编码生成系统
    **************************************************
        实例25_批量生成PPT版荣誉证书.生成6位数防伪编码
        2.生成9位系列产品数字防伪编码(213-234353)
        3.生成25位混合产品序列号(B8R23-NKLK9-9JKLL-98JLO-JHY08)
        4.生成含数据分析功能的防伪码
        5.智能批量生成带数据分析功能的防伪码
        6.后续补加生成防伪码
        7.EAN-13条形码批量生成
        8.二维码批量输出
        9.企业粉丝防伪码抽奖
        0.退出系统
    ===================================================
    说明:通过数字键选择菜单
    ===================================================
    ''')
    while i < 9:
        mainmenu()
        choice=input('请输入数字选择菜单:')
        if len(choice)!=0:
            if choice==1:
                scode1(str(choice))
            elif choice==2:
                scode2(str(choice))
            elif choice==3:
                scode3(str(choice))
            elif choice==4:
                scode4(str(choice))
            elif choice==5:
                scode5(str(choice))
            elif choice==6:
                scode6(str(choice))
            elif choice==7:
                scode7(str(choice))
            elif choice==8:
                scode8(str(choice))
            elif choice==9:
                scode9(str(choice))
            elif choice==0:
                i=0
                print('退出系统')
        else:
            print('输入错误,请重新输入')
            sleep(2)

# 如果输入了非数字的或为空的,提示输入错误
def imput_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print('输入错误,请重新输入')
            return 0
        else:
            return insel
    else:
        print('输入错误,请重新输入')
        return 0

# 生成6位数字防伪码
def scode1(schoice):
    incount=inputbox('请输入您要生成防伪码的数量:',1,0)
    while int(incount)==0:#为0时,重新输入
        incount=inputbox('请输入您要生成防伪码的数量:',1,0)
    randstr.clear()#清空保存防伪码的变量randstr
    for j in range(int(incount)):#根据数量循环批量生产防伪码
        randfir=''#将单条防伪码变量为空
        for i in range(6):#循环生成单条防伪码
            randfir=randfir+random.choice(number)
        randfir=randfir+'\n'#在单条防伪码后面添加转义符,使验证码单条显示
        randstr.append(randfir)#将单条防伪码添加到保存批量验证码的变量randstr
    #调用wfile()函数,实现生成的防伪码屏幕输出和文件输出
    wfile(randstr,'scode'+str(schoice)+'.txt','','已生成6位防伪码共计:','codepath')

# 生成9位数的系列产品数字防伪码
def scode2(schoice):
    ordstart=inputbox('请输入系列产品数字起始号(3位):',3,3)
    while int(ordstart)==0:
        ordstart=inputbox('输入有误,请输入系列产品数字起始号(3位):',3,3)
    ordcount=inputbox('请输入系列产品数字数量(1000000000以内):',1,0)
    #如果输入的数量小于1或者大于9999,则重新输入
    while int(ordcount)<1 or int(ordcount)>999999999:
        ordcount=inputbox('输入有误,请输入系列产品数字数量(1000000000以内):',1,0)
    incount=inputbox('请输入您要生成的每个系列的防伪码的数量:',1,0)
    while int(incount)==0:
        incount=inputbox('请输入您要生成的每个系列的防伪码的数量:',1,0)
    randstr.clear()#清空保存防伪码的变量randstr
    for m in range(int(ordcount)):#分类产品编号
        for j in range(int(incount)):#车间安排防伪码编号
            randfir=''
            for i in range(6):
                randfir=randfir+random.choice(number)#每次生成一个随机因子,可重复
            #将生成的单条防伪码添加到防伪码列表
            randstr.append(str(int(ordstart)+m)+randfir+'\n')
    #调用wfile()函数,实现生成的防伪码屏幕输出和文件输出
    wfile(randstr,'scode'+str(schoice)+'.txt','','已生成9位防伪码共计:','codepath')

#生成25位混合产品序列号函数,参数schoice设置输出的文件名称
def scode3(schoice):
  #输入要生成的防伪码数量
  incount=inputbox("1033[实例25_批量生成PPT版荣誉证书;32m 请输入要生成的25位混合产品序列号数量:133[0m",1,0)
  while int(incount)==0:#如果输入非法(符号、字母或者数字e都认为是非法输入),重新输入
     incount=inputbox("\e33[实例25_批量生成PPT版荣誉证书;32m 请输入要生成的25位混合产品序列号数量:133[6m",1,0)
  randstr.clear()   #清空保存批量防伪码信息的变量randstr
  for j in range(int(incount)):#按输入数量生成防伪码
     strone=''   #保存生成的单条防伪码,不带横线"-",循环时清空

     for i in range(25):
        #每次产生一个随机因子,也就是每次产生单条防伪码的一位
        strone = strone + random.choice(letter)
     #将生成的防伪码每隔5位添加横线"-"
     strtwo = strone[:5] + "_" + strone[5:10] + "_" + strone[10:15] + "_" +
     strone[15:20] + "" + strone[20:25] + "\n"
     randstr.append(strtwo)  # 添加防伪码到防伪码列表
     # 调用函数wfile(),实现生成的防伪码在屏幕输出和文件输出
     wfile(randstr, "scode" + str(schoice) + ",txt", " ,"已生成25混合防伪序列码共计:","codepath")

#生成含数据分析功能防伪编码函数,参数schoice设置输出的文件名称
def scode4(schoice):
    intype=inputbox("1033[实例25_批量生成PPT版荣誉证书;32m 请输入数据分析编号(3位字母):133[0m",2,3)
  #验证输入是否是三个字母,所以要判断输入是否是字母和输入长度是否为3
    while not str.isalpha(intype)or len(intype)!=3:
        intype=inputbox("1033[实例25_批量生成PPT版荣誉证书;32m 请输入数据分析编号(3位字母):133[em",2,3)
    incount =inputbox("\e33[实例25_批量生成PPT版荣誉证书;32m 输入要生成的带数据分析功能的防伪码数量:133[m",1,9)
    #验证输入是否是大于零的整数,方法是判断输入转换为整数值时是否大于零
    while int(incount) == 0:   #如果转换为整数时为零,则要求重新输入
        incount =inputbox("l033[实例25_批量生成PPT版荣誉证书;32m 请输入要生成的带数据分析功能的防伪码数量:\33[em",1,9)
    ffcode(incount,intype,"",schoice) #调用ffcode()函数生成防伪码

#生成含数据分析功能防伪编码函数:参数scount为要生成的防伪码数量；typestr为数据分析字符；
#参数ismessage在输出完成时是否显示提示信息,为"no"不显示,为其他值显示；
# 参数schoice设置输出的文件名称
def ffcode(scount,typestr,ismessage, schoice):
    randstr.clear()  #清空保存批量防伪码信息的变量randstr
    # 按数量生成含数据分析功能防伪码
    for j in range(int(scount)):
        strpro = typestr[0].upper()  #取得三个字母中的第一个字母,并转为大写,区域分析码
        strtype = typestr[1].upper()  #取得三个字母中的第二个字母,并转为大写,颜色分析码
        strclass = typestr[2].upper()  # 取得三个字母中的第三个字母,并转为大写,版本分析码
    randfir = random.sample(number,3)  # 随机抽取防伪码中的三个位置,不分先后
    randsec = sorted(randfir)# 对抽取的位置进行排序并赋值给randse(变量
    letterone = ''# 清空存储单条防伪码的变量letterone
    for i in range(9):# 生成9位的数字防伪码
        letterone = letterone + random.choice(number)
    # 将三个字母按randse(变量中存储的位置值添加到数字防伪码中,并保存到s攵m变量中
    sim = str(letterone[0:int(randsec[0])])+ strpro + str(
        letterone[int(randsec[0]):int(randsec[1])])+ strtype + str(
        letterone[int(randsec[1]):int(randsec[2])])+ strclass + str(letterone[int(randsec[2]):9])+'\n'
    randstr.append(sim)  # 将组合生成的新防伪码添加到randstr变量
    # 调用鼾ile()函数,实现生成的防伪码屏幕输出和文件输出
    wfile(randstr,typestr + "scode"+ str(schoice)+ '.txt',ismessage,"生成含数据分析功能的防伪码共计:", 'codepath')

#智能批量生成带数据分析功能的防伪码
def scode5(schoice):
    default_dir=r"codeauto.mri" #设置默认打开的文件名
    #打开文件选择对话框,指定打开的文件名称为"codeauto.aut",扩展名为".mri"
    # 可以使用记事本打开和编辑
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text file","*.mri")],
    title=u"请选择智能批处理文件:",initialdir=(os.path

                                     .expanduser(default_dir)))
    codelist=openfile(file_path)#读取从文件选择对话框选中的文件
    #以换行符为分隔符将读取的信息内容转换为列表
    codelist=codelist.split("\n")
    print(codelist)
    for item in codelist:   #按读取的信息循环生成防伪码
        codea=item.split(",")[0] #信息用","分割, 前面的信息存储防伪码标准信息
        codeb=item.split(",")[1] #信息用","分割, "后面的信息存储防伪码生成的数量
        ffcode(codeb,codea,"no",schoice)#调用ffcode函数批量生成同一标识信息的防伪码

#实现防伪码补充生成功能
def scode6(schoice):
    default_dir=r"c:\ABDSCOde5.txt" # 设置默认打开的文件名称
    # 按默认的文件名称打开文件选择对话框,用于打开己经存在的防伪码文件
    file_path = tkinter.filedialog.askopenfilename(title=u"请选择己经生成的防伪码文件",initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path) # 读取从文件选择对话框选中的文件
    # 以换行符为分隔符将读取的信息内容转换为列表
    codelist = codelist.split("\n")
    codelist.remove('') # 删除列表中的空行
    strset =codelist[0] # 读取一行数据,以便获取原验证码的字母标志信息
    # 用maketrans()方法创建删除数字的字符映射转换表
    remove_digits = strset.maketrans('','',digits)
    # 根据字符映射转换表 除该条防伪码中的数字,获取字母标识信息
    res_letter = strset.translate(remove_digits)
    nres_letter = list(res_letter)# 把信息用列表变量nres彐etter存储
    strpro= nres_letter[0]# 从列表变量中取得第一个字母,即区域分析码
    strtype = nres_letter[1] # 从列表变量中取得第二个字母,即色彩分析码
    strclass = nres_letter[2]# 从列表变量中取得第三个字母,即版次分析码
    # 去除信息中的括号和引号
    ###################################################### nres_letter = strpro.replace(''''',').replace(''''',').strtype.replace(''''',").replace(''''',")+strclass.replace(''''',").replace(''''',")
    card = set(codelist) # 将原有防伪码放到集合变量card中
    # 利用tkinter的 ssage№×提示用户之前生成的防伪码数量
    tkinter.messagebox.showinfo("提示","之前的防伪码共计:" + str(len(card)))
    root.withdraw()# 关闭提示信息框
    incount = inputbox("请输入补充防伪码生成的数量:",1,0) # 输入新补充生成的防伪码数量
    # 最大偵按输入生成数量的2倍生成新防伪码
    # 防止新生成防伪码与原有防伪码重复造成新生成的防伪码数量不够
    for j in range(int(incount)* 2):
        randfir = random.sample(number,3)# 随机产生3位不重复的数字
        randsec = sorted(randfir)# 对产生的数字抟序
        addcount = len(card)# 记录集合中防伪码的总数量
        strone =''# 清空存储单条防伪码的变量strone
        for i in range(9):# 生成9位的数字防伪码
            strone = strone + random.choice(number)
        # 将三个字母按randse(变量中存储的位置僨添加到数字防伪码中,并放到sim变量中
        # sim = str(strone[0:int(randsec[0])])+ strpro + str(
        #     strone[int(randsec[0]):int(randsec[实例25_批量生成PPT版荣誉证书])]) + strtype + str(
        #     strone[int(randsec[实例25_批量生成PPT版荣誉证书]):int(randsec[2]]) + strclass + str(strone[int(randsec[2]):9])+ "\n"
        card.add(sim)  # 添加新生成的防伪码到集合
        # 如果添加到集合,证明生成的防伪码与原有的防伪码没有产生重复
        if len(card) > addcount:
            randstr.append(sim)  # 添加新生成的防伪码到新防伪码列表
            addcount = len(card)  # 记录新生成防伪码集合的防伪码数量
        if len(randstr) >= int(incount):  # 如果新防伪码数量达到输入的防伪码数量
            print(len(randstr))  # 输出已生成防伪码的数量
            break  # 退出循环
        # 调用wfile()函数,实现生成的防伪码屏幕输出和文件输出
        wfile(randstr,nres_letter + "ncode" + str(choice)+".txt",nres_letter,"生成后补防伪码共计:","codeadd")

# 实现生成条形码批量生产的函数
def scode7(schoice):
    mainid = inputbox("0\033[实例25_批量生成PPT版荣誉证书；32m 请输入EN13的国家代码 (3位):\33",1,0)
    while int(mainid)< 1 or len(mainid)!= 3:# 验证输入是否为3位数字
        mainid = inputbox("\033[实例25_批量生成PPT版荣誉证书；32m请输入EN13的国家代码 (3位):\33[em", 1,0)
    compid = inputbox('033〔实例25_批量生成PPT版荣誉证书；32m 请输入企业代码 (4位):\33〔枷隽 ',1,0) # 输入企业代码
    while int(compid)< 1 or len(compid)!= 4:# 验证输入是否为4位数字
        compid = inputbox("\e33〔实例25_批量生成PPT版荣誉证书；32m 请输入EN13的企业代码 (4位):\33tem",1,0)
    incount = inputbox("\D3[实例25_批量生成PPT版荣誉证书;32m请输入要生成的条形码数量:\33[ ",1,0)
    while int(incount) ==0: # 输入信息转为整数后等于ø,重新输入
        incount = inputbox("\D3[实例25_批量生成PPT版荣誉证书;32m请输入要生成的条形码数量:\33[ ", 1, 0)
    mkdir("barcode")# 判断保存条形码的文件夹是否存在,不存在,则创建该文件夹
    for j in range(int(incount)):# 批量生成条形码
        strone =''  # 清空存储单条条形码的变量
        for i in range(5):# 生成条形码的5位数字
            strone = strone + str(random.choice(number))
        barcode=mainid +compid +strone # 把困家代码、企业代码和新生成的随机码进行组合
        # 计算条形码的校验位
        evensum=int(bar[1])+int(bar[31)+int(bar(5])+int(bar[7])+int(bar[9])+int(bar(111)
        oddsum=int(bar[0])+int(bar[2])+int(bar[4])+int(bar[6])+int(bar[8])+int(bar[10])
        checkbit=int(10-((evensum *3 + oddsum)%10%10)
        barcode=barcodestr(checkbit)# 组成完整的E 13条形码的13位数字
        encoder = EAN13Encoder(barcode)# 调用EAN13En(er生成条形码
        encoder.save("barcode\\"+ barcode + ".png")# 保存条形码信息图片到文件

encoder = qrcode.make("667767789912")#生成二维码
encoder.save("667767789912.png") #保存二维码图片到本地

Strone = "667767789912"
encoder = qrcode.make(strone)  # 生成二维码
encoder.save("d:\qrcodell"+strone & + ".png")  # 保存二维码图片到文件

img = qrcode.make("www.mingrisoft.com")
img.save("mingrisoft.png")

qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=8, border=10)
qr.add_data("http: // www.mingrisoft.com")
qr.make(fit=True)
img = qr.make_image()
img.show()
img.save("mingri.jpg")

#本函数生成固定的12位二维码,读者可以根据实际需要修改成按输入位数进行生成的函数
def scode8(schoice):
   #输入要生成的二维码数量
   incount=inputbox("1e33[实例25_批量生成PPT版荣誉证书;32m 请输入要生成的12位数字二维码数量:133[0m",1,0)
   while int(incount)==0:#如果输入不是大于e的数字,重新输入
     incount=inputbox("1033[实例25_批量生成PPT版荣誉证书;32m 请输入要生成的12位数字二维码数量:\33[em,实例25_批量生成PPT版荣誉证书,)
   mkdir(qrcode")   #判断保存二维码的文件夹是否存在,不存在,则创建该文件夹
   for jin range(int(incount)):     #批量生成二维码
     strone=''    #清空存储单条二维码的变量
     for iin range(12): #生成单条二维码数字
        strone = strone + str(random.choice(number))
     encoder =qrcode.make(strone)     #生成二维码
     encoder.save("qrcodel"+strone&+".png")#保存二维码图片到文件


def scode9(schoice):
  default_dir = r"lottery.ini" #设置默认打开文件为项目路径下的"1ottery.ini"

    # 选择包含用户抽奖信息票号的文件,扩展名为 "．in了
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("lni file","*.ini")],title=u"请选择包含抽奖号码的抽奖文件: ",initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)# 调用 openfile()函数读取刚打开的抽奖文件
    codelist = codelist.split("\n")# 通过换行符把抽奖信息分割成抽奖列表
    # 要求用户输入中 (抽)奖数量
    incount = inputbox("\e33[实例25_批量生成PPT版荣誉证书；32m请输入要生成的抽奖数量:\33[ " ,1,0)
    # 如果输入中 (抽)奖数量等于ø或超过抽奖数组数量,重新输入
    while int(incount)== 0 or len(codelist)< int(incount):
        incount = inputbox("\D3[实例25_批量生成PPT版荣誉证书;32m 请输入要生成的抽奖数量:\33[ ",1,0)
    # 根据输入的中奖数量进行抽奖 strone = random.sample(codelist,int(incount))
    for i in range(int(incount)):
        # 将抽奖列表的中括号去掉
        # 循环将抽奖列表的引号和中括号去掉
        wdata =str(strone[i].replace('[',)).replace(']',
        # 将抽奖列表的引号去掉
        wdata = wdata.replace(''''',").replace(''''',")
        # 输出中奖信息
        print(wdata)
