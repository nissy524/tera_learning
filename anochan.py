def total_price_1item(unit_price,quantity=1):
    total_price=unit_price*quantity
    return total_price
total_price=total_price_1item(unit_price=130,quantity=20)
print(total_price)

def total_price_1item(unit_price:int, quantity:int=1)->str:
    total_price=unit_price*quantity
    return f'￥{total_price:,}'

total_price=total_price_1item(1300)

print(total_price)
# ->strは関数の戻り値の型アノテーションを示している

from tqdm import tqdm
for _x in tqdm(range(10**9)):
    pass
#ターミナル押すな