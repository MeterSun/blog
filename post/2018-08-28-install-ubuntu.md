---
---
title : 双系统U盘安装 Ubuntu 16.04
date : 2018-8-28
tags : 
 - ubuntu
---
# 双系统U盘安装 Ubuntu 16.04

[TOC]
## 准备

  1. U盘一个
  1. 系统镜像 *ubuntu-16.04.3-desktop-amd64.iso*
  1. 软碟通 *UltraISO* 

##  制作Ubuntu系统盘

1. 打开 UltraISO 软碟通
2. 从 UltraISO 里打开系统镜像
3. 选择菜单栏“启动(B) > 写入硬盘映像...”
4. 勾选“刻录校验”
5. 点击“写入”
6. 等待完成

## 安装Ubuntu

1. 选择开机从U盘启动

1. 选择 ***“Install Ubuntu”*** 立即开始安装，或 *“Try Ubuntu without installing”* 先体验稍后选择安装

1. 开始安装，选择语言， ***“中文（简体）”*** ，继续

1. 不连接 wifi ，继续

1. 继续

1. 安装类型，选择 ***“其他安装选项”*** ，继续

1. 分区
    
   > 1. / , ext4 , ~20GB  
   > 1. /boot , ext4 , ~200MB  
   > 1. swap , 交换空间 ， ~8GB(电脑内存8G)  
   > 1. /home , ext4 , (other)(越大越好)  
   >  
   >  设置启动引导器设备：/boot 所在区

1. 设置地区 ***Shanghai*** ，继续

1. 键盘布局 ***英语（美国）*** ，继续

1. 设置帐号，继续

1. 大约五六分钟，安装完成， ***现在重启*** 

1. 拔掉U盘，按 ***ENTER***

> **注意：** *开机选择启动位置，依电脑而定，若无Ubuntu选项，进入Windows系统使用EasyBCD设置启动项*