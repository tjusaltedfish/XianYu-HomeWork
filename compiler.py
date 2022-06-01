"""输入程序的名字,寻找保留字及其输出它的个数"""
import keyword

def str_Processing(fileName):
    if fileName.find(".txt",0,len(fileName))==-1: #检查是否为txt文件
        raise Exception("输入格式错误!")
    else:
        f = open(fileName, encoding='utf-8')
        data = f.read()
        data = data.lower()
        for i in r'~!@#$%^&*()_+-[]{},.\?':       #处理文件中的特殊符号
            data = data.replace(i, " ")
        return data

def catch_Word(strdata):
    words = str(strdata).split()    #将每个单词分开
    counts = {}
    for word in words:              #如果遇到关键字就使其value+1，字典中没有就创建一个新key
        if keyword.iskeyword(word):
            counts[word] = counts.get(word, 0)+1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    print("---------keywordlist---------")
    for i in range(len(items)):
        key_word, key_count = items[i]
        print("{0:<10}{1:>5}".format(key_word, key_count))

def main():
    try:
        fileName = input("输入想检测的文件名字(xxx.txt):\n")
        catch_Word(str_Processing(fileName))
    except Exception as erro:
        print(erro)

if __name__ == "__main__":
    main()