from selenium import webdriver
from time import sleep
import random
import time
from email.mime.text import MIMEText
from email.header import Header
from selenium.webdriver.chrome.options import Options
import smtplib

xuehao = "202030504184"
mima = '283614'
t = time.strftime('%m%d',time.localtime())
filename = '.\\daka.txt '


def emailtx(things):
    # 邮件的内容
    mail_msg = """
           <h2 style="color:#f00"> 健康填报系统提示你：</h2>
           <p>""""""
         <p>今日健康申报"""+ things +"""</p>
         <p>祝你生活愉快</p>
                  """
    message = MIMEText(mail_msg, 'html', 'utf-8')

    # 发件人名字，可以自由填写
    message['From'] = Header('坏狗邮箱小助手', 'utf-8')
    # 收件人名字 ，可以自由填写
    message['To'] = Header('坏狗i', 'utf-8')

    # 邮件标题
    subject = '健康填报接送通知！'
    message['Subject'] = Header(subject, 'utf-8')

    # 发送方地址
    sender = '583581531@qq.com'
    # 接收方地址，可以是多个地址
    receivers = ['583581531@qq.com']

    # 使用qq邮箱的服务，发送邮件
    smtpObj = smtplib.SMTP()
    smtpObj.connect("smtp.qq.com", 25)
    smtpObj.login(sender, 'waktrmhpuniobcdf')  # 登录 地址 授权码 ：授权码是发送方开启pop3 服务，在邮箱的设置中可以找到，开启后生成授权码
    smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
    smtpObj.quit()  # 关闭
    print('邮件发送成功')

def slp():
    sleep(random.randint(1,10))



def login():
    # 模拟浏览器打开网站
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(chrome_options=chrome_options)    
    #driver = webdriver.Chrome()
    
    driver.get("http://stu.zstu.edu.cn/webroot/decision/login")
    sleep(50)
    emailtx('1')
    # 输入用户名和密码
    driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys(os.environ['SCUT_USER'])
    emailtx('2')
    driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys(os.environ['SCUT_PASSWORD'])
    emailtx('3')
    driver.find_element_by_xpath("//div[contains(@class,'bi-single bi-basic-button cursor-pointer bi-button login-button')]").click()
    sleep(50)
    emailtx('2')
    #打开健康申报页面
    driver.find_element_by_xpath("//div[@class='bi-button-tree bi-vertical-layout']/div[3]").click()
    emailtx('3')
    driver.find_element_by_xpath("//div[@class='bi-single bi-basic-button cursor-pointer dec-common-img-icon-text-item dec-frame-platform-list-item-active dec-font-size-14 bi-h-tape-layout']").click()
    sleep(50)
    emailtx('3')
    #填写
    driver.switch_to.frame("a5f79672-e7ef-4d6c-affc-1ceaa522236e")
    driver.find_element_by_id("D12-0-0").find_element_by_tag_name("span").click()
    driver.find_element_by_id("D13-0-0").find_element_by_tag_name("span").click()
    sleep(50)
    emailtx('4')
    
    target = driver.find_element_by_id("B30-0-0")
    driver.execute_script("arguments[0].scrollIntoView();", target)
    driver.find_element_by_id("B30-0-0").find_element_by_tag_name("button").click()
    sleep(50)
    
    emailtx('5')
    print("\n" + t + "疫情防控——师生健康状态采集\n已完成")
    a = "已完成"
    emailtx(a)

login()
driver.quit( )
print("运行结束")
