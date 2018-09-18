---
title : 机器学习入门 - 安装tensorflow、keras、pytorch
date : 2018-9-18
tags : 
 - ML
---
# 机器学习入门 - 安装tensorflow、keras、pytorch

[TOC]

## 背景
> 系统版本：Ubuntu 16.04  
> Python版本：Python2.7  

## 准备
安装pip
```
sudo apt-get install python-pip
```

## 安装 tensorflow

```
sudo pip install tensorflow==1.4.0
```

### 问题

 运行程序时出现以下内容

 > I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA

 **解决方法**

 > 在程序中添加以下代码 或 在 tensorflow 的包中添加
 > ```
 > import os
 > os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
 > ```


## 安装 keras
```
sudo pip install keras==2.1
```
## 安装 pytorch

**[官网](https://pytorch.org/)下载**

> torch-0.4.0-cp27-cp27mu-linux_x86_64.whl

**安装**

```
sudo pip install torch-0.4.0-cp27-cp27mu-linux_x86_64.whl
sudo pip install torchvision
```