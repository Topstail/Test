## Git的使用

### create a new repository on the command line

```
echo "# Test" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Topstail/Test.git
git push -u origin master
```

### push an existing repository from the command line

```
git remote add origin https://github.com/Topstail/Test.git
git push -u origin master
```



#### git init

　　　　当前目录下初始化git仓库；

　　  ![img](https://img2018.cnblogs.com/blog/1808994/201910/1808994-20191010162942498-387440884.png)

#### git status

　　　　可以查看git仓库的当前状态

　　　　![img](https://img2018.cnblogs.com/blog/1808994/201910/1808994-20191010163026614-1265635009.png)

#### git add -A   git add file

　　　　git add -A 添加目录下所有的文件到缓存区

　　　　git add file 添加目录下指定的文件到缓存区

　　　　![img](https://img2018.cnblogs.com/blog/1808994/201910/1808994-20191010163206404-1301308643.png)

####  git commit -m“信息”

　　　　将缓存区中的更改提交到仓库

　　　　![img](https://img2018.cnblogs.com/blog/1808994/201910/1808994-20191010163646618-758475041.png)

####  git log

　　　　查看当前版本之前的提交信息

　　　　![img](https://img2018.cnblogs.com/blog/1808994/201910/1808994-20191010163854444-1029612159.png)

####  git reflog

　　　　查看HEAD的变更记录 包括回退

　　　　![img](https://img2018.cnblogs.com/blog/1808994/201910/1808994-20191010164026679-1745855889.png)

#### git branch -b branch_name

　　　　建立一个新的分支

#### git diff

　　　　查看当前文件与缓存区文件的差异

#### git checkout -- file

　　　　取消更改，将缓存区的文件提取覆盖当前文件

#### git reset --hard 版本号

　　　　回退到相应版本号，同样也可以回退到未来的版本号

#### git clean -xf

　　　　删除当前目录中所有未追踪的文件

#### git config --global core.quotepath false

　　　　处理中文文件名