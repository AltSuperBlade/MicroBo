# DevelopmentForMicrobo

## 任务列表

- [x] 用户登录与注册页面

- [x] 所有人的留言页面

- [x] 个人资料与留言页面

- [x] 编辑个人信息页面

- [x] 新增留言编辑界面

- [ ] 更改密码

- [ ] （查找留言页面）

- [ ] （忘记密码？）

## 需要攻关的技术/商讨的问题

- [x] 不使用框架/使用框架-->使用什么框架
- **flask（首选）**\nginx
- [备选参考-log4j](https://blog.csdn.net/weixin_51194266/article/details/125524303?spm=1001.2014.3001.5502) 用别人的轮子

- [x] 使用什么数据库
- mysql

- [x] 数据库需要的表以及表中的列
  1. 用户表：id、昵称、账号、盐、密码加盐的哈希值、登陆时间、头像图片（本地链接）
   密码加盐：注册时的post请求时间生成随机数加盐
  2. 留言表：id、发帖人id、发帖时间、内容（、点赞待选）

- [ ] 数据库和代码部分的接口问题(待定)

- [x] 使用什么启动Web服务
- nginx（暂定）

- [ ] **各部分谁来做**
  1. 前端和网页：曹兴贤、叶津铭

- [ ] 漏洞类型：逻辑、命令执行、文件上传、XSS、会话保持(cookie\session\token\captcha)、中间件（Web服务或框架漏洞：Flask（SSTI）、Django（任意代码执行、重置密码等））、SQL注入（待定）

## 参考资料

- [flask部署到虚拟机服务器,flask 本地服务器部署](https://blog.csdn.net/weixin_29994499/article/details/119631320)

- [Flask - nginx部署](https://blog.csdn.net/qq_33962481/article/details/114375048)