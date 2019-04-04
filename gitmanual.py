上传本地代码至github的方法：

step1: 建立git仓库

    cd到你的本地项目根目录，执行git命令，此命令会在当前目录下创建一个.git的文件夹

    git init


step2:将项目中的所有文件谈价至仓库中

    git add. 将当前路径下所有文件添加到待上传的文件列表
    
    git add name 将name文件添加到待上传


step3:将add的文件commit到仓库
    
    git commit -m "注释语句"


step4:去github创建自己的repository

    创建后会有自己仓库的URL地址

step5:将本地仓库关联到github上

    git remote add origin https://自己仓库的URL地址


step6：上传代码至github远程仓库

    git push -u origin master

注意：以上为第一次创建git仓库并关联github的所有操作

    之后的话只要重复执行step2、step3、git push，即可上传本地代码到github
