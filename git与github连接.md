## git与github的连接

首先你需要有一个github账号，还需要一台安装有git的服务器



使用git 将项目上传到GitHub上首先要有GitHub账号,没有注册的先去注册，地址：https://github.com/login 没有仓库的话，先新创建一个仓库。

![1589244732277](C:\Users\Charles\AppData\Roaming\Typora\typora-user-images\1589244732277.png)

创建仓库： 填写新仓库名称，备注信息。点击创建即可完成。

![](C:\Users\Charles\AppData\Roaming\Typora\typora-user-images\1589244848446.png)

创建完成后，就可以使用git去连接去了



创建本地Git仓库文件夹，然后对本地仓库进行初始化

```
[root@VM_0_15_centos ~]# mkdir git_repo
[root@VM_0_15_centos ~]# cd git_repo
[root@VM_0_15_centos git_repo]# git init
Initialized empty Git repository in /root/git_repo/.git/
```

 本地Git仓库和GitHub仓库之间的传输是通过“SSH”加密传输的，GitHub需要识别是否是你推送，只要GitHub知道了你的公钥，就可以确认只有你自己才能推送，所以需要配置ssh key。 

创建SSH密钥

```
[root@VM_0_15_centos ~]#  ssh-keygen -t rsa -C "chn740932867@163.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): # 直接回车 
Enter same passphrase again: # 直接回车 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:Z6x1q7wT/YHeNDvb3/0bKUxFcCxchGozBy/SAgM4XCI chn740932867@163.com
The key's randomart image is:
+---[RSA 2048]----+
| E..oo.     ..*= |
|  .+.  o   . +o. |
|    .   o . + .. |
|         + B o.  |
|        S O.*o   |
|         =..=.+ .|
|        .  o.* * |
|         .... *.+|
|          +o  .+X|
+----[SHA256]-----+
[root@VM_0_15_centos ~]# cat /root/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPaV0XT0UQKuZou/ZfInXxR7o0EWL2Zi8NmAexsJLPl676j65a6+zV9VfifFfPjJ2wWBCWTmEOPkXJUT43gSc3pW4zkkhu9Latynvjuqv/1458MNN9rj+0u0VrbBfQLZJJWFgKsYN7AYocwWu36w2u+jbBmTntFEY/c5/ZUEfyMRdUdpih3bwDuiRZZxu5eXL+oRIk44F0zo6MzsPrzMgyFusem3RPNKaKGtFxeRIa0AXBdWQorQAM7fOAtaIA4XOIEDvCHYnmZFu0v2t27+qV7S3/vSAvlMITVL4CLkRXUNpfRBhIfiotLNWcrkf/Jyo6RXFk77gieggzG51k91tZ chn740932867@163.com   # 注意不要复制之前的邮箱 
```

开始连接本地仓库和github仓库

![1589261960671](C:\Users\Charles\AppData\Roaming\Typora\typora-user-images\1589261960671.png)

![1589262017603](C:\Users\Charles\AppData\Roaming\Typora\typora-user-images\1589262017603.png)

![1589262210524](C:\Users\Charles\AppData\Roaming\Typora\typora-user-images\1589262210524.png)

点击添加，就可以成功的连接了

![1589262259363](C:\Users\Charles\AppData\Roaming\Typora\typora-user-images\1589262259363.png)



之后就可以开始测试了，将事先准备好的python脚本上传到本地的仓库中，然后提交

```shell
[root@VM_0_15_centos git_repo]# ls
memoryAndDiskTest.py
[root@VM_0_15_centos git_repo]# git add .
[root@VM_0_15_centos git_repo]# git commit -m "第一次更新"
[master (root-commit) f4161bb] 第一次更新
 1 file changed, 39 insertions(+)
 create mode 100644 memoryAndDiskTest.py
[root@VM_0_15_centos git_repo]# git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

