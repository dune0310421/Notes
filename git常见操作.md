#### 仓库

克隆仓库 git clone xxx(可以是http链接或ssh密钥)

关联远程仓库 git remote add origin xxx(链接)

删除关联 git remote rm origin

#### 分支

> 一般本地仓库代码是在自己的单独分支中做的

新建分支 git branch xxx

删除分支 git branch -d xxx

查看分支 git branch *代表当前分支

切换到某分支 git checkout xxx

查看当前分支状态 git status

将本地仓库所有代码添加到暂存区 git add .

暂存区提交到本地分支 git commit -m "我修改了xxx"

将本地分支push到远程仓库上git push origin xxx(跟本地的分支对应的远程分支)

将远程分支的东西pull到本地 git pull

>git操作详解 https://zhuanlan.zhihu.com/p/183092443

