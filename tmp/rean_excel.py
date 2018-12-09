#coding:utf-8
#1倒入xlrd
import xlrd
#2打开excel（work__book）
excel =xlrd.open_workbook("../data/data.xls")###上级目录，找到api_teat在找到data
#3z指定工作表
# sheet = excel.sheet_by_name("登录")
# sheet= excel.sheet_by_index(0)
# print(sheet.nrows)#获取当前行数
# print(sheet.ncols)#获取当前列数
# print(sheet.row_values(0))#打印第一行数据
# print(sheet.row_values(1))#打印第一行数据
# print(sheet.cell(1,0).value)#打印指定单元格数据
###练习1：遍历注册表两条信息（不要标题行）
sheet = excel.sheet_by_name("注册")
for i in range(1,sheet.nrows):
    print(sheet.row_values(i))


