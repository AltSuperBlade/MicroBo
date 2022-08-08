# MicroBo（ych's Part）

## 个人在本次大作业中的主要贡献

* 作为小组组员参与完成了 MicroBo 的开发

* docker打包环境进行快速部署：
  
  * 整合web app，提供快速线上拉取镜像环境
  
  * 部署云端服务器

* 修复app漏洞

## 完成了哪些自认为有技术含量的工作

* 将整个flask web app以docker的方式进行打包上传至hub

* 使用docker-compose进行快速自动化部署

* 实现云端服务器部署

* 修复app漏洞，以diff文件的方式生成补丁

* 编写容器外部修改容器内部flag文件的shell脚本

## 印象深刻的一些 bug 和自己的解决方法

1. docker镜像生成运行之后无法宿主机与容器内部的flask_app沟通。

    **bug原因：** 出现这个bug的原因是flask的app.run功能默认设置为localhost，也就是说没有外部接口。在源码运行的时候没有任何问题，但是一旦打包成docker镜像之后，容器外部就无法访问，端口映射被迫无用。

    **解决办法：** ` app.run(host='0.0.0.0',port='5000',debug=True)`

    设置host为`0.0.0.0`使得外部能够访问容器内部

2. 制作flag修改脚本的时候出现 docker exec 之后脚本停止对容器内部执行命令的bug。

    **bug原因：** 推测命令执行栈并非一个栈，脚本内容完全在宿主机中执行。

    **解决办法：** 不以 `docker exec -it {container id} /bin/bash <<'EOF' ` 的方式进行容器操作，而是选择将对容器操作的脚本封装放入容器内部，外部以 `docker exec -d {container id} ./{容器内脚本}` 的方式修改


