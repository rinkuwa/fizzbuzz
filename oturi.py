def calculate_change(price, paid):
    if paid < price:
        return "支払いが不足しています。"
    
    change = paid - price
    coins = [500, 100, 50, 10, 5, 1]
    coin_count = {}

    for coin in coins:
        count = change // coin
        if count > 0:
            coin_count[coin] = count
        change = change % coin

    return coin_count

# 入力例
price = int(input("商品の価格を入力してください: "))
paid = int(input("支払った金額を入力してください: "))

# おつりの計算
result = calculate_change(price, paid)

# 結果の表示
if isinstance(result, str):
    print(result)
else:
    print("おつりの内訳:")
    for coin, count in result.items():
        print(f"{coin}円: {count}枚")
