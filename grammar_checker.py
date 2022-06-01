'''自动检测代码语法错误并提示？'''
import re

#几种关键词所对应的语法的正则表达式
RE_EXPERSSTION_FOR = r"\s*for\s.*\sin\s.*:"        
RE_EXPERSSTION_DEF = r"\s*def\s\w*\(.*\):"
RE_EXPERSSTION_IF = r"\s*if\s.*:"
RE_EXPERSSTION_ELIF = r"\s*elif\s.*:"
RE_EXPERSSTION_TRY = r"\s*try:"
RE_EXPERSSTION_EXCEPT = r"\s*except.*:"

def openfile():
    try:
        fileName = input("请输入想打开的文件:\n")
        f = open(fileName, encoding='utf-8')
        data = f.readlines()
        return data
    except:
        print("输入错误！请重新输入")
        openfile()

def seek_keyword(strdata):                  #寻找里面有的关键字，如果有则将对应的flag标1
    flags = [0 , 0 , 0 , 0 , 0 , 0]
    #分别对应for_flag 、 def_flag 、 if_flag 、 elif_flag 、 try_flag 、 except_flag
    strdata = str(strdata).lower()
    strdata = strdata.replace(r":" , " ")    #防止找不到try、except、else
    words = strdata.split()
    for word in words:
        if word == "for":
            flags[0] = 1
        elif word == "def":
            flags[1] = 1
        elif word == "if":
            flags[2] = 1
        elif word == "elif":
            flags[3] = 1
        elif word == "try":
            flags[4] = 1
        elif word == "except":
            flags[5] = 1
    return flags

def grammar_check(flags , num , each_line):         #通过正则表达式来匹配语法
    if flags[0] != 0 and re.match(RE_EXPERSSTION_FOR , each_line) is None:
        print("第%s行for语法有误!" % num)
    elif flags[1] !=0 and re.match(RE_EXPERSSTION_DEF , each_line) is None:
        print("第%s行def语法有误!" % num)
    elif flags[2] !=0 and re.match(RE_EXPERSSTION_IF , each_line) is None:
        print("第%s行if语法有误!" % num)
    elif flags[3] !=0 and re.match(RE_EXPERSSTION_ELIF , each_line) is None:
        print("第%s行elif语法有误!" % num)
    elif flags[4] !=0 and re.match(RE_EXPERSSTION_TRY , each_line) is None:
        print("第%s行try语法有误!" % num)
    elif flags[5] !=0 and re.match(RE_EXPERSSTION_EXCEPT , each_line) is None:
        print("第%s行except语法有误!" % num)

def symbol_check(num , each_line):                  #逐行寻找括号对、引号对
    l_kuohao = r_kuohao = 0     #小括号（）
    l_kuohao1 = r_kuohao1 = 0   #中括号[]
    l_kuohao2 = r_kuohao2 = 0   #大括号{}
    yinhao1 = 0                 #双引号""
    yinhao2 = 0                 #单引号''
    for i in each_line:
        if i == "(":
            l_kuohao += 1
        elif i == ")":
            r_kuohao += 1
        elif i == "[":
            l_kuohao1 += 1
        elif i == "]":
            r_kuohao1 += 1
        elif i == "{":
            l_kuohao2 += 1
        elif i == "}":
            r_kuohao2 += 1                                
        elif i == "\"":
            yinhao1 += 1
        elif i == "\'":
            yinhao2 += 1
    if l_kuohao != r_kuohao:
        print("第%s行可能缺少小括号!" % num)
    if l_kuohao1 != r_kuohao1:
        print("第%s行可能缺少中括号!" % num)
    if l_kuohao2 != r_kuohao2:
        print("第%s行可能缺少大括号!" % num)
    if yinhao1 % 2 != 0:
        print("第%s行可能缺少双引号!" % num)
    if yinhao2 % 2 != 0:
        print("第%s行可能缺少单引号!" % num)            

def checker(strdata):                           #将打开的文本文档逐行分析语法
    num = 0
    for each_line in strdata:
        num += 1
        flags = seek_keyword(each_line)
        grammar_check(flags , num , each_line)  #根据上面所得flag，来决定对这行进行哪种语法检查
        symbol_check(num , each_line)           #检查符号如括号、引号是否有多或者少

def main():
    filedata = openfile()
    checker(filedata)
    
if __name__ == "__main__":
    main()