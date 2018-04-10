# coding: utf-8
import smtplib
import traceback
from email.mime.multipart import MIMEMultipart  # 将图片和文字组装在一起
from email.mime.text import MIMEText  # 定义图片的文字数据
from email.mime.image import MIMEImage  # 定义图片的图片数据
from email.header import Header


class SendEmail(object):
    sender = '********@163.com'
    # receiver = '*******@163.com'
    receiver = '********@qq.com'
    # 邮件主题
    subject = '发送带图片的html邮件的测试邮件'
    smtpserver = 'smtp.163.com'
    username = '*********@163.com'
    password = '******'

    def __init__(self):
        self.smtp = smtplib.SMTP()  # 创建发送邮件对象
        self.msgRoot = MIMEMultipart('related')  # 设置邮件为多文本模式(可发送html/图片)
        self.msgRoot['Subject'] = Header(SendEmail.subject, 'utf-8')
        self.msgRoot['From'] = SendEmail.sender
        self.msgRoot['To'] = SendEmail.receiver

    def add_img_to_email(self, imgPath):
        """
        brief: 读取图像文件内容，保存到HTML中，最后添加到email中
        :param imgPath: 图片所在的路径
        :return: None
        """
        with open(imgPath, 'rb') as f:
            img_content = f.read()

        msgImage = MIMEImage(img_content)
        # '<image1>'是html中的标记，等价于 <image1> = msgImage
        msgImage.add_header('Content-ID', '<image1>')
        self.msgRoot.attach(msgImage)

    def add_html_to_email(self, htmlPath):
        """
        brief: 获取html的文本内容，添加到email中
        :param htmlPath: html文件路径
        :return: None
        """
        with open(htmlPath, 'r', encoding="utf-8") as f:
            html_content = f.read()

        msgText = MIMEText(html_content, 'html_file', 'utf-8')
        self.msgRoot.attach(msgText)

    def send_email(self):
        """发送邮件"""
        # 先获取html文件内容
        self.add_html_to_email('./test.html_file')
        # 后在html添加图片数据
        self.add_img_to_email('./img/pic.jpg')
        try:
            # smtp.set_debuglevel(1)
            print("连接服务器...")
            self.smtp.connect(SendEmail.smtpserver)
            self.smtp.login(SendEmail.username, SendEmail.password)
            print("登录成功！")
            self.smtp.sendmail(SendEmail.sender, SendEmail.receiver, self.msgRoot.as_string())
            print("发送邮件成功!")
        except Exception as e:
            traceback.print_exc()
        finally:
            self.smtp.quit()


if __name__ == "__main__":
    send_email = SendEmail()
    send_email.send_email()
