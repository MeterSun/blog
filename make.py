#coding=utf-8

import os
import re
import yaml
import json

postdir = './post/'
contentpath = './package/content.json'

def parseMarkdownFile(file):
    with open(file) as f:
        y = re.findall('^---([\s\S]+?)---',f.read())
    if y:
        return yaml.load(y[0].decode('utf-8'))

def createContent(a):
    with open(contentpath,'w')as f:
        json.dump(a,f)

def main():
    content = []
    for i in os.listdir(postdir):
        p = parseMarkdownFile(os.path.join(postdir,i))
        if p:
            p['filename'] = i
            content.append(p)
            print p
    createContent(content)

if __name__ == '__main__':
    main()