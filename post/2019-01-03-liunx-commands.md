---
title : '日常学习 Linux 命令'
date : '2019-1-3'
tags :
 - linux
---
# 日常学习 Linux 命令

[TOC]

## 环境

    Ubuntu 16.04

## 命令

### 切换管理员

    # 切换 root 用户
    sudo su
    # 切换普通用户
    su 用户名

### 建立链接

    # 硬链接
    ln 源文件 目标文件
    # 软链接
    ln -s 源文件 目标文件

## 搜索文件或文件夹

> 参考 https://blog.csdn.net/dcrmg/article/details/78000961

### 1. whereis+文件名

用于程序名的搜索，搜索结果只限于二进制文件（参数-b）、man说明文件（参数-m）和源代码文件（参数-s），如果省略参数，则返回所有信息。

### 2. find / -name +文件名

find是在指定的目录下遍历查找，如果目录使用 / 则表示在所有目录下查找，find方式查找文件消耗资源比较大，速度也慢一点。

### 3. locate+文件名

linux会把系统内所有的文件都记录在一个数据库文件中，使用locate+文件名的方法会在linux系统维护的这个数据库中去查找目标，相比find命令去遍历磁盘查找的方式，效率会高很多，比较推荐使用这种方法。

但有一个问题是数据库文件不是实时更新的，一般会每周更新一次，所以使用locate命令查找到的结果不一定是准确的。当然可以在使用locate之前通过 updatedb 命令更新一次数据库，保证结果的性。

### 4. which+可执行文件名

which的作用是在PATH变量指定的路径中，搜索某个系统命令的位置，并且返回第一个搜索结果。

使用which命令，就可以看到某个系统命令是否存在，以及执行的到底是哪一个位置的命令。

which指令会在环境变量$PATH设置的目录里查找符合条件的文件，所以基本的功能是寻找可执行文件。

## 解压缩

### tar

    tar [-options] [filename] [target]

    # .tar
    tar -cvf test.tar test/     # 打包
    tar -xvf test.tar           # 解包
    
    # .tar.gz
    tar -czvf test.tar.gz test/     # 压缩
    tar -xzvf test.tar.gz           # 解压
    
### xz

    xz -z xxx.tar    # 压缩得 xxx.tar.xz
    xz -d xxx.tar.xz # 解压得 xxx.tar
    # -k 保留源文件
