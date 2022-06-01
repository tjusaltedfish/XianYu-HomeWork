import turtle

def setting(Pensize, color):    #turtle的初始化设计，自行选择笔粗和颜色
    turtle.setup(650, 650, 200, 200)
    turtle.penup()
    turtle.fd(-250)
    turtle.pendown()
    turtle.pensize(Pensize)
    turtle.pencolor(color)

def init():
    myColor = input("请选择字体颜色:")
    Size = input("请选择字体大小(min/mid/max):")
    if Size in ['min','mid','max']:
        return myColor,Size
    else:
        print("输入错误!")

def drawDa(fontsize):    
    if fontsize == "min":       #用于选择字的大小
        fontsize = 100
    elif fontsize == "mid":
        fontsize = 200
    else:
        fontsize = 300
    turtle.fd(fontsize)         #固定的绘制大字轨迹
    turtle.penup()
    turtle.goto(fontsize*0.5-250, fontsize*0.3)
    turtle.pendown()
    turtle.seth(-90)
    turtle.fd(fontsize*0.5)
    turtle.seth(-120)
    turtle.fd(fontsize*0.7)
    turtle.penup()
    turtle.goto(fontsize*0.5-250, -fontsize*0.2)
    turtle.pendown()
    turtle.seth(-60)
    turtle.fd(fontsize*0.7)

def main():
    myColor,mySize=init()
    setting(25,myColor)
    drawDa(mySize)
    turtle.bye()
    
if __name__ == "__main__":
    main()