#爬一个网页，获取所有的link，然后递归爬这些link里的子link
import requests as req          
from bs4 import BeautifulSoup   
LAYER = 1

def GetURL(url):
    if ("https" not in str(url)) and ("http" not in str(url)):
        url = str(r"http://" + url)         #如果获取的链接没有http则加上
    return url

def GetLink(data , layers):
    global LAYER
    if LAYER <= layers:
        LAYER += 1
        link_list=[]
        links = req.get(data)
        soup = BeautifulSoup(links.text,"html.parser")       #使用BeautifulSoup解析获取到的数据
        for link in soup.find_all("a"):
            each_link = link.get("href")
            if ("https" in str(each_link)) or ("http" in str(each_link)):               #对一些可能格式不对的网址进行清理，不然会造成访问错误
                link_list.append(each_link)
                GetLink(each_link , layers)
        print("当前在爬第%s层网址:%s" % (LAYER-1 , data))
        link_print(link_list , len(link_list))
        LAYER -= 1                                      #当这层网址全部爬完，LAYER-1返回上一层
    else:
        return 0

def link_print(mylist , len):                           #专门用于网址列表的打印输出
    print("该网页内共%s个链接"%len)
    for i in list(mylist):
        print(i)

def main():
    url = input("请输入想爬网站(www.xxx.com):")      # 获取输入
    layers = int(input("选择想爬层数:"))
    new_url = GetURL(url)
    GetLink(new_url , layers)


if __name__ == "__main__":
    main()