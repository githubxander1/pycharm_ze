import os.path
import tkinter
from logging import root


def mkdir(path):
    isexists=os.path.exists(path)
    if not isexists:
        os.makedirs(path)

def openfile(filename):
    f=open(filename)
    flist=f.read()
    f.close()
    return flist

def inputbox(showstr,showorder,length):
    instr=input(showstr)
    if len(instr) != 0:
        if showorder ==1:
            if str.isdigit(instr):
                if instr == 0:
                    print('输入为0，请重新输入')
                    return 0
                else:
                    return instr
            else:
                print('输入错误，请重新输入数字')
                return 0
        if showorder ==2:
            if str.isalpha(instr):
                if len(instr) !=length:
                    print('您必现输入'+str(length)+'个字母，请重新输入')
                    return 0
                else:
                    return instr
            else:
                print('输入错误，请重新输入字母')
                return 0
        if showorder ==3:
            if str.isdigit(instr):
                if len(instr)!=length:
                    print('您必现输入'+str(length)+'个数字，请重新输入')
                    return 0
                else:
                    return instr
            else:
                print('输入错误，请重新输入数字')
                return 0
    else:
        print('输入为空，请重新输入')
        return 0

incount=inputbox('请输入您要生成验证码的数量：',1,0)
ordstart=inputbox('请输入起始序号(3位)：',3,3)

def wfile(sstr,sfile,typeis,smsg):
    def wfile(sstr,sfile,typeis,smsg,datapath):
        mkdir(datapath)
        datafile=datapath+'\\'+sfile
        file=open(datafile,'w')
        wrlist=sstr
        pdata=''
        wdata=''
        for i in range(len(wrlist)):# 按条循环读取防伪码数据
            wdata=str(wrlist[i].replace('['),").replace(']',")#去掉字符的中括号
            wdata=wdata.replace(''''',").replace(''''','')#去掉字符的引号
            file.write(str(wdata))  # 写入保存防伪码的文件
            pdata = pdata + wdata  # 将单条防伪码存储到pdata变量
        file.close()
        print(smsg+'防伪码共计：'+str(len(wrlist))+'条')
        print(pdata)#屏幕输出生成的防伪码信息
        if typeis != 'no':#是否显示信息提示框
            #显示‘输出完成’的信息提示框，显示信息包含防伪信息码的保存路径
            tkinter.messagebox.showinfo('提示',smsg+str(len(randstr))+'\n 防伪码文件存放位置：'+datafile)
            root.withdraw()#关闭辅助窗口


wfile(randstr,'scode1.txt','','已生成6位防伪码共计：','codepath')
