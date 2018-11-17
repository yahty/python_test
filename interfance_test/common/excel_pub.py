import xlrd
from common.readConfig import ReadConfig
import os

class ExcelUtil(object):

    def __init__(self, excel_path, sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        # get titles
        self.row = self.table.row_values(0)
        self.col = self.table.col_values(0)
        # get rows number
        self.rowNum = self.table.nrows
        # get columns number
        self.colNum = self.table.ncols
        # the current column
        self.curRowNo = 1

    def has_next(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :
            return False
        else:
            return True

    def next(self):
        r = []
        while self.has_next():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    # 以列表的形式返回第i行的数据
    def rowlist(self, i):
        # 按行读取存为list,去除空字符
        rowlist = self.table.row_values(i)
        n = rowlist.count("")
        for i in range(n):
            rowlist.remove(u'')
        return rowlist

    # 以字典的形式返回所有数据
    def readasdict(self):
        d = {}
        col = self.table.col_values(0)
        nrows = self.table.nrows
        for i in range(nrows):
            val = self.rowlist(i)[1:]
            if len(val) == 1:
                 d[col[i]] = val[0]
            else:
                d[col[i]] = val
        return d

    # 已列表的形式按行返回数据 i~j行的数据（字典形式）
    def readaslitbyrow(self, i, j):
        l = []
        s = self.rowlist(i)
        e = self.rowlist(j)
        for i in range(1, len(s)):
            d = {s[0]: s[i], e[0]: e[i]}
            l.append(d)
        return l

if __name__=="__main__":
    config = ReadConfig()
    excel_path = os.path.join(config.get_excel("path"), "login_data.xlsx")
    excel = ExcelUtil(excel_path, "帐号")
    username = excel.rowlist(1)[0]
    print(username)
    paw = excel.rowlist(1)[1]
    print(paw)
    # print(excel.readasdict())


