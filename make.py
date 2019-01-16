#coding=utf-8

import os
import re
import yaml
import json

# md 博客 路径
POST_DIR = './post/'

# 输出目录
PACKAGE_DIR = './package/'
CONTENT_PATH = os.path.join(PACKAGE_DIR, 'content.json')


# 解析md文件取得有关文件信息的内容
def parseMarkdownFile(filePath):
    with open(filePath) as f:
        fileContent = f.read()
        pattern = '^---([\s\S]+?)---'
        info = re.findall(pattern, fileContent)
        content = re.sub(pattern, '', fileContent)
    if info:
        return yaml.load(info[0].decode('utf-8')), content
    else:
        return None,None

# 将字典类型内容写入json文件
def createContentJson(a):
    with open(CONTENT_PATH,'w')as f:
        json.dump(a,f)

# 创建 md 文件
def createContentMarkdown(filename,strs):
    with open(os.path.join(PACKAGE_DIR, filename),'w')as f:
        f.write(strs)

def main():
    Content = {}
    Content.update({'all': []})
    # 首先遍历 package 目录，清空文件
    for filename in os.listdir(PACKAGE_DIR):
        _filePath = os.path.join(PACKAGE_DIR, filename)
        print '[remove file]', _filePath
        os.remove(_filePath)
                
    # 遍历 post 目录
    for filename in os.listdir(POST_DIR):
        
        # 解析 md 文档
        filePath = os.path.join(POST_DIR, filename)
        print '[parse file]', filePath
        markdownFileInfo, markdownFileContent = parseMarkdownFile(filePath)
        if not markdownFileInfo: continue
        
        # 重命名    
        newfilename = filename.replace(' ', '-').replace('.md', '')
        markdownFileInfo.update({'filename': newfilename})
        createContentMarkdown(newfilename, markdownFileContent)
                
        # 添加文档信息
        Content['all'].append(markdownFileInfo)

    # 逆序，最近更新的在最前
    Content['all'].reverse()
    for index,item in enumerate(Content['all']):
        print '[get file %d]' % index, item['date'], item['title'].encode('utf-8')
    
    for index, i in enumerate(Content['all']):
        for tag in i['tags']:  # 分类记录 t为标签tag
            if not Content.has_key(tag): Content.update({tag: []})
            Content[tag].append(index)
    
    # 创建 md 索引文件 content.json
    createContentJson(Content)
    print '\n[total] all %d files %d tags' % (len(Content['all']), len(Content.keys()) - 1)

if __name__ == '__main__':
    main()