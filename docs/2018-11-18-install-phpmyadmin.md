---
title : '安装 MySQL 图形管理界面 phpMyAdmin'
date : '2018-11-18'
tags :
 - mysql
---
# 安装 MySQL 图形管理界面 phpMyAdmin

[TOC]

## 安装

    sudo apt-get install phpmyadmin

## 配置

将 phpmyadmin 与 apache2 建立连接

    sudo ln -s 源文件 目标文件

- phpMyAdmin 在 /usr/share/phpmyadmin 目录
- 假如 www 目录在 /var/www

**所以建立连接命令如下**

    sudo ln -s /usr/share/phpmyadmin /var/www
