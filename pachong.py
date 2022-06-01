#爬一个网页，获取所有的link，然后递归爬这些link里的子link
import requests as req          
from bs4 import BeautifulSoup   

def GetURL(url):
    if ("https" not in str(url)) and ("http" not in str(url)):
        url = str(r"http://" + url)         #如果获取的链接没有http则加上
    return url

def GetLink(data):
    link_list=[]
    links = req.get(data)
    soup = BeautifulSoup(links.text,"html.parser")       #使用BeautifulSoup解析获取到的数据
    for link in soup.find_all("a"):
        each_link = link.get("href")
        if ("https" in str(each_link)) or ("http" in str(each_link)):               #对一些可能格式不对的网址进行清理，不然会造成访问错误
            link_list.append(each_link)
    return link_list , len(link_list)

def run(mylist , list_len):
    link_print(mylist , list_len)
    for each_link in list(mylist):                       #第二层的调用，对第一层的所有网址再爬一次
        print("当前在爬网址:%s" % each_link)
        layer , len = GetLink(each_link)
        link_print(layer , len)

def link_print(mylist , len):                           #专门用于网址列表的打印输出
    print("该网页内共%s个链接"%len)
    for i in list(mylist):
        print(i)

def main():
    url = input("请输入想爬网站(www.xxx.com):")      # 获取输入
    new_url = GetURL(url)
    first_layer , layer_len = GetLink(new_url)
    run(first_layer , layer_len)

if __name__ == "__main__":
    main()