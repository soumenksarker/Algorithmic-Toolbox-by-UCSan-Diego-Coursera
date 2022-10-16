# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    count = 0
    while(money!=0):
        if money>=10:
            x=money//10
            money=money%10
            count+=x
        elif money>=5 and money<10:
            y=money//5
            money=money%5
            count+=y
        else:
           count+=money
           money=0
    return count

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
