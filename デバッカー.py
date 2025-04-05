def price_format(x):
    return f'{x:,}円'

def shopping_fee(x):
    if x <12000:
        return x +500
    else:
        return x

def main():
    hand_bag=5000
    shoes=6000
    breakpoint()
    total=hand_bag+shoes
    total=shopping_fee(total)
    breakpoint()
    total=price_format(total)
    print(total)

if __name__=='__main__':
    main()
    
# ターミナルでｎを入力するとbreakpointから次の行に、ｓだとその次の行になる、ｑでデバック終了
# cを入力すると２つ目のbrakpointにとまる、確認が終わるとbreakpointを消去
# pythonデバッカーを入れたことで赤い点を打つとbreakpointになり、実行とデバック