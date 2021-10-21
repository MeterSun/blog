---
title : 'Ubuntu 安装 WPS'
date : '2019-4-13'
tags :
 - linux
---
# Ubuntu 安装 WPS

[TOC]

1. WPS 官网下载 安装包

1. 安装 dpkg -i wps....deb

1. 解决字体缺失问题

1. 下载：http://vdisk.weibo.com/s/ajLw30suHpSUg?from=page_100505_profile&wvr=6

1. 创建目录
    sudo mkdir /usr/share/fonts/wps-office

1. 将下载的字体复制到创建的目录：
    sudo cp -r wps_symbol_fonts.zip /usr/share/fonts/wps-office

1. 解压字体包:
    sudo unzip wps_symbol_fonts.zip

1. 解压后删除字体包
    sudo rm -r wps_symbol_fonts.zip
