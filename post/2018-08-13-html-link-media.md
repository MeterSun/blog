---
title : Html 中针对不同分辨率的屏幕采用不同的 CSS
date : 2018-8-13
tags : 
 - html
 - css
---
# Html 中针对不同分辨率的屏幕采用不同的 CSS

[TOC]

## 方法一：link 标签的 media 属性

例：

```html
<link rel="stylesheet" media="screen and (min-width:700px)" href="css/mobile.css" />
<link rel="stylesheet" media="screen and (max-width:700px)" href="css/main.css" />
<link rel="stylesheet" media="(min-width:700px)" href="css/mobile.css" />
<link rel="stylesheet" media="(max-width:700px)" href="css/main.css" />

```
## 方法二：CSS3 @media 查询

例：

```css
@media screen and (max-width: 300px) {
    body {
        background-color:lightblue;
    }
}
```
