import smtplib
from email.mime.text import MIMEText

mail_host = "smtp.163.com"  # 设置服务器 --- 这里是网易,你也可以改成其他的服务
mail_user = ""  # 用户名 --- 没啥好说的
mail_pass = ""  # 密码 ----没啥好说的
mail_postfix = "LucasX"  # 发件箱的后缀 --- 我的名字


def send_mail(to_list, sub, content):
    me = "Message" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False
