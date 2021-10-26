
## 使用flask快速构建项目API
### 项目创建与依赖安装
	# 进人工作区目录
	cd workspace 
	
	# 创建项目文件夹
	mkdir webapi
	
	# 如果环境中没有pipenv则安装pipenv
	pip install pipenv
	
	# 使用pipenv在当前项目中安装flask
	pipenv install flask
	
	# 安装mysql连接库pymysql
	pipenv install pymysql
	
	# 安装sqlalchemy的flask插件
	pipenv install flask-sqlalchemy
	
	# 安装flask的migrate插件，用于数据迁移
	pipenv install flask-migrate
	
	# 安装跨域插件，解决动静分离后的静态页面在不同主机名单独部署的问题
	flask-cors = "*"
	
	# 安装redis连接库
	pipenv install redis
	
### docker服务编排
    # 切换到工作目录
    cd flask-cli

    # 运行容器
    docker-compose up -d

## 产品部署请使用wsgi方式部署