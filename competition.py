"""旨在模拟真实的抢球比赛,由发球机来发出各种类型的球,A和B先抢到者为胜者(无平局),会考虑到选手雷达图以及当场风向与发球类型的影响"""
import random

def game_init(people):          #创建角色，输入初始数值
    a_power = [0 , 0 , 0 , 0]
    environment = ["身高" , "速度" , "技巧" , "稳定性"]
    print("-------请创建角色%s-------" % people)
    for i in range(4):
        power = eval(input("请输入%s在%s方面的数值:" % (str(people) , environment[i])))
        a_power[i] = power
    return a_power

def create_environment():        #模拟每一次发球时的环境变量
    i = random.randint(0 , 100)
    if i < 25:
        ball_type = 1            #发出普通球
    elif i < 50:
        ball_type = 2            #发出高飘球
    elif i < 75:
        ball_type = 3            #发出低快球
    elif i < 100:
        ball_type = 4            #发出技巧球
    j = random.randint(0 , 2)
    if j < 1:
        wind_type = 1           #风向有利
    else:
        wind_type = 2           #风向不利
    return ball_type , wind_type

def factor_init(ball_t , wind_t , power):#根据每一次模拟的发球环境，改变每一项基础数值所占综合数值的比重
    factor1 = factor2 = factor3 = factor4 = 0.25
    if ball_t == 2:
        factor1 += 0.15
        factor2 -= 0.15
    elif ball_t == 3:
        factor2 += 0.15
        factor1 -= 0.15
    elif ball_t == 4:
        factor3 += 0.3
        factor2 -= 0.15
        factor1 -= 0.15
    #每一项数值乘以受环境改变过的影响因子得到当局的能力值
    total_power = factor1*list(power)[0] + factor2*list(power)[0] + factor3*list(power)[0] + factor4*list(power)[0]
    if wind_t == 1:
        total_power *= 1.25
    else:
        total_power *= 0.75
    return total_power

def game_once_sim(a , b):           #单局的比赛模拟
    ball_type , wind_type = create_environment()
    a_power = factor_init(ball_type , wind_type , list(a))
    b_power = factor_init(ball_type , 1-wind_type , list(b))
    result = random.randint(0 , int(a_power) + int(b_power))#看这个随机量落入哪个获胜域
    if result < int(a_power):
        return 'A'
    else:
        return 'B'

def game_total_sim(a_power , b_power):#全部比赛的模拟，每一次比赛都会更新随机环境
    a_scores = b_scores = 0
    n = int(input("请输入想模拟的局数:"))
    for i in range(n):
        if game_once_sim(list(a_power) , list(b_power)) == 'A':
            a_scores += 1
        else:
            b_scores += 1
    return a_scores , b_scores

def result_print(a , b):
    print("-------模拟结束！-------")
    print("A得分为%s,B得分为%s" % (a , b))
    if a > b:
        print("A获胜!")
    elif a == b:
        print("A与B平局!")
    else:
        print("B获胜!")

def main():
    a_power = game_init("A")
    b_power = game_init("B")
    a_scores , b_scores = game_total_sim(a_power , b_power)
    result_print(a_scores , b_scores)

if __name__ == "__main__":
    main()
 