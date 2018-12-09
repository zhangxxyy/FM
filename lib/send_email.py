#coding:utf-8
import smtplib #连接stmp服务器并发送邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart##多部分
from  conf import config
def send_repport():

    #1 组装邮件正文
    msg = MIMEMultipart()#混合格式
    body = MIMEText(config.body,"plain","utf-8")#plain纯文字html
    msg.attach(body)#将正文添加到msg对象中
    #2组装邮件头
    msg["From"]=config.smtp_user
    msg["To"] =config.receiver
    msg["Subject"]=config.subject
    #4附件
    with open("../report/report.html","rb") as f:
        att_file = f.read()
    att = MIMEText(att_file,"base64","uft-8")
    att["Content-Type"]="application/octet-stream"#声明附件的内容格式MIME数据流格式
    att["Content-Disposition"] = "attachment;filename='report.html'"##附件描述信息，filename是附件的文件名
    msg.attach(att)#将附件添加到消息对象中


    #3
    smtp = smtplib.SMTP(config.smtp_server)
    smtp.login(config.smtp_user,config.smtp_password)
    smtp.sendmail(config.smtp_user,
                    config.receiver,
                  msg.as_string())#发送

