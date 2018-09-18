#coding=utf-8

import os
import re
import yaml
import json

# md博客 路径
POST_DIR = './post/'
# 输出目录的路径
CONTENT_PATH = './package/content.json'

# 解析md文件取得有关文件信息的内容
def parseMarkdownFile(file):
    with open(file) as f:
        y = re.findall('^---([\s\S]+?)---',f.read())
    if y:
        return yaml.load(y[0].decode('utf-8'))

# 将字典类型内容写入json文件
def createContent(a):
    with open(CONTENT_PATH,'w')as f:
        json.dump(a,f)

def main():
    Content = {}
    Content.update({'all':[]})
    # 遍历 post 目录
    for filename in os.listdir(POST_DIR):
        mdFileInfo = parseMarkdownFile(os.path.join(POST_DIR,filename))  # 解析 md 文档
        if not mdFileInfo: continue
        # 重命名    
        newfilename = filename.replace(' ','-').replace('.','_')
        os.rename(os.path.join(POST_DIR,filename),os.path.join(POST_DIR,newfilename))
        mdFileInfo.update({'filename':newfilename})
        Content['all'].append(mdFileInfo)  # 添加文档信息

    Content['all'].reverse()  # 逆序，最近更新的在最前
    for index, i in enumerate(Content['all']):
        for tag in i['tags']:  # 分类记录 t为标签tag
            if not Content.has_key(tag): Content.update({tag: []})
            Content[tag].append(index)
    createContent(Content)
    print 'all %d files %d tags' % (len(Content['all']), len(Content.keys()) - 1)

if __name__ == '__main__':
    main()