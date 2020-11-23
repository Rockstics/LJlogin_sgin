import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'LJlogin_sgin.settings'

if __name__ == '__main__':

    # send_mail(
    #     '邮件客户端授权码',   #主题
    #     '配置邮件客户端授权码：jsxtpamuwdpgbfdd',  ##内容
    #     '1024384924@qq.com',
    #     ['1024384924@qq.com'],
    # )
    subject, from_email, to = '来自llc的测试邮件', '1024384924@sina.com', '1024384924@qq.com'  #主题、发件人、收件人
    text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'  ##内容
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()