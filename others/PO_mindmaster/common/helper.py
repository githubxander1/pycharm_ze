import xlrd
import logging,os
class Helper:
    def readExcels(self,rowx):
        '''
        rowx是行数
        ：param rows
        :return:返回每一行的行数
        '''
        book=xlrd.open_workbook(b'C:\Program Files\1test\pycharm_ze\others\PO_mindmaster\data\info.xlsx','r')
        table=book.sheet_by_index(0)
        return table.row_values(rowx)

    def readusername(self,rowx):
        '''
        rows 返回的是第几行的用户名
        ：param rows
        ：return：
        '''
        return str(self.readExcels(rowx)[0])

    def readpassword(self, rowx):
        '''
        rows 返回的是第几行的用户名
        ：param rows
        ：return：
        '''
        return str(self.readExcels(rowx)[1])

    def dirname(self,filename,filepath='data'):
        '''
        :param filename
        :param filepath
        :return:
        '''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filepath,filename)

    def makelog(self,log_content):
        # 定义日志文件
        logFile=logging.FileHandler(self.dirname('log.txt'),'a',encoding='utf-8')
        # 设置日志格式
        fmt=logging.Formatter(fmt='%(asctime)s-%(name)s-%(levername)s-%(module)s:%(message)s')
        logFile.setFormatter(fmt)
        logger1=logging.Logger('logTest',level=logging.DEBUG)#定义日志
        logger1.addHandler(logFile)
        logger1.info(log_content)
        logFile.close()



# re=Helper()
# print(re.readExcels(2))
