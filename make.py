#coding=utf-8

import os
import re
import yaml
import json

# md博客 路径
postdir = './post/'
# 输出目录的路径
contentpath = './package/content.json'

# 解析md文件取得有关文件信息的内容
def parseMarkdownFile(file):
    with open(file) as f:
        y = re.findall('^---([\s\S]+?)---',f.read())
    if y:
        return yaml.load(y[0].decode('utf-8'))

# 将字典类型内容写入json文件
def createContent(a):
    with open(contentpath,'w')as f:
        json.dump(a,f)

def main():
    content = {}
    content.update({'all':[]})
    for filename in os.listdir(postdir):
        p = parseMarkdownFile(os.path.join(postdir,filename))
        if not p: continue
        p['filename'] = filename
        index = len(content['all']) # index文章位置索引
        content['all'].append(p)
        for t in p['tags']:         # 分类记录 t为标签tag
            if not content.has_key(t): content.update({t:[]})
            content[t].append(index)
    createContent(content)

if __name__ == '__main__':
    main()