#coding:utf-8
import xlrd
##打开一个excel并获取到指定的工作表
def get_sheet(file,sheet_name):
    excel = xlrd.open_workbook(file)
    sheet = excel.sheet_by_name(sheet_name)
    return sheet
#从一个工作表中找到指定用例名的用例数据
def get_case(sheet,case_name):
    for i in range(1,sheet.nrows):
        if sheet.cell(i,0).value== case_name:#cell指定单元格数据
            return  sheet.row_values(i)

    return None


if __name__=="__main__":
    sh = get_sheet("../data/data.xls","注册")
    print(sh)
    case_data = get_case(sh,"test_user_reg_normal")
    print(case_data)


