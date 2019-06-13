# encoding = 'utf-8'
import requests,re,os
from bs4 import BeautifulSoup

#name 表示文件名字
#url 表示题目路径
#将这个路径的题目保存为name文件
def save_html(name,url):
	'''
	#抓取页面
	res = requests.get(url,headers = headers)
	res.encoding = 'utf-8-bom'
	#页面内容
	text = res.content
	#内容写入一个文件
	f = open("temp.html",'wb')
	f.write(text)
	f.close()
	'''
	get_html("temp.html",url)
	#读出内容
	tf = open("temp.html",'r')
	input = tf.read()
	tf.close()
	
	#正则表达式替换掉部分内容
	output1 = re.sub('<iframe (.*)',' ',input)
	output2 = re.sub("<input type='hidden' (.)* value",' ',output1)
	#将最终内容写入name文件
	f = open(name,'w')
	f.write(output2)
	f.close()
	print(name," has saved ok!")

#根据mom.html文件内容得到需要进一步爬取的sonurl
def get_sonurl(url_list):
	f = open('mom.html','r')
	text = f.read()
	soup = BeautifulSoup(text,'html.parser')
	f.close()
	a_list = soup.find_all('a')
	for i in a_list:
#		print(i['href'])
		#find_all得到的list中每个是slice对象，可以直接得到属性，很舒服呀~
		url_list.append(i['href'])
#	print(url_list)
	print("find sonurl ok!")

#根据url获取mom.html
def get_html(name,url):
	f = open(name,'wb')
	res = requests.get(url,headers = headers)
	res.encoding = 'utf-8-bom'
	text = res.content
	f.write(text)
	f.close()
	print(name + " " + url," has get ok!")
	
if __name__ == "__main__":
	print("welcome!")
	print("input your cookie:\nlike this \nJSESSIONID=7CBC32078B041854FE8EFAEE1A961E98; DWRSESSIONID=Eghu$3ODyHz35BCqw4xEZV5ugJm")
	cookie = 'SESSIONID=7CBC32078B041854FE8EFAEE1A961E98; DWRSESSIONID=Eghu$3ODyHz35BCqw4xEZV5ugJm'
	cookie = input()
	print("input path:\nlike this \n xzb/")
	path = input()
	if os.path.exists(path):
		pass
	else:
		os.mkdir(path)
	#header信息，主要是cookie
	headers = {}
	headers['Cookie'] = cookie
	
	momurl = 'http://222.195.158.247/meol/common/question/test/student/stu_qtest_more_result.jsp?testId=22400165'
	faurl = 'http://222.195.158.247/meol/common/question/test/student/'
	#得到mom.html
	get_html("mom.html",momurl)
	url_list = []
	#解析mom.html
	get_sonurl(url_list)
#	print(url_list)
	cnt = 1
	for sonurl in url_list:
		url = faurl + sonurl
		name = path + str(cnt) + '.html'
		print(name)
		cnt = cnt+1
		save_html(name,url)
	os.remove("temp.html")
	os.remove("mom.html")
	
	print("finish!")
