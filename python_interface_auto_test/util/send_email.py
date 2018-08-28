#coding:utf-8
import smtplib #邮件处理库导入
from email.mime.text import MIMEText #导入系统自带邮件基础类
class SendEmail:
	global send_user  #发送者
	global email_host #邮箱服务器
	global password
	email_host = "smtp.163.com"
	send_user = "1882340@163.com"
	password = "777777"
	def send_mail(self,user_list,sub,content): #邮件接收人，主题，内容
		user = "Guohailiang"+"<"+send_user+">" #构建邮件发送者的信息，别名+邮箱地址
		message = MIMEText(content,_subtype='plain',_charset='utf-8') #内容，邮件类型，编码格式
		message['Subject'] = sub #邮件的主题
		message['From'] = user #邮件内容中的发送者信息
		message['To'] = ";".join(user_list) #邮件内容中的邮件接收者，可以有多个
		server = smtplib.SMTP()
		server.connect(email_host) #连接邮件服务器
		server.login(send_user,password) #登陆
		server.sendmail(user,user_list,message.as_string()) #发送邮件。发送者，接收者，消息内容
		server.close() #关闭邮件服务器

	#构建自动化测试结果，然后调用上述发送函数发送
	def send_main(self,pass_list,fail_list): #成功用例数目，失败用例数目
		pass_num = float(len(pass_list)) #获取列表元素个数作为数量
		fail_num = float(len(fail_list))
		count_num = pass_num+fail_num
		#90%
		pass_result = "%.2f%%" %(pass_num/count_num*100) #计算比例，保留两位小数
		fail_result = "%.2f%%" %(fail_num/count_num*100)


		user_list = ['592827060@qq.com'] #收件人邮箱
		sub = "接口自动化测试报告" #邮件主题
		content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result )
		self.send_mail(user_list,sub,content)

if __name__ == '__main__':
	sen = SendEmail()
	sen.send_main([1,2,3,4,5,6,7,8],[])