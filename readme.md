MyBlog
---

## 简介
这是我自己编写的静态博客网站，使用markdown编辑博客。

## 文件夹说明
- markdown支持文件夹：`lib/`、`css/`、`fonts/`、`js/`，改编自 [editor.md/examples](https://pandao.github.io/editor.md/examples/index.html)
- 文件夹 `.post/` 存放`.md` 格式的博客文件，文件名如 `2018-8-12-hello-world.md`
- 文件夹 `.package/`  存放生成网站而产生的文件，无需改动
- `package/content.json` 说明
    ```json
    {
    "all": [ // 所有文件目录
        {
            "date": "2018-8-13",
            "title": "...",
            "filename": "...",
            "tags": ["python", "yaml"] #标签
        },{
            ...
        }
    ],
    "yaml": [0],    // 分类项目，列表为文章在'all'中的索引
    "python": [0]
    }
    ```



## 使用说明

1.新建博客，在 post 文件夹下，新建 md 文档，例：'2018-08-08-hello-world.md'
1.编写博客，在 md 文档的正文前编写文档信息，以下为例：

    ---
    title: 'Hello World'
    date: '2018-8-8'
    tags:
    - hello
    - world
    ---

1.编写完成，执行脚本 `make.py`
1.push 到 Github 上

## 更新
#### 2018-9-2
- 增加了分页的功能
#### 2018-8-26
- 增加了点击标签可以按标签分类浏览的功能
#### 2018-8-13
- 初步建立MyBlog网站，具备最基本的写和浏览的功能