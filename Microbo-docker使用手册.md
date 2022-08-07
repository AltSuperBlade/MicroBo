# Microbo-docker使用手册

使用前准备工作:

```bash
# 需要删除所有带akairo/microbo的镜像和容器
# check container id
docker ps -a
# remove container
docker stop {container-id}
docker rm {container-id}
# check image id 
docker images
# remove image
docker rmi {image-id}
```

根据需求修改docker-compose.yml

```python
# docker-compose.yml 内容
version: "3.9"  # optional since v1.27.0
services:
  web:
    # 仅限源码生成image时使用build
    # build: ./
    container_name: microbo
    # 已有image的情况下注释掉build部分，使用下面image部分
    image: akairo/microbo:dev
    # 拉取非漏洞环境
    # image: akairo/microbo:latest
    ports:
      - "11451:5000"
        # 直接访问 127.0.0.1:11451 启动 web
```

在yml存放路径:`docker-compose up`


