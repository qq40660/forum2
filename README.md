1. 历史由来
这是一个独立的 forum程序,从 plugs 复制出来。
以前的plugs程序有一些对 uliwebzone的依赖。

2. 我目前应用在 forum.jeapedu.com

界面要做改进。

3. 你需要安装 uliweb,plugs 

关于uliweb的安装，你可以访问：
http://uliweb.cpython.org

4. 配置
cd forum2
#vim apps/local_settings.ini

增加：
	
[ORM]
CONNECTION='sqlite:///database.db'

#uliweb syncdb
#uliweb dbinit uliweb.contrib.rbac
#uliweb createsuperuser
#uliweb runserver

可以工作了。

修改：智普教育
