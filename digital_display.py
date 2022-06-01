import turtle
import datetime
import math

def init():
    turtle.setup(1000, 350, 200, 200)
    turtle.penup()
    turtle.fd(-400)
    turtle.pensize(1)
    turtle.speed(20)

def drawGap():              #每条笔画间的空格
    turtle.penup()
    turtle.fd(2)

def drawLine(up):       #绘制单根数码管，使用了细笔绘制轮廓后填充达到更真实的效果
    drawGap()
    turtle.pendown()
    if up:
        turtle.begin_fill()
    turtle.lt(45)
    turtle.fd(math.sqrt(18))
    turtle.rt(45)
    turtle.fd(34)
    turtle.rt(45)
    turtle.fd(math.sqrt(18))
    turtle.rt(90)
    turtle.fd(math.sqrt(18))
    turtle.rt(45)
    turtle.fd(34)
    turtle.rt(45)
    turtle.fd(math.sqrt(18))
    if up:
        turtle.end_fill()
    turtle.rt(135)
    turtle.pu()
    turtle.fd(40)
    drawGap()
    turtle.rt(90)

def realDraw(num, a):#决定这根管是否上色，为后续绘制减少重复代码量
    if num in a:
        drawLine(True)
    else:
        drawLine(False)

def drawNumber(num, dot):       #依次走过七根数码管
    realDraw(num, [2,3,4,5,6,8,9])
    realDraw(num, [0,1,3,4,5,6,7,8,9])
    realDraw(num, [0,2,3,5,6,8,9])
    if dot:                     #绘制小数点
        turtle.pensize(5)
        turtle.pendown()
        turtle.fd(5)
        turtle.penup()
        turtle.fd(-5)
        turtle.pensize(1)
    realDraw(num, [0,2,6,8])
    turtle.lt(90)
    realDraw(num, [0,4,5,6,8,9])
    realDraw(num, [0,2,3,5,6,7,8,9])
    realDraw(num, [0,1,2,3,4,7,8,9])
    turtle.penup()
    turtle.lt(180)
    turtle.fd(20)

def drawDate(date):             #绘制出一组字符串
    turtle.color("red")
    for i in date:
        if i == '年':
            turtle.write('年', font=("Arial", 60, "normal"))
            turtle.fd(100)
        elif i == '月':
            turtle.write('月', font=("Arial", 60, "normal"))
            turtle.fd(100)
        elif i == '日':
            turtle.write('日',font=("Arial", 60, "normal"))
        elif i == '.':
            drawNumber(i,True)
        else:
            drawNumber(eval(i), False)

def main(idx):                     #初始化turtle
    init()
    if idx == 1:#绘制自定义数字，可小数
        try:
            Number = eval(input("请输入你想显示的数字"))
            drawDate(str(Number))
            turtle.bye()
        except SyntaxError:
            print("输入错误,请输入数字!")

    elif idx == 3:#绘制当前时间
        drawDate(datetime.datetime.now().strftime('%Y年%m月%d日'))
        turtle.bye()

    elif idx == 2:#绘制自定义时间
        try:
            flag =0
            datestr = str(input("请输入想显示的时间:\n"))
            for fn in datestr:
                if fn in ["年","月","日"]:#对输入格式判断
                    flag +=1
            if flag != 3:
                raise Exception("输入格式错误")
            else:
                drawDate(datestr)
                turtle.bye()
        except Exception as err:
            print(err)
            main(idx)

if __name__ == "__main__":
    main()