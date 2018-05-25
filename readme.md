### 环境
1. 安装python3.4（已装好）
	1. 在cmd中输入python可以启动python说明python安装成功
2.  pip 安装依赖的包，django1.8和xlwt（已装好）
	1.  在cmd中输入pip install django==1.8
	2.  pip install xlwt
	3.  检查安装情况：cmd中输入pip list，当其中有django1.8 和xlwt说明安装成功
### 服务器启动
1. 修改 icbc_grade/icbc_grade/setting.py
	1. ALLOWED_HOSTS 中添加ip，引号（英文单引双引都行）内写ip地址，逗号分隔ip
		1. 如，ALLOWED_HOSTS = ['127.0.0.1','192.168.0.1']
	2. DEBUG = True
3. **启动** cmd切到icb-grade 文件夹下，注意是上层的icbc-grade
	1. python manage.py runserver 0.0.0.0:8000
	2. cmd中ctrl+C可以停止服务器

### 数据库相关
建议：judeg-user表与pub-emp表中，id与num顺序相同，最好id=num。

使id从1开始自增的方法：    
	1.  安装并进入sqlite图形界面，打开对应的sqlit3.db文件    
	2.  找到sqlite-sequence， 将其中的对应表的数字改成1。注意：进行此修改时为避免主键冲突，最后先将要修改的表的数据清空。


[author：lzyzsere@126.com]


