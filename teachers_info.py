#-*-coding:utf8-*-
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def write(xxx):
    for each in xxx:
        each = each+'\n'
        f.writelines(each)
        print each


def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    #content_feild = selector.xpath('/html/body/div[1]/div/div[3]/div/div[2]/div/div[2]')
    halfurls = selector.xpath('//div[@class="tcName"]/table/tbody/tr/td/a/@href')
    allurls=[]
    for each in halfurls:
        allurls.append('http://scce.ustb.edu.cn/'+each)
    for eachpage in allurls:
        html = requests.get(eachpage)
        selector = etree.HTML(html.text)
        basicInfo1=selector.xpath('//div[@class="faculty_part1_content"]/text()')
        basicInfo2=(selector.xpath('//div[@class="faculty_part1_content"]/a/text()'))
        basicInfo3=(selector.xpath('//div[@class="faculty_part2_content"]/text()'))
        basicInfo3.append('\n')
        #complete collecting
        write(basicInfo1)
        print '\n'
        write(basicInfo2)
        print '\n'
        write(basicInfo3)



if __name__=="__main__":
    f = open('teachersName.txt','w')
    spider('http://scce.ustb.edu.cn/article.action?categoryId=29&boardaId=132')
    f.close()


