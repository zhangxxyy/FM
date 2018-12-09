#coding:utf-
#1组装邮件正文
#2 组装邮件头
#3连接smtp服务器并发送邮件
import smtplib #连接stmp服务器并发送邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart##多部分
#1 组装邮件正文
msg = MIMEMultipart()#混合格式
body = MIMEText("python发送的邮件","plain","utf-8")#plain纯文字html
msg.attach(body)#将正文添加到msg对象中
#2组装邮件头
msg["From"]="test_results@sina.com"
msg["To"] ="m18548919162@163.com"
msg["Subject"]="from Python"
#4附件
with open("../report/report.html","rb") as f:
    att_file = f.read()
att = MIMEText(att_file,"base64","uft-8")
att["Content-Type"]="application/octet-stream"#声明附件的内容格式MIME数据流格式
att["Content-Disposition"] = "attachment;filename='report.html'"##附件描述信息，filename是附件的文件名
msg.attach(att)#将附件添加到消息对象中


#3
smtp = smtplib.SMTP("smtp.163.com")
smtp.login("ivan-me@163.com","hanzhichao123")
smtp.sendmail("ivan-me@163.com",
              "m18548919162@163.com",
              msg.as_string())#发送
