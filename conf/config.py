
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'
#路径配置
import os
#项目路径__file__当前文件
##os.path.abspath(__file__)获取当前config的绝对路径，dirname上一级文件夹的路径
project_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#数据文件目录
data_path=os.path.join(project_path,"data","data.xls")
#日志文件
log_file=os.path.join(project_path,"log","log.txt")
report_file= os.path.join(project_path,"report","report.html")


#log配置
import logging
logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt = "%Y-%m-%d %H:%M:%S",
                    filename=log_file,#../log/log.txt相对路径你
                    filemode="a",##每次新加一条log,默认选项
                    )#时间，日志级别
##邮件配置
smtp_server="smtp.163.com"
smtp_user="ivan-me@163.com"
smtp_password="hanzhichao123"
receiver="m18548919162@163.com"
subject="接口测试报告"
body = "hi,all,\n附件中是接口测试报告，请查收"
is_send_report=False
if __name__=="__main__":
    logging.info("hello,world")

