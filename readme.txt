http://222.195.158.247/meol/homepage/common/ 
chrome 登录这个网址

找到看结果的页面url
http://222.195.158.247/meol/jpk/course/layout/newpage/index.jsp?courseId=24949
查看综合测试结果url
http://222.195.158.247/meol/common/question/test/student/stu_qtest_more_result.jsp?testId=22400165
这个作为momurl

F12
刷新，network中找到cookie
例如JSESSIONID
JSESSIONID=08EE6EBD573EC9B22214EB8E6E35E8BC; DWRSESSIONID=RX9ouBRSAh8kk5kmKyflHOSkhJm
运行程序，按要求输入cookie和路径即可得到。

注意：这个cookie应该是记录了最近登陆的用户，你爬完之前不要关掉chrome这个页面，不然cookie很有过期，就爬不完整