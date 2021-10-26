# 基础镜像
FROM python:3.9

# 设置环境
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 设置工作目录
WORKDIR /code
EXPOSE 5000
# 安装依赖
COPY Pipfile  /code/
RUN pip install -i 'https://mirrors.aliyun.com/pypi/simple' pipenv && pipenv install &&pipenv install --system